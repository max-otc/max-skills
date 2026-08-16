#!/usr/bin/env python3
"""Serve one decision sheet on localhost and capture the answer it posts back.

Usage: python3 serve.py /path/to/<topic>-decisions.html

Prints `PORT=<n>` as the first stdout line, then serves the sheet at
http://127.0.0.1:<n>/ . A POST to /answer writes two files next to the sheet:

    <topic>-decisions-answers.json
    <topic>-decisions-answers.md

and the server stops a moment later. With no answer, the server stops itself
after 12 hours.

The sheet is served over HTTP on purpose. A page opened as file:// has an
opaque origin and cannot POST to localhost.
"""

import json
import os
import sys
import threading
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

MAX_BODY = 4 * 1024 * 1024
LIFETIME_SECONDS = 12 * 60 * 60
SHUTDOWN_DELAY_SECONDS = 1.0


def answer_paths(sheet_path):
    base = sheet_path[:-5] if sheet_path.lower().endswith(".html") else sheet_path
    return base + "-answers.json", base + "-answers.md"


def render_markdown(payload, sheet_path):
    title = payload.get("title") or os.path.basename(sheet_path)
    summary = payload.get("summary") or ""
    answers = payload.get("answers") or []
    notes = payload.get("notes") or ""
    stamp = payload.get("timestamp") or datetime.now(timezone.utc).isoformat()

    lines = ["# Answers — %s" % title, ""]
    if summary:
        lines += ["`%s`" % summary, ""]
    lines += ["Answered %s" % stamp, "", "## Decisions", ""]

    for item in answers:
        head = "**%s%s**" % (item.get("n", "?"), item.get("choice", ""))
        label = item.get("label")
        if label:
            head += " — %s" % label
        lines.append("- %s" % head)
        question = item.get("question")
        if question:
            lines.append("  - _q:_ %s" % question)
        comment = (item.get("comment") or "").strip()
        if comment:
            for para in comment.splitlines():
                lines.append("  - %s" % para.strip() if para.strip() else "  -")

    if notes.strip():
        lines += ["", "## Notes", "", notes.strip()]

    lines.append("")
    return "\n".join(lines)


def build_handler(sheet_path, stop_event):
    json_path, md_path = answer_paths(sheet_path)

    class Handler(BaseHTTPRequestHandler):
        server_version = "MaxDecisions/1.0"

        def log_message(self, fmt, *args):
            sys.stderr.write("%s %s\n" % (self.address_string(), fmt % args))

        def _send(self, code, body, ctype):
            data = body.encode("utf-8") if isinstance(body, str) else body
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            path = self.path.split("?", 1)[0]
            if path in ("/", "/index.html"):
                try:
                    with open(sheet_path, "rb") as fh:
                        body = fh.read()
                except OSError as err:
                    self._send(500, "cannot read sheet: %s" % err, "text/plain; charset=utf-8")
                    return
                self._send(200, body, "text/html; charset=utf-8")
            elif path == "/health":
                self._send(200, "ok", "text/plain; charset=utf-8")
            else:
                self._send(404, "not found", "text/plain; charset=utf-8")

        def do_POST(self):
            if self.path.split("?", 1)[0] != "/answer":
                self._send(404, "not found", "text/plain; charset=utf-8")
                return
            try:
                length = int(self.headers.get("Content-Length") or 0)
            except ValueError:
                length = 0
            if length <= 0 or length > MAX_BODY:
                self._send(400, "bad length", "text/plain; charset=utf-8")
                return
            raw = self.rfile.read(length)
            try:
                payload = json.loads(raw.decode("utf-8"))
            except (UnicodeDecodeError, ValueError) as err:
                self._send(400, "bad json: %s" % err, "text/plain; charset=utf-8")
                return
            if not isinstance(payload, dict):
                self._send(400, "expected a json object", "text/plain; charset=utf-8")
                return

            payload.setdefault("timestamp", datetime.now(timezone.utc).isoformat())
            payload.setdefault("sheet", sheet_path)

            try:
                with open(json_path, "w", encoding="utf-8") as fh:
                    json.dump(payload, fh, indent=2, ensure_ascii=False)
                    fh.write("\n")
                with open(md_path, "w", encoding="utf-8") as fh:
                    fh.write(render_markdown(payload, sheet_path))
            except OSError as err:
                self._send(500, "write failed: %s" % err, "text/plain; charset=utf-8")
                return

            self._send(200, json.dumps({"ok": True, "json": json_path, "md": md_path}),
                       "application/json; charset=utf-8")
            print("ANSWERED=%s" % json_path, flush=True)
            threading.Timer(SHUTDOWN_DELAY_SECONDS, stop_event.set).start()

    return Handler


def main():
    if len(sys.argv) < 2:
        sys.stderr.write("usage: serve.py <sheet.html>\n")
        return 2
    sheet_path = os.path.abspath(os.path.expanduser(sys.argv[1]))
    if not os.path.isfile(sheet_path):
        sys.stderr.write("no such sheet: %s\n" % sheet_path)
        return 2

    stop_event = threading.Event()
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), build_handler(sheet_path, stop_event))
    httpd.daemon_threads = True
    port = httpd.server_address[1]

    print("PORT=%d" % port, flush=True)
    print("URL=http://127.0.0.1:%d/" % port, flush=True)

    thread = threading.Thread(target=httpd.serve_forever, kwargs={"poll_interval": 0.2})
    thread.daemon = True
    thread.start()

    deadline = time.time() + LIFETIME_SECONDS
    try:
        while not stop_event.is_set():
            if time.time() >= deadline:
                print("EXPIRED", flush=True)
                break
            stop_event.wait(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        httpd.shutdown()
        httpd.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())

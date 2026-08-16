#!/usr/bin/env python3
"""CRX document QA probe - run on any document built from crx-doc-template.html.

Checks, per the formatting-marketmaker-documents framework:
  1. PDF page count == .sheet count (overflow past the page edge)
  2. Bottom clearance per page: last ink row must sit ~at the sheet's bottom
     padding boundary (content silently eating the margin is the failure the
     page count alone cannot catch - flex overflows into padding without
     splitting the page).

Usage:  python3 doc-qa.py crx-<topic>-vN.html [--bottom 0.75]
Needs:  Google Chrome, Pillow (pip install pillow).
"""
import re, subprocess, sys, tempfile, os

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PAGE_H = 1056  # 11in @ 96dpi

def main():
    path = sys.argv[1]
    bottom_in = float(sys.argv[sys.argv.index('--bottom')+1]) if '--bottom' in sys.argv else 0.75
    html = open(path).read()
    sheets = len(re.findall(r'class="sheet', html))

    with tempfile.TemporaryDirectory() as td:
        pdf = os.path.join(td, 'q.pdf')
        subprocess.run([CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
                        f'--print-to-pdf={pdf}', path], capture_output=True)
        m = re.search(rb'/Count (\d+)', open(pdf, 'rb').read())
        pages = int(m.group(1))
        png = os.path.join(td, 'q.png')
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                        f'--screenshot={png}', f'--window-size=816,{PAGE_H*sheets}',
                        f'file://{os.path.abspath(path)}'], capture_output=True)
        from PIL import Image
        im = Image.open(png).convert('L')

    ok = True
    if pages != sheets:
        print(f'FAIL  page count {pages} != sheet count {sheets} (a sheet overflowed 11in)')
        ok = False
    else:
        print(f'ok    page count {pages} == sheet count')

    for i in range(sheets):
        y0, y1 = i*PAGE_H, (i+1)*PAGE_H - 1
        last = None
        for y in range(min(y1, im.height-1), y0, -1):
            if min(im.getpixel((x, y)) for x in range(100, im.width-100, 4)) < 200:
                last = y
                break
        clear_in = (y1 - last) / 96
        # footer sits at the padding boundary; allow 0.06in tolerance
        if clear_in < bottom_in - 0.06:
            print(f'FAIL  sheet {i+1}: bottom clearance {clear_in:.2f}in < {bottom_in}in - content is overflowing into the margin; repaginate')
            ok = False
        else:
            print(f'ok    sheet {i+1}: bottom clearance {clear_in:.2f}in')
    sys.exit(0 if ok else 1)

if __name__ == '__main__':
    main()

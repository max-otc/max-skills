# max-skills

A Claude Code plugin marketplace. Personal skills, shipped as a catalog.

## Install the marketplace

Once. From inside Claude Code:

```
/plugin marketplace add max-otc/max-skills
```

## Install a plugin

```
/plugin install <plugin-name>@max-skills
```

Replace `<plugin-name>` with one of the entries below.

## Plugins

### reddit-persona-research

Deep qualitative Reddit research. Reconstructs a target persona for a brand or product from real Reddit discussions: pain points, language, objections, current solutions, journey, strategic gaps. Eleven sections, evidence-loaded. Refuses to summarize.

```
/plugin install reddit-persona-research@max-skills
```

Then invoke by asking Claude to do Reddit research on a brand, build a persona, or run voice-of-customer analysis. The skill loads itself.

## Update

```
/plugin marketplace update max-skills
```

## Uninstall

```
/plugin uninstall <plugin-name>@max-skills
```

## Adding a new plugin

1. Create `plugins/<plugin-name>/.claude-plugin/plugin.json`
2. Add skills under `plugins/<plugin-name>/skills/<skill-name>/SKILL.md`
3. Add an entry to `.claude-plugin/marketplace.json`
4. Commit, push, bump

## License

MIT.

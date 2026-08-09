# prepping — Claude Code plugin marketplace

A personal marketplace hosting `merge-prepping` (a PR title rewriter / tracking
issue enforcer for the myPlanet house style). Maintain the skill here once; opt
any project into it — including **Claude Code on the web / cloud** sessions.

## Structure

```
.claude-plugin/marketplace.json          # marketplace catalog
plugins/merge-prepping/
├── .claude-plugin/plugin.json           # plugin manifest
└── skills/prepping/
    ├── SKILL.md                         # skill definition
    └── references/
        └── title-corpus.md              # past titles, for nearest-precedent lookup
```

`references/title-corpus.md` is not committed yet — step 5 of the skill's
procedure skims it for the nearest existing phrasing. Generate it from the
myPlanet log (`git log --format=%s master`) and drop it in; until then the skill
still works, it just composes titles from the rules alone.

## Hosting

This marketplace is hosted at `dogi/merge-prepping`. The
`.claude-plugin/marketplace.json` catalog lives at the repo root so Claude Code
can discover it when the repo is added as a marketplace.

## Use it in the terminal (CLI)

```
/plugin marketplace add dogi/merge-prepping
/plugin install merge-prepping@prepping
/reload-plugins
```

Then invoke: `/merge-prepping:prepping` (or just ask to "prep this PR" / "fix
the title" — the description auto-triggers it).

## Use it on Claude Code web / cloud

Cloud sessions can't see your local `~/.claude`, and user-scoped `enabledPlugins`
does **not** carry over. Declare the marketplace + plugin in the target repo's
`.claude/settings.json` (this file is part of the clone, so the cloud VM installs
the plugin at session start — needs network access to GitHub, which the default
allowlist covers):

```json
{
  "extraKnownMarketplaces": {
    "prepping": {
      "source": {
        "source": "github",
        "repo": "dogi/merge-prepping"
      }
    }
  },
  "enabledPlugins": {
    "merge-prepping@prepping": true
  }
}
```

Commit that to each repo where you want the skill available in web sessions.
The skill itself stays maintained here — bump `version` in `plugin.json` on each
release so installs pick up updates.

## What the skill does

Turns an arbitrary PR title into the shape every commit on `master` already has:

```
<scope>: smoother <noun phrase> <gerund> (fixes #N)
<scope>: less <noun phrase> is more (fixes #N)
all: bump `<coordinate>` to <version> (fixes #N)
```

It picks the scope from where the diff's centre of gravity sits, walks the noun
phrase across every changed file (layer words, not entity names) and takes the
gerund from the class suffix — reading all of that off the file list rather than
the old title. The old title has one job: becoming the issue title when the PR
arrived without an issue, which is the usual case for Jules- and Copilot-opened
PRs. Human PRs normally already have a number in the title, the body, or the
`<N>-slug` branch name. `(fixes #N)` goes in the title, not the body, because the
squash commit message *is* the PR title.

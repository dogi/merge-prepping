---
name: pr-prep
description: Rewrite a pull request title into the myPlanet house style (`scope: smoother thing doing (fixes #N)`) and make sure a tracking issue is attached, creating one from the PR's current title when none exists. Use this whenever preparing, cleaning up, retitling, or getting a PR ready to merge in this repo — including when the user says "prep this PR", "fix the title", "massage the title", "does this need an issue?", or just points at a PR number or branch and asks to tidy it up. Also use it before opening a new PR, so the title is right the first time.
---

# PR prep

Every commit that lands on `master` here reads the same way. That consistency is
the point: the log doubles as a changelog, and every line traces back to an issue.
This skill turns an arbitrary PR title into that form and guarantees the issue link
exists.

## The grammar

Three shapes cover the last 200 commits. All lowercase, no trailing period, no
conventional-commit types (`feat:`, `fix:`, `refactor:` never appear).

| Shape | When | Share |
|---|---|---|
| `<scope>: smoother <noun phrase> <gerund> (fixes #N)` | Anything that improves, fixes, adds, or reworks | 184/200 |
| `<scope>: less <noun phrase> is more (fixes #N)` | A named thing *ceases to exist* | 9/200 |
| `all: bump \`<coordinate>\` to <version> (fixes #N)` | Dependency version bumps only | 6/200 |

**`smoother` is the default and it isn't close — 92% of titles.** Reach for it
unless you can point at the specific class, method, file, layout, or feature that
is gone after the change. A net-negative diff is *not* the signal: a refactor that
restructures code into a tidier shape deletes plenty of lines and is still
`smoother`. Ask what the PR is *for*. If its purpose is "get rid of X", use `less`;
if its purpose is "make X work better" and deletion is a side effect, use `smoother`.

Worked failure: a PR converting `LoginSyncManager.login` to a `suspend` function
was 89 additions against 106 deletions, and stripped a dozen
`withContext(dispatcherProvider.main)` wrappers. Net-negative, lots of removal — so
`less login sync main dispatcher is more` looked right. It wasn't. Nothing named
ceased to exist; the login path was restructured. The correct title was
`sync: smoother login auth utils managing`.

Never type the trailing `(#<pr>)` you see in the git log — GitHub appends that at
squash-merge time. The PR title stops after `(fixes #N)`.

`(fixes #N)` belongs in the **title**, not the body. GitHub only auto-closes from
the body or the commit message, and the squash commit message *is* the PR title —
so putting it in the title is what actually closes the issue on merge. Get the
spelling exact: lowercase `fixes`, a space, `#`, the number, wrapped in round
parens. Real typos in the log (`{fixes #14889)`, `(fixes 14801)` with no `#`)
broke the link and the issue stayed open.

## Choosing the scope

`all:` is the workhorse (59/200) and the right default whenever the change reaches
shared layers — `model/`, `repository/`, `di/`, `base/`, `callback/`, `utils/`,
`data/`, `MainApplication.kt` — or spans more than one feature.

Reach for a feature scope only when the change sits squarely inside one domain,
including that domain's own repository:

| Scope | Owns |
|---|---|
| `teams` | `ui/teams/**`, `ui/voices/`, `ui/events/`, `ui/surveys/`, team tasks |
| `courses` | `ui/courses/`, `ui/exam/`, `ui/submissions/`, `ui/ratings/`, progress, tags |
| `sync` | `services/sync/`, `services/upload/`, `services/retry/`, uploads, downloads |
| `resources` | `ui/resources/`, `ui/viewer/`, webview, media playback |
| `dashboard` | `ui/dashboard/` and the bell — but **not** `ui/notifications/` |
| `chat` | `ui/chat/` |
| `login` | `ui/settings/`, `ui/user/`, onboarding; `ui/sync/` — see below |
| `life` | `ui/health/`, `ui/life/` |
| `community` | `ui/community/` |
| `enterprises` | `ui/enterprises/` |
| `actions` | `.github/workflows/` |

When torn between a feature scope and `all:`, look at where the *centre of gravity*
of the diff sits. A change to `TeamsRepositoryImpl` alone is `teams:`; the same
change plus a shared `RealmRepository` tweak is `all:`.

`ui/notifications/` is a trap: the bell *icon* on the dashboard is `dashboard`, but
the notifications package itself is always `all` — four for four in the log
(`all: smoother notifications text caching`, `all: smoother notification item
sorting`, `all: less notification bell icon list item is more`, `all: smoother view
model scoping`). Notifications are surfaced across the app, not owned by one
screen, which is presumably why.

`ui/sync/` is genuinely ambiguous in the log — `GuestLoginExtensions.kt` has landed
as both `sync: smoother guest login validating` and `login: smoother guest
extensions validating`. Don't agonise: `sync` if the change is about the sync or
login *transaction*, `login` if it's about the screen and what the user sees.
Anything under `services/sync/` is unambiguously `sync`.

## Building the phrase — read it off the diff, not the old title

The title is close to a mechanical function of the files changed. Once you see
that, most titles write themselves:

**The noun phrase is the principal changed file, de-CamelCased and lowercased,
with its role suffix dropped. The gerund comes from that suffix.**

```
ui/dashboard/BellDashboardFragment.kt   → dashboard: smoother bell reminding
services/upload/PhotoUploader.kt        → sync: smoother photo uploading
ui/health/HealthUsersAdapter.kt         → life: smoother health users item callback diffing
ui/health/HealthExaminationAdapter.kt   → life: smoother health examination item callback diffing
```

Pick the *principal* file first: the one the PR exists to change. Test files,
generated files, `strings.xml`, and drive-by formatting are never the principal
file. If the diff has no single centre, name the behaviour instead of a file —
that is also how the `all:` titles read.

Some suffixes carry their own verb, so the gerund is mechanical:

| Suffix | Gerund |
|---|---|
| `…Uploader` | `uploading` |
| `…Adapter` | `item callback diffing` (or `…listing` when the change is the list itself) |
| `…Manager` | `managing` |
| `…Repository` / `…RepositoryImpl` | `caching` or `querying`, whichever the diff does |
| `…ViewModel` | `scoping`, `loading`, or `state handling` |

`…Fragment` and `…Activity` carry no verb of their own — name what the screen
actually does, which is why `BellDashboardFragment` becomes `bell reminding` and
not `bell fragmenting`. Same for a layout-only or `strings.xml`-only change: the
gerund describes the change (`… layouting`, `… wording`).

Keep it short. Two to five words between `smoother` and the parens is the norm;
if it is running longer, the noun phrase is carrying detail that belongs in the
PR body.

## The tracking issue

A PR without `(fixes #N)` is not ready, full stop. Resolve the number before
touching the title:

1. **Read the current title and body** for an existing reference — `(fixes #N)`,
   `fixes #N`, `closes #N`, or a bare `#N`. If one is already there and points at
   an open issue, reuse that number; just move it into the title in the exact
   `(fixes #N)` spelling.
2. **Search the open issues** for the thing this PR is about before creating
   anything. Re-filing a duplicate is worse than a slightly-off match.
3. **Only then create one.** Title the new issue from the PR's *current*
   human-readable title — the issue is where prose is allowed, so it does not
   need `smoother` grammar. Body: a sentence on the observed problem plus a link
   to the PR.

Then set the PR title to the house-style form ending in `(fixes #N)`. Change the
title only — do not rewrite the PR body to add a `fixes` line, since the body
plays no part in the squash commit message.

## Procedure

1. Identify the PR (number, branch, or "this one"). Fetch its title, body, and
   changed files with additions/deletions.
2. Pick the shape: `smoother` unless something named ceases to exist (`less …
   is more`), or it is purely a dependency bump (`all: bump …`).
3. Pick the scope from the centre of gravity of the diff.
4. Build the noun phrase and gerund off the principal changed file.
5. Resolve the issue number — find it, or create the issue.
6. Update the PR title. Nothing else.
7. Report the old title, the new title, and the issue you linked or created.

## Before you call it done

- [ ] all lowercase, except identifiers inside backticks in a `bump` title
- [ ] no `feat:` / `fix:` / `refactor:` / `chore:` prefix
- [ ] no trailing period
- [ ] no trailing `(#<pr number>)` — GitHub adds that itself
- [ ] ends in exactly `(fixes #N)`: lowercase, space, `#`, digits, round parens
- [ ] scope is one from the table, not invented
- [ ] the noun phrase names what changed, not what the old title said

# myplanet — reference pack

`open-learning-exchange/myplanet`. Kotlin / Android, Gradle, sources under
`app/src/main/java/org/ole/planet/myplanet/`.

Read this with the shared grammar in `SKILL.md`; this file is only what myplanet
does differently. Corpus: `references/myplanet/title-corpus.md` — the last 500
landed titles with the files that produced them, and `## What a prep pass gets
wrong`, the draft-versus-landed pairs. Read that section before composing.

The automerge drain (`.github/scripts/automerge.sh`, `link_title_issues`) mirrors
a title's closing reference into the PR body just before squash-merging, so
queued PRs are covered but hand-merged ones are not. Write the body line at prep
time regardless; the drain is a safety net, and it is idempotent.

Most PRs here are agent-opened (`openhands/…`, `jules-…`, `claude/…`, task-id
branch suffixes) and arrive with prose titles that do not survive — but those
agents are dispatched from the backlog, so most already carry an issue, numbered
below the PR. Check before creating one.

## Scopes

The vocabulary is **closed**: these eleven words, which cover 499 of the last
500 titles — the odd one out is `lifel:`, a typo for `life:`. `all:` is the
workhorse (127/500) and the default whenever the change reaches shared layers — `model/`,
`repository/`, `di/`, `base/`, `callback/`, `utils/`, `data/room/`,
`MainApplication.kt` — or spans more than one feature.

| Scope | Owns | Share |
|---|---|---|
| `sync` | `services/sync/`, `services/upload/`, `services/retry/`, uploads, downloads; `ui/sync/` — see below | 71 |
| `teams` | `ui/teams/**`, `ui/voices/`, `ui/events/`, `ui/surveys/`, team tasks, members | 69 |
| `courses` | `ui/courses/`, `ui/exam/`, `ui/submissions/`, `ui/ratings/`, progress, tags | 67 |
| `resources` | `ui/resources/`, `ui/viewer/`, collections, webview, media playback | 41 |
| `actions` | `.github/workflows/`, `.github/scripts/`, `CLAUDE.md`, `docs/`, Gradle/CI config | 28 |
| `life` | `ui/health/`, `ui/life/`, achievements, personals | 26 |
| `login` | `ui/settings/`, `ui/user/`, onboarding; `ui/sync/` — see below | 23 |
| `dashboard` | `ui/dashboard/` and the bell — but **not** `ui/notifications/` | 17 |
| `enterprises` | `ui/enterprises/`, finances | 14 |
| `community` | `ui/community/` | 8 |
| `chat` | `ui/chat/` | 8 |

When torn between a feature scope and `all:`, follow the *centre of gravity* of
the diff: `TeamsRepositoryImpl` alone is `teams:`; the same change plus a shared
`RealmRepository` tweak is `all:`.

Two border zones. `ui/notifications/` is always `all` — the bell *icon* on the
dashboard is `dashboard`, but the package is surfaced app-wide. `ui/sync/` is
genuinely split, six titles each way: `sync` for the sync or login *transaction*,
`login` for the screen and what the user sees. Anything under `services/sync/` is
`sync`.

Invented scopes are the most common way to get a title wrong — the word is
usually right, it just belongs in the noun phrase:

| Wrote | Should be |
|---|---|
| `retry:`, `downloads:` | `sync:` |
| `voices:`, `members:` | `teams:` |
| `collections:` | `resources:` |
| `health:`, achievements under `login:` | `life:` |
| `submissions:` | `courses:` |
| `notifications:`, `ui:`, `model:`, `diagnostics:` | `all:` |
| `docs:`, `ci:` | `actions:` |

## Reading the phrase off the filenames

Titles here are close to a **mechanical function of the changed files** —
163/500 diffs touch one file beyond the version bump, 363/500 touch three or
fewer. **The noun phrase is the principal changed file, de-CamelCased and
lowercased with its role suffix dropped; the gerund comes from that suffix.**

```
services/upload/PhotoUploader.kt        → sync: smoother photo uploading
utils/Utilities.kt                      → all: smoother utilities hex mapping
services/NetworkMonitorWorker.kt        → all: smoother network monitor working
ui/teams/members/MembersAdapter.kt      → teams: smoother members view binding
di/NetworkDependenciesEntryPoint.kt ✗   → all: less network dependencies entry point is more
```

Keep it a **bare chain of nouns**: no prepositions, articles, `and`, commas or
hyphenated compounds — zero of the 492 non-`bump` titles have any. The median is
`smoother` plus three words counting the gerund. Say the layer and the operation
and drop the glue, but don't drop the layer word itself — where a draft names
the entity or the symptom, the title names the layer:

```
courses: smoother filtered-course sort without per-item lowercase
                                        → courses: smoother repository sorting
members: smoother last-visit date formatting via shared TimeUtils
                                        → teams: smoother members date formatting
```

### Suffix → gerund

| Principal file | Gerund |
|---|---|
| `*Provider`, `*Module`, `*Logger`, `*Interceptor` | providing |
| `*ViewModel` | **view** modelling (both words — 62 of 65) |
| `*Worker` | working |
| `*Adapter` — `DiffUtil` / `ItemCallback` / payload changes | diffing |
| `*Adapter` — row binding, holders, layout | binding, or `view binding` for a ViewBinding conversion |
| `*Uploader`, upload repositories | uploading |
| `*Manager` | managing |
| `*RepositoryImpl` reads, DAO queries | querying |
| a repository/DAO/controller *starts exposing* a `Flow` | flowing |
| a Fragment/Activity *collects* a `Flow` | collecting |
| Hilt bindings, constructor injection replacing lookups | injecting |
| lazy init, memoisation, reuse of a computed value | caching |
| `res/layout-land/`, landscape cropping and orientation fixes | landscaping |
| a diff that is **nothing but** `app/src/test/` | testing |
| anything with no sharper operation word | handling |

Three of those get chosen wrongly most often:

- **`view modelling` outranks a better verb.** A search debounce plus its view
  model is `life: smoother health search view modelling`, not `… debouncing`.
- **`handling` is a fallback that happens to be the second most common gerund**
  (40/500). If the diff has an operation, name it: `life: smoother achievements
  editing`, not `… achievement handling`.
- **`testing` needs a test-*only* diff.** Tests ship with the change they cover,
  so `test/…` paths appear in most entries without earning the gerund.

The corpus's gerund league table is the full picture; `modelling` and `coloring`
are the established spellings where the log is inconsistent about doubling.

### Layer words, not entity names

When the diff spans two or three files the noun phrase **walks across all of
them**, each contributing a word or two in diff order, and only the gerund is
picked — from whichever suffix best describes the change.

What a file contributes is its **layer word** — `repository`, `dao`, `utils` —
not the entity it is named after: `VoicesRepositoryImpl.kt` + `NewsDao.kt` is
**voices repository dao**, not `voices news dao`. Those layers keep their noun
because none has a natural gerund (nobody writes *repositorying*), so the
operation supplies it and `repository` ends up the most common word in the
corpus after the scopes (131 uses, plus 15 `repositories`, 37 `utils`, 25 `dao`).

Where the suffix *does* supply the gerund it is converted, not repeated:
`activity` and `viewmodel` appear as nouns **zero** times in 500 titles,
`fragment`, `adapter`, `module` and `worker` two or three each. Write `smoother
courses binding`, never `smoother courses adapter adapting`.

```
VoicesRepositoryImpl.kt + NewsDao.kt        → teams: smoother voices repository dao querying
LoginSyncManager.kt + AuthUtils.kt          → sync: smoother login auth utils managing
GuestLoginExtensions.kt + LoginActivity.kt  → login: smoother guest extensions validating
```

The second is the rule in miniature: `LoginSyncManager` gives **login**,
`AuthUtils` gives **auth utils**, `Manager` gives **managing**. Every changed
file is represented and nothing is invented.

Near-duplicates are fine — the qualifier and issue number distinguish them, and
`voices repository dao querying` sits happily beside an earlier `voices
repository querying`. Era vocabulary is fine too: `realm` ran through the
Realm-to-Room migration and vanished, `view binding` is doing it now.

A branch of many small commits still gets **one** title for the whole branch,
not the last commit's: `actions: smoother workflows playstore automerge priority
queuing`.

## `less … is more`

38 of 500. `SKILL.md` has the rule; the myplanet tell is that a
removal-flavoured ending on a `smoother` draft means the shape is wrong —
`smoother enriched-libraries encapsulation` is `less repository enriched
libraries is more`. Check the diff first: one draft ending in `log removing`
landed as `sync: smoother retry repository queue testing`, the diff being tests.
`less` also arrives in sweeps — a dozen of the 38 are the `UploadManager`
teardown — so match a sweep already in the log.

## Dependency bumps

Backtick the full coordinate, `*` for an artifact family, version only — no `v`,
never dependabot's `from A to B`. Gradle and Android coordinates are `all:`,
GitHub Actions are `actions:`:

> `` all: bump `androidx.media3:media3-*` to 1.11.0 (fixes #15548) ``
> `` actions: bump `actions/upload-artifact` to 7 (fixes #16240) ``

## Version bump to check

Every merged PR bumps one patch in `app/build.gradle` (`versionCode = 6888` /
`versionName = "0.68.88"` on 2026-09-01 → `6889` / `"0.68.89"`); the release
workflow tags off `versionName`, so a missing bump collides with the previous
release. Read the values off `master`, not the branch. The automerge drain
pushes the bump itself, so an unbumped branch only matters for a PR going out by
hand.

## Worked examples

**Verb in the incoming title.** Branch `16640-identical-callback-interfaces`,
arriving as *Unify callback interfaces into OnChangedListener*; 14 files under
`callback/`, so `all:`. No suffix rule fires on an interface and the change is
the verb, so the verb becomes the gerund.

> `all: smoother callback listeners unifying (fixes #16640)`

**Deletes a lot, removes nothing.** *Optimize Dispatchers in LoginSyncManager*
over `services/sync/LoginSyncManager.kt` (71+/81−) and `utils/AuthUtils.kt`
(18+/25−). Net-negative, but nothing named is gone — `smoother`, not `less`.

> `sync: smoother login auth utils managing (fixes #15151)`

**Deletion.** `NetworkDependenciesEntryPoint` folded into
`ServiceDependenciesEntryPoint`, touching `di/` and `MainApplication.kt`.

> `all: less network dependencies entry point is more (fixes #15143)`

**Four mistakes in one draft.** `downloads: smoother file-not-found logging
through diagnostics`, over `repository/DownloadRepositoryImpl.kt` and the
diagnostics helper: invented scope, hyphenated compound, preposition, no layer
word.

> `sync: smoother download repository file handling (fixes #16356)`

# myplanet — reference pack

`open-learning-exchange/myplanet`. Kotlin / Android, Gradle, sources under
`app/src/main/java/org/ole/planet/myplanet/`.

Read this together with the shared grammar in `SKILL.md`. Everything here is
what myplanet does *differently* from planet; the shapes, the `smoother`
default and the `(fixes #N)` rules are shared and live in `SKILL.md`.

Corpus: `references/myplanet/title-corpus.md` — the last 500 merged PRs
(#15363 … #16641, 2026-08-10 … 2026-09-01), plus a reconstruction of what the
last 220 of those titles looked like **before** they were prepped and landed.
Read that reconstruction (`## The 27 corrections a prep draft needed`) before
composing: it is a list of the mistakes a prep pass actually makes on this repo.

One myplanet-specific note on the body line `SKILL.md` requires: the automerge
drain (`.github/scripts/automerge.sh`, `link_title_issues`) mirrors a title's
closing reference into the PR body just before it squash-merges, so PRs that go
out through the queue are covered. **PRs merged by hand are not.** Write the
body line at prep time regardless — the drain's pass is a safety net, not the
mechanism, and it is idempotent about refs the body already links.

## Where PRs come from — read this before the mechanics

Of the last 220 merges, **190 (86%) arrived as an agent PR** (task-id branch
suffixes, `openhands/…`, `jules-…`, `claude/…`) and 21 as a human, issue-first
PR. **Not one of 203 recoverable initial titles was in house style**: 77 came
with a conventional-commit prefix (`refactor:`, `perf:`, `feat:`, `chore:`,
`ci:`, even `perf(teams):`), 103 opened with a capitalised imperative verb, 103
named a CamelCase class, and the median was 8 words against a landed median of
4.

So assume you are rewriting from scratch, not editing. **118 of 203 landed
titles share no content word at all with the title the PR arrived with.**

The issue is as likely to exist as not: 138 of 220 landed titles close an issue
numbered *below* their PR (filed first, then handed to an agent), 82 close one
numbered above it (created during the prep pass, from the PR's own title). Check
the three places `SKILL.md` lists before creating anything.

## Scopes

The scope vocabulary is **closed**: these twelve words and nothing else. Over
the last 500 merges the only scope outside the table was `lifel:`, a typo for
`life:`. Inventing a scope out of the feature or layer word in front of you is
the single most common prep mistake — 13 of the 27 observed corrections. The
invented word is usually right, just in the wrong slot: it belongs in the noun
phrase.

`all:` is the workhorse (127/500) and the right default whenever the change
reaches shared layers — `model/`, `repository/`, `di/`, `base/`, `callback/`,
`utils/`, `data/room/`, `MainApplication.kt` — or spans more than one feature.

Reach for a feature scope only when the change sits squarely inside one domain,
including that domain's own repository:

| Scope | Owns | Share |
|---|---|---|
| `sync` | `services/sync/`, `services/upload/`, `services/retry/`, uploads, downloads; `ui/sync/` — see below | 71 |
| `teams` | `ui/teams/**`, `ui/voices/`, `ui/events/`, `ui/surveys/`, team tasks, members | 69 |
| `courses` | `ui/courses/`, `ui/exam/`, `ui/submissions/`, `ui/ratings/`, progress, tags | 67 |
| `resources` | `ui/resources/`, `ui/viewer/`, collections, webview, media playback | 41 |
| `actions` | `.github/workflows/`, `.github/scripts/`, `CLAUDE.md`, `docs/`, `.coderabbit.yaml`, Gradle/CI config | 28 |
| `life` | `ui/health/`, `ui/life/`, achievements, personals | 26 |
| `login` | `ui/settings/`, `ui/user/`, onboarding; `ui/sync/` — see below | 23 |
| `dashboard` | `ui/dashboard/` and the bell — but **not** `ui/notifications/` | 17 |
| `enterprises` | `ui/enterprises/`, finances | 14 |
| `community` | `ui/community/` | 8 |
| `chat` | `ui/chat/` | 8 |

`feedback:` was in the previous window's table with a single use and is **gone**
— zero uses in 500. `FeedbackDao`/feedback repository work now lands as `all:`,
with `feedback` as a noun.

When torn between a feature scope and `all:`, look at where the *centre of
gravity* of the diff sits. A change to `TeamsRepositoryImpl` alone is `teams:`;
the same change plus a shared `RealmRepository` tweak is `all:`.

The corpus carries a generated `## Scope ↔ directory` cross-tab — where each
scope's diffs actually landed, counted. Consult it when a directory is not in
the table above.

### The named traps

`ui/notifications/` is the classic: the bell *icon* on the dashboard is
`dashboard`, but the notifications package itself is always `all` — notifications
are surfaced across the app, not owned by one screen. A prep draft in this
window still wrote `notifications:` and had to be corrected to `all:`.

`ui/sync/` is genuinely ambiguous and stayed that way: six diffs under it landed
`sync:` and six landed `login:`. `sync` if the change is about the sync or login
*transaction*, `login` if it's about the screen and what the user sees. Anything
under `services/sync/` is unambiguously `sync`.

Repo documentation — `CLAUDE.md`, `docs/`, skill files — lands as `actions:`
(alongside the workflow that reads it) or `all:`, never `docs:`.

These are the invented scopes that had to be corrected in this window, with what
they should have been. Read the pattern, not just the list:

| Wrote | Should be | Because |
|---|---|---|
| `retry:` | `sync:` | `services/retry/` is sync's |
| `downloads:` | `sync:` | downloads are sync's |
| `notifications:` | `all:` | surfaced app-wide |
| `voices:`, `members:` | `teams:` | both live under teams |
| `collections:` | `resources:` | collections are a resources screen |
| `health:` | `life:` | `ui/health/` is life's |
| `submissions:` | `courses:` | `ui/submissions/` is courses' |
| `ui:`, `model:`, `diagnostics:` | `all:` | a shared layer is not a scope |
| `docs:`, `ci:` | `actions:` | repo plumbing |
| `login:` (achievements) | `life:` | achievements are life's |

## Reading the phrase off the filenames

myplanet titles are close to a **mechanical function of the changed files** —
163/500 diffs touch a single file beyond the version bump, and 363/500 touch
three or fewer (median: two). Once you see that, most titles write themselves:

**The noun phrase is the principal changed file, de-CamelCased and lowercased,
with its role suffix dropped. The gerund comes from that suffix.**

```
ui/dashboard/BellDashboardFragment.kt   → dashboard: smoother bell reminding
services/upload/PhotoUploader.kt        → sync: smoother photo uploading
utils/Utilities.kt                      → all: smoother utilities hex mapping
services/NetworkMonitorWorker.kt        → all: smoother network monitor working
ui/teams/members/MembersAdapter.kt      → teams: smoother members view binding
repository/UserRepositoryImpl.kt        → sync: smoother user repository shelf batch uploading
di/NetworkDependenciesEntryPoint.kt ✗   → all: less network dependencies entry point is more
```

### Keep it a bare chain of nouns

Of the 492 non-`bump` titles in the last 500, **zero** contain a preposition, an
article, `and`, a comma or a hyphenated compound. The landed median is
`smoother` plus **three words including the gerund** — a two-word noun phrase.
Distribution over the 454 `smoother` titles: one word 9, two 50, three 195,
four 142, five 55, six 3.

Prep drafts fail here constantly, and the fix is always the same — say the layer
and the operation, drop everything that glues them together:

```
courses: smoother filtered-course sort without per-item lowercase
                                        → courses: smoother repository sorting
ui: smoother viewbinding for server address, life, and voices
                                        → all: smoother data binding
members: smoother last-visit date formatting via shared TimeUtils
                                        → teams: smoother members date formatting
dashboard: smoother fragment navigation and tab handling
                                        → dashboard: smoother navigating
```

Compression is not deletion of the layer word: where the draft names the entity
or the symptom, the landed title names the layer the diff sits in.

### Suffix → gerund

| Principal file | Gerund |
|---|---|
| `*Provider`, `*Module`, `*Logger`, `*Interceptor` | providing |
| `*ViewModel` | **view** modelling (always both words — 62 of 65, never bare `modelling`) |
| `*Worker` | working |
| `*Adapter` — `DiffUtil` / `ItemCallback` / payload changes | diffing |
| `*Adapter` — row binding, holders, layout | **binding**, or `view binding` for a ViewBinding conversion |
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

Gerund league table over the 454 `smoother` titles: modelling 65 · handling 40 ·
querying 34 · caching 33 · testing 17 · managing 16 · providing 12 · flowing 10
· filtering 8 · binding 7 · mapping 6 · uploading 6 · checking 6 · diffing 6 ·
landscaping 4 · inserting 4 · configuring 4 · importing 4 · injecting 4.

Four rows moved since the previous window and are worth calling out:

- **`binding` replaced `adapting`.** Adapter row-binding work lands as
  `binding` (7 uses; five of them `view binding` during the ViewBinding
  migration), and `adapting` is down to 2 uses in 500. `diffing` for
  `DiffUtil`/`ItemCallback`/payload work is intact.
- **`working`, `injecting`, `landscaping` are new** and none of them was in the
  previous pack: `all: smoother network monitor working` ←
  `services/NetworkMonitorWorker.kt`; `all: smoother gson injecting` ←
  `di/NetworkModule.kt` and 12 repositories; `courses: smoother submissions
  landscaping` ← `res/layout-land/fragment_my_submission.xml`.
- **`handling` widened and is now the second most common gerund** (40). It is
  no longer only the Fragment/Activity fallback — it is the fallback for any
  principal file with no sharper operation word: `utils/Utilities.kt` → `all:
  smoother utilities toast handling`, `model/MyPlanet.kt` → `all: smoother
  myplanet context handling`. It is still a fallback: a prep draft that reached
  for `handling` when the diff was an edit screen was corrected from `login:
  smoother edit achievement handling` to `life: smoother achievements editing`.
- **`testing` needs a test-*only* diff.** Tests now ship with the change they
  cover, so `test/…` paths appear in most entries and no longer imply the
  gerund. `inserting` collapsed 17 → 4 with the end of the Room migration.

`view modelling` outranks a better verb. If a `*ViewModel` is in the diff, that
is the gerund, however sharp the draft's wording was: `health: smoother patient
search debouncing` → `life: smoother health search view modelling`.

Other gerunds in circulation, for when no suffix rule applies:

> coloring · scoping · linking · loading · requesting · deleting · viewing ·
> sorting · searching · marking · listing · joining · fetching · creating ·
> configuring · syncing · validating · building · checking · finding · mapping ·
> naming · notifying · posting · selecting · sharing · starting · updating ·
> factoring · parsing · counting · indexing · listening · coordinating ·
> picking · editing · exporting · serializing · initializing · normalizing ·
> unifying · navigating · versioning · generating · tagging · formatting

Note `modelling` and `coloring` — the log is inconsistent about doubling, but
those two spellings are the established ones.

### Layer words, not entity names

When the diff spans two or three files, the noun phrase **walks across all of
them** — each contributes a word or two, in diff order — and only the gerund is
picked, from whichever file's suffix best describes the change.

What a file contributes is its **layer word** — `repository`, `dao`, `utils` —
not the entity it happens to be named after. `VoicesRepositoryImpl.kt` +
`NewsDao.kt` becomes **voices repository dao** — one feature word, then the two
layers — not `voices news dao`. `News` is what the voices domain stores, so it
adds nothing `voices` didn't already say.

Those three layers keep their noun because none of them has a natural gerund —
nobody writes *repositorying* — so the gerund comes from the operation instead
(`querying`, `uploading`, `deleting`, `marking`) and the layer stays a noun.
That makes `repository` the most common word in the corpus after the scopes:
131 uses, plus 15 `repositories`, 37 `utils` and 25 `dao`.

The opposite holds wherever the suffix *does* supply the gerund. `Adapter`,
`ViewModel`, `Manager`, `Provider`, `Fragment`, `Activity`, and `Worker` are
converted, not repeated — `activity` and `viewmodel` appear as nouns **zero**
times in 500 titles, `fragment`, `adapter`, `module` and `worker` two or three
each. Don't write `smoother courses adapter adapting`; write `smoother courses
binding`.

```
VoicesRepositoryImpl.kt + NewsDao.kt        → teams: smoother voices repository dao querying
LoginSyncManager.kt + AuthUtils.kt          → sync: smoother login auth utils managing
UploadManager.kt + DispatcherProvider.kt    → sync: smoother upload immediate dispatcher providing
SharedPrefManager.kt + LoginActivity.kt     → login: smoother shared preferences credentials managing
GuestLoginExtensions.kt + LoginActivity.kt  → login: smoother guest extensions validating
```

Read the second one closely, since it's the whole rule in miniature:
`LoginSyncManager` contributes **login** (drop `Sync`, drop the `Manager`
suffix), `AuthUtils` contributes **auth utils**, and `Manager` supplies the
gerund **managing**. Every changed file is represented and nothing is invented.

Don't swerve away from a layer word just because a similar title already
exists. Near-duplicates are fine and common here — the qualifier and the issue
number distinguish them. `voices repository dao querying` sits happily
alongside the earlier `voices repository querying`.

Era vocabulary is fine: `realm` appears in titles from the Realm-to-Room
migration and then disappears; `view binding` is doing the same thing now.
Titles name what the diff touches *today*; don't sand off project-phase words.

A branch made of many small commits still gets **one** title composed for the
whole branch, not the last commit's. The three `actions:` PRs in this window
each carried eight to eleven house-style commit subjects and landed as, e.g.,
`actions: smoother workflows playstore automerge priority queuing`.

## When `less … is more` is the right shape

38 of 500. The `SKILL.md` rule — a named thing ceases to exist — holds, but
there is a myplanet-specific tell: **a removal-flavoured ending on a `smoother`
draft means the shape is wrong.** `removing`, `cleanup`, `encapsulation` were
each corrected in this window:

```
resources: smoother enriched-libraries encapsulation
                    → resources: less repository enriched libraries is more
resources: smoother filter dialog duplicate close button removing
                    → resources: less apply filter button is more
retry: smoother dead queue api surface
                    → sync: less retry repository reset all pending is more
```

It cuts the other way too: `sync: smoother retry repository log removing` landed
as `sync: smoother retry repository queue testing`, because what the diff
actually contained was tests. Check the diff before switching shape.

`less` also arrives in sweeps — a dozen of the 38 are the `UploadManager`
teardown (`sync: less upload manager teams repository is more` and eight
siblings). If your diff is one step of a sweep already in the log, match its
phrasing.

## Dependency bumps

Backtick the full Gradle coordinate and use `*` for a family of artifacts.
Version only — no `v` prefix, and never dependabot's `from A to B`:

> `` all: bump `gradle-wrapper` to 9.7.1 (fixes #16147) ``
> `` all: bump `com.squareup.okhttp3:okhttp` to 5.5.0 (fixes #16017) ``
> `` all: bump `androidx.media3:media3-*` to 1.11.0 (fixes #15548) ``

**The scope depends on what is being bumped**, which `SKILL.md`'s shared table
simplifies: Gradle/Android coordinates are `all:` (6 of 8), GitHub Actions are
`actions:` (2 of 8):

> `` actions: bump `actions/upload-artifact` to 7 (fixes #16240) ``

## Version bump to check

Every merged PR bumps the app version by one patch in `app/build.gradle`
(`versionCode = 6888` / `versionName = "0.68.88"` on 2026-09-01 → `6889` /
`"0.68.89"`). If the PR touches app code and doesn't bump it, mention it — the
release workflow tags off `versionName`, so a missing bump collides with the
previous release.
Read the current values off `master` rather than the branch, since a stale
branch will have drifted behind. In practice the automerge drain's
`github-actions[bot]` pushes a `version: bump to 0.68.NN` commit onto the branch
before merging, so an unbumped branch is normal mid-review and only worth
raising if the PR is going out by hand.

## Worked examples

**Agent PR, verb in the init title.** PR #16641, branch
`16640-identical-callback-interfaces`, arriving as *Unify callback interfaces
into OnChangedListener*. Diff is 14 files under `callback/` — a shared layer, so
`all:`. No suffix rule fires on an interface, and the change genuinely is the
verb, so the verb becomes the gerund.

> `all: smoother callback listeners unifying (fixes #16640)`

**Agent PR, ViewModel in the diff.** Branch
`move-finance-totals-to-viewmodel-7363882240006723470`, arriving as *Move
finance totals calculation into EnterprisesFinancesViewModel*. `ui/enterprises/`
fixes the scope; the `*ViewModel` fixes the gerund.

> `enterprises: smoother finances totals view modelling (fixes #16586)`

**Refactor that deletes a lot but removes nothing.** PR #15040,
Jules-authored, titled `Optimize Dispatchers in LoginSyncManager`, no issue.
Create the issue from that title, then read the diff:
`services/sync/LoginSyncManager.kt` (71+/81−) and `utils/AuthUtils.kt`
(18+/25−). `services/sync/` fixes the scope. Both files feed the noun phrase;
`Manager` gives the gerund. Net-negative, but nothing named is gone — so
`smoother`, not `less`.

> `sync: smoother login auth utils managing (fixes #15151)`

**Deletion.** PR removes `NetworkDependenciesEntryPoint` and folds it into
`ServiceDependenciesEntryPoint`; touches `di/` and `MainApplication.kt`, so
`all`. Primarily a removal, so the `less` shape.

> `all: less network dependencies entry point is more (fixes #15143)`

**A draft that needed all four corrections at once.** Prep proposed
`downloads: smoother file-not-found logging through diagnostics` for a diff over
`repository/DownloadRepositoryImpl.kt` and the diagnostics helper. Invented
scope, a hyphenated compound, a preposition, and no layer word.

> `sync: smoother download repository file handling (fixes #16356)`

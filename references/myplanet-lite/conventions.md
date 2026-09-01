# myplanet-lite — reference pack

`open-learning-exchange/myplanet-lite`. Kotlin / Android, Gradle Kotlin DSL,
sources under `app/src/main/java/org/ole/planet/myplanet/lite/`.

**This pack borrows.** lite is myplanet's sibling app in the same language, so
the phrase mechanics carry over wholesale and there is no separate corpus:

- **Corpus:** `references/myplanet/title-corpus.md`. Use it as written — the
  suffix conversions, layer words and multi-file walks are all directly
  applicable. lite has no corpus of its own because it has no house-style log
  to build one from (see below).
- **Phrase mechanics, layer words, gerund vocabulary:**
  `references/myplanet/conventions.md`, with the deltas in this file applied on
  top.

What this file overrides: the scope table, four suffix rows, the version-bump
file, and the issue expectation.

## ⚠️ You are establishing the style here, not matching it

myplanet and planet both have logs where every line already reads the same way,
and the skill's job is to make one more line match. lite is different: **not one
of the last 200 titles links an issue, and none follow the house style.** They
look like this:

```
🧹 [Code Health] Refactor loadNextCoursesPage in DashboardCoursePageActions (#1178)
🧪 [testing improvement] Add test for DashboardTeamsOperations network failure (#1171)
⚡ perf: Optimize synchronous I/O in flushPendingSurveyOutbox (#1201)
Extract routing logic into AppNavigator (#1160)
```

Consequences, all of them deliberate:

- **Don't skim lite's own log for precedent.** There is none. Go to myplanet's
  corpus.
- **Step 5 of the procedure will fire on nearly every PR.** Zero of 200 titles
  carry `fixes` / `closes` / `resolves`, so almost no lite PR has an issue to
  reuse. Creating one — with the PR's current descriptive title promoted
  verbatim — is the expected path here, not the exception. Those emoji-prefixed
  titles make unusually good issue titles, which is the whole point of the
  promotion move.
- **Say so when you propose the first few.** A house-style title lands in a log
  where nothing else looks like it. That is the intent, but the PR author may
  not know it, so show the before/after and the reasoning rather than just
  renaming.

## Scopes

lite's package tree is flat and mostly one directory deep — 54 files in
`lite/dashboard/`, ~40 more sitting directly in `lite/`, then `util/` (18),
`profile/` (13), `auth/` (5), `surveys/` (3), `model/` (3), `signup/` (1).
**Scope off the class-name prefix, not the directory.** Scoping by directory
would put `dashboard:` on roughly seven titles in ten and carry no information.

The scope names deliberately mirror myplanet's, so the two sibling logs read
side by side.

| Scope | Class-name prefixes |
|---|---|
| `teams` | `Team*`, `DashboardTeam*`, `*Member*`, `DashboardSurvey*`, `Survey*`, `SurveyWizard*`, `Voice*`, `CreateVoice*`, `*Post*`, `*News*` |
| `courses` | `Course*`, `DashboardCourse*`, `CourseWizard*`, `OfflineCourseStorage` |
| `resources` | `Resource*`, `DashboardResource*`, `Audio*`, `*Waveform*`, `FullscreenPdfActivity`, `FullscreenPlayerActivity` |
| `login` | `Auth*`, `Profile*`, `UserProfile*`, `Signup*`, `Token*`, `MyPlanetLiteLogin`, `ProfileCredentialsStore` |
| `sync` | `*Sync*`, `Server*`, `DashboardServer*`, `*Outbox*`, `ServerConnectivity*`, `ServerMetadata*` |
| `dashboard` | `DashboardActivity*`, `AppNavigator`, `SplashScreen`, `DeepLinkResolverActivity`, `DashboardAvatarLoader` |
| `all` | everything else — `util/`, `model/`, `*Utils`, `BaseActivity`, `MyPlanetLite`, `ApplicationScope`, `SecurePreferences*`, `Shared*`, `Language*`, `Gender*`, `*Translat*`, and anything spanning more than one feature |

Same centre-of-gravity test as the other repos: one feature's classes alone →
that feature; the same change plus something from the `all` row → `all:`.

Two things to know about this table:

- **`teams` is broad on purpose.** It absorbs surveys, voices, news and posts,
  exactly as myplanet's `teams` absorbs `ui/voices/`, `ui/events/` and
  `ui/surveys/`. Don't invent a `surveys:` or `voices:` scope — myplanet has
  neither, and the point of mirroring is that a reader of both logs sees one
  vocabulary.
- **`Server*` sits in myplanet's documented border zone.** myplanet flags
  `ui/sync/` as genuinely ambiguous between `sync` and `login`, and lite
  inherits it: `DashboardServerCatalog` and `ServerConfigurationRepository` are
  about picking a server, which is both a login-time screen and a sync
  concern. Same tiebreak — `sync` if the change is about the transaction,
  `login` if it's about the screen and what the user sees.

Scopes that exist on myplanet but have nothing to point at in lite: `life`,
`chat`, `community`, `enterprises`, `feedback`. Don't reach for them.
`actions:` applies if a PR touches `.github/workflows/`, same as everywhere.

## Suffix → gerund: four deltas

myplanet's table applies as written, with these changes.

**`*ViewModel` is dead here — delete that row.** It is myplanet's single most
common gerund (`view modelling`, 40 of 500 titles), and lite contains **zero**
`ViewModel` classes. If you find yourself writing `view modelling` in a lite
title, you have pattern-matched the corpus instead of reading the diff. Same
for `*Dao`, `*Uploader`, `*Worker` and `*Module` — none exist in lite.

**`*Extensions` is the #1 suffix (32 files) and takes no gerund.** lite's
dominant idiom is splitting a screen into extension-function files:
`SurveyWizardBirthDateExtensions`, `DashboardResourcesUploadAudioExtensions`,
`ProfileActivityAvatarExtensions`. Treat `Extensions` exactly like myplanet
treats `repository` and `utils` — it has no natural gerund, so it either stays
a noun or drops out, and the **operation** supplies the gerund. myplanet's own
corpus already does this in the one place it comes up:

```
GuestLoginExtensions.kt + LoginActivity.kt → login: smoother guest extensions validating
```

Applied to lite:

```
DashboardResourcesUploadAudioExtensions.kt  → resources: smoother audio extensions uploading
SurveyWizardBirthDateExtensions.kt          → teams: smoother survey wizard birth date validating
ProfileActivityAvatarExtensions.kt          → login: smoother profile avatar loading
```

Keep the word `extensions` when it earns its place — when the change is *about*
how the file is split — and drop it when the operation already says everything,
as in the last two. Note the first: `Upload` in the class name and `uploading`
as the gerund would be the same word twice, so the noun phrase drops it.

**`*Operations` and `*Actions` behave the same way.** `DashboardTeamsOperations`,
`DashboardCoursePageActions`, `CourseWizardProgressActions` — bundles of
operations, no natural gerund. Drop the suffix and let the specific operation
name the gerund.

**Four new suffixes that *do* supply a gerund**, converted not repeated, exactly
like myplanet's `*Manager` → managing:

| Suffix | lite count | Gerund |
|---|---|---|
| `*Store` | 5 | storing |
| `*Navigator` | 2 | navigating |
| `*Loader` | 2 | loading |
| `*Service` | 3 | from the operation — `ResourceDownloadService` → downloading, `ResourceSyncService` → syncing |

`*Wizard` is a lite-only concept with no myplanet counterpart. It is a noun —
`survey wizard`, `course wizard` — and never a gerund.

The suffix counts for the rest, so you know what you will actually meet:
`Activity` 16, `Repository` 12, `Fragment` 11, `Utils` 8, `Adapter` 5,
`Dependencies` 3, `Provider` 2, `Mapper` 1, `Manager` 1, `Api` 1.

`handling` stays the licensed fallback for `*Activity` and `*Fragment` with no
sharper operation word, same as myplanet.

## Tests

myplanet's rule holds with a different path: **a diff touching only
`app/src/test/` or `app/src/androidTest/` always ends in `testing`**, and the
noun phrase names the class under test. lite's log is full of these — the 🧪
titles are a running test-coverage campaign — so expect the rule to fire often.

```
test/…/DashboardCoursesFragmentTest.kt → courses: smoother dashboard courses fragment testing
test/…/DashboardTeamsOperations…       → teams: smoother teams operations network failure testing
```

## Version bump to check

`app/build.gradle.kts` — **Kotlin DSL, not myplanet's Groovy `app/build.gradle`**
— holds `versionCode = 525` / `versionName = "0.5.25"`, bumped one patch per
merged PR (18 of the last 20 PRs do it). Same rule, different file. Read the
current values off the default branch rather than the PR branch.

## Worked examples

Rewritten from real lite PRs, showing what the skill would produce.

**Refactor, agent-authored, no issue.** PR #1178, titled `🧹 [Code Health]
Refactor loadNextCoursesPage in DashboardCoursePageActions`. No issue anywhere
— create one with that title verbatim. Diff is `DashboardCoursePageActions.kt`;
`DashboardCourse*` → `courses:`, `Actions` drops out, and the operation is
paging through courses.

> `courses: smoother course page loading (fixes #N)`

**Extension-file split.** Diff is `DashboardResourcesListLoadingExtensions.kt`.
`DashboardResource*` → `resources:`; `Extensions` takes no gerund and the
operation is list loading.

> `resources: smoother resources list loading (fixes #N)`

**Test-only diff.** Diff is a single new test for
`DashboardTeamsOperations`'s network-failure path. Test-only → `testing`, and
the noun phrase names the class under test.

> `teams: smoother teams operations network failure testing (fixes #N)`

**Extraction into a new shared class.** PR #1160, `Extract routing logic into
AppNavigator`. `AppNavigator` is app-shell routing, so `dashboard:`, and
`*Navigator` supplies the gerund — which already means routing, so the noun
phrase doesn't repeat it.

> `dashboard: smoother app navigating (fixes #N)`

**Removal.** A PR that deletes an unused helper and folds it into a caller —
the `less` shape, naming the thing that is gone.

> `all: less cursor extensions is more (fixes #N)`

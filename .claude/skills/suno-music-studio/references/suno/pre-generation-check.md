# Pre-Generation Check

The final gate before a track goes to Suno. Run it on one track or every track in an album. **You are a gate, not a fixer**: report pass/fail for each check, name exactly what is wrong and where, and point to the stage that fixes it. Do not rewrite anything during the check.

Order of work this gate sits after: lyrics written (references/lyrics/writing.md) → Suno inputs built ([prompting.md](prompting.md)) → pronunciation resolved ([pronunciation.md](pronunciation.md)) → lyrics reviewed (references/lyrics/review.md) → **this check** → generate.

---

## Instrumental Tracks

First establish whether the track is instrumental. If anything about the track says both "instrumental" and "has vocals" (for example the brief says instrumental but a Lyrics Box with sung words exists, or vice versa), **FAIL immediately** and ask which is true — the gate routing depends on it.

For a confirmed instrumental: mark Gates 2, 3 and 4 `SKIP — instrumental`. In Gate 5, do not require a vocal description or `[Verse]`/`[Chorus]` tags; require genre/instrumentation/mood in the Style Box and structural tags such as `[Intro]`, `[Main Theme]`, `[Bridge]`, `[Outro]`, `[End]`. Instrumental must be On in the settings.

---

## Blocking Gates

Any FAIL here means **NOT READY**. Never say "can proceed with caution" on a blocking gate.

### Gate 1 — Sources Verified
- [ ] If the song makes factual claims drawn from sources (documentary, true-crime, historical, news), a human has verified those sources. Not source-based → `N/A` (passes).
- FAIL if verification is pending. Never generate with unverified sources.
- Fix: walk the user through verifying each pending claim (references/lyrics/compliance.md).

### Gate 2 — Lyrics Complete
- [ ] Lyrics Box contains real lyrics, not template text.
- [ ] No `[TODO]`, `[PLACEHOLDER]`, `TBD` or other draft markers.
- [ ] No parenthetical stage directions or production notes (`(guitars explode)`, `(Verse 1)`) — they would be sung.
- [ ] Within 5,000 characters; length suits the target duration (typically 200–350 words, up to ~500 for rap).
- FAIL if empty, templated, or containing sung-by-accident directions.
- Fix: finish or clean the lyrics (references/lyrics/writing.md).

### Gate 3 — Pronunciation Resolved
- [ ] Every entry in the song's pronunciation table appears **in phonetic form** in the Suno Lyrics Box — every occurrence, every section.
- [ ] No unresolved homographs (live, read, lead, wind, close, tear, bow, bass, wound…).
- [ ] Acronyms, numbers and non-English names are respelled.
- FAIL on any table entry not applied, or any homograph left unfixed. Suno cannot infer pronunciation from context; one missed fix ruins the take.
- Fix: run the pronunciation workflow ([pronunciation.md](pronunciation.md)).

### Gate 4 — Explicit Flag Set
- [ ] The track is marked Explicit **Yes** or **No** (needed at release).
- FAIL if unset — this fails closed.
- Fix: check the lyrics for explicit content and set the flag (references/lyrics/compliance.md).

### Gate 5 — Style Box Complete
- [ ] Style Box is non-empty and within 1,000 characters.
- [ ] Includes a vocal description, placed first (vocal tracks; omitted when a Voice supplies it).
- [ ] Lyrics Box has section tags on every section (`[Verse]`, `[Chorus]`, …).
- [ ] Exclude Styles decided: 0–4 bare elements (`drums`, not `no drums`), within 1,000 characters, or explicitly "none".
- [ ] No inline "no X" phrases in the Style Box (ignored on v6, and can ask for X).
- FAIL on empty Style Box or missing section tags.
- Fix: build the Suno inputs ([prompting.md](prompting.md)).

### Gate 6 — Artist Names Cleared
- [ ] Style Box contains no real artist or band names — check against the blocklist in [prompting.md](prompting.md#artist-name-blocklist) and for any proper name hidden in a phrase ("X-style", "Y-era").
- [ ] Lyrics avoid filter-triggering producer tags (e.g. "ninety-three" → `'93`).
- FAIL on any hit. Suno rewrites names and your intent goes with them.
- Fix: replace each name with a description of the sound (genre, vocal, rhythm, era, instruments).

---

## Advisories (WARN, non-blocking)

Report these; they do not block, but they predict weak output.

- **Descriptor count** — WARN above ~12 Style Box descriptors or on obvious synonym piles. A focused ~10 is fine; 4–7 is a heuristic, not a rule.
- **Performance Cues** — WARN when 2 or more structure tags lack a cue (`[Verse 1 - cold regal]`). Bare tags are a common cause of flat output. Also WARN if any section carries more than 3 bracketed descriptors.
- **Generation Settings** — WARN unless all are recorded:
  - Model is a real current option (`v6`, `v6-wild`, `v6-mini`, `Custom: <name>`); `v6-mini` noted as not releasable.
  - **Variety Off** (above Off, Suno rewrites the Style Box and the checks above are meaningless).
  - Max Mode On for tracks targeting more than ~2:00 (and any Cover or Voice); note it when Off on a track of 2:30 or longer.
  - Duration Auto, or a Custom value that the lyric load fits.
  - With a Voice: no gender/register descriptors in the Style Box; Audio Influence ~0.70–0.85.

---

## Report Format

Single track:

```markdown
# Pre-Generation Check

**Album**: [name]
**Date**: YYYY-MM-DD

## Track: [XX] - [Title]

| Gate | Status | Details |
|------|--------|---------|
| Sources Verified | PASS | Verified 2026-10-01 |
| Lyrics Complete | PASS | 247 words, all sections tagged |
| Pronunciation Resolved | PASS | 3/3 entries applied |
| Explicit Flag | PASS | No |
| Style Box | PASS | "Male baritone, gritty..." (412 chars) |
| Artist Names | PASS | None found |
| Descriptor Count | PASS | 9 descriptors |
| Performance Cues | PASS | 8/8 sections cued |
| Generation Settings | PASS | v6, Variety Off, Max Mode On, Duration Auto |

**Verdict**: READY FOR GENERATION
```

Failing track:

```markdown
## Track: [XX] - [Title]

| Gate | Status | Details |
|------|--------|---------|
| Sources Verified | FAIL | 2 claims pending verification |
| Lyrics Complete | PASS | 312 words |
| Pronunciation Resolved | FAIL | "live" unresolved in V2:L3 |
| Explicit Flag | FAIL | Not set |
| Style Box | PASS | Complete |
| Artist Names | FAIL | "Nirvana" found in Style Box |
| Performance Cues | WARN | 4 tags without cues |
| Generation Settings | WARN | Variety is Normal — set Off |

**Verdict**: NOT READY — 4 blocking, 2 warnings
```

Album summary (after the per-track tables):

```markdown
## Album Summary

| Status | Count |
|--------|-------|
| Ready | 6 |
| Not Ready | 2 |
| **Total** | **8** |

**Blocking issues**: 3
**Warnings**: 1

**Album verdict**: NOT READY — fix 2 tracks before proceeding
```

Verdicts: track → `READY FOR GENERATION` or `NOT READY`; album → `ALL READY`, `PARTIAL` (list the ready tracks) or `NOT READY`.

---

## Rules

1. **Gate, not fixer.** Report; don't edit.
2. **Blocking means blocking.**
3. **Check every pronunciation entry against every section.** One missed respelling ruins the take.
4. **Artist names are sneaky** — read the whole Style Box, not just the start.
5. **Be specific.** "Gate failed" is useless; "`live` in V2:L3 unresolved" is actionable.
6. **Instrumentals skip Gates 2–4.**

When everything passes, present the final Style Box, Exclude Styles and Lyrics Box in separate code blocks with the Generation Settings beneath, ready to copy into Suno.

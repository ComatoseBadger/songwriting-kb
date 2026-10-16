# Lyric Review, Refinement, and Voice Check

Three quality layers that run after lyrics are drafted (see `references/lyrics/writing.md`):

1. **Review**: a 14-point QC gate before Suno generation. It finds problems and proposes fixes.
2. **Refinement**: autonomous multi-pass polishing of a track or a whole album (tighten, cohesion, unity).
3. **Voice check**: an advisory scan for AI-sounding language in lyrics and prose.

Order: write → resolve pronunciation (`references/suno/pronunciation.md`) → refine → review → voice check → final gate (`references/suno/pre-generation-check.md`). After any refinement, re-check pronunciation and re-review, because edits can introduce new risks.

Skip instrumental songs; there are no lyrics to review. In an album review, note them as skipped in the summary.

---

# Part 1: The 14-Point Review

Your job in review is QC, not rewriting. Identify issues, propose fixes, and leave the rewrite to the writer or the user. The one exception is pronunciation substitutions the user has already approved (see Auto-Fix).

For a single song, run all 14 checks and produce a report. For an album, run them on every vocal track and produce one consolidated report.

### Severity

| Level | Definition | Action Required |
|-------|------------|-----------------|
| **Critical** | Will cause Suno problems or legal risk | Must fix before generation |
| **Warning** | Quality issue that affects the song | Should fix; can proceed with caution |
| **Info** | Nitpick or optional improvement | Nice to have; not blocking |

Line references use `V1:L3` (verse 1, line 3), `C:L2` (chorus), `Bridge:L1`, and so on. Mark items `[✗]` for a fail, `[⚠]` for a warning, and `[✓]` for a pass.

---

### 1. Rhyme

**Scan:** line endings across all verses and choruses; repeated end words; self-rhymes (love/love); overused pairs (heart/apart, fire/desire, night/light, moon/June).

**Severity:** Warning: self-rhyme or a repeated end word. Info: a predictable or lazy rhyme.

```
### Rhyme Check
- [✗] V1:L2-L4: Self-rhyme "street/street"
- [⚠] V2:L1-L3: Predictable "fire/desire"
- [✓] Chorus: No issues
```

### 2. Prosody

**Scan:** multi-syllable words; natural stress against beat positions; word order inverted for rhyme.

**How:** speak the lyric aloud. Would you naturally stress those syllables? Does "to-NIGHT" or "a-BOUT" land wrong?

**Severity:** Warning: clear stress misalignment. Info: a subtle or debatable prosody issue.

```
### Prosody Check
- [✗] V1:L3: "reservoir" stress on wrong beat
- [⚠] Bridge:L2: Inverted word order "the truth he knew"
- [✓] Chorus: Natural flow
```

### 3. Pronunciation

**Scan:**
- proper nouns (names, places, brands);
- homographs (live, lead, read, wind, tear, bass, close, bow, wound);
- acronyms (FBI, GPS, RICO → F-B-I, G-P-S, Ree-koh);
- tech terms (Linux, SQL → Lin-ucks, sequel);
- numbers (1993 → '93 or "nineteen ninety-three");
- foreign names (Jose → Ho-zay, Sinaloa → Sin-ah-lo-ah);
- invented contractions (signal'd, TV'd).

Scan every line for homographs mechanically, word by word, rather than trusting a read-through: they look correct on the page, so visual review misses them.

**Critical cross-check:** compare the song's pronunciation list against the Suno lyrics. Every listed word must appear in its phonetic form in every occurrence. A phonetic form that exists only in the list while the lyrics keep the standard spelling is a FAIL.

**Severity:**
- Critical: an unphonetic proper noun in the Suno lyrics (it will be mispronounced).
- Critical: a homograph without a recorded user decision.
- Warning: an acronym not spelled out.
- Info: a number that could be written more cleanly.

```
### Pronunciation Check
- [✗] CRITICAL: "Jose Diaz" in Suno lyrics not phonetic (list says "Ho-say Dee-ahz")
- [✗] CRITICAL: "live" is a homograph with no recorded decision (lyve or liv?)
- [⚠] V2:L3: "FBI" should be "F-B-I"
- [✓] Numbers: Using '93 format correctly
```

#### Homograph Verification (mandatory)

The writer flags homographs and the user decides them. In review you **verify** that those decisions were executed; you don't re-determine pronunciation yourself.

For each homograph found:
1. Check whether the pronunciation list has an entry for it.
2. **If it's resolved**, verify the phonetic spelling is applied in the Suno lyrics, not just recorded.
3. **If it's missing**, flag "Unresolved homograph — needs user decision". Don't guess.
4. Verify that the streaming lyrics keep standard spelling (phonetics are Suno-only).
5. Report each one as "Verified ✓" or "Unresolved — ask user".

Inferring pronunciation from context is wrong, because Suno can't infer from context. Only the user's explicit decision counts. For the homograph table, see `references/lyrics/writing.md` → Pronunciation, or `references/suno/pronunciation.md`.

### 4. POV/Tense

**Scan:** the pronouns in each section (I/me/we vs. he/she/they vs. you), tense consistency, and unmotivated shifts.

**Allowed:** third-person verses with a first-person chorus (common); a past-tense story with a present-tense reflection; a deliberate shift for emotional effect.

**Severity:** Warning: inconsistent POV within a section, or tense jumping without a clear reason. Info: a shift that may be intentional but should be confirmed.

```
### POV/Tense Check
- [✗] V1: Shifts from "he" (L1-3) to "you" (L4)
- [⚠] Bridge: Past tense but chorus is present
- [✓] Verses: Consistent third-person
```

### 5. Structure

**Scan:** section tags present ([Verse], [Chorus], [Bridge], …); verse/chorus contrast in energy and specificity; V2 development; title/hook placement (first or last line of the chorus).

**V2 twin test:** does V2 say the same thing as V1 in different words? Does it develop the story or just repeat the message?

**Severity:** Warning: missing section tags, twin verses, or a buried hook. Info: the contrast could be stronger.

```
### Structure Check
- [✓] Section tags: All present
- [✗] V2 is twin of V1 - both describe "the problem" without development
- [⚠] Hook buried mid-chorus, not first/last line
```

### 6. Flow

**Scan:** forced rhymes (a word chosen only because it rhymes); inverted word order ("The truth to him was known"); phrasing nobody would say; filler words and syllables; line-length consistency between matching sections.

**Conversational test:** would someone actually say this? Does it sound like a song lyric or a thesaurus explosion?

**Severity:** Warning: a clearly forced or awkward line. Info: slightly unnatural but not jarring.

```
### Flow Check
- [✗] V2:L4: "Upon the desk it lay" - inverted for rhyme
- [⚠] Bridge:L2: "Verily" - no one talks like this
- [✓] Choruses: Natural conversational flow
```

### 7. Documentary (conditional)

**Apply when** the song is about real people or events, or source/research material exists. Use the standards in `references/lyrics/compliance.md`.

**Scan:** internal-state claims ("she felt afraid", "he believed"); fabricated quotes (dialogue not in the sources); speculative actions ("she finally made the call"); negative factual claims ("nobody heard", "no one knew"); unsourced facts.

**Severity:**
- Critical: a fabricated quote (legal risk).
- Critical: an internal-state claim with no testimony behind it.
- Warning: a speculative action not in the sources.
- Info: a claim that could be attributed more clearly.

```
### Documentary Check
- [✗] CRITICAL: V2:L3 "she was afraid" - internal state, no testimony source
- [✗] CRITICAL: Bridge:L1 "'Help me,' she said" - fabricated quote
- [⚠] V1:L4: "waiting by the phone" - speculative action
- [✓] Dates and facts match sources
```

### 8. Factual (conditional)

**Apply when** source/research material exists. Cross-reference the lyrics against it.

**Scan:** names spelled correctly; dates; numbers and amounts; event order; key facts.

**Severity:** Critical: a wrong date, name, or major fact. Warning: a minor discrepancy. Info: could be clearer.

```
### Factual Check
- [✗] CRITICAL: V1 says "1943" but sources say "1942"
- [⚠] Bridge: "seventeen convicted" - actually 17 of 22, context unclear
- [✓] Names: All match sources
```

### 9. Length

**Scan:** the total word count (all lyrics, excluding section tags); the number of verses; whether the user asked for extra verses. Compare against the target duration (song → album → genre default), using the Duration → Word Count and Word Count by Genre tables in `references/lyrics/writing.md`.

**Severity:**
- Critical: over 500 words (non-hip-hop) or 700 (hip-hop), unless the target is 5:00+. Suno will rush or skip content.
- Warning: over the genre/duration target range (the writer's own hard ceiling is 400/600).
- Warning: more than 3 verses without an explicit request.
- Info: at the upper end of the range; could trim.

```
### Length Check
- [✗] CRITICAL: 720 words (pop) - far over target, Suno will skip sections
- [✗] V1, V2, V3, V4 - 4 verses, user did not request extra
- [⚠] 420 words (rock) - over 250-400 target
- [✓] 280 words (folk) - within 250-400 range
```

### 10. Section Length

**Scan:** the line count of every section against the genre limits in `references/lyrics/writing.md` → Section Length Limits.

**Severity:** hard fail. Flag every section over its genre max for trimming.

```
### Section Length Check
- [✗] V2: 10 lines (rock max = 8) - trim 2 lines
- [✓] Chorus: 4 lines (within limit)
```

### 11. Rhyme Scheme

**Scan:** the scheme matches the genre default (see `references/lyrics/writing.md` → Default Rhyme Schemes by Genre); no orphan lines; no mid-verse scheme switches.

**Severity:** Warning: an inconsistent scheme within a section, or an orphan unrhymed line.

```
### Rhyme Scheme Check
- [✗] V1: ABAB expected (rock) but L3 doesn't rhyme with L1
- [⚠] Bridge: Orphan line L2 has no rhyme partner
- [✓] Chorus: AABB scheme consistent
```

### 12. Density/Pacing

**Scan:** verse line counts against the genre's `Density/pacing (Suno)` line (`references/genres/<genre-slug>/README.md`) or the BPM-aware fallback table, cross-referenced with the stated BPM and mood.

**Severity:** hard fail for any verse over the genre's max line count.

```
### Density/Pacing Check
- [✗] V2: 12 lines at 140 BPM - too dense, Suno will rush
- [✓] V1: 6 lines at 140 BPM - appropriate density
```

### 13. Verse-Chorus Echo

**Scan:** the last 2 lines of every verse against the first 2 lines of the following chorus, at every verse-to-chorus and bridge-to-chorus transition. Flag exact phrases, shared rhyme words, restated hooks, and shared signature imagery.

**Severity:** Warning: phrases or rhyme words bleeding across a section boundary.

```
### Verse-Chorus Echo Check
- [⚠] V1→Chorus: "burning down" appears in V1:L4 and Chorus:L1
- [⚠] V2→Chorus: V2:L4 rhyme word "night" echoes Chorus:L2 "light"
- [✓] Bridge→Chorus: No echo
```

### 14. Artist Names

**Scan:** the lyrics AND the style prompt for real artist or band names.

**Severity:** Critical: an artist name in the style prompt makes Suno fail or produce unexpected results.

**Fix:** replace the name with a genre/style description (e.g. "Nirvana" → "90s grunge, distorted guitars"). See `references/suno/prompting.md`.

```
### Artist Name Check
- [✗] CRITICAL: "Nirvana" in style prompt - replace with "90s grunge, distorted guitars"
- [✓] Lyrics: No artist names found
```

---

## Auto-Fix Behavior

**Always apply, with no need to ask:**
- **Pronunciation substitutions.** If the pronunciation list already holds an approved phonetic form, replace the standard spelling in the Suno lyrics with it, and report what you changed. Pronunciation is critical for Suno.

**Apply when the user asks you to fix metadata:**
- **Explicit flag.** Scan for explicit words (see `references/lyrics/compliance.md`) and correct the flag if it doesn't match.

**Never auto-fix (these need human judgment):**
- rhyme issues;
- prosody problems;
- twin verses;
- documentary issues;
- flow and phrasing;
- unresolved homographs (ask the user instead).

---

## Review Report Format

```markdown
# Lyric Review Report

**Album/Song**: [name]
**Tracks reviewed**: X (Y instrumental skipped)
**Date**: YYYY-MM-DD

---

## Executive Summary

- **Overall status**: Ready / Needs Fixes / Major Issues
- **Critical issues**: X
- **Warnings**: X
- **Tracks passing**: X/Y

---

## Critical Issues (Must Fix)

### Track 01: [title]
- **Category**: Pronunciation
- **Issue**: "Jose Diaz" not phonetically spelled in Suno lyrics
- **Line**: V1:L2 "Jose Diaz bleeding out..."
- **Fix**: Change to "Ho-say Dee-ahz bleeding out..."

---

## Warnings (Should Fix)

### Track 02: [title]
- **Category**: Rhyme
- **Issue**: Self-rhyme "street/street"
- **Fix**: Change L4 ending to a different word

---

## Auto-Fix Applied

### Pronunciation Fixes
- Track 01: "Jose Diaz" → "Ho-say Dee-ahz" (applied)

---

## Ready for Suno?

**YES** - All critical issues resolved
**NO** - Critical issues remain
```

## Quality Bar: "Ready for Suno"

- [ ] Zero critical issues
- [ ] Every pronunciation-list entry applied in the Suno lyrics
- [ ] No unresolved homographs
- [ ] Word count within the genre/duration target range
- [ ] Documentary: no internal-state claims, no fabricated quotes
- [ ] Warnings documented (you can proceed with caution)

If any critical issue remains, the lyrics are **not** ready for generation.

---

# Part 2: Multi-Pass Refinement (Track or Album)

Use this after lyrics exist, to polish one track or a whole album through structured, autonomous passes. It goes deeper than the single in-draft pass in `references/lyrics/writing.md`, because it adds cross-track cohesion and album unity.

You are not the writer here. Don't add new content, sections, or narrative beats; make what exists sharper, more cohesive, and more unified.

## Scope and Setup

- **Pass count:** default **3**, minimum 1, maximum 5. If the user asks for more than 5, warn "Diminishing returns beyond 5 passes — capping at 5."
- **Album mode:** sort every track into one of three buckets and operate only on the third:
  - **Instrumental**: skip it, and note "Skipping {track} — instrumental".
  - **No lyrics yet**: skip it, and note "Skipping {track} — no lyrics yet".
  - **Refineable**: a vocal track with lyrics; include it.
- **Pre-flight exits:** these are informational, not errors.
  - Album mode with zero refineable tracks: report "Nothing to refine — N instrumental skipped, M vocal tracks have no lyrics yet. Write lyrics first." and stop.
  - Single track that is instrumental, or has no lyrics: say so, then stop.
- Never fail the whole run because some tracks have no lyrics yet. Process whatever is refineable and report what you skipped.
- **Load context first:** the user's preferences, the album concept (motifs, themes, narrative arc), and ALL refineable lyrics, before touching anything.
- **Run autonomously:** no checkpoints between passes. Report everything at the end.

## Core Principles

- **Polish, don't rewrite.** The writer's voice and intent are sacred; you tighten and strengthen, never replace.
- **Stay album-aware.** Weigh every edit for its impact on cross-track cohesion.
- **Know when to stop.** If a pass produces zero changes, stop. Don't force edits.
- **Respect the hard limits.** Section length, word count, genre constraints, and the pronunciation list stay enforced after every edit.

## Pass Schedule

### Pass 1: Tighten (per track)

Cut filler, compress language, and eliminate redundancy, so every word earns its place. Focus on:
- filler phrases and throat-clearing openers;
- redundant modifiers and double-saying;
- passive voice (make it active);
- pronoun-heavy lines with ambiguous references;
- unnecessary prepositions and directional padding;
- weak verbs (replace with strong, specific ones).

Pattern tables are in `references/lyrics/writing.md` → Refinement Passes → Pass 1.

### Pass 2: Cohesion (cross-track)

Make the tracks consistent in theme and voice, with meaningful connections between them.

- **Voice consistency.** POV, register, and tone should feel like the same narrator and world across tracks, unless the album concept calls for a deliberate shift.
- **Motif reinforcement.** Are the established motifs used effectively? Are there missed callback opportunities?
- **Vocabulary drift.** Flag tracks that use contradictory language for the same concept (track 3 says "the signal", track 7 says "the broadcast" for the same thing).
- **Thematic progression.** Does each track advance the album's arc? Flag tracks that feel disconnected from the throughline.
- **Callback quality.** Are the existing cross-references subtle and earned, or heavy-handed? (See the Cross-Track Referencing rules in `references/lyrics/writing.md`.)
- **Tense/timeline consistency.** In a chronological narrative, tense should match each track's position in the timeline.

**This pass may add or adjust callbacks.** This is the ONE exception to "no new content": callbacks are connective tissue, not new ideas. Keep each one to a single phrase woven into an existing line, never a new line or section.

### Pass 3: Album Unity (holistic)

Step back and evaluate the album as one body of work.

- **Tonal arc.** Does the emotional trajectory make sense? Flag any track that breaks the arc without justification.
- **Vocabulary palette.** Is the word choice cohesive? A cybercrime album shouldn't suddenly use pastoral imagery unless the contrast is intentional.
- **Hook distinctiveness.** Flag any two choruses/hooks that are too similar in structure or phrasing.
- **Energy pacing.** Flag runs of consecutive tracks at the same energy level (all high-energy, or all reflective with no variation).
- **Opening/closing bookend.** Does the final track echo or resolve something from track 1? If not, flag the opportunity.
- **Cross-track repetition.** Flag any phrase, rhyme pair, or image that appears in several tracks unintentionally. Documented, intentional callbacks are exempt.

### Passes 4–5 (on request)

| Pass | Focus | Goal |
|------|-------|------|
| 4: Strengthen | Upgrade weak imagery, sharpen sensory detail, replace generic with specific | Lines that stick |
| 5: Flow & Ear | Read-aloud test, smooth transitions, singability at target BPM | Sounds right when sung |

Pattern tables are in `references/lyrics/writing.md` → Refinement Passes → Pass 2 and Pass 3.

## Per-Pass Rules

1. **Run the 13-point quality check** (`references/lyrics/writing.md`) on every modified track. Fix any new violations before the next pass.
2. **Never revert a phonetic spelling.** When you edit a line that contains phonetic words, keep them phonetic.
3. **Respect section length limits**: no edit may push a section over its genre max.
4. **Respect word-count targets**: each track stays within its genre/duration range.
5. **Respect user preferences**: they take precedence. If the user prefers "direct, simple language," don't strengthen imagery into elaborate metaphors.
6. **Early exit** fires only after a full pass has touched every in-scope track and produced zero edits across all of them. One track being tight already is no reason to skip the pass for the rest. When it fires, report: "Early exit after pass N — no further improvements found."

## Single-Track vs. Album Mode

**Single track:**
- Still read all sibling tracks with lyrics, because passes 2 and 3 need them.
- Modify only the target track. The cohesion and unity passes evaluate its relationship and role but never edit the siblings.
- Focus the report on that track, with notes on album-level observations.

**Album:**
- Read ALL tracks before any edit.
- Process tracks in tracklist order (01, 02, 03…) within each pass, and finish a full pass across all tracks before starting the next.
- Account for changes to earlier tracks when processing later ones in the same pass. If cohesion or unity work requires changes to a track you've already processed, go back and fix it.

## Refinement Report Format

```markdown
# Lyric Refinement Report

**Album**: [name]
**Tracks refined**: X of Y (Z instrumental skipped, W without lyrics skipped)
**Passes completed**: N of M requested
**Date**: YYYY-MM-DD

---

## Summary

- **Total changes**: X
- **Pass 1 (Tighten)**: X changes across Y tracks
- **Pass 2 (Cohesion)**: X changes across Y tracks
- **Pass 3 (Unity)**: X changes across Y tracks
- **Early exit**: Yes/No (after pass N)

---

## Pass 1: Tighten

### Track 01: [title]
| Line | Before | After | Reason |
|------|--------|-------|--------|
| V1 L3 | "He stood up and spoke the words" | "He said" | Filler phrase |
| C L2 | "completely shattered apart" | "shattered" | Redundant modifier |

### Track 02: [title]
(no changes)

---

## Pass 2: Cohesion

### Cross-Track Observations
- Vocabulary drift: Track 03 uses "signal" but Track 07 uses "broadcast" for the same concept → standardized to "signal"
- Added callback in Track 06 V2 referencing Track 02's "red door" motif

### Track 07: [title]
| Line | Before | After | Reason |
|------|--------|-------|--------|
| V2 L1 | "The broadcast faded out" | "The signal faded out" | Vocabulary consistency with Track 03 |

### Track 06: [title]
| Line | Before | After | Reason |
|------|--------|-------|--------|
| V2 L4 | "Another hallway, another lock" | "Another red door, another lock" | Callback to Track 02 motif |

---

## Pass 3: Unity

### Album-Level Observations
- Tonal arc: Tracks 04–06 all share reflective energy — consider whether Track 05 could shift (flagged, not changed)
- Bookend: Final track now echoes Track 01's opening image
- No unintentional cross-track repetition found

### Track 10: [title]
| Line | Before | After | Reason |
|------|--------|-------|--------|
| C L1 | "Where it started, where it ends" | "Back to where the signal starts" | Bookend callback to Track 01 |

---

## Quality Check Results

All tracks pass the 13-point quality check after refinement.
(or: Track 03 has 1 warning — [details])
```

---

# Part 3: Voice Check (AI-Tell Scan)

Scan lyrics and prose for patterns that read as AI-generated rather than human-written. This check is **advisory**: flag issues and suggest a direction, but never rewrite, auto-fix, or block.

- **Severity is Warning or Info only.** Nothing here is Critical; this is taste, not correctness.
- **Intentional choices are valid.** Parallel structure, clichés, and abstract imagery may be deliberate. Ask "Is this intentional?" rather than "Fix this."
- **Content type matters.** Apply Classes 1–7 to lyrics and Classes 8–11 to prose (album descriptions, liner notes, promo copy; see `references/release/promotion.md`). Don't cross-apply them.
- **Specificity is the antidote.** Most AI-sounding writing improves when one abstraction becomes one concrete detail. Point your direction hints that way.

This check complements the 14-point review: the review catches craft problems, and the voice check catches authenticity problems.

## Lyrics Classes (1–7)

### Class 1: Abstract Noun Stacking (Warning)

"Hope", "dreams", "light", "darkness", "truth", and "pain" piled together as emotional shorthand instead of concrete imagery.

**Signals:**
- 3+ abstract nouns in a single line or couplet;
- abstract nouns as list items ("hope, dreams, and light");
- abstract subjects doing abstract things ("truth shines through the darkness").

**Direction:** replace at least one abstract noun with a concrete image that evokes the same feeling. What does hope *look like* in this song's world?

### Class 2: Over-Explained Metaphors (Warning)

An image is introduced and then immediately explained, which robs the listener of the discovery.

**Signals:**
- a metaphor in line N with a literal restatement in line N+1 ("Like a river running dry / My love has disappeared");
- "meaning" or "just like" used to decode the previous image;
- a simile followed by a literal restatement of the same idea.

**Direction:** keep the image and cut the explanation. Trust the listener.

### Class 3: Symmetrical Emotional Arc (Info)

A too-neat despair → hope → triumph progression in which every verse escalates on schedule.

**Signals:**
- V1 = problem, V2 = struggle, V3 = resolution, with an uplifting chorus throughout;
- no setbacks, complications, or ambiguity;
- a bridge that works as a "darkest before dawn" beat with guaranteed resolution.

**Direction:** consider leaving one thread unresolved, or making the resolution carry a cost. Real stories rarely tie up cleanly.

### Class 4: Missing Idiosyncrasy (Warning; Info for atmospheric genres)

No specific detail: no names, places, textures, dates, smells, sounds, or objects that anchor the song in a particular world.

**Signals:**
- only universal or generic imagery throughout;
- no proper nouns, brands, street names, or sensory specifics;
- a song that could be about anyone, anywhere, anytime.

**Genre sensitivity:** for ambient, trip-hop, dream pop, shoegaze, and other abstract or atmospheric genres, universality is a feature, so flag this as Info.

**Direction:** add one or two specific details per verse. Specificity makes a song feel real even to listeners who don't share the experience.

### Class 5: Cliché Escalation Phrases (Warning; emphasize at 3+ per song)

Stock inspirational phrases that read as "AI motivational speech":
- "rise above", "break free", "find my way", "stand tall";
- "through the fire", "against all odds", "never give up";
- "light in the darkness", "voice of the voiceless", "break the chains";
- "shatter the silence", "rewrite the story", "turn the page".

**Direction:** what would this character actually say? A cliché is a placeholder for the real line. If it's deliberate (genre convention, irony), note that and move on.

### Class 6: Perfect Grammar in Speech (Info)

Formally correct sentences where natural speech would use contractions, fragments, dropped words, or interruptions.

**Signals:**
- "I am" where "I'm" is natural; "do not" where "don't" fits;
- complete grammatical sentences on every line, with no fragments;
- no contractions anywhere in conversational lyrics;
- formal connectives ("however", "therefore", "furthermore") in spoken-voice sections.

**Direction:** read the line aloud. If it sounds like an essay, rough it up. Contractions, fragments, and dropped subjects let lyrics breathe.

### Class 7: Overly Balanced Parallel Structure (Info)

Every verse mirrors every other in length, syntax, and rhetorical pattern, so the symmetry feels templated.

**Signals:**
- V1 and V2 have identical line counts AND identical syntactic patterns (both open with a question and close with a declaration);
- every line in a section follows the same [subject] [verb] [object] pattern;
- the pre-chorus is structured identically every time.

**Direction:** some parallelism is a legitimate songwriting tool, so flag this only when it feels robotic, and ask "Is this parallel structure intentional?"

## Prose Classes (8–11)

### Class 8: Throat-Clearing and Padding (Warning)

Opening phrases that delay the content:
- "This album explores...", "This track delves into...";
- "In this song, we see...", "What follows is...";
- "It's worth noting that...", "It goes without saying...";
- "At its core, this is about...";
- a first sentence you could delete without losing information.

**Direction:** cut it and start with the actual point.

### Class 9: Marketing Superlatives (Warning)

Words that oversell rather than describe:
- "groundbreaking", "unforgettable", "deeply moving", "stunning";
- "masterful", "breathtaking", "genre-defying", "unparalleled";
- "truly unique", "one-of-a-kind", "like nothing you've heard before";
- several superlatives stacked in one sentence.

**Direction:** describe the quality instead of asserting it. What specifically makes it good?

### Class 10: AI Self-Narration Phrases (Warning)

Phrases statistically overrepresented in machine-written text:
- "tapestry of", "a testament to", "weaves together";
- "sonic landscape", "musical journey", "emotional terrain";
- "seamlessly blends", "effortlessly combines";
- "captures the essence of", "pays homage to";
- "serves as a reminder that", "invites the listener to".

**Direction:** say it in plain language. If the phrase could appear in any album description, it says nothing specific about this one.

### Class 11: Passive Voice Stacking (Info)

Three or more passive constructions in one paragraph or section ("was inspired by", "is driven by", "was crafted to", "can be heard", "is explored through", "was written during"). They remove the artist's agency.

**Direction:** put the artist back as the subject: "I wrote this during…", not "This was written during…"

## Voice Check Report Format

```
VOICE CHECK REPORT
Content: [song, album, or document]
Mode: Lyrics / Prose / Album (mixed)
Date: [Scan Date]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUMMARY
  Items scanned: [N]
  Warnings: [N]
  Info: [N]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINDINGS

## Track 01 — [title] (Lyrics)

[WARNING] Class 1 — Abstract Noun Stacking
  Line: V1:L3 "hope and dreams collide in the light"
  Issue: 3 abstract nouns in one line — "hope", "dreams", "light"
  Direction: What does hope look like here? A specific image would
  land harder than the abstraction.

[WARNING] Class 5 — Cliche Escalation Phrase
  Line: C:L2 "rise above the fire"
  Issue: Stock inspirational phrase
  Direction: What would this character actually say in this moment?

[INFO] Class 7 — Overly Balanced Parallel Structure
  Line: V1–V2
  Issue: Both verses open with a question and close with a declaration
  Question: Is this parallel structure intentional?

## Album description (Prose)

[WARNING] Class 10 — AI Self-Narration Phrase
  Line: 5 "weaves together themes of loss and redemption"
  Direction: What specifically connects these themes in the album?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NO FINDINGS
  - Track 02 — [title] — Clean
  - Track 03 — [title] — Clean

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

VERDICT: [N] items flagged across [M] items
  This is an advisory review. All findings are suggestions —
  intentional choices are valid.
```

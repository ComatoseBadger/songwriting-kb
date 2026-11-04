# The Suno Optimization Method

> **CANONICAL METHODOLOGY** -- This file is the single source of truth for Suno AI optimization.
> A non-Kiro user can read ONLY this file and prepare any song for optimal Suno rendering.
> For the complete tag catalog, see `references/SUNO_TAGS_REFERENCE.md`.
> For genre/key/BPM tables, see `references/SUNO_STYLE_GENRE_REFERENCE.md`.

---

## Current Suno v6 workflow (2026-10-29)

This section governs new tracks and supersedes conflicting legacy instructions below.
The October 28–29 requirements are **user workflow policy**, not claims about Suno's parser.
Use [the complete package template](../../templates/suno-v6-song.md).

### Evidence and platform scope

**Officially documented:** [Current Models](https://help.suno.com/en/articles/13924737)
describes v6, v6-wild and v6-mini. The [v6 FAQ](https://help.suno.com/en/articles/13924481)
states that earlier models are retired, Variety modifies Style prompts (0 retains control),
and Max Mode uses more credits. These facts do not guarantee any particular render.
[Creative Sliders](https://help.suno.com/en/articles/6141377) documents Weirdness and
Style Influence, with Audio Influence for audio uploads.
[Personas](https://suno.com/products/personas) carry a song's voice and style profile;
this is support for continuity, not a guarantee of an identical singer.
Sources checked 2026-10-29. Availability can depend on account, mode and UI.

**House recommendations:** Style <=1000 characters per alternative and Lyrics <=5000
are conservative repository budgets, not newly verified v6 platform ceilings.
Genre-first, descriptor counts, era cues, exact slider ranges and bracket directives
are creative heuristics. Tags such as `[control:]`, `[sequence:]`, `[Title:]`,
`[Production Direction:]`, `[Vocal Direction:]` and `[end]` are house notation;
no claim is made that v6 treats them as deterministic commands. Listen to the render.
Do not move positive overflow into Exclude or invent an Advanced Settings text box.

### Before production lock

1. State the song thesis and a reusable **Vocal Identity** anchor: register, timbre,
   phrasing/accent, clean/harsh balance and emotional delivery. Repeat that concise
   anchor verbatim in each Style alternative. Keep the singer recognizable while
   changing the arrangement. Record the selected Persona/Voice if available; audit
   any automatically populated Style text for unwanted palette repetition.
2. Provide at least **two meaningfully different Style prompts** in separate
   `## Style Prompt A`, `## Style Prompt B` sections. Front-load the defining sound
   and vocal identity; a useful starting constraint is <=2 genre anchors, 3–4 named
   instruments and two mood/energy words. These are editing recommendations, not
   parser limits. Change tempo feel, rhythmic engine, guitar/synth roles, ambience
   and section-entry behavior rather than substituting synonyms. Count each prompt
   independently. Keep alternatives visible after selection.
3. Provide at least **two Intro Concepts** with different opening mechanisms.
   Options include immediate full-band, vocal-first, bass-led, guitar-signature,
   drum-led, cold verse or a custom architecture. For each, specify mechanism,
   first sound, groove (kick/snare behavior), vocal entry, sound envelope and
   transition into the next section. Connect the mechanism to the song's emotion.
   Do not default to ambient swells, synth pulses, risers or gradual drum builds;
   use them only with a specific musical reason. No fixed BPM, chord pattern,
   section order, vocal effect or formula is mandatory across tracks.
4. Run the **Intro Differentiation Gate** on the first **15–20 seconds** against
   the previous **three tracks when available**. Name each reference and compare
   first sound/envelope, groove, vocal entry and transition. Explain the audible
   difference and revise a repeated fingerprint. With fewer tracks, list those
   available; with none, record `History: unavailable` and explain why. Never invent
   comparisons. A text plan is provisional until audio is heard.
5. Record `Production Lock` status (`draft` or `locked`) and selected Style/Intro
   IDs. Lock only after alternatives, voice continuity and gate review. If history
   is unavailable, explicitly disclose that limitation. A locked document records
   an arrangement decision, not proof of audio quality.

### Complete output and controlled iteration

Keep output in ordinary chat unless a file is requested. Include thesis, Vocal
Identity, Style alternatives, Intro Concepts, Intro Differentiation Gate, Production
Lock, Exclusions, Lyrics, Production Notes, **Advanced Options**, **Changes** and
**Next Changes**. The validator accepts the combined `Changes / Next Changes` heading
as well. Metadata stays outside the paste-ready Lyrics and Style blocks.

Preserve craft checks: emotional progression, distinct verse development, strong
hook, natural language, rhyme that serves meaning, breath placement, prosody,
section contrast, named vocal layers and artist-reference conversion. Retain key,
BPM, time signature, Nashville AND actual chords, vocal description, instrument
prominence, dynamics, hook placement, rhyme scheme and emotional arc in Production
Notes. Choose these for this song, rather than filling a recurring formula.

Advanced Options must record Model, Persona/Voice, Weirdness, Style Influence,
Audio Influence (or N/A), Exclude, Variety and Max Mode (or unavailable). Explain
song-specific recommendations and tradeoffs; do not impose universal values.
For controlled comparisons, Variety 0 is a useful recommendation because the FAQ
says it preserves Style control. Keep paid generation manual unless authorized.

Changes describes edits already made (or explicitly none); Next Changes gives
prioritized optional improvements and a listening test. Change one variable at a
time during diagnosis. Recheck singer identity and first 15–20 seconds after renders.

### Validation contract

`python3 tools/validate-song.py song.md` validates the v6 package by default.
`--legacy` retains the older single-prompt format for historical files. Every Style
alternative gets the existing length, genre, tag-count, artist and layer checks.
The v6 checks enforce visible sections, distinct alternatives and intro mechanisms,
voice-anchor reuse, gate documentation and selection references. They cannot judge
musical distinctness, hear audio, or certify vocal continuity. Human listening is
required even when structural checks pass.

## Legacy reference (v4.5–v5.5; not v6 guarantees)

## Overview

Suno optimization is the FINAL technical pass before rendering. It does NOT change creative content -- it adds technical formatting that ensures Suno produces the best possible output. If the song was written with the full songwriting procedure (which includes formatting), this SOP functions as a verification pass.

---

## Three-Tier Evidence Labeling System

Claims in this methodology carry one of three evidence tiers:

| Label | Meaning |
|---|---|
| **[Tier 1: Scholarship-backed]** | Documented academic framework with primary sources and peer-reviewed research. |
| **[Tier 2: Professional heuristic]** | Widely-used craft guidance supported by professional practice but not empirically validated as universal law. |
| **[Tier 3: Community/platform heuristic]** | Empirical observation from practitioner testing (e.g., Suno community experiments). Unverified, version-dependent. |

Unlabeled claims are general craft consensus or structural descriptions that do not require tiering.

> **Note:** Most Suno-specific claims in this document are Tier 3 unless otherwise noted. Suno's behavior changes across versions; verify against the version you are using.

---

## The Complete 13-Step Optimization Procedure

### Step 1 -- Character Count Audit

**Measure Style Prompt:**
- Copy the full genre/BPM/mood description
- Count characters (must be <=1000)
- If over: move negatives/exclusions to Exclude field first, then trim least essential descriptors

**Measure Lyrics Field:**
- Count from `[track:]` through `[end]` (including ALL tags, direction blocks, section tags)
- Must be <=5000 characters
- If over: trim direction blocks first, reduce section production tags, shorten outro
- If still over: overflow additional direction to Suno's Advanced Settings box

**Record counts:**
```
Style: ___/1000 chars
Lyrics: ___/5000 chars
```

### Step 2 -- Add Global Control Tags

If missing, add at the TOP of Lyrics field (before first section):

```
[track: genre: [your genre], mood: [your mood], length: [seconds]]
[control: no-repeat, dynamic transitions]
[sequence: [list all sections in order]]
```

**Length calculation:** (total lyric lines x 2.5) + intro/outro bars x (60/BPM x 4). Round to nearest 15 seconds.

**Sequence:** List EVERY section tag that appears, in order:
```
[sequence: intro, verse, pre-chorus, chorus, verse, pre-chorus, chorus, bridge, final chorus, outro]
```

### Step 3 -- Validate Control Parameters

Only these `[control:]` values are confirmed valid (tested v4.5/v5.0):
- `no-repeat` -- prevents auto-looping
- `dynamic transitions` -- enables section contrast
- `instrumental` -- removes vocals entirely

**Invalid (remove if present):** `build across sections`, custom phrases, unconfirmed terms.

### Step 4 -- Optimize Section Tags

**Convert stacked tags (>3 per section) to pipe notation:**

```
BEFORE (too many stacked):
[Heavy drums]
[Distorted bass]
[Staccato guitar]
[Cave reverb]

AFTER (pipe notation):
[chorus | powerful, heavy drums, distorted bass, cave reverb]
```

**Valid pipe parameters:**
- Adjectives/descriptors: powerful, intimate, wide, dark, stripped, rising, sparse, full, layered, driving
- Vocal delivery: vulnerable vocals, close-mic, whispered, spoken

**Invalid pipe parameters (move elsewhere):**
- Instrument instructions: "cello enters low", "drums enter soft"
- Custom phrases: "maximum width", "build across sections"

**Practical limit:** 2-4 pipe parameters per section tag. Beyond 5, Suno may deprioritize later descriptors.

### Step 5 -- Add Vocal Delivery Tags

Per-section vocal tags SUPPLEMENT the global Vocal Direction block -- they specify WHERE a delivery change happens.

| Section Character | Tag to Add |
|---|---|
| Confessional/grief/intimate | `[vulnerable vocals]` in pipe or standalone |
| Lead vocal whispered | `[whisper]` before the line |
| Background whisper atmosphere | `[whispering]` as texture tag |
| Spoken/non-sung | `[spoken word]` or `[narrator]` |
| Repeated hook/mantra | `[chant]` |
| Dialogue/call-response | `[call-and-response]` |

### Step 6 -- Add Dynamics Tags

Dynamics can be standalone tags or pipe parameters:

| Moment | Standalone Tag | Pipe Alternative |
|---|---|---|
| Pre-chorus building | `[build]` | `[pre-chorus | building, rising tension]` |
| Dramatic silence | `[silence: sudden]` | N/A (mid-section event) |
| Key change | `[modulation: ascending]` or `[modulation: sudden]` | N/A |
| Volume increasing | `[crescendo]` | `[section | swelling, crescendo]` |
| Volume decreasing | `[diminuendo]` | `[section | fading, pulling back]` |
| Rhythm change | `[beat-switch: half-time]` | N/A |
| Grand ending | `[big finish]` | `[final chorus | powerful, big finish]` |
| Held note | `[fermata]` | N/A |

Use standalone tags for mid-section dynamic events. Use pipe parameters when the dynamic applies to the entire section.

### Step 7 -- Add Termination

At the very bottom of lyrics:
```
[end]
```

If the song should fade rather than cut:
```
[fade: layered]
[end]
```

### Step 8 -- Check for Obsolete Tags

Scan for and REMOVE any of these:

| Obsolete Tag | Action |
|---|---|
| `[bpm: X]` | Put BPM in Style Prompt text |
| `[key: X]` | Put key in Style Prompt text |
| `[loop]` | Remove entirely (unsupported) |
| `[autotune]` | Remove (deprecated) |
| `[mix]` / `[master]` | Remove (ineffective) |
| `[volume]` | Use dynamics tags instead |
| `[filter]` | Describe in Production Direction |
| `[section: X]` | Use specific section names |

### Step 9 -- Artist Reference Conversion

If any artist or band name appears in the Style Prompt, Production Direction, or Vocal Direction as creative shorthand (e.g., "in the style of Radiohead", "Billie Eilish vibes"), convert it to descriptive production language BEFORE final output. Artist names are not recognized as Suno prompt parameters -- descriptive language gives Suno actionable production instructions.

**Conversion method:** Translate the artist's SOUND into: genre + era + instruments + production characteristics + vocal style + structural habits. The artist name should NOT survive into the Style Prompt or Production Direction.

| Artist Reference | Converted To |
|---|---|
| "In the style of Radiohead" | "Atmospheric post-rock, electronic textures, unconventional structures, falsetto vocals, quiet-loud dynamics, 2000s experimental production" |
| "Like Billie Eilish" | "Dark minimal pop, whispered close-mic vocals, heavy sub bass, sparse production, intimate bedroom aesthetic, 2019 lo-fi pop" |
| "Wardruna vibes" | "Nordic folk, ancient instrumentation, throat singing textures, ritualistic percussion, vast reverb, pre-Christian atmosphere" |
| "Sigur Ros feel" | "Ethereal post-rock, bowed guitar, falsetto vocals as texture, glacial builds, Icelandic atmosphere, vast reverb spaces" |
| "Like Hozier" | "Dark folk-rock, rich baritone, gospel-influenced builds, literary lyrics, organic production, Celtic-soul fusion" |

**Why this matters:** Suno does not understand "make it sound like [Artist]." It DOES understand specific production descriptors, era references, genre combinations, and vocal delivery characteristics. Converting artist references to descriptive language produces dramatically better renders.

### Step 10 -- Verify Suno Compatibility

Final checklist:
- [ ] No prohibited end punctuation on lyric lines (no periods, commas, semicolons, exclamation marks, question marks). Em-dashes are allowed for phrasing/breath. Apostrophes and hyphens are fine.
- [ ] Each line = one melodic phrase
- [ ] 4-8 lines per section maximum (instrumental sections with only a tag and no lyrics are valid)
- [ ] No lyrics on same line as tags
- [ ] Tags on their own line
- [ ] `[track:]` tag present with genre, mood, and length
- [ ] Production Direction block present
- [ ] Vocal Direction block present

### Step 11 -- Set Creative Sliders

Recommend slider values based on song type:

| Song Type | Weirdness | Style Influence | Audio Influence (if Inspo) |
|---|---|---|---|
| Radio pop/rock | 35-45% | 55-65% | 40-50% |
| Concept album | 50-55% | 50-60% | 45% |
| Dark cinematic | 50-60% | 55-65% | 45-55% |
| Intimate ballad | 45-55% | 50-60% | 40-50% |
| Epic orchestral | 50-55% | 60-70% | 45-55% |
| Experimental | 60-75% | 40-50% | 30-40% |

**Album consistency note:** Document slider values per track. If a render captures the intended palette, note settings as baseline for adjacent tracks.

### Step 12 -- Prepare Exclude Field Content

Format exclusions for the dedicated Exclude field:
```
distortion, electric guitar, synthesizers, trap drums, beatboxing, vocal hums
```

**Format note:** In the dedicated Exclude field, list items as plain comma-separated text -- no dash prefix needed (the field implies exclusion). The dash-prefix format (`-item`) is only needed when placing exclusions WITHIN the Style Prompt field.

### Step 13 -- Final Output

Document the optimized version:
```
## SUNO-OPTIMIZED VERSION

### Changes Made:
- [list of specific additions/changes]
- (If no changes: "Verification pass -- all checks passed, no changes needed")

### Character Counts:
- Style: XXX/1000
- Lyrics: XXXX/5000

### Slider Recommendations:
- Weirdness: XX%
- Style: XX%
- Audio: XX% (if applicable)

### Exclude Field:
[content for Exclude]

### [Full optimized song]
```

---

## The 7-Dimension Style Prompt Formula

Every Style Prompt should specify all 7 dimensions for maximum control:

```
Genre, BPM, Mood, Instruments, Vocal Style, Era/Production, Space/Direction
```

| # | Dimension | Purpose | Example |
|---|---|---|---|
| 1 | Genre | Cultural container (MUST be first) [Tier 3] | "Progressive dark folk" |
| 2 | BPM | Tempo anchor | "92 BPM" |
| 3 | Mood | Emotional direction | "melancholic, haunting" |
| 4 | Instruments | Timbral palette | "acoustic guitar, cello, distant choir" |
| 5 | Vocal Style | Delivery character | "deep male baritone, intimate" |
| 6 | Era/Production | Sonic period | "early 2000s production warmth" |
| 7 | Space/Direction | Atmosphere | "wide reverb, cinematic" |

**Missing any dimension = Suno guesses (fills with statistical averages).**

---

## Genre Combination Rules

- **Genre-First Principle:** Genre MUST be the first element -- it anchors everything else. [Tier 3: community practice, not official. v4.5+ allows conversational prompts.]
- **5-8 Tag Sweet Spot:** Comma-separated descriptors. Past 10 tags, signals conflict and Suno defaults to generic. [Tier 3: Suno v4.5+ docs encourage more descriptive prompting. Test by version.]
- **70/30 Rule:** One dominant genre (70%) + one flavor (30%). 50/50 splits confuse Suno. Use `+` to combine
- **Era Anchoring:** Time references ("early 2000s garage rock") outperform genre labels ("indie rock") because they give Suno a specific sonic PERIOD. [Tier 3: promising but not A/B tested.]
- **The Separation Principle:** Era tags aggressively bias PRODUCTION style (recording technique, mix character). To get a retro instrument with modern production: "modern production, vintage 1970s guitar tone" -- separate the era from the mix

---

## Parenthetical Layers System

Text in parentheses = secondary vocal layer. Suno treats it differently from main lyrics.

| Pattern | Effect | Style Prompt Declaration Needed? |
|---|---|---|
| `(whispered) text` | Delivery cue -- whispers next text | Usually works alone |
| `(spoken) text` | Spoken not sung | Usually works alone |
| `(robotic layer: text)` | Named secondary voice (AI/machine) | **YES** -- must declare |
| `(echo layer: text)` | Delayed/echo treatment | **YES** -- must declare |
| `(whisper layer: text)` | Background whisper texture | **YES** -- must declare |
| `(response text)` | Backup vocal / duet response | Best with declaration |

**Key rule:** Named layers (`X layer: text`) REQUIRE the Style Prompt to declare them (e.g., "low-register AI voice layered during system sections"). Without this, Suno may just sing parenthetical content normally.

**Duet modes:**
- **Mode A:** `[Male Vocal]`/`[Female Vocal]` per line (complex, explicit)
- **Mode B:** Main + `()` response, declared in Style (efficient)
- **Mode C:** Custom layers + stacked tags (theatrical)

When using any `()` content, add `-vocal overlap confusion` to exclusions.

---

## Compliance Checklist (Required Elements)

Every Suno-ready song MUST have:

- [ ] `[track: genre: X, mood: X, length: XXX]` -- global control
- [ ] `[control: no-repeat, dynamic transitions]` -- prevent loops
- [ ] `[sequence: ...]` -- section order declaration
- [ ] `[Title: Song Title]` -- title tag
- [ ] `[Production Direction: ...]` -- tone/dynamics guidance
- [ ] `[Vocal Direction: ...]` -- voice/delivery guidance
- [ ] `[end]` -- termination signal
- [ ] Section tags on their own lines
- [ ] Genre first in Style Prompt
- [ ] Style <=1000 characters
- [ ] Lyrics <=5000 characters
- [ ] Tag count 5-8 (never >10)
- [ ] No contradictory tags
- [ ] Named `()` layers declared in Style Prompt
- [ ] Exclusions in dedicated Exclude field

---

## Common Suno Problems and Fixes

| Problem | Likely Cause | Fix |
|---|---|---|
| Song runs too long | No length tag | Add `[length: XXX]` in `[track:]` |
| Sections out of order | Complex structure confuses parser | Add `[sequence: ...]` |
| Lines get auto-repeated | Suno auto-loops | Add `[control: no-repeat]` |
| Wrong voice gender | Unclear vocal assignment | Use `[Male Vocal]`/`[Female Vocal]` explicitly |
| Song will not end | No termination signal | Add `[end]` after outro |
| Bridge gets sung not spoken | No delivery tag | Add `[spoken word]` or `[narrator]` |
| No dynamic contrast | All sections same energy | Add `[build]`, `[silence]`, `[crescendo]` |
| Genre drift mid-song | Conflicting style cues | Use `[track: genre: X]` globally + exclusions |
| Over character limit | No audit before render | Run character count FIRST (Step 1) |
| Parenthetical sung normally | Layer not declared | Declare named layers in Style Prompt |
| Sound too generic | Too many tags/signals conflict | Reduce to 5-8 focused tags, use era anchoring |
| Render does not match intent | Wrong dimension in Style Prompt | Run the 7-Dimension check |

---

## Historical v5.5 feature notes (verify availability in current UI)

These are set in the Suno interface, not in text fields:

| Feature | What It Does | When to Use |
|---|---|---|
| **Personas/Voices** | Lock a consistent vocal identity across all generations | One Persona per album character |
| **Stems** | Extract up to 12 individual tracks (vocals, drums, bass, etc.) | DAW mixing/mastering, album consistency |
| **Custom Models** | Train Suno on your completed tracks to learn your sound | Pro/Premier only, after establishing palette |

---

## Exclusions Format

The Exclude field in Suno's UI takes plain comma-separated items:
```
distortion, electric guitar, synthesizers, trap drums, beatboxing
```

No dash prefix needed in the dedicated field. The dash-prefix format (`-item`) is only for exclusions placed WITHIN the Style Prompt field.

---

## Tag Priority Order (Character Budget)

When tight on character count, prioritize in this order:

1. `[control]` + `[length]` + `[sequence]` (structural)
2. Section names with pipe notation (saves chars)
3. `[modulation]` / `[silence]` / `[beat-switch]` (specific moments)
4. `[vulnerable vocals]` / `[whisper]` / `[chant]` (vocal delivery)
5. `[crescendo]` / `[diminuendo]` / `[build]` (dynamics)
6. `[end]` (termination)

---

## Section Tag Formatting Rules

Section tags control how Suno interprets each part of the song. Strict formatting rules apply:

**Placement:**
- Tags MUST be on their own line -- never on the same line as lyrics
- Place section tags immediately before the lyrics they govern
- Global control tags go at the TOP of the lyrics field

**Line discipline:**
- Each lyric line = one melodic phrase = one breath
- Target 7-12 syllables per line
- 4-8 lines per section maximum (sung/spoken sections)
- Instrumental sections with only a tag and no lyrics are valid
- No end punctuation on lyric lines (no periods, commas, semicolons, question marks)
- Em-dashes are allowed for phrasing/breath
- Apostrophes and hyphens are fine

**Pipe notation syntax:**
```
[section-name | parameter1, parameter2, parameter3]
```

Only adjectives and delivery descriptors go after the pipe. Instrument-specific instructions belong in Production Direction blocks or standalone tags.

**Contrast principle:** Adjacent section tags should specify DIFFERENT qualities to prevent monotony. If your verse is `[verse | vulnerable, sparse, close-mic]`, your chorus should contrast: `[chorus | powerful, wide, full band]`.

---

## Creative Sliders -- Detailed Guidance

The three creative sliders are set in the Suno UI, not in text fields. They interact with each other and with the Style Prompt.

### Weirdness (Default: 50%)

Controls how much creative latitude Suno takes. Higher values produce more unexpected interpretations.

| Range | Behavior | Best For |
|---|---|---|
| 30-40% | Very faithful to prompt, predictable | Radio pop, covers, tight genre adherence |
| 45-55% | Balanced -- follows prompt with creative additions | Most concept album work |
| 55-65% | Adventurous -- may surprise with unexpected choices | Dark cinematic, atmospheric |
| 65-80% | Experimental -- prompt is a suggestion, not a rule | Ambient, experimental, noise |

### Style Influence (Default: 50%)

Controls how much the Style Prompt text steers the output. Higher = more prompt control.

| Range | Behavior | Best For |
|---|---|---|
| 40-50% | Loose -- Suno interprets freely | Experimental, when you want surprises |
| 50-60% | Balanced -- prompt guides, Suno fills gaps | Standard songwriting |
| 60-70% | Strong -- prompt dominates output character | When you need specific genre adherence |
| 70%+ | Maximum -- very literal prompt following | Matching a specific reference closely |

### Audio Influence (Default: ~45%, only if Inspiration Track used)

Controls how much a reference audio track affects the output.

| Range | Behavior | Best For |
|---|---|---|
| 30-40% | Subtle -- captures vague feel of reference | When you want slight flavor only |
| 40-50% | Moderate -- adopts key characteristics | Matching album palette to reference |
| 50-60% | Strong -- closely mirrors reference character | Recreating a specific sound |
| 60%+ | Dominant -- output may sound derivative | Rarely recommended |

**Interaction effects:**
- High Weirdness + High Style Influence = creative within your genre boundaries
- High Weirdness + Low Style Influence = chaos (sometimes useful for experimental)
- Low Weirdness + High Style Influence = extremely predictable, genre-locked

---

## Key Optimization Principles

1. **Genre-Emotion Alignment (Fabbri):** The genre must SIGNIFY what the lyrics express. Dark lyrics in upbeat genre = semiotic violation.
2. **Key is King (Eerola, Friberg & Bresin, 2013):** Mode is the #1 emotional cue. Wrong key = wrong emotion at the deepest level.

   > **Tier split:** Mode effects on perceived valence = [Tier 1: confirmed by Eerola, Friberg & Bresin 2013 and multiple replications]. Specific key character associations (e.g., D minor = devotional, F# minor = mysterious) = [Tier 2: historical tradition (Schubart 1806, Mattheson), not cognitive science. Useful as creative prompts, not empirical claims.]
3. **BPM Serves Two Masters:** Must satisfy genre convention AND emotional pacing simultaneously.
4. **Instruments Carry Meaning (Tagg):** Every instrument signifies independently of melody. Piano != guitar != synth even playing the same notes.
5. **Era Anchoring > Genre Labels:** Time references give Suno specific sonic periods. "1995 trip-hop" > "dark electronic." [Tier 3: promising but not A/B tested.]
6. **The 70/30 Rule:** Genre combinations -- one dominant (70%) + one flavor (30%). 50/50 splits confuse Suno.
7. **5-8 Tags Maximum:** Past 10, signals conflict and Suno defaults to generic. [Tier 3: Suno v4.5+ docs encourage more descriptive prompting. Test by version.]
8. **Section Tags = Musemic Signification:** Per-section tags should carry correct connotation for THAT section's content (Tagg applied to Suno tags).
9. **Separation Principle:** Separate era from instrumentation when you want retro sounds with modern production.

---

## Time Estimate

15-20 minutes per song (verification pass if song was written with full procedure).

---

## Theoretical Foundation

| Scholar/System | Contribution |
|---|---|
| **Philip Tagg** | Musemic analysis -- applied to section tag signification |
| **Franco Fabbri** | Genre theory -- validates genre selection |
| **Patrik Juslin** | BRECVEMA emotional mechanisms |
| **Eerola, Friberg & Bresin** (2013) | Cue hierarchy -- key/mode as #1 emotional driver |
| **Allan F. Moore** | Soundbox theory -- spatial tag design |
| **Serge Lacasse** | Proxemic distance -- reverb/space as emotional signal |
| **Suno community research** (2025-2026) | Era anchoring, genre-first, 5-8 sweet spot, slider behavior, v5 parsing rules |

---

## References

- `references/SUNO_TAGS_REFERENCE.md` -- Complete tag catalog with all confirmed/obsolete tags, pipe notation rules, and formatting details
- `references/SUNO_STYLE_GENRE_REFERENCE.md` -- Full genre/key/BPM/instrument/emotion mapping tables for Style Prompt optimization

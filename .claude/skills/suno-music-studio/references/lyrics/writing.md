# Lyric Writing

How to write and revise lyrics with sound prosody, rhyme craft, and Suno-safe pacing. Run the quality check and at least one refinement pass before you present any draft.

Related: before/after examples are in `references/lyrics/examples.md`, the review checklist in `references/lyrics/review.md`, and true-story/explicit/originality rules in `references/lyrics/compliance.md`. Phonetic spelling is covered in `references/suno/pronunciation.md`.

---

## Before You Start

- **Instrumental?** If the song is instrumental, don't write lyrics. Go straight to the style prompt (see `references/suno/prompting.md`).
- **Read the genre reference.** `references/genres/<genre-slug>/README.md` → "Lyric Conventions" gives that genre's rhyme scheme, rhyme strictness, verse structure, and `Density/pacing (Suno)` line. Where it is more specific than the tables below, the genre reference wins.
- **User preferences win.** If the user has stated preferences, they override these base guidelines when the two conflict. These can cover style (e.g. "prefer first-person", "avoid religious imagery", "vivid sensory detail"), default POV per context, vocabulary to prefer or avoid (e.g. "no utilize/commence/endeavor"), themes to focus on or avoid, structure (e.g. "verses 4–6 lines, chorus 4 lines"), and custom rules (e.g. "never use the word 'baby'", "always end with a callback to the opening line"). Combine rather than discard: if the base says "show don't tell" and the user says "prefer first-person", show emotion through first-person actions and observations.

## Workflow

1. **Take the concept** from the user or the album plan.
2. **Load album context** (concept albums only): read the album concept and the earlier tracks to find callback opportunities (see Cross-Track Referencing).
3. **Draft** using the core principles below, weaving in callbacks where they fit naturally.
4. **Run the 13-point quality check.** Fix every violation before going further.
5. **Run refinement passes**: default 1, with the Refinement Log.
6. **Scan for pronunciation risks** (proper nouns, homographs, acronyms) and apply phonetic spellings to the Suno lyrics.
7. **Verify against sources** if the song is documentary or about real events (see `references/lyrics/compliance.md`).
8. **Finalize**: produce the Suno lyrics (phonetic, with section tags) and the streaming lyrics (standard spelling), and record any callbacks/motifs for the album.
9. **Move on to the Suno prompt** without waiting to be asked: build the style prompt (see `references/suno/prompting.md`).

When you're asked to work on an existing track, scan it first for weak or awkward lines, forced rhymes, prosody problems, POV/tense inconsistencies, twin verses, a missing hook or buried title, factual inaccuracies, and pronunciation risks. Report every issue with a proposed fix, then continue.

---

## Core Principles

### Watch Your Rhymes

- Don't rhyme the same word twice in consecutive lines.
- Don't rhyme a word with itself.
- Avoid near-repeats (mind/mind, time/time).
- Fix lazy patterns before anyone has to point them out.

### Prosody (Syllable Stress)

Prosody means matching stressed syllables to strong musical beats.

- Stressed syllables land on downbeats (beats 1 and 3 in 4/4).
- Multi-syllable words keep their natural emphasis: HAP-py, not hap-PY.
- Content words (nouns, verbs) take the emphasis. Function words (into, the, of) stay off strong beats.
- High melody notes go on emphasized words.

**Test**: speak the lyric. If the emphasis feels wrong, rewrite the line.

### Show, Don't Tell

- **Action**: what would someone *do* while feeling this?
  - Weak: "My heart is breaking"
  - Strong: "She fell to her knees as he packed his bag"
- **Imagery**: use nouns that can be seen or touched.
  - Weak: "I felt so sad"
  - Strong: "Coffee gone cold on the counter"
- **Sensory detail**: engage several senses: sight, sound, smell, touch, taste, organic (body), kinesthetic (motion).

**Section balance**: verses carry the sensory detail; choruses carry the emotional statement.

### Verse/Chorus Contrast

| Element | Verse | Chorus |
|---------|-------|--------|
| Lyrics | Observational, narrative | Emotional, universal |
| Energy | Building | Peak |
| Detail | Specific sensory | Abstract emotional |

**V2 must not equal V1.** The second verse advances the story, deepens the emotion, or shifts perspective. It never just rephrases V1. For example, after V1 "Streets are cold, I walk alone", a bad V2 is "Roads are freezing, I'm by myself" (the same idea reworded). A good V2 is "Found your old coat in the closet / Still smells like smoke and home" (a new detail and an emotional shift).

### No Verse-Chorus Echo

A verse must never repeat a key phrase, image, or rhyme word from the chorus it leads into. The chorus is the hook; if the verse already said it, the chorus loses its impact.

**Check:** compare the last 2 lines of every section that precedes a chorus with the first 2 lines of that chorus. Do this at every verse-to-chorus and bridge-to-chorus transition, not just the first one. Flag:

- **Exact phrase**: the same words in both (e.g. "digital heart" / "digital heart")
- **Same rhyme word**: the verse ends on "start" and the chorus opens on "start"
- **Restated hook**: the verse paraphrases the chorus hook
- **Shared imagery**: the verse uses the chorus's signature image (e.g. both say "warehouse")

**Red flags:** the last verse line contains any phrase from the first chorus line; the hook word appears anywhere in the preceding verse; the verse gives away the chorus before it hits.

**Fix:** rewrite the verse line with different imagery that *sets up* the chorus. The verse creates tension or expectation and the chorus resolves it. Make the two complementary, not redundant: the verse says "spark", the chorus says "start".

> Bad: This is where the future of tech TV got its start. / [Chorus] Five-three-five York Street — where the future got its start,
> Good: This is where it all began, the very first spark. / [Chorus] Five-three-five York Street — where the future got its start,

### Hook and Title Placement

- Put the title in the first or last line of the chorus.
- Repeat the title at the song's beginning AND end.
- Give the title priority: a rhythmic accent and the melodic peak.

### Point of View and Tense

**POV**: choose one and keep it.
- First (I/me): the most intimate; the usual default.
- Second (you): draws the listener in; suits songs aimed at audience connection.
- Third (he/she/they): storyteller distance; the default for narrative and required for documentary.

**Tense**: stay consistent within a section.
- Present: immediate and powerful.
- Past: distance and reflection.

Allowed shifts: third-person verses with a first-person chorus; a past-tense story with a present-tense reflection; any shift made deliberately for emotional effect. Unmotivated shifts are errors.

---

## Rhyme Craft

### Rhyme Types (use variety)

| Type | Description | Example |
|------|-------------|---------|
| Perfect | Exact match | love/dove |
| Slant/Near | Similar but not exact | love/move |
| Consonance | Same ending consonants | blank/think |
| Assonance | Same vowel sounds | lake/fate |
| Internal | Rhymes within a line | "fire and desire higher" |

### Rhyme Scheme Patterns

| Pattern | Effect |
|---------|--------|
| AABB | Stable, immediate resolution |
| ABAB | Classic, delayed resolution |
| ABCB | Lighter, less pressure |
| AAAX | Strong setup, surprise ending |

### Default Rhyme Schemes by Genre

There is no universal default. Check the genre reference before you write.

| Genre Family | Default Scheme | Rhyme Strictness | Key Difference |
|---|---|---|---|
| **Hip-Hop / Rap** | AABB (couplet) | High: multisyllabic and internal rhyme mandatory | Rhyme density throughout the bar, not just end rhymes |
| **Pop** | XAXA (conversational) | Low: near rhymes preferred | Conversational phrasing; if it sounds "crafted," it fails |
| **Rock** | XAXA or ABAB | Low: meaning over rhyme | Imagery and emotional energy over technical rhyming |
| **Punk** | AABB (loose) | Low: half-rhymes read as authentic | Direct, shoutable, works at 150+ BPM |
| **Metal** | Optional | Very low: can skip rhyme entirely | Concrete imagery and riff alignment over rhyme |
| **Country / Folk** | ABCB (ballad stanza) | Moderate: near rhymes OK | Storytelling; lines 2 & 4 rhyme, 1 & 3 free |
| **Blues** | AAB (3-line form) | Moderate | Line 1 stated, line 2 repeats, line 3 resolves |
| **Electronic / EDM** | Repetition over rhyme | Minimal | Less is more; single phrases looped, not verses |
| **Ambient / Lo-Fi** | None | None | Vocals are texture, not content |
| **Trip-Hop** | XAXA (loose) | Low | The most lyrical electronic genre; abstract, moody |
| **R&B / Soul** | Flexible | Low: emotion first | Leave space for melisma and vocal runs |
| **Funk** | Minimal | Very low | Groove lock; lyrics accent the downbeat |
| **Gospel** | Repetitive build | Low | Call-and-response; repetition builds intensity |
| **Jazz** | AABA (32-bar) | Sophisticated | Internal rhyme, wordplay; phrasing behind or ahead of the beat |
| **Reggae / Dancehall** | Riddim-driven | Moderate | Groove lock; audience participation by design |
| **Afrobeats** | Call-and-response | Low | Code-switching (English / Pidgin / local languages) |
| **Ballad (any)** | ABCB or ABAB | Moderate | Emotion and narrative serve the story |

### Rhyme Quality Standards (all genres)

- **Forced rhymes are never acceptable.** Never bend grammar, invent words, or add filler just to land a rhyme.
- **No self-rhymes**: never rhyme a word with itself.
- **No lazy repeats**: don't rhyme near-identical words (mind/mind, time/time).
- **Meaning over rhyme**: if a perfect rhyme sounds unnatural, use a near rhyme or restructure the line.
- **Consistency within sections**: keep the scheme you chose for the whole section. No switching mid-verse.

### Flow Checks (all genres)

1. Read each rhyming pair aloud. Do the end words actually rhyme, by the genre's standard?
2. Are there orphan lines that should rhyme with something but don't?
3. Is the syllable count roughly consistent across corresponding lines? (See the tolerances under Line Length.)
4. Are filler phrases ("spoke the words", "you know what I mean") padding any lines?
5. Do quoted or paraphrased lines come from sourced material (documentary songs)?
6. Does the scheme match the genre? Don't put AABB couplets in a folk ballad, and don't use ABCB for hip-hop.
7. Say the lyrics as plain prose, without melody. Do they sound natural for the genre's vocal style?

### Common Anti-Patterns

- The wrong rhyme scheme for the genre (hip-hop couplets in a folk song, etc.)
- Forcing perfect rhymes where near rhymes would sound more natural
- Filler lines that set up quotes ("he stood up and spoke the words")
- Invented quotes for real people when source quotes exist
- Ending a verse on a line that doesn't connect to its rhyme partner
- Inconsistent line lengths that break the vocal pocket
- Clichés: "cold as ice," "broke my heart," "by my side," "set me free," "tonight" (as a line ending), "learning to fly"
- Telling instead of showing ("I was angry" instead of showing the anger through imagery)
- Generic abstractions where specificity would serve better

---

## Line Length

| Genre | Syllables/Line | Tolerance |
|-------|----------------|-----------|
| Pop / Folk / Punk | 6–8 | ±2 |
| Rock / Indie | 8–10 | ±2 |
| Hip-Hop / Rap | 10–13+ | ±3 |
| Metal / Electronic | Varies | Flexible |

**Critical**: Verse 1 line lengths must match Verse 2 line lengths. Parallel lines must fit the same melodic phrase.

---

## Song Length

Songs that run too long (800+ words) make Suno rush, compress sections, or skip lyrics. Songs that are too short produce tracks under 3 minutes. That's fine if it's intentional, but usually it isn't what the user wants.

### Target Duration

The default is **3:30–5:00** for all genres unless the user specifies otherwise. Precedence: the song's stated target duration, then the album's target duration, then the genre default below.

**Duration → word count:**

| Target Duration | Non-Hip-Hop Words | Hip-Hop Words |
|-----------------|-------------------|---------------|
| 2:00–2:30 | 120–180 | 200–300 |
| 2:30–3:30 | 150–250 | 250–400 |
| 3:30–5:00 | 220–400 | 400–600 |
| 5:00–7:00 | 350–500 | 550–750 |

Add about 30 words per instrumental break or solo when you estimate.

### Word Count Targets by Genre (Suno)

These targets produce tracks in the 3:30–5:00 range. Lower targets (e.g. 150 words for electronic) produce 2:00–2:30 tracks.

| Genre | Target Duration | Word Count | Structure |
|-------|-----------------|------------|-----------|
| Electronic / Synthwave / EDM | 3:30–5:00 | 220–300 | 3 verses + pre-chorus + chorus + bridge + instrumental break |
| Pop / Synth-Pop | 3:30–4:30 | 250–350 | 2–3 verses + pre-chorus + chorus + bridge |
| Rock / Alt-Rock | 3:30–5:00 | 250–400 | 2–3 verses + chorus + bridge |
| Hip-Hop / Rap | 3:30–5:00 | 400–600 | 3 verses + hook + bridge |
| Folk / Country | 3:30–5:00 | 250–400 | 3 verses + chorus + bridge |
| Ballad (any) | 3:30–5:00 | 200–300 | 2–3 verses + chorus + bridge (slower tempo = fewer words) |
| Punk / Pop-Punk | 2:30–3:30 | 150–250 | 2 verses + chorus + bridge (punk is short by design) |

### Instrumental Tags Count as Runtime

Instrumental tags (`[Instrumental Break]`, `[Synth Solo]`, `[Guitar Solo]`, `[Drop]`, `[Interlude]`, etc.) each add roughly **20–40 seconds**. A track with 220 words and 2 instrumental breaks runs longer than 220 words alone.

### Structure Defaults

- **Default**: 2–3 verses + chorus + bridge. Use 3 verses to reach the duration target.
- **Chorus**: 4–6 lines, repeated verbatim each time, not rewritten.
- **Bridge**: 2–4 lines.
- **Pre-chorus**: 2–4 lines. Adding one is an effective way to add duration without bloating sections.
- **Outro**: optional, 2–4 lines max. It is not a new verse.
- **Instrumental breaks**: add runtime without adding words.

### How to Hit Duration

**Add more sections, not longer sections.** The per-section maximums below are correct for Suno pacing. To reach 3:30+:
- add a **3rd verse** (the most effective option);
- add a **pre-chorus** before each chorus;
- add an **instrumental break** or solo;
- add a **bridge** if the song lacks one.

Never write 10-line verses or 8-line choruses; Suno rushes them.

### Length Limits

- **Over 400 words (non-hip-hop) or 600 words (hip-hop)**: hard fail. Cut the song down before presenting it, unless the target duration is 5:00+.
- **Under 200 words**: flag it as likely too short for 3:30–5:00 and suggest a 3rd verse, a pre-chorus, or an instrumental break.
- Count words after drafting. If you're over target, remove a verse or trim sections rather than just shortening lines.

---

## Section Length Limits by Genre

Suno rushes, compresses, or skips content when a section runs long. These limits are hard: trim before you present.

**Hip-Hop / Rap / Trap / Drill / Grime / Phonk / Nerdcore**

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 8 | Standard 16-bar verse (each written line ≈ 2 bars) |
| Chorus / Hook | 4–6 | Shorter hooks hit harder |
| Bridge | 4–6 | |
| Pre-Chorus | 2–4 | |
| Outro | 2–4 | Spoken-word and ad-lib sections are exempt |

**Pop / Synth-Pop / Dance-Pop / K-Pop / Piano Pop**

| Section | Max Lines |
|---------|-----------|
| Verse | 6–8 |
| Chorus | 4–6 |
| Bridge | 4 |
| Pre-Chorus | 2–4 |

**Rock / Alt-Rock / Indie Rock / Grunge / Garage Rock / Post-Rock / Prog Rock**

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 6–8 | |
| Chorus | 4–6 | |
| Bridge | 4 | |
| Pre-Chorus | 2–4 | |
| Guitar solo / Interlude | 0 (instrumental) | Use a `[Guitar Solo]` or `[Interlude]` tag |

**Punk / Hardcore Punk / Emo / Pop-Punk / Ska Punk**

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 4–6 | Short and fast; keep it tight |
| Chorus | 2–4 | Punchy, shoutable |
| Bridge | 2–4 | |
| Pre-Chorus | 2 | |

**Metal / Thrash / Doom / Black Metal / Metalcore / Industrial**

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 4–8 | |
| Chorus | 4–6 | |
| Bridge | 4 | |
| Pre-Chorus | 2–4 | |
| Breakdown | 2–4 | Often instrumental or minimal lyrics |

**Country / Folk / Americana / Bluegrass / Singer-Songwriter / Blues**

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 4–8 | Storytelling verses can use the full 8 |
| Chorus | 4–6 | |
| Bridge | 2–4 | |
| Pre-Chorus | 2–4 | |

**Electronic / EDM / House / Techno / Trance / Dubstep / DnB / Synthwave**

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 4–6 | Electronic vocals are sparse; less is more |
| Chorus / Hook | 2–4 | Often just a repeated phrase |
| Bridge | 2–4 | |
| Drop | 0 (instrumental) | Use a `[Drop]` or `[Break]` tag |

**Ambient / Lo-Fi / Chillwave / Trip-Hop / Vaporwave**

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 2–4 | Minimal vocals; atmosphere first |
| Chorus / Hook | 2–4 | |
| Bridge | 2 | |

**R&B / Soul / Funk / Gospel**

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 6–8 | |
| Chorus | 4–6 | |
| Bridge | 4 | |
| Pre-Chorus | 2–4 | |
| Vamp / Ad-lib | Flexible | Outro vamps are genre-standard |

**Jazz / Swing / Bossa Nova**

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 4–8 | Standard 32-bar form |
| Chorus | 4–6 | |
| Bridge | 4–8 | Jazz B-sections can run longer |

**Reggae / Dancehall / Afrobeats**

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 4–8 | |
| Chorus / Hook | 4–6 | |
| Bridge | 2–4 | |
| Toast / DJ | 4–8 | Dancehall toasting sections |

**Ballad (any genre)**

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 4–6 | Slower tempo needs fewer lines |
| Chorus | 4–6 | |
| Bridge | 2–4 | |

### Enforcement

1. After drafting, count the lines in each section and compare them with the table.
2. If a section exceeds its max, trim it. Don't ask; cut it down, then present.
3. A hip-hop verse over 8 lines gets split into two verses or cut. No exceptions.
4. Trim any chorus over 6 lines. A long chorus loses its punch and makes Suno rush.
5. Cut any electronic verse over 6 lines. Electronic tracks need space, not walls of text.
6. Keep punk sections within their limits. Punk is short and fast; if it's long, it isn't punk.
7. If you're unsure of the genre, use the Pop/Rock defaults: verse 6–8, chorus 4–6, bridge 4.
8. Also apply the BPM-aware limits below. A genre may allow 8-line verses at a fast tempo but only 4 at a slow one.

**How to trim:** cut the redundant or weakest lines first, and keep the strongest imagery and rhymes. Tighten the transitions. In a narrative section, cut middle exposition; in a descriptive one, cut repeated imagery. Never cut the hook or the opening line.

**Why Suno needs this:** long sections cause vocal rushing (words crammed into fixed musical time), loss of clarity (words blur together), section compression (Suno shortens the music to fit), and skipped lyrics (Suno drops lines entirely).

---

## Lyric Density and Pacing (Suno)

Suno rushes through dense verse blocks, so verse length has to match tempo and feel. **The slower the BPM, the fewer lines Suno can handle** before it rushes, compresses, or skips. The genre reference's `Density/pacing (Suno)` line takes precedence over these defaults.

### Verse Length Defaults by Genre

| Genre Family | Default Lines/Verse | Max Safe | Topics/Verse | Key Rule |
|---|---|---|---|---|
| **Hip-Hop / Rap** | 8 (4 couplets) | 8 | 2–3 | Never exceed 8; treat half-time trap as 65–75 BPM |
| **Pop** | 4 | 6–8 | 1–2 | Chorus-first; longer verses bury the hook |
| **Rock** | 6 | 8 | 2 | 120 BPM sweet spot; guitar riffs need space |
| **Punk** | 4 | 4 | 1 | Fast and short; every word punches |
| **Hardcore Punk** | 2–3 | 3 | 1 | Extreme tempo; shouted, minimal |
| **Metal** | 6–8 | 10 | 2–3 | Vocal delivery compresses syllables; thrash handles the most |
| **Doom Metal** | 4 | 6 | 1 | The slowest metal; each word carries crushing weight |
| **Country / Folk** | 6 | 8 | 1–2 | Storytelling pace; ballads drop to 4 |
| **Blues** | 3 (AAB) | 3 | 1 | Rigid structure; never break AAB |
| **Electronic / EDM** | 2–4 | 4 | 1 | Production is the star; vocals are texture |
| **Ambient / Shoegaze** | 0–2 | 4 | 1 | Often instrumental; vocals are texture |
| **R&B / Soul** | 6 | 8 | 1–2 | Melisma stretches syllables; groove over density |
| **Jazz** | 6–8 | 8 | 1–2 | Bebop: 2–4 lines; ballads: 6–8 |
| **Singer-Songwriter** | 6–8 | 8 | 2–3 | Confessional; stripped-back production carries the words |
| **Progressive Rock** | 8–10 | 12 | 3–4 | The exception: handles long verses |

### BPM-Aware Limits (universal fallback)

| BPM Range | Max Lines/Verse | Topics/Verse | Feel |
|-----------|----------------|-------------|------|
| < 80 | 4 | 1–2 | Slow, heavy; fewer lines needed |
| 80–94 | 4–6 | 1–2 | Laid back, mid-tempo |
| 94–110 | 6 | 2–3 | Energetic, driving |
| 110–140 | 6–8 | 2–3 | Standard rock/pop range |
| 140+ | 4 | 1 | Fast; short verses, energy over density |

**Default: 4 lines per verse** unless the genre and tempo justify more.

### Topic Density

- Allow at most **1–2 topics per 4-line verse** and **2–3 per 6–8-line verse**.
- If a 4-line verse covers 3+ topics, split it.
- **More short verses beat fewer dense ones**: two 4-line verses are better than one 8-line verse.

### Red Flags

- An 8-line verse at any BPM under 100 (too dense for Suno).
- A verse that reads like a list of names or facts. That's a Wikipedia entry, not a verse.
- A concept that says "laid back" while the verses are wall-to-wall syllables.
- More than 3 proper nouns introduced in a single verse.
- Every verse in the song is dense, with no breathing room anywhere.

### Fixing a Dense Verse

1. Prefer adding a verse over cutting content: spread it out rather than compressing.
2. Give each topic at least a full couplet (2 lines) to land.
3. Re-read it at the target BPM. Can it be sung or rapped at tempo without rushing?

Before finalizing, ask: "Does the verse length match the BPM and mood the user described?" If a verse exceeds the genre default, flag it.

**Streaming exception:** streaming/distributor lyrics aren't generated by Suno, so they can use longer verse blocks. But the verse *breaks* should still match the Suno structure, so the text lines up with what's actually sung.

---

## Pronunciation (Suno-Facing)

Suno pronounces words literally from their spelling and can't use context. Keep two versions of the lyrics:
- **Suno lyrics**: phonetic spellings applied, section tags included.
- **Streaming lyrics**: standard English spelling for distributors and display.

Keep a **pronunciation list** for each song (word → phonetic spelling, plus the user's decision for homographs). For the full method and a larger word list, see `references/suno/pronunciation.md`.

### Phonetic Spelling for Risky Words

| Type | Example | Write As |
|------|---------|----------|
| Names | Ramos, Sinaloa, Jose | Rah-mohs, Sin-ah-lo-ah, Ho-zay |
| Acronyms | GPS, FBI, RICO | G-P-S, F-B-I, Ree-koh |
| Tech terms | Linux, SQL | Lin-ucks, sequel |
| Numbers | 1993 / ninety-three | '93 (or "nineteen ninety-three") |
| Homographs | live (verb) | lyve or liv |

### Homographs: Flag, Batch-Ask, Apply

Even when a sentence makes the intended reading obvious to a human, Suno picks one pronunciation and locks it in. A wrong choice gives a wrong vocal line on every regeneration.

1. **Identify** every homograph in the lyrics (the table below is a baseline, not an exhaustive list).
2. **Batch-ask.** When a song has several homographs, present them all in a single message as a numbered list with both pronunciation options per word, and take all the decisions in one reply. Per-word back-and-forth bloats the conversation.
3. **Apply** the chosen phonetic spelling in the Suno lyrics only.
4. **Record** each decision in the song's pronunciation list.

| Word | Pronunciation A | Phonetic | Pronunciation B | Phonetic |
|------|----------------|----------|-----------------|----------|
| live | real-time / broadcast ("live show") | lyve | reside / exist | liv |
| read | present tense | reed | past tense | red |
| lead | to guide | leed | metal | led |
| wound | injury | woond | past of wind | wownd |
| close | to shut | kloze | nearby | klohs |
| bass | low sound | bayss | the fish | bas (rhymes with "pass") |
| tear | from crying | teer | to rip | tare |
| wind | air movement | wihnd | to turn / coil | wynd |
| bow | ribbon | boh | to bend | bow (rhymes with "cow") |

**Rules:**
- Every homograph must trace to an explicit user decision. "Context makes it clear" is not a valid resolution.
- The user is the only authority on which pronunciation is meant. Treat ambiguity as a flag, not a judgment call.
- Phonetic spellings go in the Suno lyrics only; streaming lyrics keep standard spelling.

### No Invented Contractions

Suno only recognizes standard English contractions. Never append 'd, 'll, etc. to nouns, brand names, or other non-standard words.

- **Standard (OK):** they'd, he'd, you'd, she'd, we'd, I'd, wouldn't, couldn't, shouldn't
- **Invented (breaks Suno):** signal'd, TV'd, network'd, podcast'd, channel'd
- **Fix:** spell it out: "signal would", not "signal'd"; "TV could", not "TV'd".
- **Rule:** if the base word isn't a pronoun or a standard auxiliary verb, don't contract it. Suno will mispronounce or skip it.

### Enforce the Pronunciation List

The pronunciation list is a checklist of required substitutions, not documentation. Before finalizing for Suno:

1. Read the list top to bottom.
2. For each entry, search the Suno lyrics for the standard spelling.
3. Replace every occurrence with the phonetic form: every verse, every chorus repeat, every bridge.
4. Where the phonetic form is already applied, confirm it matches the list.

Common failures:
- a word added to the list but never applied to the lyrics;
- a phonetic applied in one verse but missed in a chorus repeat or the bridge;
- a later edit that reintroduces the standard spelling of a listed word.

```
WRONG:   List: Potrero → poh-TREH-roh
         Suno lyrics: "Potrero Hill, industrial..."

CORRECT: List: Potrero → poh-TREH-roh
         Suno lyrics: "poh-TREH-roh Hill, in-DUST-ree-ul..."
```

When you're unsure whether a word needs phonetic treatment, ask. Flagging and confirming beats shipping a guess.

---

## Documentary and True-Story Songs

When a song is about real people or real events, follow the five rules below. The full standards, with safe and unsafe phrasings, are in `references/lyrics/compliance.md`.

1. **Third-person narrator only.** Tell the story from outside the subject; the narrator describes and never impersonates.
2. **Quote only what's in the source record.** Use it verbatim. Anything in quotation marks must trace to testimony, a transcript, or a recorded statement.
3. **Internal states require testimony.** Describe thoughts, feelings, or motives only when a source (interview, statement, court record) supports them.
4. **Actions must be in the record.** Describe only events that appear in the sources: no invented beats, no implied scenes.
5. **Limit factual claims to what the sources affirm.** Absence of evidence is not a claim. "Nobody saw" needs a source that says so, not a gap in the record.

---

## Cross-Track Referencing (Concept Albums)

Do this when **both** conditions hold:
- the album is narrative, thematic, a character study, documentary, or a soundtrack/OST; and
- the track is not track 1. Track 1 establishes motifs and references nothing.

For album planning more broadly, see `references/album/concept.md`.

### Process

1. Read the album context: concept, structure, motifs and threads.
2. Read the earlier tracks (1 through N−1): their lyrics, concepts, and existing cross-references.
3. Find 1–3 callback opportunities: images, phrases, character moments, or thematic threads to echo, invert, or resolve.
4. Draft with the references woven in. Each should feel like part of this track, not a footnote.
5. Record each callback and motif (track, line, type) so later tracks and the refinement pass can build on it.

### Reference Density by Album Position

| Position | Target References | Rationale |
|----------|-------------------|-----------|
| Track 01 | 0 | Establishes motifs; nothing to reference yet |
| Tracks 02–04 (early) | 1–2 | Light callbacks; building the vocabulary |
| Tracks 05–08 (mid) | 2–3 | Weaving threads together; peak density |
| Final 1–2 tracks | 2–4 | Resolving threads; bookend with track 01 |

### Reference Types

| Type | What It Does | Example |
|------|-------------|---------|
| **Callback** | Echoes an earlier lyric or image in a new context | Track 01: "the door was red" → Track 07: "red doors don't open twice" |
| **Motif** | A recurring thematic element that gains meaning | "static" appearing across tracks as technology fails |
| **Character thread** | The same character reappears or is referenced | Track 03 introduces a witness; Track 08 shows their testimony |
| **Contrast/Inversion** | Deliberately flips an earlier idea | Track 02: "the signal's strong" → Track 09: "nothing but noise" |
| **Resolution** | Resolves a tension or question from an earlier track | Track 04 asks "who called the cops?" → Track 11 answers it |

### Quality Rules

- **Subtle over heavy.** A single echoed image beats a quoted line; the listener should feel the connection, not get hit with it.
- **New context required.** A callback must mean something different in its new place. The same phrase with the same meaning is lazy repetition, not a callback.
- **Don't force it.** If no natural opportunity exists, write the track without one. A forced reference hurts more than none.
- **Bookend rule.** The final track echoes at least one element from track 01.
- **Each track stands alone first.** Every track must work as a complete song without its callbacks. References are a bonus layer, not a crutch.

### Anti-Patterns

- Quoting whole lines from earlier tracks verbatim (transform the reference instead)
- Forward references to tracks not yet written (reference backward only)
- Referencing every earlier track in one song (pick the 1–3 strongest connections)
- Making the callback the hook or chorus (callbacks belong in verses and bridges; the hook stands alone)
- Explaining the reference in the lyrics ("just like track three said…")

---

## The 13-Point Quality Check

Run this automatically after writing or revising any lyrics, report every violation you find, and fix them without waiting to be asked.

1. **Rhyme**: repeated end words, self-rhymes, lazy patterns.
2. **Prosody**: stressed syllables on strong beats.
3. **Pronunciation**: (a) phonetic risks: proper nouns, homographs, acronyms, tech terms, invented contractions (no noun'd/brand'd); (b) list enforcement: every entry in the pronunciation list is applied as phonetic spelling in the Suno lyrics.
4. **POV/tense**: consistent throughout.
5. **Source verification**: if source-based, the lyrics match the source material.
6. **Structure**: section tags present, verse/chorus contrast, V2 develops.
7. **Flow**: syllable counts consistent within verses (genre tolerance), no filler padding lines, no forced rhymes bending grammar.
8. **Length**: word count against the target duration (song → album → genre default). Over 400 words (non-hip-hop) or 600 (hip-hop) is a hard fail unless the target is 5:00+. Under 200, flag it as likely too short and suggest sections to add.
9. **Section length**: lines per section against the genre limits. **Hard fail**: trim before presenting.
10. **Rhyme scheme**: matches the genre default; no orphan lines; no mid-verse scheme switches. Read each rhyming pair aloud.
11. **Density/pacing**: verse line count against the genre's density line and the BPM/mood. **Hard fail**: trim or split any verse over the max.
12. **Verse-chorus echo**: the last 2 lines of each verse (and bridge) against the first 2 lines of the following chorus, at every transition.
13. **Pitfalls**: run the checklist below.

### Pitfalls Checklist

- [ ] Forced emphasis (stressed syllables on wrong beats)
- [ ] Inverted word order for rhyme
- [ ] Predictable rhymes (moon/June, fire/desire, heart/apart, night/light)
- [ ] Pronoun inconsistency
- [ ] Tense jumping without reason
- [ ] Too specific (alienating names and places)
- [ ] Too vague (abstractions without imagery)
- [ ] Twin verses (V2 = V1 reworded)
- [ ] No hook
- [ ] Disingenuous voice
- [ ] Section too long for the genre
- [ ] Orphan lines (should rhyme with a partner per the genre scheme but don't)
- [ ] Wrong rhyme scheme for the genre (e.g. AABB couplets in a folk ballad)
- [ ] Filler phrases padding lines for rhyme or to set up a quote
- [ ] Inconsistent syllable counts within a verse
- [ ] Verse over the Suno line limit for the genre
- [ ] 8-line verse at a BPM under 100 (split or trim)
- [ ] More than 3 proper nouns introduced in one verse
- [ ] Density mismatch ("laid back" direction with packed verses)
- [ ] Verse-chorus echo (verse repeats a chorus phrase, rhyme word, hook, or signature image)
- [ ] Invented contractions (signal'd, TV'd)
- [ ] Pronunciation list not enforced (listed word in standard spelling in the Suno lyrics)

---

## Refinement Passes

After the 13-point check, run refinement passes to tighten and polish the draft. **The default is 1 pass**; the user can choose 0–3. If they ask for more than 3, warn them that returns diminish and cap at 3. (Album-wide cohesion and unity passes are in `references/lyrics/review.md`.)

| Pass | Focus | Goal |
|------|-------|------|
| 1: Tighten | Cut filler, compress language, remove redundancy | Every word earns its place |
| 2: Strengthen | Upgrade weak imagery, sharpen sensory detail, replace generic with specific | Lines that stick |
| 3: Flow & Ear | Read-aloud test, smooth transitions, singability at target BPM | Sounds right when sung |

**Rules:**
- **Re-run the 13-point check after each pass.** Fix any new violations before you start the next pass.
- **Exit early**: if a pass produces zero changes, skip the remaining passes.
- **Preserve voice.** Refinement polishes word choice and density; tone, register, personality, and narrative beats stay as the draft left them.
- **Work within the existing canvas.** New metaphors, characters, or narrative beats are out of scope. If the draft needs new content, that's a writing task, not a refinement.
- **Respect the hard limits**: section length, word count, and genre constraints still apply after every pass.
- **Keep phonetics intact**: never revert a phonetic spelling to standard spelling while editing a line.
- **Respect user preferences.** If the user wants "direct, simple language," don't strengthen imagery into elaborate metaphors.

### Pass 1: Tighten

| Pattern | Before | After | Why |
|---------|--------|-------|-----|
| Filler phrases | "He stood up and spoke the words" | "He said" | Setup phrases pad lines without adding meaning |
| Redundant modifiers | "completely destroyed" | "destroyed" | Absolute verbs don't need intensifiers |
| Passive voice | "The door was opened by her" | "She opened the door" | Active voice is more direct and singable |
| Pronoun-heavy lines | "He told him that he should go" | "Get out — the message clear" | Ambiguous pronouns weaken imagery |
| Unnecessary prepositions | "She looked up at the sky above" | "She searched the sky" | Trim directional padding |
| Throat-clearing openers | "Well, I think that maybe I should" | "I should" | Cut hedging; commit to the statement |
| Double-saying | "alone and by myself" | "alone" | One expression per idea |

### Pass 2: Strengthen

| Pattern | Before | After | Why |
|---------|--------|-------|-----|
| Generic imagery | "The city at night" | "Neon bleeding on wet asphalt" | Specific images stick; generic ones slide |
| Abstract emotion | "I felt so lost" | "Couldn't find my keys, my name, my street" | Show the feeling through concrete details |
| Clichés | "Cold as ice" | "Cold as a landlord's smile" | Fresh comparisons earn attention |
| Single-sense lines | "The room was dark" (sight only) | "Dark — just the hum of pipes and mildew air" | Multi-sensory lines immerse the listener |
| Weak verbs | "He went across the room" | "He cut across the room" | Strong verbs carry energy and specificity |
| Telling emotions | "She was angry" | "Her knuckles white around the glass" | Action reveals emotion without naming it |
| Vague quantities | "A lot of people came" | "Thirty faces in a room for ten" | Numbers create instant visual scale |

### Pass 3: Flow & Ear

| Pattern | Before | After | Why |
|---------|--------|-------|-----|
| Consonant clusters | "Sixth street's strict structures" | "Sixth Street's sharp edges" | Tongue-trippers kill vocal delivery |
| Unsingable vowel sequences | "She oughta allow our hour" | "She gave us the hour" | Stacked diphthongs muddy at tempo |
| Transition bumps | V1 ends reflective → V2 opens aggressive with nothing between | Add a pre-chorus or a transitional line | Jarring shifts break the listener's flow |
| Missing breath points | A 12-syllable line with no natural pause | Split at the caesura or add a comma break | Singers need air; dense lines get rushed |
| Stress misalignment | "into the DARK-ness" on a weak beat | "the DARKness CALLS" on strong beats | Stressed syllables must land on downbeats |
| Choppy rhythm | "Stop. Go. Wait. No. Run." | "Stop and go — wait, no — run" | Staccato lines need connective tissue to sing |
| Syllable mismatch | V1 line: 8 syllables, V2 line: 13 | Match within ±2 syllables | Parallel lines must fit the same melodic phrase |

### Refinement Log

After the passes, show what changed:

```
## Refinement Log

### Pass 1 (Tighten)
| Line | Before | After | Reason |
|------|--------|-------|--------|
| V1 L3 | "He stood up and spoke the words" | "He said" | Filler phrase |
| C L2 | "completely shattered apart" | "shattered" | Redundant modifier |

### Pass 2 (Strengthen)
(no changes — early exit)
```

---

## Remember

1. **User preferences first.** Load them before you draft the first line.
2. **Watch your rhymes**: no self-rhymes, no lazy patterns.
3. **Prosody matters**: stressed syllables on strong beats.
4. **Show, don't tell**: action, imagery, sensory detail.
5. **V2 ≠ V1**: the second verse develops.
6. **Pronunciation is critical**: phonetic spelling for risky words, and the user decides every homograph.
7. **Documentary means legal risk**: follow the five rules.
8. **Concept albums connect**: read the earlier tracks and weave in 1–3 callbacks.
9. **Refine before presenting**: at least 1 pass, with a Refinement Log.
10. **Deliverable**: polished Suno lyrics plus streaming lyrics, with sound prosody, clear pronunciation, and factual accuracy where it applies, followed by the Suno style prompt.

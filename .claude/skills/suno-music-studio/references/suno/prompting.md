# Building a Suno Generation

How to turn a finished song (or an instrumental concept) into Suno inputs: the Style Box, the Lyrics Box, Exclude Styles and the Generation Settings. Tag vocabularies live in [tags.md](tags.md); model and slider detail in [models-and-sliders.md](models-and-sliders.md); phonetic fixes in [pronunciation.md](pronunciation.md); the final gate in [pre-generation-check.md](pre-generation-check.md).

Facts about Suno's UI and models below reflect the v6 family as of mid-September 2026. Suno changes fast; re-check limits and defaults if something behaves differently.

If the user has stated preferences (genre mappings such as "my dark-electronic = dark techno, industrial, EBM", a default vocal, words or genres to avoid, an "always include" suffix), those preferences win over everything in this file.

---

## Core Principles

1. **Suno is literal.** Simple, clear prompts work best. Say what you want directly.
2. **Work in Advanced Mode only.** Simple Mode treats typed lyrics as a seed and writes extra lines; switching to Advanced does not carry the prompt across. All the controls that matter (Vocal Gender, Duration, sliders, Exclude Styles, Variety, Max Mode) are under More Options in Advanced Mode.
3. **Variety Off** whenever you engineered the Style Box. At any setting above Off, Suno rewrites and expands the style prompt before the model sees it. Defaults to Normal on v6 / v6-mini / Custom Models, Off on v6-wild — check it every session, the default reasserts when you switch models.
4. **Vocals first** in the Style Box.
5. **Every section gets a structure tag, and every tag gets a Performance Cue** (`[Verse 1 - cold regal]`). Bare `[Verse]`/`[Chorus]` tags are a common cause of flat, generic output.
6. **Never put an artist or band name in the Style Box.** Describe the sound instead (see [Artist Name Blocklist](#artist-name-blocklist)).
7. **Prompts written for pre-v6 models do not transfer.** Re-prompt; don't rerun.

Formula: simple prompt + good lyrics + section tags with cues + user preferences + targeted exclusions + Variety Off = best results.

---

## The Prompt Surface

| Field / limit | Value | Notes |
|---|---|---|
| Style Box ("Style of Music") | 1,000 chars | |
| Lyrics Box | 5,000 chars | everything in it is sung except bracket tags |
| Exclude Styles | 1,000 chars | the only reliable negative path |
| Simple Mode prompt | 3,000 chars | not used for engineered songs |
| Maximum length | 8 min | Auto and Extend; Duration Custom range is 10 s–6:00 |
| Weirdness / Style Influence / Audio Influence | defaults 50 / 50 / 25 | Audio Influence appears only with uploaded audio |
| Credits | 10 per generation (two songs); 20 with Max Mode | same on v6, v6-wild, v6-mini |

Present the final Style Box, Exclude Styles and Lyrics Box to the user in **separate code blocks** so each is easy to copy into its field, followed by the Generation Settings as a small table.

---

## Workflow

1. **Check whether the track is instrumental.** If so, follow [Instrumental Tracks](#instrumental-tracks) and skip lyric and pronunciation steps.
2. **Check the target duration** (track target, then album target, then genre default). See [Duration](#duration).
3. **Check for a saved Voice or Custom Model.** Adjust the Style Box accordingly (see below).
4. **Select genre**: primary genre plus 1–2 modifiers.
5. **Define the vocal**: voice type, texture, delivery. Pull a concrete texture/style descriptor from [tags.md § Voice Tags](tags.md#voice-and-vocal-tags) ("gravelly, belting" beats "powerful").
6. **Choose 2–3 key instruments** matched to the genre ([tags.md § Genre-Specific Instruments](tags.md#genre-specific-instruments)). Every instrument earns its place.
7. **Check for sound effects / atmosphere** in the lyrics (rain, footsteps, crowds, laughter) and add matching tags; environmental sounds go in both the Lyrics Box and the Style Box.
8. **Add Performance Cues** to every structure tag so the emotional arc plays out section by section.
9. **Choose model and settings** per [Generation Settings](#generation-settings).
10. **Build the Style Box** (vocals first), populate Exclude Styles if needed, then review the descriptor mix and collapse synonym piles.
11. **Run the final gate** in [pre-generation-check.md](pre-generation-check.md).
12. **Generate.** On v6-wild budget two or three generations before judging; its length is unpredictable (~50 s to ~7 min on similar prompts).
13. **Iterate one change per pass** (see [Common Issues & Fixes](#common-issues--fixes)) and log every attempt: model, settings, Style Box, verdict.

---

## The Style Box

### Structure

```
[Vocal description]. [Genre / instrumentation]. [Production notes]
```

```
Male baritone, storytelling delivery. Alternative rock, clean electric guitar,
driving bass, tight drums. Modern production.
```

- Put the vocal first: "Male baritone, gritty, emotional. Heavy rock, distorted guitars" — not "Heavy rock, distorted guitars. Male baritone vocals".
- Commas separate descriptors; periods separate blocks. Semicolons, slashes and quotes are reported to parse inconsistently; avoid them.
- Early words are weighted more heavily.

### Alternative Formulas

Use whichever fits; all put the important information first.

| Formula | Shape | Example |
|---|---|---|
| Quick start | `[genre], [subgenre], [instruments], [mood], [tempo], [vocal]` | `nerdcore hip-hop, glitchy IDM beats, lo-fi digital artifacts, nostalgic, melancholic, 85 BPM, male vocals, gravelly voice, introspective` |
| Four-part anatomy | 1 Genre + era + influences · 2 Tempo/BPM + key (optional) · 3 Instrumentation & arrangement · 4 Production & mix notes | `90s alt-rock with Britpop undertones, 120 BPM, A minor, live drums with room ambience, palm-muted guitars, warm bass, analog glue compression, tape saturation, lead vocal upfront` |
| Top-loaded palette | `[Mood] + [Energy] + [2 instruments] + [Vocal identity]` | `Melancholic, slow-burn, piano and strings, female alto with subtle vibrato` |
| Priority order | genre, vocal, mood, production | `Dark synthwave, female alto vocal, melancholic, analog warmth, 100 BPM` |
| Starter | `[Primary genre], [modifier], [vocal cluster], [BPM] BPM, [3 key instruments], [production era + mix character], [2 mood words]` | |
| Card | `[Genre], [BPM], [mood]` / `[Vocal]: gender, texture, style` / `[Instruments]: 2–4` / `[Mix]: 1–2 hints` | |

### Descriptor Discipline (Prompt Fatigue)

Every descriptor must add distinct information: vocal identity, genre, tempo, 2–3 instruments, a production note, a mood. A focused box of ~10 descriptors is fine. What dilutes Suno is a **synonym pile**: "imperious, commanding, regal, grand, theatrical, explosive" is one mood said six ways.

- Collapse synonyms to 1–2 words per concept. Trim synonyms, not detail.
- "4–7 descriptors" is a starting heuristic, not a Suno rule. Treat more than ~12 as genuine bloat worth trimming.
- If you need a paragraph, you are probably describing two songs.
- Keep the baseline mood/energy in the Style Box; move section-by-section variation into Performance Cues in the Lyrics Box. (The alternative is a Style-Box "Performance:" line mapping sections — see [tags.md § Emotion Arc Mapping](tags.md#emotion-arc-mapping). Use one approach per track, not both.)

```
Bad (synonym pile): "Ethereal indie folk with vintage analog warmth and melancholic
undertones, finger-picked acoustic, tape hiss, lo-fi, intimate, breathy, whispery,
nostalgic, contemplative, minimalist production"

Bad (too vague): "Nice upbeat music"

Good: "Sad indie folk, acoustic, gentle, breathy female vocal, intimate"
```

### Genre Selection

More specific is better, but stop at 2–3 genre descriptors. Five or more genre terms dilute rather than clarify.

**Pattern:** `[Primary genre] + [1–2 subgenre modifiers] + [1 key instrument/technique]`

| Level | Example |
|---|---|
| Generic | "Rock" |
| Better | "Alternative rock" |
| Best | "Midwest emo, math rock influences, clean guitar" |
| Too much | "Midwest emo, math rock, post-rock, shoegaze, ambient, clean guitar, intricate picking, reverb-heavy" |

Genre mixing: combine up to 3 ("Hip-hop with jazz influences", "Country with electronic elements", "Indie folk meets trip-hop"). "Country trap jazz fusion" is a coin flip; "Country, trap-influenced drums" works.

### Concrete Beats Abstract

- **Tempo as a number**: `128 BPM`. "Fast" means different things in doom metal and drum and bass.
- **Era anchors** conjure instrumentation, mix and vocal delivery at once: `1994 boom bap`, `late-70s AOR`.
- **Name the instruments** to steer away from genre clichés: `fretless bass, Rhodes, brushed snare`.
- **Production language** moves the needle: `tape saturation, wide stereo, dry vocal, punchy compressed drums` — not "good quality, professional".
- **Describe the room**: `recorded in a wooden church`, `dead vocal booth`, `stadium echo`.
- **Period gear** says the era without a name: `Juno-106 pads, LinnDrum, gated reverb` = 1984.
- **State tempo, density and length.** On Duration Auto, v6 leans slower, sparser and longer whenever the brief leaves those open. Use a BPM or "uptempo"/"driving", and "busy"/"layered" or "sparse".
- **Imperfection must be asked for.** Suno's own advice: if you want imperfect vocals, write that into the prompt via instrumentation, recording quality or performance.
- **House sound suffix**: 10–15 words appended to every prompt in a project (`warm analog mix, slight vinyl crackle, intimate vocal`) keeps an album coherent. Saved styles (bookmark icon next to the style prompt) make reuse easy.

### Production Direction Reference

| Mix style | Effect |
|---|---|
| Clean production | Polished, professional, clear separation |
| Lo-fi | Vintage, tape hiss, warm distortion |
| Raw | Unpolished, garage band, live feel |
| Polished | Radio-ready, compressed, loud |
| Atmospheric | Spacious, reverb, ambient |

| Era | Implies |
|---|---|
| 80s production | gated reverb, synths, big drums |
| 90s grunge | raw, mid-heavy, distorted |
| Modern pop | compressed, bright, wide stereo |
| Vintage soul | warm, analog, tape saturation |

| Dynamics | Use |
|---|---|
| Dynamic range | loud/soft variation — ballads, emotional arcs |
| Compressed | consistent volume — pop, radio |
| Punchy | impactful transients — rock, hip-hop |

Mix tags: punchy, wide stereo, vintage, modern, lo-fi, crisp, warm, bright, deep, spacious.

### Voice Type and Delivery

| Voice type | Range | Best for |
|---|---|---|
| Soprano | High female | Pop, musical theater, operatic |
| Mezzo-soprano | Mid female | Pop, rock, belting |
| Alto / contralto | Low female | Jazz, soul, folk |
| Tenor | High male | Pop, rock, R&B |
| Baritone | Mid male | Rock, country, spoken word |
| Bass / bass-baritone | Low male | Blues, gospel, deep storytelling |

| Delivery | Effect | Use for |
|---|---|---|
| Gritty | Raw, textured | Rock, grunge, blues |
| Smooth | Polished, clean | Pop, R&B, jazz |
| Raspy | Worn, emotional | Country, rock, soul |
| Breathy | Intimate, soft (skews young) | Indie, folk, bedroom pop |
| Powerful | Commanding, strong | Anthems, ballads, gospel |
| Conversational | Natural, storytelling | Folk, hip-hop, indie |

Vocal persona examples:

```
Male tenor, warm, slightly raspy, indie rock delivery
Female alto, sultry, breathy, R&B phrasing with subtle runs
Male baritone, gravelly, introspective, folk storyteller
```

Emotion words ("defiant", "powerful", "heartbroken") describe intent, which Suno cannot render; range and texture words ("mezzo-soprano, raw chest voice, rasp on the belted notes") describe sound, which it can. Lead with the latter. See [tips.md § Vocals](tips.md#4-vocals) for the escalation ladder when a vocal comes back generic or too young.

### With a Voice or Custom Model

- **Voice attached**: drop gender/register descriptors (the Voice carries them). Keep 1–2 genres plus instrumentation. Max Mode On. Voices cannot be used on instrumentals.
- **Custom Model**: drop generic production language ("glossy", "modern pop production") — the model already encodes the aesthetic. Keep genre, tempo, featured instruments and section-level direction.

---

## The Lyrics Box

### Everything Is Sung

Suno sings everything in the Lyrics Box except bracketed tags.

Never put these in the Lyrics Box — they will be sung as words:
- `(Machine-gun snare, guitars explode)`
- `(Instrumental break)`
- `(Verse 1)`
- stage directions, production notes, vocalist names, parenthetical descriptions

Only put actual lyrics and bracket tags. For instrumental passages use a tag alone: `[Instrumental]`, `[Break]`, `[Guitar Solo]`, `[Drum Break]`.

Parentheses around **words meant to be sung** are fine and useful: `Take me home (take me home)` produces a backing-vocal echo.

### Format

```
[Short Instrumental Intro]

[Verse 1 - quiet intimate]
First line of lyrics here
Second line of lyrics here

[Pre-Chorus - rising]
Build lines here

[Chorus - building anthemic]
Chorus lyrics here

[Guitar Solo]

[Bridge - raw exposed]
Bridge lyrics here

[Outro - fading]
Closing line
[End]
```

Rules:
- A structure tag on every section; numbered verses (`[Verse 1]`, `[Verse 2]`).
- A short Performance Cue (a word or two, no commas) after ` - ` on every tag. Cues plus any standalone delivery tag stay at **3 or fewer bracketed descriptors per section**.
- Clean lyrics only, with phonetic respellings applied ([pronunciation.md](pronunciation.md)). The published/streaming lyric sheet keeps standard spelling.
- End explicitly: `[Outro]` then `[End]` or `[Fade Out]`.
- Repeat the chorus verbatim; small variations are reported to come back as different melodies.

### Length and Line Shape

- Target **200–350 words** (up to ~500 for hip-hop/rap). Two verses + chorus + bridge is the sweet spot; avoid 4–5 verse songs. Dense or long lyrics make Suno rush, compress sections or skip content.
- Syllables per line: verses 7–9, choruses 10–12, overall 6–12 (mid-tempo pop 8–12, rap 12–16, ballads 6–8).
- Line breaks are breaths; `...` is a hold or trailing pause; commas mid-line barely register.
- Extended vowels (`Loooove`, `Ohhhh`) or hyphens (`lo-ove`, `sooo-long`) sustain notes. ALL CAPS reads as shouting — unpredictable, use for one line at most.
- Full lyric craft: references/lyrics/writing.md.

### Sound Effects and Atmosphere

Bracketed effect tags placed **mid-line** (not as standalone lines) trigger vocal/foley effects: `Walking through the night [footsteps]`. Full list in [tags.md § Sound Effect Tags](tags.md#sound-effect-tags).

For environmental sound, mention it in **both** boxes — repetition strengthens recognition:

| Lyrics Box mentions | Style Box adds |
|---|---|
| rain | `lofi effects rain` |
| thunder | `ambient thunder` |
| wind | `ambient wind textures` |
| fire | `crackling fire ambience` |
| ocean | `ocean waves background` |

### Prevent Word Changes and Token Bias

Suno gravitates toward pet words — **Neon, Echo, Ghost, Silver, Shadow, Whisper, Crystal, Velvet** — and may substitute them for yours. A reported countermeasure is the instruction `Do not change any words. Sing exactly as written.` at the top of the prompt. Put it in the Style Box, not the Lyrics Box (anything unbracketed in the Lyrics Box gets sung). Also avoid writing those words yourself unless you mean them.

---

## Exclude Styles (Negative Prompting)

Exclusions **shift the odds** against an element. They are probabilistic, not a hard filter, and cannot override a prompt that strongly implies the excluded thing.

- **Use the dedicated Exclude Styles field** (Advanced Mode → More Options; Pro/Premier). Inline `no drums` in the Style Box is ignored on v6 (a launch-week hands-on test saw "no drums" and "monotone vocals" both ignored). On a plan without the field, restructure the prompt so it does not imply the element.
- **2–4 items max.** Over-specifying dilutes the effect.
- **Bare elements, never "no"**: `drums`, `electric guitar`, `autotune`. The field is the negation; if `no drums` ever lands in the Style Box it asks *for* drums.
- **Only add exclusions with a clear reason.** "None" is the most common correct answer — but always decide explicitly and say "Exclude Styles: none" so it is visibly considered.

Typical values:
- Instruments: `drums`, `electric guitar`
- Vocal effects: `autotune`, `heavy reverb`
- Stylistic elements: `EDM drops`, `screaming`, `rap verse`
- Unwanted group vocals (a common Suno over-add): `choir`, `crowd vocals`, `backing vocals`, `gang vocals`, `call-and-response`, `vocal harmonies`, `layered vocals` — still probabilistic; pair with a leaner, more intimate Style Box.
- Vocal character: `youthful or breathy vocals`, `generic or polished studio pop vocal`

Auto-populate when the context implies it:

| Context | Exclusions |
|---|---|
| Acoustic folk | `electric instruments, drums` |
| A cappella | `instruments` |
| Lo-fi chill | `aggressive vocals` |
| Organic, unprocessed vocal | `autotune` (plus `natural pitch` in the Style Box) |

```
Good:  Style Box: "Acoustic folk, warm, intimate"   Exclude Styles: drums, electric instruments
Bad:   Exclude Styles: drums, bass, synths, reverb, distortion, ...
```

---

## Generation Settings

All under Advanced Mode → More Options. Fill these for every track and present them alongside the prompt.

| Setting | Rule |
|---|---|
| **Model** | `v6` for finished tracks. `v6-wild` for a first pass on an undecided sound, or genres where v6 is reported weak/generic (grunge, metal, alt-country, synth-pop, any rock or era-soul vocal drifting to a stock timbre); then Cover the keeper on `v6` — treat that step as experimental. `Custom: <name>` for album-wide consistency. `v6-mini` only on a Free account (not releasable). Details: [models-and-sliders.md](models-and-sliders.md). |
| **Variety** | **Off**, always, for an engineered Style Box. State a reason if you ever raise it. |
| **Max Mode** | **On** for tracks over ~2:00, any Cover, any Voice (20 credits instead of 10). Off for short ideas and sketches. Untested on v6-wild. |
| **Vocal Gender** | From the vocal description (most reliable gender control); leave unset when a Voice or Custom Model supplies the voice. |
| **Duration** | `Auto` unless a target duration is set. Custom accepts 10 s–6:00 and hard-cuts at the value, rushing lyrics that do not fit. |
| **Weirdness / Style Influence** | 50 / 50 unless a genre range in [models-and-sliders.md](models-and-sliders.md#recommended-starting-ranges-by-genre) says otherwise. Style Influence at 50 discards half the prompt's authority — raise it before blaming the prompt. |
| **Audio Influence** | Only with attached audio (Cover / Voice / upload): ~0.70–0.85 for a Voice. |

---

## Duration

| Target | Structure |
|---|---|
| Under 2:00 | 1–2 sections + `[End]`. Minimal tags. Add "short" or "concise" to the Style Box. Good for title screens, cutscenes, interludes. |
| Under 3:00 | 2 verses max, short bridge, no extended instrumentals |
| 3:00–5:00 | Standard structure |
| Over 5:00 | 3+ verses, pre-chorus, bridge, 1–2 instrumental sections; consider "extended" or "epic" in the Style Box. Max 8:00 (Auto/Extend); Custom Duration caps at 6:00. Quality may degrade past 6–7 min. |

Duration levers (especially for instrumentals/OSTs):
- **Section count is the primary lever** — fewer tags, shorter track.
- **`[End]` after `[Outro]`** is the strongest stop signal.
- **Duration Custom** hard-cuts; Auto plus section count is safer for lyric tracks. Expect 2–3 generations to hit a target either way.
- **Trim in post**: generate slightly long, fade/cut to length.
- **Very short (~1:00–1:30)**: `[Intro]` → `[Main Theme]` → `[End]` with Instrumental On.
- **Bar counts**: `[INTRO 4] [VERSE 1 8] [CHORUS 8] ... [OUTRO 4]` targets bars per section (approximate; see [tags.md](tags.md#bar-count-targeting)).

---

## Instrumental Tracks

- Advanced Mode, **Instrumental: On** (or leave lyrics blank). Simple Mode is unreliable for instrumentals.
- **Style Box**: genre, instrumentation, mood, tempo. No vocal description.
- **Lyrics Box**: structural tags only — `[Intro]`, `[Main Theme]`, `[Build-up]`, `[Drop]`, `[Bridge]`, `[Guitar Solo]`, `[Outro]`, `[End]`. No sung lyrics, no parentheticals.
- No pronunciation pass, no lyric review, no Voices (Voices cannot be instrumental).
- Narrative "producer's prompt" phrasing often beats a flat tag list: "Start with a lonely, overdriven slide guitar intro. Build into a heavy, stomping drum groove." See [tags.md § Instrumental Tags](tags.md#instrumental-tags) for section tags, solo-forcing tricks and genre instrument lists.
- Test a Style Box as an instrumental first to validate the bed independently of lyric problems.

---

## Genre-Specific Practices

### Hip-Hop / Rap

- **Vocals**: clear enunciation, rhythmic delivery, confident; describe flow if it matters.
- **Beat**: name the drums (808 kick, crisp snare, trap hi-hats, sampled drums).
- **Subgenre**: boom bap, trap, lo-fi, nerdcore.
- **Tempo**: 70–100 BPM laid-back, 100–140 energetic.
- **Production**: vocal upfront, beat as foundation; minimal, let vocals breathe.
- **Key instruments**: kick, snare, hi-hats, 808 bass; piano, strings, vocal samples.

```
Male rapper, clear delivery, storytelling flow. Boom-bap hip-hop,
808 kick, vinyl crackle, dusty samples. Lo-fi production.
```

| Arrangement | Exclude Styles |
|---|---|
| Boom-bap | `autotune, synths` |
| Lo-fi | `live drums, electric guitar` |
| Trap | `live instruments, acoustic guitar` |

### Alternative Rock

- **Vocals**: passionate, dynamic (quiet verse / loud chorus).
- **Guitars**: specify clean vs distorted and tone.
- **Energy**: build verse to chorus. **Production**: live feel, room ambience.
- **Key instruments**: electric guitar (clean/distorted), bass, drums; optional organ/keys.

```
Male baritone, emotional delivery, dynamic range. Alternative rock,
clean guitar in verses, distorted chorus, driving bass, tight drums.
Modern production with live energy.
```

| Arrangement | Exclude Styles |
|---|---|
| Acoustic version | `electric guitar, drums` |
| Stripped-down | `synths, backing vocals` |
| Unplugged | `electric instruments, programmed drums` |

Rock, metal, grunge, blues-rock and alt-country are v6's weakest genres: vocals drift to a generic post-grunge timbre and heavy guitars can blur together. Sharpen the vocal texture descriptor and keep it first; if it still drifts, first-pass on v6-wild or use a Custom Model. Lock Style Influence high and Weirdness low for metal.

### Punk

- Specify subgenre: pop-punk, hardcore, skate punk.
- Note tempo (usually fast) and vocal style: snotty, shouted, melodic.
- Short and fast structure; see [tags.md](tags.md#example-structures).

### Electronic

- **Name the subgenre**: house, techno, IDM, synthwave. **BPM is critical** for dance music.
- **Synths**: describe texture (warm analog, cold digital, chiptune; pad, lead, arp).
- **Rhythm**: programmed drums, quantized or swung. **Vocals**: often processed (reverb, delay, vocoder).
- **Production**: layered, atmospheric, effects.

```
Female alto, ethereal, breathy vocals. Downtempo electronic,
warm analog synths, sub-bass, crisp programmed drums.
Atmospheric production, spacious reverb.
```

| Arrangement | Exclude Styles |
|---|---|
| Ambient | `drums, vocals` |
| Minimal | `vocals, acoustic instruments` |
| Downtempo | `live drums, electric guitar` |

### Folk / Indie

- **Vocals**: conversational, intimate, natural; state the intimacy level.
- **Instruments**: acoustic, organic — fingerpicked guitar, banjo, mandolin, upright bass, light percussion.
- **Arrangement**: sparse, room for vocals. **Production**: minimal, natural ambience.

```
Male tenor, intimate storytelling, conversational. Indie folk,
fingerpicked acoustic guitar, subtle upright bass, light brushed drums.
Natural room sound, minimal production.
```

| Arrangement | Exclude Styles |
|---|---|
| Sparse/intimate | `drums, electric instruments` |
| Solo acoustic | `drums, electric instruments, harmony vocals` |
| Full band | `synths, electric guitar` |

### Country

- **Vocals**: twang optional, clear storytelling. **Rhythm**: straight or shuffle.
- **Instruments**: steel guitar, fiddle, acoustic rhythm, walking bass, light drums.
- **Production**: natural, warm, organic.

```
Male baritone, warm twang, clear storytelling. Traditional country,
steel guitar, acoustic rhythm, walking bass. Classic Nashville production.
```

| Arrangement | Exclude Styles |
|---|---|
| Traditional | `electric instruments, synths` |
| Acoustic | `drums, electric instruments` |
| Bluegrass | `drums, electric guitar, synths` |

### K-Pop

K-pop is hard for Suno: maximalist production, multi-vocal architecture, language mixing and mid-song genre switches.

- Always include `K-pop` plus production terms (`maximalist`, `glossy`, `dynamic shifts`).
- Vocal description first: `mixed group vocals, layered harmonies, K-pop idol group`. **`mixed group vocals` is the single most important tag** for a multi-member sound; add `gang vocals`, `group chant` for chorus density.
- Concept type: `girl crush`, `cute concept`, `dark concept`, `retro disco`.
- BPM: dance 120–140, ballads 60–80, hip-hop 80–100.
- Backing echoes in lyrics: `I'm on fire (on fire!)`. Use `[All]` or `[Group]` before chant sections and `[Rap Verse]` to signal a different vocal character.
- **Korean-English code-switching**: romanized Korean with hyphens is more reliable than Hangul (`Sa-rang-hae`, not `Saranghae`). Add `[Clear Vocals]` when mixing languages; keep English hooks and Korean verses in separate sections.
- **The switch-up** (mid-song genre change): put a genre cue on each section, and add `genre-fluid, dynamic shifts, maximalist K-pop production` to the Style Box. Carry the cue in the tag (`[Chorus - explosive EDM drop]`); the community pattern of a parenthetical line under the tag (`(Soft R&B groove, gentle piano)`) risks being sung.
- **Section structure** (more sections than Western pop): Intro → Verse 1 → Pre-Chorus → Chorus → Post-Chorus → Verse 2 → Pre-Chorus → Chorus → Rap Verse → Bridge → Dance Break → Final Chorus (key change up) → Outro. `[Dance Break]` with minimal/no lyrics; mark the final chorus `[Final Chorus - key change up]`.

| Problem | Solution |
|---|---|
| Generic pop, not K-pop | `K-pop` + `maximalist` + `glossy` + concept keywords |
| Solo voice instead of group | `mixed group vocals`, `layered harmonies`, `K-pop idol group` |
| No mid-song switch-up | Per-section genre cues, not just the global prompt |
| Korean garbled | Romanized Korean with hyphens; `[Clear Vocals]` |
| Rap sounds like singing | `[Rap Verse - aggressive rap flow]` |
| Dance break has singing | Leave `[Dance Break]` empty; `[Dance Break - instrumental heavy beat]` |

```
Girl crush:   K-pop girl group, fierce EDM trap, sassy vocals, heavy bass drop, chant chorus, 135 BPM, confident attitude, glossy production
Bright/cute:  K-pop, bubblegum pop, bright synths, chirpy vocals, catchy hook, youthful energy, 125 BPM, layered harmonies
Dark:         K-pop, industrial synths, aggressive rap, EDM bass drops, distorted bass, maximalist chaos, 140 BPM, mixed group vocals
K-ballad:     Korean ballad, emotional piano, string orchestra, soaring vocals, key change final chorus, 70 BPM, cinematic, lush arrangement
```

### Genre Quality Notes (v6)

- Reported strong: pop, drum & bass, UK garage.
- Reported weak: grunge, metal, alt-country, synth-pop, rock/era-soul vocals; niche heavy subgenres (metalcore, extreme styles) may miss hallmarks; acoustic nuance not always captured; extreme cross-style fusions get muddy.

For a full genre profile (characteristics, lyric conventions, keywords), read references/genres/<genre-slug>/README.md.

---

## Duets and Voice Switching

Alternate section tags per character (`[Verse - Character A]` / `[Verse - Character B]`) **and** say it in the Style Box: `Dual vocalists, male and female, trading verses`. Without both you get one singer. For a joint chorus describe it in the Style Box (`duet chorus, blended male/female harmony`) rather than inventing a tag. See [tags.md § Duet](tags.md#duet--call-and-response).

---

## Common Issues & Fixes

| Problem | Fix |
|---|---|
| Vocals buried in mix | Put the vocal description first; say "clear and prominent vocals" or "lead vocal 1–2 dB louder than band"; shorten the intro (`[Short Instrumental Intro]`) |
| Lyrics not audible / clip won't sing | Simplify the prompt; describe vocals explicitly; introduce vocals early (a hook or "Ahh ahh ahh") |
| Wrong genre interpretation | Be more specific with the genre; raise Style Influence |
| Song cuts off early / rambles | `[Outro]` then `[End]` |
| Repeating sections | Clear section tags; vary Verse 2 lyrics |
| Mispronunciation | Phonetic spelling in the Lyrics Box ([pronunciation.md](pronunciation.md)) |
| Unwanted elements | Exclude Styles, 2–4 bare elements |
| Slower, sparser or longer than intended | State BPM/"driving", density ("busy"/"layered") and length explicitly |
| Vocal drifts to a generic timbre (rock, metal, grunge, alt-country) | Sharpen the vocal texture descriptor and keep it first; then v6-wild first pass or a Custom Model |
| Cover drifts from the source melody | Confirm Variety Off and Max Mode On before touching Audio Influence |
| Narrow stereo image | Reported on v6; fix in the mix rather than the prompt (references/production/mixing.md) |
| Mix feels flat | Add "bus compression 2–3 dB, slow attack/fast release" |
| Arrangement too busy | Specify rests: "verse 2: bass rests for 4 bars" |
| Genre drift | Reassert influences mid-prompt |
| Chorus not lifting | Add "double-time hats; octave guitars" |
| Flat, generic performance | Add Performance Cues to every section tag |

---

## Quality Standards (after generating)

Keep a take only when:
- [ ] Vocal clarity and pronunciation are right
- [ ] Genre/style matches intent
- [ ] Emotional tone is appropriate
- [ ] Mix balance is right (vocals not buried)
- [ ] Structure follows the tags
- [ ] No awkward cuts, loops or transitions; ending is clean
- [ ] Lyrics match what was written
- [ ] No unwanted instruments/elements (exclusions worked)

---

## Artist Name Blocklist

**Never use real artist or band names in the Style Box.** On v6 Suno rewrites them and shows "Artist name '…' replaced" ("We don't reference artists directly, so we've replaced your prompt with similar styles you might like.") — your intent goes with the name. Partner-label deals do not unlock names.

**The rule:** if you are about to type an artist name, stop and describe the sound instead. Reverse-engineer in five dimensions — instrumentation, vocal character, rhythm feel, production era, lyrical stance — and use the Sound Blueprint in [tips.md](tips.md#5-distilling-an-artists-sound). Rhythm-section descriptions carry the most identity with the least baggage.

Suno also filters words matching producer tags in lyrics: **"ninety-three"** collides with the producer tag "ninetythree" — write `'93` or rephrase. If you hit a filter error, try an alternate spelling or rephrase.

The list below is not exhaustive; any real artist name is out.

### Electronic & Dance
| Don't say | Say instead |
|---|---|
| Daft Punk | French house, vocoder vocals, disco-funk, filtered synths |
| Deadmau5 | progressive house, melodic synths, building drops |
| Aphex Twin | IDM, glitchy beats, ambient textures, experimental |
| Skrillex | aggressive dubstep, heavy drops, distorted bass |
| The Prodigy | big beat, aggressive electronic, rave energy |
| Kraftwerk | robotic vocals, minimal synths, electronic pioneer |
| Tiesto | euphoric trance, festival anthems, building energy |
| Calvin Harris | dance pop, catchy hooks, polished production |
| Carly Rae Jepsen | upbeat synth-pop, 80s-influenced, breathy female vocals |

### Hip-Hop & Rap
| Don't say | Say instead |
|---|---|
| Eminem | rapid-fire aggressive rap, complex rhyme schemes, intense delivery |
| Kendrick Lamar | conscious hip-hop, jazz samples, introspective, dynamic flow |
| Drake | melodic rap, R&B-infused, emotional, atmospheric |
| Jay-Z | confident flow, luxury rap, storytelling, NYC style |
| Nas | lyrical hip-hop, boom bap, street poetry, NYC golden era |
| Kanye West | experimental hip-hop, soulful samples, genre-bending |
| Travis Scott | dark trap, auto-tuned vocals, psychedelic, atmospheric |
| MF DOOM | abstract lyrics, jazz samples, complex wordplay, masked villain |

### Jazz & Blues
| Don't say | Say instead |
|---|---|
| Miles Davis | cool jazz, modal, atmospheric trumpet, sophisticated |
| John Coltrane | spiritual jazz, intense saxophone, exploratory |
| BB King | expressive blues guitar, soulful bends, Memphis blues |
| Robert Johnson | delta blues, acoustic, haunting, raw |
| Herbie Hancock | jazz fusion, funky keyboards, experimental |
| Billie Holiday | torch song, melancholic jazz vocals, intimate |

### Rock & Metal
| Don't say | Say instead |
|---|---|
| Metallica | thrash metal, aggressive riffs, double bass drums, heavy |
| Led Zeppelin | blues rock, powerful vocals, heavy riffs, epic |
| Pink Floyd | progressive rock, atmospheric, psychedelic, conceptual |
| Nirvana | grunge, raw vocals, quiet-loud dynamics, angst |
| Black Sabbath | doom metal, heavy riffs, occult themes, dark |
| Radiohead | art rock, experimental, electronic textures, melancholic |
| AC/DC | hard rock, driving riffs, raw vocals, high energy |
| The Beatles | British invasion, melodic pop rock, harmonies |

### Punk
| Don't say | Say instead |
|---|---|
| Pennywise | fast melodic punk, aggressive male vocals, skate punk energy |
| Green Day | pop punk, snotty vocals, power chords, anthemic chorus |
| Blink-182 | pop punk, nasally vocals, youthful, catchy hooks |
| NOFX | fast punk, sarcastic, political, melodic |
| Bad Religion | melodic hardcore, intellectual, harmonized vocals |
| Ramones | classic punk, simple chords, fast tempo, NYC punk |
| Sex Pistols | raw punk, sneering vocals, rebellious, aggressive |
| Dead Kennedys | hardcore punk, satirical, surf-influenced guitar |

### Pop & Contemporary
| Don't say | Say instead |
|---|---|
| Taylor Swift | narrative pop, confessional lyrics, polished production |
| The Weeknd | dark synth-pop, falsetto, 80s-inspired, moody R&B |
| Dua Lipa | disco-pop, dance-floor ready, confident female vocals |
| Beyonce | powerful R&B vocals, dance pop, empowering |
| Michael Jackson | pop perfection, dance grooves, iconic hooks |
| Madonna | dance pop, provocative, reinvention, iconic |
| Prince | funk-pop, falsetto, genre-blending, virtuosic |
| Lady Gaga | theatrical pop, dance beats, dramatic, avant-garde |

### R&B & Soul
| Don't say | Say instead |
|---|---|
| Frank Ocean | alternative R&B, dreamy production, falsetto, introspective |
| SZA | neo-soul, vulnerable vocals, atmospheric, confessional |
| Marvin Gaye | smooth soul, romantic, socially conscious, Motown |
| Aretha Franklin | powerful soul vocals, gospel-influenced, commanding |
| D'Angelo | neo-soul, organic production, sensual, groove-heavy |
| Erykah Badu | neo-soul, jazz-influenced, spiritual, eclectic |

### Country & Folk
| Don't say | Say instead |
|---|---|
| Johnny Cash | deep baritone, traditional country, train-beat rhythm |
| Dolly Parton | bright female country vocals, Appalachian, storytelling |
| Willie Nelson | outlaw country, conversational vocals, acoustic guitar |
| Bob Dylan | folk rock, poetic lyrics, harmonica, nasal vocals |
| Joni Mitchell | folk, soprano vocals, open tunings, introspective |
| Hank Williams | honky tonk, lonesome vocals, classic country |

### World & Cultural
| Don't say | Say instead |
|---|---|
| Bob Marley | roots reggae, conscious lyrics, one drop rhythm |
| Fela Kuti | afrobeat, polyrhythmic, brass sections, political |
| Buena Vista Social Club | Cuban son, nostalgic, acoustic, warm |
| Ravi Shankar | Indian classical, sitar, meditative, intricate |

### Classical, Film & Game
| Don't say | Say instead |
|---|---|
| Hans Zimmer | epic film score, powerful brass, modern orchestral |
| John Williams | sweeping orchestral, heroic themes, cinematic |
| Beethoven | romantic classical, dramatic dynamics, symphonic |
| Mozart | classical period, elegant, balanced, melodic |
| Ennio Morricone | spaghetti western, dramatic, haunting melodies |
| Danny Elfman | quirky film score, gothic, whimsical orchestral |
| Vangelis | synth soundtrack, atmospheric, epic electronic |
| Nobuo Uematsu | JRPG score, emotional, orchestral with synths |
| Koji Kondo | video game music, melodic, adventurous, iconic |

### Vocal & Choral
| Don't say | Say instead |
|---|---|
| Pentatonix | modern acapella, vocal percussion, pop arrangements |
| Bobby McFerrin | vocal jazz, scatting, innovative, playful |
| The King's Singers | classical choral, precise harmonies, British |
| Sweet Honey in the Rock | acapella gospel, African-American spiritual, powerful |

### K-Pop & Korean
| Don't say | Say instead |
|---|---|
| BTS | genre-fluid K-pop, anthemic hooks, trap-to-R&B shifts, stacked vocal harmonies, hip-hop dance pop |
| BLACKPINK | fierce EDM trap, bass drops, sassy rap vocals, chant chorus, booming 808s, glossy K-pop |
| Stray Kids | noise K-pop, industrial synths, aggressive rap, frenetic bass, EDM breakdowns, hard-hitting trap |
| NewJeans | Y2K pop, jersey club beats, UK garage two-step, dreamy R&B, minimal layering, retro 2000s |
| aespa | hyperpop, glitchy synths, bubblegum bass, cyberpunk electropop, futuristic maximalist |
| (G)I-DLE | moombahton-trap, orchestral over modern drums, pop-rock crossover, bold genre shifts |
| ATEEZ | anthemic K-pop, explosive EDM drops, theatrical energy, dramatic trap, brass-heavy |
| EXO | polished R&B-pop, electropop, 90s-inspired harmonies, synth-pop, smooth layered vocals |
| Girls' Generation | bubblegum electropop, bright high-register vocals, Europop synths, chirpy hooks |
| Big Bang | hip-hop electro-pop, genre-bending, swaggering rap verses, electronic dance hooks |
| TWICE | bubblegum pop, chirpy hooks, color-pop energy, brass electro-pop, youthful dance-pop |
| Red Velvet | dual-concept pop, bright quirky hooks and sleek 90s R&B, neo-soul undertones |
| SHINee | contemporary R&B, acid electro funk, sophisticated dance-pop, late-80s pop groove |
| IU | acoustic pop-jazz, coffeehouse instrumentation, breathy intimate vocals, orchestral strings |
| SEVENTEEN | self-produced pop, orchestral arrangements, bright synth-pop, layered harmonies |
| IVE | glamorous synth-pop, bold dance-pop, reverb-heavy chorus, anthemic melodies |
| LE SSERAFIM | polished synth-pop, punchy electronic beats, R&B-tinged dance-pop, shimmering layers |
| 2NE1 | swaggering hip-hop, explosive EDM, fierce female rap, reggae-trap fusion, bold electropop |
| Dreamcatcher | K-pop metal, distorted guitars with dance-pop, rock-electronic hybrid, dark melodic hooks |
| ITZY | teen crush pop-EDM, bass house verses, electro house chorus, sassy attitude |
| TXT | dreamy ethereal pop, pop-rock crossover, falsetto layered vocals, stadium rock energy |
| ENHYPEN | dark electronic pop, eerie synths, cinematic falsettos, vampiric atmosphere |
| Epik High | alternative K-hip-hop, boom bap beats, bilingual rap, soul-infused, genre-crossing |
| Zion.T | minimalist K-R&B, dreamy Rhodes piano, smooth falsetto, jazz-pop fusion |
| Crush | neo-soul K-R&B, jazz harmony, intimate vocal delivery, analog warmth |

### Industrial & Experimental
| Don't say | Say instead |
|---|---|
| Nine Inch Nails | dark industrial, grinding synths, distorted vocals, aggressive |
| Ministry | industrial metal, aggressive, political, heavy guitars, rapid-fire percussion |
| KMFDM | industrial rock, electronic beats, German, heavy |
| Throbbing Gristle | industrial pioneer, noise, confrontational, experimental |
| Bjork | art pop, experimental, eclectic, theatrical vocals |

Before finalizing, scan the Style Box for any proper name at all — including names hidden inside descriptive phrases ("X-era groove", "Y-style vocals").

---

## Genre Vocabulary

Suno recognizes 500+ style names. Combine for fusions ("Disco Funk", "Arabian Rock", "Jazz Hip Hop", "Electronic Folk", "Cyberpunk Country", "Psychedelic Blues", "Gothic Pop", "Orchestral Metal").

**Electronic & Dance:** Acid Jazz, Ambient, Bass House, Brostep, Chillwave, Club, Cyberpunk, Dance, Dance Pop, Dark Ambient, Dark Electro, Deep House, Deep Techno, Downtempo, Drone, Dub, Dub Techno, Dubstep, EDM, Electro, Electro Swing, Electroacoustic, Electronic, Electropop, Eurodance, French House, Future Bass, Future Garage, Future House, Gabber, Glitch, Glitch Hop, Glitch Pop, Goa Trance, Happy Hardcore, Hardstyle, House, Hyperpop, IDM, Industrial, Jungle, Minimal Techno, Moombahton, Neurofunk, Nu Disco, Post-Disco, Post-Dubstep, Progressive House, Psybient, Psychedelic Trance, Rave, Space Disco, Synthwave, Tech House, Techno, Trance, Trip Hop, Tropical House, UK Funky, UK Garage, Vaporwave, Vocal House, Vocal Trance, Witch House

**Hip Hop & Rap:** Crunk, Hip Hop, Mumble Rap, Pop Rap, Rap, Trap, UK Drill, West Coast Rap, Jazz Rap, Boom Bap, Lo-fi Hip Hop, Conscious Hip Hop, Gangsta Rap, Southern Hip Hop, East Coast Hip Hop, Underground Hip Hop, Nerdcore

**Jazz & Blues:** Bebop, Big Band, Blues, Cool Jazz, Dark Jazz, Delta Blues, Gypsy Jazz, Hard Bop, Jazz, Jazz Fusion, Latin Jazz, Modal Jazz, New Orleans Jazz, Nu Jazz, Piano Blues, Piedmont Blues, Post-Bop, Punk Blues, Smooth Jazz, Soul Jazz, Swing

**Rock & Metal:** Alternative Rock, Arena Rock, Art Rock, Black Metal, Blues Rock, Classic Rock, Death Metal, Doom Metal, Emo, Garage Rock, Glam Rock, Gothic Rock, Grunge, Hair Metal, Hard Rock, Heavy Metal, Indie Rock, Math Rock, Metal, Metalcore, New Wave, Noise Rock, Nu Metal, Post-Hardcore, Post-Punk, Post-Rock, Progressive Metal, Progressive Rock, Psychedelic Rock, Punk, Punk Rock, Shoegaze, Skate Punk, Sludge Metal, Soft Rock, Southern Rock, Stoner Rock, Surf Rock, Thrash Metal

**Pop & Contemporary:** Adult Contemporary, Avant-garde, Bedroom, Broadway, Disco, Disco Funk, Dream Pop, Europop, Funk, Indie, Indie Pop, J-pop, K-pop, Latin Pop, Lounge, Motown, Neon Pop, Noise Pop, Pop, Pop Punk, Pop Rock, Power Pop, Psychedelic Pop, R&B, Contemporary R&B, Singer-Songwriter, Soul, Synth-pop, Thai Pop, Urban Contemporary

**Folk & Country:** Acoustic, Alt-Country, Americana, Appalachian, Bluegrass, Celtic, Country, Country Rock, Folk, Folk Pop, Folk Rock, Honky Tonk, Irish Folk, Nashville Sound, Neo-Folk, Outlaw Country, Traditional Folk

**World & Cultural:** Afrobeat, Arabian, Bossa Nova, Calypso, Cumbia, Dancehall, Flamenco, Forro, Highlife, Indian Classical, Klezmer, Latin, Mariachi, Mediterranean, Middle Eastern, Persian, Polka, Reggae, Reggaeton, Salsa, Samba, Soca, Tango, Zouk

**Classical & Orchestral:** Baroque, Chamber Music, Choral, Classical, Contemporary Classical, Film Score, Impressionist, Minimalist, Neo-Classical, Opera, Orchestral, Romantic, Symphony

**Soundtrack & Theme:** Audiobook Background, Background, Cinematic, Movie Soundtrack, Score, Spaghetti Western, TV Themes, Video Game Music, Villain Theme

**Experimental & Avant-garde:** Avant-garde Jazz, Dark Cabaret, Dungeon Synth, Experimental, Harsh Noise, Martial Industrial, Musique Concrète, Noise, No Wave, Power Electronics, Sound Art, Sound Collage, Tape Music

**Vocal & Choral:** Acapella, Barbershop, Beatboxing, Choir, Christmas Carol, Doo Wop, Gregorian Chant, Islamic Call to Prayer, Throat Singing, Vocal, Vocal Jazz, Vocaloid

Short style-prompt examples:

```
EDM future bass, syncopated rhythms
Upbeat House, Female vocal
Jazzy Blues, sparse vocals, acoustic guitar, stomp
Bittersweet Hindustani Electro-pop, melodic sarod, ornamental singing
Folk, Introspective, Banjo and synthesizer, Rural futurism, Minimalist
```

---

## Writing a New Genre Profile

When a genre has no profile yet, create references/genres/<genre-slug>/README.md.

1. **Slug**: lowercase, hyphenated ("Math Rock" → `math-rock`). If the profile already exists, stop and use it.
2. **Research**: verify origin years, pioneers, landmark albums and track titles with a web search. Do not guess dates or album names — omit rather than guess.
3. **Read 1–2 existing profiles** (e.g. references/genres/hip-hop/README.md) for tone and depth.
4. **Write the file** starting directly with `# Genre Name` (no frontmatter), in exactly this section order:

```
# {Genre Name}

## Genre Overview
## Characteristics
## Lyric Conventions
## Subgenres & Styles
## Artists
## Suno Prompt Keywords
## Reference Tracks
```

**Genre Overview** — three prose paragraphs, no bullets. P1: origin, cultural roots, pioneers with names and years. P2: evolution across decades, key moments, mainstream breakthrough, regional variants. P3: current state, influence on other genres, modern scene. Encyclopedic but alive: concrete names, years, albums.

**Characteristics** — bullets, exactly these six:
- **Instrumentation**: typical instruments, specific models/brands where relevant
- **Vocals**: singing style, processing, delivery
- **Production**: techniques, mix aesthetic, sonic character
- **Energy/Mood**: mood spectrum, emotional range
- **Structure**: song form, typical length, structural quirks
- **Tempo**: BPM ranges per subgenre, rhythm feel (half-time, swing, straight)

**Lyric Conventions** — bullets, exactly these six:
- **Default rhyme scheme**: with shorthand (AABB, ABAB, XAXA)
- **Rhyme quality**: multisyllabic, slant, internal, etc.
- **Verse structure**: line count, bar structure
- **Key rule**: the single most important lyric rule in this genre
- **Avoid**: what not to do
- **Density/pacing (Suno)**: `Default **X lines/verse** at Y BPM. [Context]. Topics: Z/verse.`

**Subgenres & Styles** — table `| Style | Description | Reference Artists |`; 6–12 rows; descriptions 2–3 sentences with musical specifics, not adjectives; 3–4 reference artists each. If a subgenre has its own profile, reference it instead of duplicating.

**Artists** — table `| Artist | Key Albums | Era | Style Focus |`; 10–20 artists mixing pioneers, peak-era and current acts; albums in italics.

**Suno Prompt Keywords** — one fenced code block of comma-separated English keywords on thematic lines: genre/subgenre labels, instruments, production, mood/atmosphere, vocals, tempo/rhythm, era/aesthetic. Only terms Suno understands. No artist names.

**Reference Tracks** — 10–15 entries, `- **Artist - "Track Title"** — description`; 2–3 sentences each on what makes it a reference point (concrete musical elements, historical significance); chronological spread from founding tracks to modern.

Rules: every section substantive (research rather than leave one thin); English throughout; Lyric Conventions and Suno Prompt Keywords matter most because they drive generation. Ban these phrases: "tapestry of sound", "sonic landscape", "testament to", "rich tapestry", "sonic journey", "pushing boundaries", "transcends genre".

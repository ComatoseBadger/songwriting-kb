# Suno Tags

Bracket tags and Style Box descriptors: structure, delivery, instrumental and vocal vocabulary. How to assemble them into a full generation is in [prompting.md](prompting.md).

---

## Meta-Tag Syntax

"Metatag" is used loosely for any bracketed Suno keyword. Keep four categories apart:

| Category | Example | Where it goes | Use |
|---|---|---|---|
| Structure tags | `[Verse]`, `[Chorus]`, `[Post-Chorus]` | Lyrics Box | **Mandatory** on every section |
| Performance Cues | `[Verse 1 - quiet intimate]` | Lyrics Box, appended to the structure tag after ` - ` | **Default** on every section |
| Delivery/mood bracket tags | `[Whispered]`, `[Aggressive]` | Lyrics Box, standalone | Optional accent |
| Style Box descriptors (prose, not brackets) | `gravelly, belting, Southern rock vocal` | Style Box, comma-separated | How Suno wants mood/energy/instrumentation |
| Inline lyrical metatags | `[Verse 1: Raspy older female vocal, husky contralto]` | Lyrics Box, inside the section tag | Escalation for stubborn vocal-identity problems, not a default |

Syntax rules:
- Square brackets are tags and are not sung. Anything unbracketed in the Lyrics Box — including parenthetical stage directions — is sung.
- Parentheses hold **sung** backing vocals/echoes: `Take me home (take me home)`.
- Performance Cue format: structure tag, space, hyphen, space, a word or two, no commas: `[Outro - chant fading]`, not `[Outro - chant, fading]`.
- **Budget: at most 3 bracketed descriptors per section** (cue + any accent tags). More causes noise ("tag soup" / prompt fatigue).
- Bar-count numbers follow the tag name: `[VERSE 1 8]`.
- Effect tags (`[laughter]`) go mid-line, not on their own line.
- Suno's own lyrics editor now offers "Melodic instructions" that add one bracketed production note per section (e.g. `[half-time drums]`), and a launch-day test found v6's description of an output naming details that existed only in a `[Bridge | Female — Whispered …]` cue — per-section direction is read.

---

## Structure Tags

### Section Tags

```
Intro:         [Intro]  [Short Instrumental Intro]  [Intro - Spoken]
Verse:         [Verse]  [Verse 1]  [Verse 2]  [Catchy Verse]  [Rap Verse]
Pre/Post:      [Pre-Chorus]  [Post-Chorus]
Chorus:        [Chorus]  [Hook]  [Catchy Hook]  [Final Chorus]
Bridge:        [Bridge]
Instrumental:  [Break]  [Interlude]  [melodic interlude]  [Guitar Solo Interlude]  [Percussion Break]  [Instrumental Break]
Group:         [All]  [Group]
Endings:       [Outro]  [End]  [Fade Out]  [Fade to End]  [Big Finish]  [Refrain]
Other:         [Fade In]  [Dance Break]  [Main Theme]
Extend:        [Continue]   (when continuing from an existing song)
```

`[Intro]` is notoriously unreliable and can bury the vocal; prefer `[Short Instrumental Intro]` or `[Intro - Spoken]`. If the vocal disappears, cut intro descriptors or open with `[Vocals enter immediately]`.

### Reliability Tiers

| Tier | Tags |
|---|---|
| Reliable | `[Verse]`/`[Verse 1]`, `[Chorus]`, `[Pre-Chorus]`, `[End]`, `[Fade Out]` |
| Moderately reliable | `[Bridge]`, `[Break]`, `[Outro]` |
| Less reliable | `[Intro]` (use descriptive alternatives); `[Post-Chorus]`, `[Fade In]` (less field-tested — test first); custom tags (results vary) |

Untagged blocks get treated as verses. `[Solo]` alone often produces noodling — name the instrument (`[Guitar Solo]`, `[Saxophone Break]`); `[Instrumental Break]` beats `[Solo]`.

### Performance Cues

Append a brief cue to every structure tag. This is how an emotional arc is carried across a song; bare tags throughout are a common, easy-to-miss cause of flat output. Put the sharpest variation where the arc shifts.

```
[Verse 1 - quiet intimate]
[Pre-Chorus - rising]
[Chorus - building anthemic]
[Verse 2 - cold regal]
[Bridge - raw breaking]
[Final Chorus - full release]
[Outro - chant fading]
```

Keep the cue to a word or two. Long cue lists cause noise. Combined descriptions also work as the tag itself: `[Soft Verse]`, `[Building Chorus]`.

Section dynamics to aim for:

| Section | Dynamics | Phrasing | Vibrato |
|---|---|---|---|
| Verse | Low | Tight | Minimal |
| Pre-Chorus | Rising | Shorter | Growing |
| Chorus | High/open | Sustained | Full |
| Bridge | Variable | New texture | Altered |

### Delivery / Mood Bracket Tags

Standalone accents that color delivery without defining a section. Count them against the 3-per-section budget.

```
[Shout]        aggressive, shouted delivery
[Whimsical]    playful, light tone
[Melancholy]   sad, reflective
[Spoken]       spoken word, not sung
[Whispered]    quiet, intimate
[Energetic]    high energy
[Aggressive]   intense, confrontational
[Intimate]     personal, close, hushed
[Playful]      lighthearted, fun
[Triumphant]   victorious, anthemic
[Vulnerable]   raw, exposed
[Haunting]     eerie, unsettled
[Full voice]   opens up after a whispered section
[Clear Vocals] / [High Fidelity Vocals]   when mixing languages
```

Whisper and spoken tags work best paired with contrast: `[Whispered, intimate]` at the start of a verse, then `[Full voice]` at the pre-chorus.

### Inline Lyrical Metatags (escalation)

When Style Box range/texture descriptors still fail to fix vocal identity on a fresh generation, put the vocal descriptor inside every section tag — Suno may weight it independently of the Style Box:

```
[Verse 1: Raspy older female vocal, husky contralto]
[Chorus: Raspy older female vocal, husky contralto]
```

Repeat it on every section, not just the first. This is not a default pattern.

### Bar Count Targeting

```
[INTRO 4] [VERSE 1 8] [PRE 4] [CHORUS 8] [VERSE 2 8] [PRE 4] [CHORUS 8] [BRIDGE 8] [CHORUS 8] [OUTRO 4]
```

Numbers are target bar counts. Results are approximate (guidance, not limits). Useful for intro/outro length and balancing section proportions; combine with normal section tags in the Lyrics Box. Not verified on v6.

### Example Structures

Basic pop/rock:
```
[Short Instrumental Intro]
[Verse 1]
[Chorus]
[Verse 2]
[Chorus]
[Bridge]
[Chorus]
[Outro]
[Fade Out]
```

Hip-hop:
```
[Intro - Spoken]
[Verse 1]
[Chorus]
[Verse 2]
[Chorus]
[Verse 3]
[Outro]
[End]
```

Punk (short and fast):
```
[Intro]
[Verse 1]
[Chorus]        shout-along
[Verse 2]
[Chorus]
[Break]
[Chorus]
[Big Finish]
```

Radio edit (~3:00), chorus inside the first 45 seconds:
```
[Intro]          4 bars, one spoken or sung line optional
[Verse 1]        4–8 lines, establish scene
[Pre-Chorus]     2–4 lines, build
[Chorus]         4 lines, title twice
[Verse 2]        4–8 lines, change time/perspective
[Pre-Chorus]
[Chorus]
[Bridge]         4 lines, new truth
[Chorus]         final, with lift
[Outro]
[End]
```

(The annotations to the right are notes for you, not Lyrics Box content.)

Noise / ambient pieces still respond to structure tags, including custom ones: `[Build]`, `[Collapse]`, `[Drone]`, `[Silence]`, `[Rupture]`.

---

## Sound Effect Tags

Place mid-line: `Then suddenly [laughter] breaks the silence`.

| Group | Tags |
|---|---|
| Human | `[laughter]` `[screaming]` `[whisper]` `[sigh]` `[gasp]` `[cough]` |
| Crowd | `[crowd]` `[applause]` `[cheering]` |
| Mechanical / transition | `[echo]` `[phone ringing]` `[static]` `[record scratch]` `[footsteps]` |
| Ad-libs | `[yeah]` at line end — keep to the second half of the song where energy peaks |

Environmental sounds (rain, wind, fire, ocean) go in both the Lyrics Box and the Style Box — see [prompting.md § Sound Effects and Atmosphere](prompting.md#sound-effects-and-atmosphere).

---

## Instrumental Tags

### Instrumental Section Tags

Use like `[Verse]` but with no lyrics under them:

```
[Instrumental]  [Instrumental Break]  [melodic interlude]  [Guitar Solo Interlude]
[Guitar Solo]  [Piano Solo]  [Drum Solo]  [Bass Solo]  [Synth Solo]
[Saxophone Solo]  [Violin Solo]  [Drum Break]
```

Genre-specific:
```
[Dubstep Bass Drop]  [Bluegrass Fiddle Break]  [Jazz Piano Solo]  [Metal Guitar Shred]
[EDM Build-up]  [Funk Bass Groove]  [Blues Harmonica Solo]
```

### Breaks, Builds and Drops

```
[Break]              silence for lead, accompaniment plays
[Percussion Break]   drums only
[Bass Drop]          heavy bass emphasis
[Breakdown]          stripped-down section
[Build-up] [Build] [Rising tension]
[Drop]
```

Style Box phrasing for a drop: `EDM build-up, increasing tension, white noise sweep, pitch-rising synth`.

### Forcing Instrumental Sounds

Non-singable text under a tag can trigger instruments:

```
[Jazzy Trumpet Break]
. .! .. .! !! … ! ! !
```

A punctuation line such as `!!! --- !!!` between section tags sometimes forces a solo.

Onomatopoeia sometimes triggers the instrument (and may be sung instead — test):
```
[wailing electric guitar]
wah-Wah-WAH-SCREECH

[funky slap bass]
bowm-bowm-b-b-bowm-bowm

[drum fill]
ba-da-da-da-CRASH
```

For rhythmic noise pieces, sound-word lyrics (`tk tk tsss`, `brrrap`, `hush hush`) produce percussive vocal textures the model treats as instruments.

### Genre-Specific Instruments

Pick 2–3 for the Style Box, not the whole list.

| Genre | Instruments / textures |
|---|---|
| EDM / Electronic | pulsing bassline, synth leads, 808 drums, arpeggiated synths, sidechained bass, white noise sweeps, pitch-rising synth |
| House | four-on-the-floor beat, deep house bassline, house piano riff, atmospheric pads, uplifting synth chords, subtle arpeggiator |
| Rock | distorted guitar, power chords, driving drums, bass guitar, guitar riff, wah pedal, guitar feedback |
| Jazz | walking bass, jazz piano, brushed drums, saxophone, trumpet, upright bass, jazz guitar, vibraphone |
| Hip-Hop | 808 bass, trap hi-hats, boom bap drums, sampled loops, vinyl scratches, sub bass, crispy snares |
| Folk / Acoustic | acoustic guitar, fingerpicking, banjo, mandolin, violin, fiddle, harmonica, upright bass, stomps and claps |
| Orchestral | strings, brass section, woodwinds, timpani, harp, orchestral swells, pizzicato strings, French horn |
| Noise / experimental | granular synthesis, feedback loops, contact mic on metal, bit-crushed, tape stop |

Genre context matters: a fiddle works better in country than hip-hop (unless that is the point).

### Instrumental Prompt Examples

EDM:
```
Style: High-energy EDM track, pulsing kick drum, electrifying synth leads, powerful bassline

[Intro]
[Build-up]
[Drop]
[Breakdown]
[Build-up]
[Drop]
[Outro]
```

House:
```
Style: Energetic house track, four-on-the-floor beat, pulsing bassline, uplifting synth chords

[Intro]
[Main groove]
[Breakdown - atmospheric pads]
[Build]
[Drop]
[Outro]
```

Jazz:
```
Style: Smooth jazz, piano trio, walking bass, brushed drums

[Head - main melody]
[Piano Solo]
[Bass Solo]
[Trading fours]
[Head out]
```

### The Producer's Prompt

Suno responds better to narrative arrangement descriptions than flat tag lists. Brief it like a session musician:

```
Tag soup:        [Genre: Southern Rock], [Tempo: 110 BPM], [Instrumentation: Slide Guitar, Heavy Drums]
Producer prompt: Start with a lonely, overdriven slide guitar intro.
                 Build into a heavy, stomping drum groove for the verse.
```

| Pattern | Technique |
|---|---|
| Live band sim | Name rhythm guitar, lead guitar, bass, drums separately |
| EDM drops | Pad build → drop to drums + bass → full stack return |
| Branding | Keep 1–2 signature instruments across an album |

Instrumental tag tips: one tag at a time is most reliable; comma-combined tags are less predictable; descriptive tags (`[melodic interlude]`) beat bare ones (`[Interlude]`); keep to 2–3 instrument cues per section.

---

## Voice and Vocal Tags

Many voice tags are hit-or-miss. Concrete range and texture words are the strongest lever; emotion words are weak. For album-wide vocal consistency use a saved Voice ([models-and-sliders.md](models-and-sliders.md#voices)).

### Vocal Gender

The **Vocal Gender** selector (Advanced Mode → More Options, male/female) is the most reliable gender control — more consistent than Style Box wording. Leave it unset when a Voice or Custom Model supplies the voice.

### Vocal Style Tags (how notes are performed)

| Tag | Description |
|---|---|
| Staccato | Short, detached notes |
| Legato | Smooth, connected notes |
| Vibrato-heavy | Strong pitch oscillation |
| Monotone | Flat, single-pitch delivery |
| Melismatic | Multiple notes per syllable |
| Syncopated | Off-beat rhythmic emphasis |
| Operatic | Classical opera style |
| Chanting | Repetitive, ritualistic |
| Spoken-word | Speech-like delivery |
| Growling | Aggressive, guttural |
| Belting | Powerful, projected singing |
| Yodeling | Rapid pitch changes |
| Humming | Closed-mouth singing |
| Rapping | Rhythmic speech |
| Scatting | Jazz vocal improvisation |
| Falsetto runs | High-pitched runs |
| Yelping | Sharp, cry-like sounds |
| Grunting | Low, forceful sounds |
| Call-and-response | Interactive vocal pattern |

### Vocal Texture Tags (how the voice sits in the mix)

| Tag | Description |
|---|---|
| Whispered | Soft, breathy, intimate |
| Gravelly | Rough, textured |
| Velvety | Smooth, rich |
| Dreamy | Ethereal, floaty |
| Resonant | Full, vibrant |
| Nasal | Through-the-nose |
| Brassy | Bright, bold |
| Metallic | Hard, ringing |
| Saturated | Warm, full-bodied |
| Smoky | Husky, sensual |
| Chilled | Relaxed, cool |
| Rough-edged | Raw, unpolished |
| Shimmery | Light, sparkling |
| Glassy | Clear, crystalline |
| Crunchy | Distorted, gritty |
| Liquid-like | Flowing, fluid |
| Breathy exhale | Airy, exhaled |

More texture words: chesty, airy, throaty, sibilant, boyish, matronly, weathered, lived-in. Pick two.

Age/maturity: `breathy`, `whispered`, `delicate`, `intimate` skew young; `smoky`, `weathered`, `resonant`, `gravelly` read older. Use a range word (`alto`, `contralto`, `low register`, `baritone`, `bass-baritone`) rather than "mature".

### Production / Vocal FX Descriptors (Style Box prose)

| Descriptor | Effect |
|---|---|
| `reverb` / `spacious reverb` | Echoing, roomy — ballads, ambient |
| `delay` / `slapback delay` | Repeated echoes — dub, experimental |
| `auto-tuned` | Pitch-corrected modern pop/trap |
| `natural pitch` + `autotune` in Exclude Styles | Organic, unprocessed vocal |
| `vocoded` / `vocoder` | Robotic, electronic |
| `distorted vocals` | Gritty, overdriven — rock, industrial |
| `filtered` / `telephone effect` | Narrow-band, lo-fi/vintage transition |
| `close-mic`, `dry vocal` | Up-front, intimate |

To remove one, use Exclude Styles (bare element) — prompt-level "no …" is ignored on v6.

### Regional Vocal Styles

`British rock vocal`, `Southern gospel`, `Nashville country`, `New York hip-hop`, `Jamaican dancehall`, `Irish folk`. Use as Style Box descriptors (bracketed forms such as `[British rock vocal]` are also seen).

### Combining

Texture + style + regional:
```
Gravelly, belting, Southern rock vocal
Whispered, dreamy, British indie vocal
Nasal, rapping, New York hip-hop flow
```

Voice description examples:
```
Pop, upbeat, clear and prominent vocals, 120 BPM
Rock, gravelly male vocals, powerful, emotional
R&B, sultry female singer, smooth, soulful
Hip-hop, aggressive rap delivery, hard-hitting flow
Folk, intimate whispered vocals, acoustic, gentle
```

One vocal descriptor cluster placed early beats six scattered adjectives: `Breathy female mezzo, close-mic, slight rasp`.

### Vocal & Choral Genres

Acapella, Barbershop, Beatboxing, Choir, Christmas Carol, Doo Wop, Gregorian Chant, Throat Singing, Vocal Jazz, Vocaloid.

### Sustained Notes & Emphasis

| Technique | Example | Effect |
|---|---|---|
| Extended vowels | `Loooove`, `Ohhhh` | Sustained notes, emphasis |
| Hyphens | `lo-ove`, `sooo-long` | Extended vowels with syllable guidance |
| ALL CAPS | `NEVER AGAIN` | Shouting — unpredictable; test on a short generation, use for one line |

### Duet / Call-and-Response

```
[Verse - Character A]
First character's lyrics

[Verse - Character B]
Second character's lyrics
```

Also state it in the Style Box: `Dual vocalists, male and female, trading verses`. For a joint chorus describe it (`duet chorus, blended male/female harmony`) rather than inventing a tag. One report says the word `Duet` must appear in the Style Box; the pattern above works without it.

### Emotion Arc Mapping

An alternative to per-section Performance Cues: map the arc in a Style-Box "Performance:" line.

```
Vocal: female alto, breathy, intimate, close-mic.
Performance: whispered verse with micro-pauses at line ends, minimal vibrato;
chorus slightly wider and warmer with gentle vibrato on sustained notes;
bridge raw and exposed, single-take feel.
```

Pick one route per track — this or Performance Cues — not both.

### Non-Human Character Voices

Overload the Style Box with 5–8 descriptive adjectives; overloading overrides the default human-voice training.

- Bad: `goblin voice`. Good: `raspy, guttural, high-pitched, cackling, snarling goblin voice`.
- Robot/synthetic: `metallic, autotuned, monotone, robotic, synthetic voice`; modifiers `glitchy`, `vocoded`, `bitcrushed`.
- Goblin: `raspy, guttural, high-pitched, cackling, snarling, menacing`
- Demon: `deep, growling, distorted, rumbling, ominous, demonic`
- Alien: `ethereal, otherworldly, modulated, echoing, strange harmonics`

Combine with a genre for context (`industrial metal, robotic voice`); results vary by character, so iterate.

### Advanced Vocal Workflow

1. Use a saved Voice (Pro/Premier) for the most consistent identity across tracks.
2. Or upload a vocal sample (e.g. from a sample library) or your own recording.
3. **Extend** it with different lyrics, or **Cover** it into a different style.
4. Apply voice tags to manipulate the sound.
5. Layer styles by repeating with different prompts.
6. Pull stems and delete unwanted vocals.

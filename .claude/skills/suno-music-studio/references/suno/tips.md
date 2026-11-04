# Suno Tips

Craft advice and troubleshooting, grouped by topic. The mechanics (field limits, settings, tag syntax) are in [prompting.md](prompting.md), [tags.md](tags.md) and [models-and-sliders.md](models-and-sliders.md); where a tip here seems to conflict with those, they win. "Reported" means community observation, not tested behavior.

---

## 1. Mindset and Workflow

- **Suno is a session musician, not a vending machine.** Brief it like a player: genre, feel, tempo, reference era, what to leave out. Vague briefs get generic takes.
- **Decide the song's job before writing the prompt.** Background for a video, club track, lullaby — the job dictates length, dynamics, vocal density and how much ear candy is needed.
- **Generate in batches of 4–6, never 1.** Suno is non-deterministic; one generation tells you nothing about the prompt. Five tell you whether the prompt or the dice are the problem. (Batches come from generating again, not from Variety.)
- **Start broad, then refine. Change one variable per iteration** — Style Box OR lyrics OR sliders. Change all three and you learn nothing.
- **Keep a prompt journal**: date, slug, Style Box, sliders, take, one-line verdict. Every keeper becomes a template; every failure a lesson.
  ```
  | date | slug | style box | sliders (SI/W/AI) | model / variety / max | take | verdict |
  ```
- **Seed with short generations.** A 30-second instrumental test is cheap and tells you whether the palette is right before committing lyrics. Test Style Boxes as instrumentals first.
- **Try both models on hard genres.** v6 and v6-wild read the same prompt differently; for heavy or "attitude" genres run a first pass on wild and Cover the keeper on v6.
- **Set a kill limit.** If a concept isn't landing after 12–15 generations, the concept is wrong, not the luck. Rewrite the brief or bench the song.
- **Listen on three systems** (phone speaker, earbuds, monitors or car) before keeping anything. Suno mixes can sound huge on headphones and hollow on a phone.
- **Save keepers to a workspace immediately** and name files like a producer (`songslug_v03_takeB_vocal-warm.wav`).
- **Finish songs.** Ten released tracks teach more than a hundred 80% drafts.
- **Your taste is the product.** Anyone can prompt; what matters is knowing which of six generations is the one, and why. Spend as long listening critically as generating.

---

## 2. Style Box Craft

- **Order: genre, vocal, mood, production** (or vocal first, then genre — both front-load what matters). Early words weigh more.
- **Two or three genres max.** Pick a primary genre and one modifier: `Country, trap-influenced drums`, not `Country trap jazz fusion`.
- **Describe the sound, never the artist** — names are replaced with a visible notice and your intent goes with them.
- **Production language over quality adjectives**: `tape saturation, wide stereo, dry vocal, punchy compressed drums` beats `good quality, professional`.
- **Tempo as a number** (`128 BPM`). "Fast" means different things across genres.
- **Era anchors beat adjectives**: `1994 boom bap`, `late-70s AOR`.
- **Name the instruments** you want to hear to escape genre clichés: `fretless bass, Rhodes, brushed snare`.
- **Exclusions go in the Exclude Styles field**, 2–4 bare items (`autotune, EDM drops, rap verse`) — inline "no X" is ignored on v6.
- **Every descriptor earns its place.** ~10 focused descriptors is fine; synonym piles are the problem. If you need a paragraph, you are describing two songs.
- **Punctuation is structure**: commas separate descriptors, periods separate blocks. Avoid semicolons, slashes, quotes (reported to parse inconsistently).
- **Keep a house-sound suffix** (10–15 words appended to every prompt in a project: `warm analog mix, slight vinyl crackle, intimate vocal`) and keep 1–2 signature instruments across an album. Save the style with the bookmark icon.
- **Narrative beats tag lists** for arrangement: "Start with a lonely, overdriven slide guitar intro. Build into a heavy, stomping drum groove for the verse."

---

## 3. Lyrics and Structure

- **Every section gets a structure tag with a Performance Cue.** Untagged blocks are treated as verses.
- **Write the hook first.** If you can't hum the chorus after writing it, Suno won't make it memorable. The model amplifies what is there; it doesn't invent a hook.
- **Chorus within the first 45 seconds** for streaming: a four-bar intro, one short verse, chorus. Save long intros for the album cut.
- **Shorter lyrics generate better**: 200–350 words (up to ~500 for rap); two verses + chorus + bridge.
- **Syllable budget**: verses 7–9, choruses 10–12 per line; mid-tempo pop 8–12, rap 12–16, ballads 6–8. Overstuffed lines get rushed or dropped.
- **Make every verse different.** Twin verses (same shape, same images) are the clearest sign of AI-written lyrics. Verse 2 advances time, perspective or stakes.
- **Repeat the chorus verbatim.** Small variations are reported to come back as different melodies, and the song loses its anchor.
- **Parentheses for backing vocals**: `Take me home (take me home)`. Overuse it and everything becomes a gang chant.
- **Phrasing by layout**: a line break is a breath; `...` is a held note or pause; mid-line commas barely register.
- **Line length shapes melody**: stacked four-word lines feel punchy and urgent; fourteen-word lines meander and reflect.
- **End lines on strong stressed syllables** — nouns and verbs. Lines ending on "the", "of", "and" get swallowed.
- **Put the title in the chorus at least twice.**
- **A bridge is a change of key, view or truth.** If it restates the chorus in other words, cut it and go to a final chorus with a lift.
- **Name the solo instrument**: `[Guitar Solo]`, `[Saxophone Break]`; bare `[Solo]` noodles.
- **Control the ending**: `[Outro]` plus `[Fade Out]` or `[End]`. Without it Suno rambles or cuts mid-phrase.
- **Read the lyrics aloud with a metronome.** If you stumble, Suno stumbles. Fix prosody on paper before spending credits.
- More lyric craft: references/lyrics/writing.md; review checklist: references/lyrics/review.md.

---

## 4. Vocals

- **One vocal descriptor cluster, placed early**: `Breathy female mezzo, close-mic, slight rasp`. Six scattered adjectives produce mush.
- **Texture words are the strongest lever**: nasal, chesty, airy, smoky, glassy, throaty, sibilant, boyish, matronly. Pick two.
- **Duets need explicit handoffs** in both the tags and the Style Box (see [tags.md](tags.md#duet--call-and-response)).
- **Whisper/spoken tags work with contrast**: `[Whispered, intimate]` on the verse, `[Full voice]` at the pre-chorus.
- **If the vocal disappears, the intro is too long.** Use `[Short Instrumental Intro]`, cut intro descriptors, or open with `[Vocals enter immediately]`. Introducing vocals early with a hook or "Ahh ahh ahh" also helps.
- **Ad-libs go in brackets at line end**: `Running out of time [yeah]` — mostly in the second half where energy peaks.
- **All caps = shouted, usually.** Unpredictable; one line, not a verse.

### Vocal sounds too young despite "mature"/"deep"

Vague age adjectives are weak and get outcompeted, especially by nearby soft-coded words (intimate, whispered, delicate).

1. Replace the age word with a range: `alto`, `contralto`, `low register` / `baritone`, `bass-baritone`.
2. Add maturity textures (`smoky`, `weathered`, `resonant`, `gravelly`, `lived-in`); drop `breathy`, `whispered`, `delicate`, `intimate`.
3. Exclude Styles: `youthful or breathy vocals`.
4. Expect 2–3 regenerations; this narrows the odds, it doesn't guarantee.

- Weak: `Female character vocal, mature and deep, aching and intimate`
- Stronger: `Female alto vocal, low register, smoky and weathered, resonant and world-weary`

### Vocal sounds generic despite "powerful"/"defiant"

Emotion words describe what the performance should feel like, not what the voice sounds like; Suno falls back to a default genre voice.

1. Add a range: `mezzo-soprano`, `alto`, `contralto`, `baritone`, `tenor`.
2. Add audible textures: `gritty`, `raspy`, `rasp on the belted notes`, `raw chest voice`, `commanding`, `weathered`.
3. Exclude Styles: `generic or polished studio pop vocal`.
4. Keep one or two emotion words only to set the arc ("controlled and low in the verses, breaking open into a full-throated belt on the chorus").

- Generic: `Female character vocal, powerful and defiant`
- Specific: `Female mezzo-soprano, gritty and raw, rasp on the belted notes, commanding chest voice, weathered and fierce`

### Escalation ladder (both problems)

1. Confirm on a fresh generation (rule out carryover).
2. Inline metatags on **every** section: `[Verse 1: Raspy older female vocal, husky contralto]`, `[Chorus: Gritty, raw, commanding female belt]`.
3. Check whether the genre tag is fighting you. "Pop", "bright", "modern electronic" carry a bright/young/generic bias. Swap to mature-vocal-coded genres — `torch song`, `vintage soul`, `cabaret`, `1940s jazz`, `vintage country` — keeping other identity tags.
4. Rock/metal drift to a generic timbre: v6-wild first pass, or a Custom Model.
5. Last resort: a saved Voice from a take you liked, or your own cloned voice — more reliable than further Style Box iteration.

---

## 5. Distilling an Artist's Sound

- **Reverse-engineer in five dimensions**: instrumentation, vocal character, rhythm feel, production era, lyrical stance. Fill all five and the description beats a name.
- **Sound Blueprint template:**
  ```
  [genre] + [subgenre modifier], [vocal: gender, range, texture, delivery],
  [rhythm: tempo, feel, drum sound], [key instruments x3],
  [production: era, mix width, effects], [mood: 2 words]
  ```
  Example: `Indie folk, chamber-pop touches, soft male tenor with cracked falsetto, 78 BPM brushed kit, nylon guitar, upright piano, string quartet, 2008 lo-fi warmth, wide reverb, wistful and tender`.
- **Borrow the drums, not the melody.** Rhythm-section descriptions carry the most identity with the least legal and ethical baggage.
- **Describe the room**: `recorded in a wooden church`, `dead vocal booth`, `stadium echo`.
- **Use the era's gear**: `Juno-106 pads, LinnDrum, gated reverb` says 1984 without a name.
- **Blend two blueprints** (rhythm block from one, vocal block from another) — that's where original sounds live.
- **Lock the vocal with a Voice**: generate the definitive vocal first, save it, write the other songs to it with Max Mode On.

---

## 6. Sliders, Voices, Covers and Editing

- **Commercial work: Style Influence up, Weirdness down.** Start at 50/50, raise Style Influence before blaming the prompt; 70/20 is a common commercial setting. Raise Weirdness only when results are boring, not when they're wrong.
- **Weirdness above ~60 is an experimental tool** (tempo shifts, odd instrumentation, structure drift).
- **Audio Influence by purpose**: low = loose seed, mid = balanced, high = faithful; ~0.70–0.85 for a Voice.
- **Upload a hummed melody or one clean instrument**, not a full demo — a spine without your bad mix.
- **Cover as a re-arrangement tool**: cover a song into three genres (Variety Off, Max Mode On); the surprise is often the release.
- **Extend from a timestamp, not the end** — trim to the last good bar first.
- **Crop before extend, extend before replace.** Replace Section fixes a bad line surgically — one change per edit, with a list of what must survive.
- **Replace Section with identical lyrics to fix pronunciation**: keep the text, respell only the problem word.
- **Regenerate the section, not the song** when 90% is right; listen to the seam.
- **Keep extensions to 2–3 per song.**
- **A Voice is only as good as the take it's saved from**; test it short, upgrade old ones to v6 before an album run.

---

## 7. Spoken Word, Poetry, Noise and Ambient

- **Tag spoken word explicitly**: `[Spoken word]` at the section head and `spoken word, no singing, poetry reading` in the Style Box, or the model sings your poem.
- **Give spoken word a bed**: `sparse ambient piano, field recordings, distant traffic`.
- **Punctuation is the performance**: periods stop, line breaks breathe, em-dashes hold.
- **Keep spoken lines under ten words**; break thoughts across lines like a poem.
- **Mix one sung refrain into a spoken piece** — a four-line sung chorus between spoken verses gives an anchor and makes it playlist-friendly.
- **For noise, describe textures and processes**: `granular synthesis, feedback loops, contact mic on metal, bit-crushed, tape stop`. Genre names are too broad.
- **Noise sliders**: Weirdness 80+, Style Influence ~30.
- **Sound-word lyrics** (`tk tk tsss`, `brrrap`, `hush hush`) make percussive vocal textures.
- **Custom structure tags still steer**: `[Build]`, `[Collapse]`, `[Drone]`, `[Silence]`, `[Rupture]`.
- **Generate short cells (30–60 s) and stitch in a DAW** for control the model won't give you.
- **Field recordings via Audio Influence**: upload rain, a train, a crowd at ~40 influence and let the model build harmony on top.
- **ASMR / meditation / sleep**: `Whispered, ASMR, soft background hum, slow` (exclude `drums`, `instruments` as needed) with gentle-instruction lyrics. Long-form, low competition.

---

## 8. Troubleshooting

| Problem | Fix |
|---|---|
| Lyrics not audible / clip won't sing | Simplify the prompt (fewer tags); `[Short Instrumental Intro]`; "clear and prominent vocals"; bring vocals in early |
| Vocals buried | Vocal description first; "lead vocal 1–2 dB louder than band" |
| Mix flat | "bus compression 2–3 dB, slow attack/fast release" |
| Arrangement too busy | Specify rests: "verse 2: bass rests for 4 bars" |
| Chorus not lifting | "double-time hats; octave guitars" |
| Genre drift | Reassert influences mid-prompt; raise Style Influence |
| Unrequested words (Neon, Echo, Ghost, Silver, Shadow, Whisper, Crystal, Velvet) | Model token bias; "Do not change any words. Sing exactly as written." in the Style Box |
| Lyrics go wrong after extending | Back to an earlier clip; extend from an earlier timestamp; make several versions |
| Filter error on a lyric word | Producer-tag collision (e.g. "ninety-three") — respell (`'93`) or rephrase |
| Group vocals/choir appear uninvited | Exclude `choir, backing vocals, gang vocals` and lean the Style Box |
| Slow, sparse, long output | State BPM, density and length |
| Cover drifts | Variety Off, Max Mode On, then Audio Influence |
| Heavy guitars dirty/blended; niche metal hallmarks missing | Known weakness; v6-wild first pass, Custom Model, high Style Influence/low Weirdness |
| Quality drops late in long songs | Max Mode On; keep under 6–7 min |

**Known limitations**: heavy electric guitars can sound dirty or blur; acoustic nuance not always captured; niche heavy subgenres miss hallmarks; extreme cross-style fusions get muddy; quality may degrade past 6–7 minutes; rock/metal vocals drift toward a generic post-grunge timbre; prompt-level "no X" ignored.

---

## 9. Post-Production

- **Suno output is loud but not mastered.** Typical output: pop/EDM -9 to -7 LUFS, lo-fi -12 to -11, podcast/spoken -16 to -14. Master to **-14 LUFS / -1.0 dBTP** for streaming. Genre context: rock/pop around -12 to -14, EDM/hip-hop -8 to -12, classical/jazz -16 to -18 — different destinations, different masters; don't upload the club master to streaming.
- **Download WAV, not MP3.** MP3 artifacts compound at every step.
- **Stem-split before polishing**, and use stems for balance moves (level, pan, broad tone), not surgery — Suno stems bleed into each other.
- **High-pass everything except bass and kick**; keep the bass stem's high-pass low (20–35 Hz) to protect the sub.
- **Tame 2–5 kHz vocal sizzle gently** — a broad, shallow cut at most; surgical cuts on a synthesized stem eat consonants. Confirm the harshness is really there first.
- **Check mono compatibility.** Wide Suno stereo can cancel on phone speakers; fold to mono and confirm the vocal and kick survive. (v6 is also reported to render narrower than expected — widen in the mix, not the prompt.)
- **Master the album as a set**: match tonal balance and loudness across tracks; reference-match to your best song.
- Full procedures: references/production/mixing.md and references/production/mastering.md.

---

## 10. Music Video Process

1. **Lock the audio first.** Never storyboard to a draft.
2. **Shot list from the lyrics**: one visual idea per section (verse 1 a room, chorus the open road, bridge close-up hands).
3. **Visual bible**: 3–5 reference images, a palette, a lens, a time of day; every image prompt inherits it, like a Style Box suffix.
4. **Stills before motion**: approve the look in an image model, then animate only the winners image-to-video.
5. **Cut on the beat, not every beat**: section downbeats and chorus entrances. Every bar reads as a slideshow.
6. **Sync lyrics from a transcript** with word timestamps for overlays or lip-sync.
7. **Budget videos**: 4–6 looping 5-second clips, alternated and speed-ramped, carry a three-minute song; spend expensive generations on the chorus.
8. **Export 9:16 and 16:9**; frame the visual bible for both crops from step 3.

```
| section | timestamp | visual idea | image prompt | motion prompt | status |
```

---

## 11. Rights, Release and Income

- **Know the plan's license**: Free is personal/non-commercial; Pro/Premier commercial use requires a permitted paid-plan download; Remixes of others' songs are never commercial; never strip the in-audio watermark. Terms changed 2026-09-03 and will again — details in [models-and-sliders.md](models-and-sliders.md#plans-downloads-and-rights-terms-effective-2026-09-03).
- **Register your songs** with a PRO; use a distributor that accepts AI-assisted work and disclose per its policy.
- **Disclose honestly.** Owning AI use builds an audience; getting caught loses one.
- **Build catalogs, not singles**: ambient, lo-fi, sleep, focus and workout playlists reward volume and consistency — twenty coherent tracks under one project name beat one great song.
- **Sync and stock**: instrumental beds for creators, podcasts and ads; deliver stems, multiple lengths (15 s, 30 s, 60 s, full) and clean loop points.
- Release workflow: references/release/release.md; promotion: references/release/promotion.md.

---

## 12. Quality Checklist

Before generating:
- [ ] Style Box specific but not overcomplicated; vocals described clearly
- [ ] Intro short (won't bury vocals)
- [ ] Reliable structure tags, each with a cue
- [ ] Lyrics clear, not overlong, pronunciation fixed
- [ ] Variety Off, Max Mode decided

After generating:
- [ ] Vocals audible and clear; lyrics match what was written
- [ ] Structure makes sense; no awkward transitions; clean ending
- [ ] Sounds right on phone, earbuds and monitors

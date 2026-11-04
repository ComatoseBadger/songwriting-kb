# Suno Models, Settings and Features

Model choice, generation controls (Variety, Max Mode, Duration), the creative sliders, Voices / Custom Models, Covers / Extend / editing tools, plans and downloads, and workspace habits.

**Freshness:** written against the v6 family as launched 2026-09-09, with hands-on reports through mid-September 2026. Suno ships changes often; if the model picker, slider labels or limits look different, trust the UI and update this file. Facts marked "reported" are community observations, not Suno documentation.

---

## Models

### How to Choose

| Situation | Model | Settings |
|---|---|---|
| Finished track with engineered lyrics and Style Box (default) | **v6** | Variety Off · Max Mode On if over ~2:00 · Duration Auto |
| Exploring a sound, or an "attitude" genre where v6 plays it safe (rock, metal, era soul, anything drifting to a generic voice) | **v6-wild**, then Cover the keeper on v6 | Variety Off (its default) · listen to both takes |
| Album-wide brand or vocal consistency | **Custom Model** (or v6 + a Voice) | Max Mode On |
| Free account | **v6-mini** (only option) | not releasable (trial downloads, non-commercial) |
| Quick sketch, high-volume idea generation | **v6-mini** | Variety Normal is fine here |

Log which model each attempt actually ran on.

### v6

- Suno: "our flagship model … reliable, precise and consistently delivers polished music across every genre and style."
- Tier: Pro, Premier. Selected by default ("v6 · Pro").
- Variety default: **Normal** — set Off for an engineered Style Box.
- Credits: 10 per generation (two songs); 20 with Max Mode.
- Use for every finished track. Follows the brief closely, adds few unrequested elements.
- Quality is genre-dependent: reported strong on pop, drum & bass, UK garage; weak on grunge, metal, alt-country, synth-pop.
- Reported quirks: on Duration Auto, output runs slower, sparser and longer than the prompt implies (state tempo and density); rock/metal/grunge/alt-country vocals drift to a generic or artifact-laden timbre; stereo image narrower than expected (two independent reports); Covers hold melody and structure with Variety Off, drift with Variety on; mixes reported going muffled after ~2:30 without Max Mode.
- Internal id (only relevant when reading payloads): `chirp-hawk`.

### v6-wild

- Suno: "built for exploration … less predictable and more varied, producing unexpected, textured and ambitious results." The CEO: great for "maybe a verse, maybe even 5 seconds … not going to be perfect for the whole song."
- Tier: Pro, Premier ("Best for experimental ideas").
- Variety default: **Off** (the only model whose default is Off).
- Credits: 10; Max Mode supported (untested in practice).
- Workflow: generate on wild, pick the take with the character you want, **Cover it on v6** to polish. One attempt found the Cover step did not clearly keep wild's character; treat it as experimental.
- Reported: less polish; length unpredictable (~50 s to ~7 min on similar prompts) — generate several takes before judging; drifts from the brief by design. In a seven-genre A/B, v6 won vocal fidelity and prompt adherence 7/7; wild won on character in indie rock, R&B/soul and metal. Exclude Styles works on wild. Tuned less toward average user preference, so niche genres skew less "poppy".
- Internal id: `chirp-hawk-wild`.

### v6-mini

- Suno: "a faster, more efficient version available to everyone."
- Tier: all plans including Free. Variety default Normal. 10 credits; Max Mode plan-gated.
- Use for sketches and high-volume ideation; the only model on Free.
- Reported: "simpler and often more artifacts". Free output is personal-use only (7 lifetime trial downloads, no commercial rights). A "keep one of two" flow exists ("Choose one to keep for free" / "Keep both for N credits"); its trigger is unconfirmed.
- Internal id: `chirp-goose`.

### Custom Models

- Private model fine-tuned on your own catalog. Upload **at least 6** original tracks ("24+ for best results"); **100 credits**; 2–5 min build; up to **3 per account**; not shareable. Appears as `Custom: <name>`.
- Variety default Normal — set Off.
- Use for album-wide consistency of voice and aesthetic; also the reported workaround for rock vocals drifting to a generic "southern" timbre. Stackable with a Voice. Plain v6 is often better for deliberately off-brand tracks.
- Prompting: drop generic production language; keep genre, tempo, featured instruments, mood shifts and section direction.
- Created before v6: upgraded automatically.

### Made Before v6

Suno retired every earlier model on **2026-09-09**.
- Old **songs** stay playable. **Remaster** when you only want better audio; **Cover** when you want v6 to reinterpret while following the melody. Both render on v6; the original is untouched; results "may sound different". On a Cover meant to stay close, use Max Mode On and Variety Off.
- Old **prompts** do not transfer (tempo, density, length differ). Re-prompt.
- Old **Voices** keep working and offer "Upgrade Voice to v6"; test a migrated Voice on a short generation before an album run.
- There is no official Suno API, and identifiers like `V6` / `V6_WILD` / `V6_MINI` do not exist. Third-party "API" parameter tables (`styleWeight`, `weirdnessConstraint`, `negativeTags`) are historical.

---

## Generation Controls

### Simple vs Advanced Mode

Simple Mode hosts Suno's plain-language section edits, single-lyric swaps, multi-source mashups, sample-and-isolate and image/video/voice-memo inputs. It treats typed lyrics as a seed and writes extra lines; its single-word replacement is reported unreliable and syllable-sensitive; switching to Advanced does not carry the prompt across. **Use Advanced Mode** for finished lyrics and an engineered Style Box.

### Variety

Not a "how weird" dial — a **prompt-rewriting** dial. Suno's FAQ: "The Variety slider is designed to introduce variety in your outputs by adjusting and updating your style prompts. If you'd like to retain full control of your style tags, reduce the Variety slider to 0." Above Off, Suno expands your style text server-side, differently for each of the two takes (a style box reading only "R&B" at High came back as two different multi-line prompts).

| Stop | Suno's label | What happens |
|---|---|---|
| **Off** | "Exact style" | Style Box used verbatim. **Use this.** |
| Normal | "Balanced variety" | Default on v6, v6-mini, Custom |
| High | "Distinct styles" | Two clearly different reads |
| Extra | "Bold exploration" | |
| Max | "Unreasonably varied" | Clips may differ significantly from your input |

- Defaults reassert when you switch models — check every session.
- **Personalize** ("Make Variety match your taste"), fed by **My Taste** passive preference learning, sits next to Variety; off by default and inert while Variety is Off. Leave it off.
- A/B testing a prompt edit requires Variety Off, or take-to-take variance swamps your change.
- Set Variety first: Style Influence governs how hard Suno commits to the prompt it has; Variety changes which prompt it has.
- Covers drift in melody with Variety above Off.
- Batch diversity comes from generating again, not from Variety.

### Max Mode

Toggle under More Options. Suno: "Uses more compute to maximize consistency throughout the song. Costs 2x credits per song." (20 credits.) Recommended for songs over two minutes, covers that should stay close to the source, style transfer, and keeping vocals consistent — so default it **On** for full tracks and anything with a Voice; Off for short sketches. One creator reported two weak/broken launch-day outputs with it on (single source).

### Duration

Auto (default) or Custom 10 s–6:00. Custom hard-cuts at the value and rushes lyrics that do not fit; Auto plus section count is safer for lyric tracks. Max length is 8:00 via Auto/Extend. See [prompting.md § Duration](prompting.md#duration).

---

## Creative Sliders

The sliders sit on top of the prompt. They don't change **what** Suno makes — the prompt does. They change **how hard** Suno commits to the prompt and **how far** it may wander. Positions below use a 0.00–1.00 scale; on a 0–100 UI read `0.70` as `70`. Bands are starting points, not Suno defaults. Defaults: Weirdness 50, Style Influence 50, Audio Influence 25; "Reset sliders" restores them.

### Weirdness

How experimental the melody, harmony, arrangement and structure are.

| Position | Behavior |
|---|---|
| Low (0.00–0.30) | Predictable, hooky, familiar; conventional shapes. Radio-safe. |
| Mid (0.30–0.55) | Mostly conventional with occasional pleasant surprises |
| High (0.55–1.00) | Odd chord moves, unusual textures, less predictable structure; drift and misfires increase |

Raise when output is too safe; lower when you need a dependable hook. High Weirdness increases take-to-take variance — generate more and cherry-pick. Above ~0.60 expect tempo shifts, odd instrumentation and structure drift: great for noise and ambient, wrong for a wedding song.

### Style Influence

How tightly the output hugs the style prompt (genre hallmarks, named instruments, mood words).

| Position | Behavior |
|---|---|
| Low (0.00–0.40) | Prompt is a suggestion; free blending; good for fusions and happy accidents |
| Mid (0.40–0.60) | Honors the prompt with room to breathe |
| High (0.60–1.00) | Tags enforced hard; strong genre purity |

Raise for genre purity or when tags are ignored (at 50 it discards half the prompt's authority — raise it before blaming the prompt). Lower for surprise, blends, or when a Voice comes back over-processed/dominant. Very high on a thin or contradictory prompt gives a rigid, wooden result — fix the prompt first. A 70/20 Style Influence/Weirdness split is a common commercial setting.

### Audio Influence

Appears only with uploaded audio (Cover, Upload Audio, Sample to Song, Voices).

| Position | Behavior |
|---|---|
| Low (0.00–0.40) | Upload is a loose seed; prompt leads |
| Mid (0.40–0.65) | Carries the reference's character while following the prompt |
| High (0.65–1.00) | Hews to the upload's melody, feel and arrangement; safest for faithful covers |

With a **Voice**, keep it fairly high (~0.70–0.85) or the vocal drifts generic. For field recordings (rain, train, crowd) as a bed, ~0.40.

### Recommended Starting Ranges by Genre

| Genre | Weirdness | Style Influence | Why |
|---|---|---|---|
| Pop / radio pop | 0.10–0.30 | 0.60–0.80 | Familiar hooks, clean structure, on-genre |
| Hip-hop / rap | 0.20–0.40 | 0.50–0.70 | Protect the pocket; some room for beat character |
| Rock / punk | 0.20–0.45 | 0.55–0.75 | Hallmarks matter; punk stays tight and fast |
| Folk / acoustic | 0.10–0.30 | 0.60–0.80 | Intimacy and coherence over surprise |
| Electronic / EDM | 0.30–0.55 | 0.45–0.65 | Sound design rewards experimentation |
| K-pop | 0.20–0.40 | 0.65–0.85 | Maximalist but genre-precise; switch-ups come from the prompt |
| Cinematic / orchestral | 0.15–0.40 | 0.55–0.75 | Mood and coherence carry it |
| Jazz / improv | 0.40–0.65 | 0.40–0.60 | Improvisational feel benefits from deviation |
| Ambient / experimental / IDM | 0.55–0.85 | 0.25–0.50 | The unexpected is the point |
| Noise | 0.80+ | ~0.30 | Keep the model off-balance so textures collide |
| Metal / heavy | 0.10–0.30 | 0.65–0.85 | Suno struggles here — lock on-genre; consider v6-wild first pass then Cover on v6 |
| Documentary / narrative | 0.10–0.30 | 0.55–0.75 | Clear vocals, predictable structure so the story lands |

### Interaction Effects

| | Low Style Influence | High Style Influence |
|---|---|---|
| **High Weirdness** | Wild card — maximum surprise, genre may dissolve; idea-mining, many regenerations | Adventurous within the lane — the sweet spot for keeping a familiar genre fresh (pair with a specific genre tag) |
| **Low Weirdness** | Loose and smooth — gentle fusions | Safe and on-genre — release-ready; risk is generic |

- High Audio Influence + low Weirdness: tracks the reference closely.
- High Audio Influence + high Weirdness: tug-of-war — striking reinterpretations or mud. Move one slider at a time.
- High Audio Influence + high Style Influence: two adherence pulls; if upload and prompt describe different things, pick one source of truth and relax the other.

### Slider or Prompt?

The prompt decides *what* the track is; sliders decide *how strictly* and *how far*. No slider adds a banjo, fixes a mispronunciation or changes the tempo.

| Symptom | First move |
|---|---|
| Generic / too safe | Raise Weirdness a little, **or** lower Style Influence a little |
| Off-genre / ignores tags | Raise Style Influence; then sharpen the genre tag |
| Chaotic / incoherent | Lower Weirdness; keep Style Influence mid–high |
| Rigid / wooden | Lower Style Influence slightly, or simplify the prompt |
| Wrong instruments, mood, tempo | Change the prompt |
| Mispronunciation / wrong words | Fix lyrics and pronunciation |
| Cover doesn't resemble source | Confirm Variety Off and Max Mode On; then raise Audio Influence |
| Cover too close | Lower Audio Influence and/or raise Weirdness |

Workflow: write a focused prompt → generate at defaults → listen and diagnose prompt vs slider → move **one** slider a small step → log the value and result.

---

## Voices, Custom Models and Personas

### Voices

Pro/Premier (limited free trial). Suno folded Personas into Voices in March 2026 ("Personas are now Voices"); a Legacy option remains for existing Personas.

Two ways to get one:
- **Save a Voice from a generation** whose vocal you love (song menu → save as Voice). A Voice is only as good as the take it comes from — pick one you'd happily hear across an album, test on a short generation, then write the other songs to it.
- **Clone your own voice**: upload a clean acapella, a full track, or sing into the mic (15 s–4 min; cleaner source needs less). Suno then has you read a spoken phrase as a consent check. Own voice only; 18+.

Rules:
- Upgrade older Voices with "Upgrade Voice to v6" (picker shows **Voice (new)** vs **Style Voice (legacy)**) before an album run so every track uses the same engine.
- Not usable on instrumentals.
- Max Mode On; Audio Influence ~0.70–0.85.
- Style Box: drop gender/register descriptors; 1–2 genres plus instrumentation.
- If a Voice comes back over-processed or dominant, simplify the Style Box or lower Style Influence.
- Reported: likeness is "bent rather than reproduced" on big choruses; one launch-day test found a Custom Model beat a Voice for consistency. If a Voice keeps drifting, try a Custom Model.
- Suno's Voices FAQ is stale (still names a retired model).

Voice workflow and album planning: references/album/personas-and-covers.md.

### Voice or Custom Model?

See [Custom Models](#custom-models) above. A Voice carries one vocal identity; a Custom Model carries voice plus aesthetic and is reported more consistent. They can be stacked.

---

## Covers, Extend and Editing

### Cover

Re-arranges an existing song (yours or an upload) into a new style while following the melody. **Variety Off and Max Mode On** or the melody drifts; then adjust Audio Influence. Generate a song once and cover it into three genres — the one that surprises you is often the release. Voice + Cover carries a vocal identity through a genre shift; layer multiple Covers for genre-bending results.

### Remaster

For songs you like where you only want better audio (renders on v6).

### Extend

1. Click **Extend** on the clip (or "Continue from this song", with `[Continue]` at the top of the new Lyrics Box). Each extension generates about a minute and returns two clips.
2. Pick the best and extend again. Build verse 1 + chorus 1 (several versions), then verse 2 + chorus 2, then bridge, final chorus — catches problems early.
3. **Extend from a timestamp**, not the end: trim the tail to the last good bar first. Also use it when the song ended too soon, a lyric or sung word is wrong, you want a style change, or an instrumental lead-in.
4. Max total 8:00. Keep extensions to **2–3 per song**; more causes uneven lyrics, weaker vocals and quality loss.
5. If lyrics go wrong after extending (random words, repeats, gibberish): go back to an earlier clip, extend from an earlier timestamp, and make several versions.

### Song Editor

| Action | What it does |
|---|---|
| Remake | Regenerate one section with the same prompt |
| Rewrite | Change lyrics/melody for one section, preserving role and intent |
| Extend | Append bars at the tail of a section |
| Reorder | Move sections |
| Delete | Remove weak sections; transitions handled by the engine |

Extend 1–2 bars into/out of a chorus for smoother transitions.

### Replace Section (Pro/Premier)

Edit lyrics or insert an instrumental within a 10–30 s segment:

```
[Verse]
What a maze

[Instrumental]
[drum break]
```

- **One change per edit.** Before replacing, write down the single change and what must survive it (tempo, key feel, bassline, groove, the vocal, section timing). If feedback names several problems, queue them and fix the highest-impact first; log each pass with its parent take so a bad edit is reversible.
- Fix a pronunciation by replacing with **identical lyrics** except the respelled word — the surrounding audio stays intact.
- Order of operations: crop before extend, extend before replace.
- Regenerate the section, not the song, when 90% is right — but listen to the seam: launch-week reports say Studio's regenerate-section can garble vocals.

### Suno Studio (Premier)

Generative audio workstation (released 2025-09-25; Studio 2.0 in 2026): multitrack timeline editor, stem controls, MIDI export, audio upload, **Sample to Song** (upload a riff or vocal idea, describe the full composition, Suno expands it), **pitch transpose** (clip settings, ±12 semitones, preserves melody/phrasing/rhythm — fixes key mismatches without regenerating). Studio exports are 32-bit float / 48 kHz and do not count against download caps. Reported at launch: regenerate-section produced garbled or invented-language vocals for two creators; single-instrument generation no longer adds extra parts; one imported-keys timing offset on multitrack export. Verify by ear before exporting.

### Stems

Three modes (overhauled June 2026): More Actions (…) → Get Stems.

| Mode | Output |
|---|---|
| **Auto Split** | 12 stems: Vocals, Backing Vocals, Drums, Bass, Guitar, Keyboard, Strings, Brass, Woodwinds, Percussion, Synth, FX/Other |
| **Split from Mix** | 2 stems: the chosen target, and everything else |
| **Advanced Split** | 1 instrument chosen from ~100 (Premier, per-extraction credits) |

Suno says the new pipeline regenerates stems rather than frequency-carving; that is unverified. In practice Auto Split shows bleed/crosstalk, reverb shared across stems and separation artifacts, and returns a near-silent (~-55 dBFS) placeholder for categories the song lacks. Plan stems for balance moves, not surgery. For an isolated part, **Split from Mix** targeting it is usually cleanest; if it still bleeds, extract again from the extracted stem. Mixing workflow: references/production/mixing.md.

### Other Tools

- **Save style prompts**: bookmark icon next to the style prompt → name it; reuse from the library-book icon at the bottom-left of the style box. Keeps album tracks consistent.
- **Layering styles**: run the same idea through successive prompts ("Ethereal pop, dreamy synths, soft vocals" → "R&B hip-hop fusion, smooth singer, trap beats" → "Electronic elements, glitch effects, pulsing bassline") via Cover/Extend.
- **Upload workflow**: upload a vocal or instrument sample (a hummed melody or single clean part beats a full messy demo), Extend with new lyrics or Cover into a new style, apply voice tags, then pull stems and delete unwanted parts.

---

## Plans, Downloads and Rights (Terms effective 2026-09-03)

- **Downloads**: Free 7 lifetime (personal use only); Pro 20/month; Premier 60/month. One song = one download whatever the format, stems included; re-downloads free. Studio exports uncapped. Download the WAV of every keeper while the monthly allowance is open, and pull stems later at no extra cost.
- **Commercial use** (Pro/Premier) requires a permitted download on a paid plan. Suno assigns its rights in outputs but "makes no representation or warranty … that any copyright will vest in any Output"; rights holders "may also have the right to collect revenue related to distribution of Outputs on third party platforms."
- **Remixes** of other people's songs are never commercial.
- **Watermark and fingerprint** are embedded in the audio; the Terms forbid removing or circumventing them. Never use "watermark remover" tools.
- **Distribution**: some distributors (e.g. Believe/TuneCore) accept only tracks made on the current model family; check each distributor's policy. Release workflow: references/release/release.md.

---

## Workspace Management

Workspaces are folders in Suno's web UI for in-progress projects, separate from the Library (everything) and Playlists (listening sets). Organization is manual.

- **Before an album**: create a workspace named after the project (e.g. `connection-lost`).
- **After each generation**: clips land in the Library. Find them by title → ⋯ → Move to Workspace. Batch: Shift-click ranges or Ctrl/Cmd-click, More actions, move all. Do it immediately — liked tracks get buried within a day.
- **Review**: thumbs up marks keepers; thumbs down moves a clip to Trash (Library → Trash → Delete Permanently).
- **Naming**: keep the Suno track title identical to the title in your notes; name downloaded files like a producer (`songslug_v03_takeB_vocal-warm.wav`).
- **Archiving**: prefix finished workspaces `ARCHIVE_`, or export finals to external storage; keep the latest two exports plus milestone versions and clear old iterations.

---

## What Changed Between Versions (summary)

Dated so you can tell when this goes stale.

| Date | Change |
|---|---|
| 2025-09 | v5 era: 8-minute generations, 12-stem extraction, four-part prompt anatomy; Suno Studio launched 2025-09-25 (Premier). |
| 2025-11-25 | Warner Music Group partnership: download caps introduced, licensed models announced for 2026. |
| 2026-02 | Personas, Song Editor, bar-count tags, creative sliders documented; "prompt fatigue" guidance; IPA confirmed unsupported. |
| 2026-03/04 | v5.5: **Voices** (voice cloning), **Custom Models**, **My Taste**. "Personas are now Voices". Limits unchanged (Style 1,000 / Lyrics 5,000). |
| 2026-06-11 | Stem separation overhauled into Auto Split / Split from Mix / Advanced Split. |
| 2026-07 | Descriptor guidance reframed: "4–7" is a heuristic; bloat means synonym piles (>~12), not count. Exclude Styles field confirmed as the reliable negative path; group-vocal exclusion vocabulary. Performance Cues written comma-free. |
| 2026-07-20 / 08 | Duration slider (Custom 10 s–6:00); Voices update; Studio 2.0 (32-bit/48 kHz uncapped exports). |
| 2026-09-03 | New Terms: paid-download commercial rights, Free 7 lifetime / Pro 20 / Premier 60 downloads, Remixes never commercial, watermark/fingerprint removal prohibited. |
| 2026-09-09 | **v6 family** launched (v6, v6-wild, v6-mini); all earlier models retired. New **Variety** control (rewrites the Style Box above Off) and **Max Mode** (2× credits). Prompt syntax and limits unchanged. Custom Models auto-upgraded; Voices get "Upgrade Voice to v6". Artist names rewritten with a visible notice. Inline "no X" ignored — Exclude Styles field only. |
| 2026-09-10/11 | Hands-on reports: genre-dependent quality (weak rock/metal/grunge/alt-country vocals), narrower stereo, v6 runs slow/sparse/long on Auto, Covers drift with Variety on, wild's length unpredictable. |

Claims checked and **not** adopted (do not reintroduce): v6 changed prompt syntax or limits; partner-label artist names allowed; per-section parameterized tags like `[Verse: whispered vocals, acoustic only]` as a default pattern; inline `no autotune` as reliable; `V6`/`V6_WILD` API identifiers; "Personas were removed"; "v6 has fewer artifacts" as a blanket claim.

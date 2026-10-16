# Personas (Voices), Covers & Editing Songs

Suno lets you build on earlier work instead of starting every track from a blank prompt:

- **Voices** (formerly **Personas**) save a vocal identity, so the *same singer* appears across many songs. They can also be a clone of the user's own voice.
- **Covers** reimagine an *existing* song or sample in a new style, keeping the song and changing the production.
- **Song Editor, Extend, and Replace Section** fix a generated take section by section without throwing the whole take away.

Plan tiers, credit costs, and feature names change often. Treat the specific numbers here as recent reports and check them against Suno's current UI. For slider behavior, see references/suno/models-and-sliders.md.

---

## When to Use What

| You want to… | Use | Notes |
|--------------|-----|-------|
| Write a brand-new song from lyrics and a style prompt | **Original generation** | The default for most album tracks |
| Keep the same singer across different songs | **Voice / Persona** | Save one good vocal and reuse it. Pro/Premier. |
| Reinterpret an existing song or sample in a new style | **Cover** | Keeps the song, changes the production |
| Bring an old (pre-v6) song forward, same arrangement, better audio | **Remaster** | Only the audio quality changes |
| Have a track sung in the user's own voice | **Voice (cloned)** | Pro/Premier. Own voice only, 18+. |
| One voice *and* genre variety across an album | **Voice + Cover** | The Voice holds the singer, and the Cover shifts the genre |
| Fix one weak section of an otherwise good take | **Song Editor** | Re-rolls only that section |

---

## Voices / Personas: A Reusable Vocal Identity

Suno folded Personas into the **Voices** menu (a Legacy option remains for older ones). A saved Voice does what a Persona did, carrying one vocal identity across songs, and also supports cloning the user's own voice. It is the most reliable way to keep one singer consistent across an album.

### Plan the voice first

Write the vocal identity as a short persona description in the album brief before generating anything. The description is the *plan*, and the saved Voice is the *artifact* that enforces it.

```
Male baritone, gravelly, introspective, folk storyteller
Male tenor, warm, slightly raspy, indie rock delivery
Female alto, sultry, breathy, R&B phrasing with subtle runs
Female mezzo-soprano, gritty and raw, rasp on the belted notes, commanding chest voice, weathered and fierce, not a polished pop voice
```

Specific texture words (rasp, chest voice, breathy, weathered) beat generic ones (powerful, emotional). If the result still comes back generic, add per-section vocal direction in the lyrics (`[Chorus: gritty, raw, commanding female belt]`). Also check whether a genre tag like "pop" is pulling the voice toward a default. For more on tags, see references/suno/tags.md.

### Create a Voice from a generation

1. Generate (using the persona description in the style prompt) until the vocal is one you'd happily hear on every track.
2. Keep the style prompt simple on that source take, so the Voice captures the *voice* and not the arrangement.
3. From the song's menu, save the vocal as a Voice.
4. Apply that Voice to every new song on the album.

### Clone the user's own voice

Upload a clean a cappella, a full track, or a mic recording, 15 seconds to 4 minutes long. Cleaner sources need less length. Suno then asks the user to read a phrase aloud as a consent check. Own voice only, 18+.

### Generating with a Voice

- **Simplify the style prompt** to 1-2 genres plus instrumentation. Drop gender and register descriptors, because the Voice carries them.
- **Max Mode On** when a Voice is attached. Suno recommends it for voice consistency, and it costs more credits per generation.
- Keep **Audio Influence** fairly high, around 0.70-0.85.
- **Voices can't be used on instrumentals.**
- A Voice works **independently of style**, so the same singer can do a folk track and an electronic track.
- **Voices run dominant.** If the style prompt fights the Voice, the Voice usually wins. Work with it. If the result sounds overprocessed or the voice swamps the mix, simplify the style prompt or lower **Style Influence**.
- **Upgrade older Voices** to the current engine (Suno offers a one-click upgrade) *before* an album run, so every track uses the same one. Test a migrated Voice on a short generation first.
- If a Voice keeps drifting, a **Custom Model** may hold consistency better (one launch-day report, unverified). The two can be stacked.

### Custom Models (fine-tuning)

Train on at least 6 of the user's original tracks (Suno recommends 24+). Pro/Premier, up to 3 per account. When prompting with one, drop generic production language ("glossy", "modern pop production"), because the model already encodes the aesthetic. Keep genre, tempo, featured instrument, and section direction. A Custom Model is best for album consistency, and plain v6 is often better for a deliberately off-brand track.

### Before saving a Voice

- [ ] The source vocal is one you'd want across the whole album
- [ ] The source style prompt was simple enough to capture the voice, not the arrangement

---

## Covers: Reimagining an Existing Song

A Cover reinterprets an existing track in a different style, for example a folk song covered as electronic.

**Keeps:** the underlying song, meaning its topline melody and structure.
**Changes:** the production: genre, instrumentation, tempo feel, era.
**Doesn't change the words.** To change lyrics, use Extend, Replace Section, Song Editor Rewrite, or a fresh generation. A Cover restyles a song. It doesn't rewrite it.

### When to use a Cover

- You have an acoustic demo or a sample (for example from Splice) that you want rendered as a full production.
- You want a second version of a track in a contrasting genre, such as an album cut plus an electronic remix.
- You're genre-bending, layering new styles onto a song you already like.
- **Model split:** for heavy or "attitude" genres, try a first pass on v6-wild, then Cover the keeper on v6 to clean it up (see references/suno/models-and-sliders.md).
- **Older songs:** to bring a pre-v6 song forward, use **Remaster** to keep it as is with better audio, or **Cover** to have v6 reinterpret it while following the original melody. Neither modifies the original.

### Setting up a Cover

**From an uploaded sample**
1. Upload the audio.
2. Choose **Cover** to restyle it, or **Extend** to add or replace lyrics.
3. In the style prompt, describe the *new* target style, not the original.
4. Set **Audio Influence** on purpose. Higher stays closer to the source, and lower gives Suno more freedom. The slider appears only when audio is uploaded.
5. Optionally pull stems afterward and drop the parts you don't want (for example, unwanted vocals from a sample).

**From a prior generation**
1. Open the song.
2. Choose **Cover** and set the new target style.
3. Generate several takes and pick the best.

**Melody lock:** set Variety to **Off** and Max Mode to **On** for a Cover that should stay close to its source. With Variety above Off, the melody and structure drift.

### Cover vs original generation

- **Use original generation** whenever the song doesn't exist yet. It gives Suno the most room and is the cleanest path to a strong first take.
- **Use a Cover** only when you already have audio whose *song* you want to keep and whose *style* you want to change. If you'd end up rewriting the lyrics or melody anyway, a fresh generation is faster than fighting the Cover.
- **Use a Voice** (with or without a Cover) when the thing to hold constant is the *voice*, not the song.

### Rights

Covering your own generations or cleared samples is clean. Covering someone else's copyrighted recording raises a rights question, as any release would. Stick to material the user has rights to (see references/lyrics/compliance.md).

### Voice + Cover: genre-bending with one singer

1. Generate a song with a Voice applied.
2. Cover it into a different genre with Variety Off and Max Mode On.
3. The Voice's identity carries through the genre shift.
4. Layer several Covers for more complex genre-bending.

If a Voice-based Cover comes back overprocessed or the voice dominates, simplify the style prompt or lower Style Influence.

### Before generating a Cover

- [ ] The source is the user's own generation or a cleared sample
- [ ] The style prompt describes the NEW target style
- [ ] Variety Off and Max Mode On (melody lock)
- [ ] Audio Influence set on purpose
- [ ] If a Voice is applied, the style prompt is kept simple

---

## Editing & Extending Songs

### First diagnose what kind of wrong it is

| Symptom | Scope | Tool |
|---------|-------|------|
| One section is off (a cracked chorus note, a rushed bridge) and the rest is a keeper | Section | **Song Editor: Remake** |
| Wrong words or melody in one section (a factual error, a weak line, a mispronunciation) | Section | **Song Editor: Rewrite** (or Replace Section) |
| Section order or length is wrong | Arrangement | **Song Editor: Reorder / Delete / Extend** |
| The whole track is wrong (genre, tempo, mood, vibe) | Whole track | **Full regeneration** with a revised style prompt |
| You changed the style prompt or rewrote most of the lyrics | Whole track | **Full regeneration** |
| Words and performance are right, but the audio is noisy, muddy, harsh, or clicky | Audio quality | **Mix polish on stems** (references/production/mixing.md). No credits, no re-roll. |

Rules of thumb:
- **A localized problem in a keeper take → Song Editor first.** Full regeneration is non-deterministic and can lose the parts you'd already approved. Song Editor re-rolls only the part you point at.
- **An audio-quality-only problem → polish, not regeneration.** Re-rolling spends credits and replaces a performance that was already right.

### Song Editor operations

| Operation | What it does | Use it when | Watch for |
|-----------|--------------|-------------|-----------|
| **Remake** | Re-rolls one section with the same prompt | A single section is the only weak spot | The new section can land at a slightly different timbre or level. Listen to the seams, and remake again before download if the jump is obvious. |
| **Rewrite** | New lyrics or melody, same structural role | The content of a section is wrong but its slot is right (a factual fix, a tighter line, a hook that doesn't land, a pronunciation fix) | Fix the line first (references/lyrics/writing.md, references/suno/pronunciation.md) so you rewrite once. Keep the role: turning a pre-chorus into a verse is a regeneration job. |
| **Extend** | Appends bars at a section's tail | An abrupt ending, a transition that needs room (1-2 bars into or out of a chorus), an outro that needs to breathe, a longer intro | **2-3 extensions max per song.** More causes uneven lyrics, weaker vocals, and lower quality. It also changes track length. |
| **Reorder** | Moves sections around | The bridge hits harder before the final chorus, or verses play better swapped | On story or documentary tracks, reordering can scramble the chronology or break a callback. Reread the whole lyric afterward. |
| **Delete** | Removes a section, and the engine smooths the join | A redundant twin verse, a dead instrumental stretch, a pointless second bridge, trimming length (quality degrades past about 6-7 minutes) | It can pull the track under its target duration. On true-story tracks, check that a sourced fact isn't lost with the section. |

### Extend (clip-level)

- **Extend** generates about 1 minute and returns 2 clips. Pick the best and extend again.
- **Extend from a timestamp** to continue from an earlier point when the song ended too soon, a lyric or vocal went wrong, you want a style change, or you want an instrumental lead-in before the vocals.
- **Build in stages:** extend verse 1 + chorus 1 several times, pick the best, then extend verse 2 + chorus 2, then the bridge and final chorus. This catches problems early.
- **If the lyrics go wrong after extending** (random words, repeated sections, gibberish): go back to an earlier clip and regenerate, extend from an earlier timestamp, or generate several extension versions and pick one.
- To extend an uploaded sample with new lyrics, use **Extend** rather than Cover.

### Replace Section (Pro/Premier)

Edit lyrics or insert an instrumental passage within a 10-30 second segment:
```
[Verse]
What a maze

[Instrumental]
[drum break]
```
Use it for fine-tuning specific lyrics, adding a solo or break, or fixing a small mistake without regenerating. Some reports say regenerating a section can garble vocals, so listen to the seam before you judge the edit.

### One change per edit

Before you replace, rewrite, or extend, write down the **single** thing you're changing and what must survive it (tempo, key feel, bassline, drum groove, the vocal, section timing). If the feedback names several problems, queue them and fix the highest-impact one first. When a bundled edit comes back wrong, you can't tell which change caused it. Record each pass with its parent take so a bad edit can be reversed.

### Keep the lyrics in sync

Song Editor changes the **audio**, not your lyric sheet. After any Rewrite, Reorder, or Delete, update the written lyrics (and their order) to match, and note the edit (section, operation, parent take). On true-story albums, a lyric sheet that doesn't match the audio breaks the trail between lyrics and verified sources.

### Lock the arrangement before download

Everything downstream (stem extraction, mix polish, mastering) runs on the downloaded WAV. Song Editor runs *upstream* of it.

- **Finish every section edit before you download, pull stems, polish, or master.** Going back into Song Editor afterward produces a new WAV. The stems go stale, and the polish and master have to be redone.
- **Master the finished track as one unit, never section by section.** A remade or extended section is still raw Suno output (pop/EDM often comes out around -9 to -7 LUFS). Master the whole arrangement-locked track once to the delivery target (-14 LUFS integrated / -1.0 dBTP for streaming) so loudness stays consistent across the seams. See references/production/mastering.md.
- **Fix bad seams in Suno, not in the master.** Mixing and mastering blend *minor* level or timbre differences between sections. A jarring mismatch needs another Remake before download.
- Add "all section edits final?" to the pre-download check.

### Fix path for a rejected take

| Rejection reason | Fix path |
|------------------|----------|
| Whole track wrong (genre, tempo, mood) | Revise the style prompt (references/suno/prompting.md), then regenerate fully |
| Wrong words or pronunciation in one or a few sections | Fix the lyric and phonetics, then Song Editor Rewrite on those sections |
| One flubbed section, take otherwise a keeper | Song Editor Remake on that section |
| Order or length wrong | Song Editor Reorder / Delete / Extend |
| Words and performance right, only the audio is off | Mix polish (not a regeneration) |

Log every attempt, section edits included: the reason, the section, the operation, and the result.

### Checklists

**Before a Song Editor pass**
- [ ] The problem is section-level, not global (global → regenerate)
- [ ] It's a content or performance problem, not audio quality (audio → polish)
- [ ] For Rewrite: the lyric and pronunciation are already fixed

**After a Song Editor pass**
- [ ] Listened to the seams between edited and untouched sections
- [ ] Lyric sheet updated to match the audio
- [ ] Edit logged (section, operation, parent take)
- [ ] Total extensions within 2-3
- [ ] Arrangement locked before download, polish, and master

See also references/suno/tips.md for more workflow tips and references/suno/pre-generation-check.md for the check to run before generating.

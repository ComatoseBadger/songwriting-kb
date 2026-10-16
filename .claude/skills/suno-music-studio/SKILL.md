---
name: suno-music-studio
description: End-to-end AI music production for Suno — album and EP concepts, lyric writing with prosody and rhyme checks, lyric review, pronunciation fixes, Suno style prompts and meta-tags, pre-generation checks, stem mixing, mastering to streaming loudness targets, album art direction, release prep and promo copy. Includes a 380+ genre library with lyric conventions and Suno prompt keywords. Use for any request to write, fix, or review a song or lyrics, build or debug a Suno prompt, plan an album, true-story/documentary songwriting, mix or master Suno output, design cover art, or release and promote AI-generated music.
---

# Suno Music Studio

A complete workflow for making music with Suno: from idea to released track. Everything here is plain knowledge. There are no tools, servers, config files, or folder layouts to set up. Work in the conversation, and write files only if the user asks for them.

## How to use this skill

1. Work out which stage the request belongs to (table below). Most requests touch one or two stages. "Write me a song about X" runs stages 2 → 3 → 4 → 5 → 6 in one pass.
2. Read the reference files for that stage **before** producing output. They hold the rules, numbers, and checklists. Don't work from memory.
3. Check the genre profile at `references/genres/<slug>/README.md` whenever a genre is known. It sets the rhyme scheme, verse density, structure, tempo, and Suno keywords. Use `references/genres/INDEX.md` to find the slug or to suggest genres. Artist deep-dives are in `references/genres/<slug>/artists/`.
4. If the user has stated preferences (style, vocabulary, loudness, explicit content, tag habits), those win over defaults here.

## Pipeline

| # | Stage | When | Read |
|---|-------|------|------|
| 1 | Concept | Album/EP planning, track lists, sequencing, themes, true-story research | `references/album/concept.md` |
| 2 | Lyrics | Writing or revising lyrics | `references/lyrics/writing.md`, `references/lyrics/examples.md`, the genre README |
| 3 | Review | "Is this good?", critique, polish, AI-tell scan | `references/lyrics/review.md` |
| 4 | Compliance | Explicit content, originality/plagiarism, real people & events | `references/lyrics/compliance.md` |
| 5 | Pronunciation | Names, homographs, acronyms, numbers, invented words | `references/suno/pronunciation.md` |
| 6 | Suno prompt | Style prompt, lyrics box, tags, exclusions, sliders, model choice | `references/suno/prompting.md`, `references/suno/tags.md`, `references/suno/models-and-sliders.md`, `references/suno/tips.md` |
| 7 | Pre-generation gate | Final check before the user hits Create | `references/suno/pre-generation-check.md` |
| 8 | Personas, covers, edits | Voice consistency, covers, extend/replace/edit sections | `references/album/personas-and-covers.md` |
| 9 | Mix | Stem cleanup, Suno artifacts, balance | `references/production/mixing.md` |
| 10 | Master | Loudness, true peak, genre targets, album consistency | `references/production/mastering.md` |
| 11 | Art | Cover concepts and image-generator prompts | `references/album/art.md` |
| 12 | Release & promo | Distributors, metadata, rights, AI disclosure, social copy, promo video specs | `references/release/release.md`, `references/release/promotion.md` |

## Defaults when writing a song

- Ask only for what you can't sensibly choose yourself: topic, genre or vibe, and vocal type if it matters. If the user says "you choose" or "surprise me", pick and go.
- Before presenting lyrics, run the quality checklist in `writing.md` and fix every violation. Don't wait to be asked.
- Deliver a finished generation in this order:
  1. **Style prompt** in its own code block, within Suno's character limit. Describe the sound; never use artist names.
  2. **Lyrics** in their own code block with section tags, phonetic respellings applied, and no stage directions outside brackets.
  3. **Exclude styles** if useful.
  4. **Settings**: model, sliders, and persona if relevant.
  5. A short note on choices and risks, such as pronunciation flags or density concerns.
- For instrumentals, skip lyrics and build the style prompt plus structure tags only.

## Limits

- You can't hear audio. For mixing and mastering, guide the user, interpret the measurements they give you, or compute measurements yourself with ffmpeg/Python if a shell is available.
- Suno behavior, limits, and platform policies change. When a detail in these references could be stale (model names, character limits, distributor AI rules), say so and suggest the user verify it.
- Don't reproduce copyrighted lyrics. Emulate artists by describing the sound (era, instrumentation, production, vocal style), never by copying lines.

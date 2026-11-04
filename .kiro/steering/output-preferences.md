---
inclusion: auto
description: Song output format conventions — Production Notes block, direction blocks, parenthetical layers, duet formatting, hit formulas, and song thesis requirement.
---

# Output & Format Preferences

> Auto-loaded. Recommended output format for all song files.
> Customize this file for your own conventions — see examples/preferences/ for a filled-in reference.

---

## Always Include: Production Notes Block

Every song output MUST include a detailed Production Notes section:

```
• Key: [Key] — [reasoning]
• Tempo: [X] BPM — [justification]
• Time Signature: [4/4 or 3/4 or 6/8]
• Chord Progression: [Nashville numbers] / [actual chords in key]
  (Describe each section; reuse or change progressions as the song needs)
• Vocal: [Type + delivery description]
• Instruments: [listed by prominence]
• Dynamics: [section-by-section energy with arrows]
• Hook Type: [Title/Melodic/Rhythmic/Instrumental + placement notes]
• Rhyme Scheme: [per section with reasoning if unconventional]
• Emotional Arc: [one-sentence narrative journey]
```

Chord notation shows BOTH Nashville numbers AND actual chords: `i – VI – III – iv (Em – C – G – Am)`

## Direction Blocks (Keep in Lyrics)

Always include these as consistency anchors:
- `[Production Direction: ...]` — overall tone, dynamics arc, what to avoid
- `[Vocal Direction: ...]` — voice type, delivery, emotional progression

These express continuity intent; listening must verify each generation.

## Artist Reference Conversion

Any artist name used as creative shorthand during writing (e.g., "in the style of Radiohead") must be converted to descriptive production language before appearing in the Style Prompt or Direction blocks. Translate to: genre + era + instruments + production characteristics + vocal style + structural habits. No artist names in final output.

## Per-Section Production Tags

Keep per-section tags like `[Sparse piano, room ambience]` — these guide instrument changes section-by-section. Limit to 2-3 tags per section for best Suno parsing.

## Duet Format Preferences

- `[Male Vocal]` / `[Female Vocal]` — capitalized, standardized
- Duet: give-and-take alternating (Male then Female per exchange)
- Target 4 exchanges per section (8 lines) but flexible

## Parenthetical Layers (Inline Vocal Effects)

- **Backup/response vocals:** plain `(text)` — works when Style declares who sings them
- **Delivery cues:** `(whispered) text` / `(spoken) text` — changes performance of next line
- **Named layers:** `(robotic layer: text)` / `(echo layer: text)` / `(whisper layer: text)` — creates a distinct secondary vocal identity. MUST be declared in Style Prompt.
- **Whisper Rule pattern:** Declare at top of lyrics: `[Whisper Rule: Lyrics in parentheses are whispered intrusive thoughts, close and breathy.]`
- **Echo/Layer treatment notation:** `[deep echo layer]` or `[distant burr echo]` after parenthetical lines to specify production treatment of those layers
- Always include `‑vocal overlap confusion` in negatives when using layers

## Character Limit Strategy

- Style 1000 chars → positives and core vocal rules FIRST
- Lyrics 5000 chars → must fit within limit (trim if needed)
- Exclude field = ONLY for negative prompts / exclusions (not overflow)

## Hit Formula Awareness

- **Formula 1 (Vulnerability):** 70-85 BPM, minor, minimal, confession hook, specific lyrics, imperfect vocal. Men's mental health territory.
- **Formula 2 (Anthem):** 90-110 BPM, minor→major lift, maximum production, chant hook, universal lyrics.
- These are optional reference shapes; combine or depart from them when the song benefits.

## Song Thesis

Every song should have a one-sentence thesis stated at the top of the file:
> *Song Thesis: The core truth this song expresses in a single sentence.*

## Current v6 package requirements


Follow `core/methodology/suno-optimization.md`, section "Current Suno v6 workflow".
It supersedes legacy tags, model advice and fixed production formulas elsewhere.

- Use `templates/suno-v6-song.md` for new complete packages.
- Before lock: >=2 distinct Style prompts and >=2 distinct intro architectures.
- Preserve the Vocal Identity anchor across alternatives; vary production freely.
- Intro Differentiation Gate: compare first 15–20 seconds with previous three tracks
  when available, documenting references/differences or unavailable history honestly.
- Include Advanced Options, Changes and Next Changes in every complete package.
- Keep metadata outside paste-ready Lyrics and Style; Exclude contains negatives only.
- House budgets: Style <=1000 each, Lyrics <=5000. Count fields separately.
- Preserve section-tag isolation, named layer declarations, artist conversion,
  prosody, breath, hook and emotional-arc checks. No compulsory intro or song formula.
- Bracket directives and exact slider recipes are heuristics, not guaranteed commands.
- Official facts and dated primary sources are listed in the canonical methodology.
- CLI defaults to v6; use `--legacy` for historical single-prompt files.

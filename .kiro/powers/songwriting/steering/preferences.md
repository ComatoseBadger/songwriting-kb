# User Preferences — Power Steering

## Always Output: Production Notes Block

Every song must include:
- Key (+ reasoning)
- Tempo (BPM + justification)
- Time Signature
- Chord Progression (Nashville numbers AND actual chords, per section)
- Vocal description
- Instruments (by prominence)
- Dynamics arc (section arrows)
- Hook Type (+ placement)
- Rhyme Scheme (per section)
- Emotional Arc (one sentence)

## Format Conventions
- `[Production Direction:]` and `[Vocal Direction:]` blocks in lyrics (consistency anchors)
- Per-section production cues: `[Sparse piano, room ambience]`
- `[Male Vocal]` / `[Female Vocal]` capitalized
- Duet: alternating lines, 4 exchanges per section
- Em dashes (—) for phrasing/breath within lines

## Parenthetical Layers
- Backup/response vocals: plain `(text)` — Style must declare who sings them
- Delivery cues: `(whispered) text`, `(spoken) text` — changes next-line performance
- Named layers: `(robotic layer: text)`, `(echo layer: text)`, `(whisper layer: text)` — MUST declare in Style Prompt
- Layer treatment tags: `[deep echo layer]` after parenthetical lines for production treatment
- Always add `‑vocal overlap confusion` to exclusions when using layers

## Song Thesis
Every song starts with:
> *Song Thesis: [one sentence core truth]*

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

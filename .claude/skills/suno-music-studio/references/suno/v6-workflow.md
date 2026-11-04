# Suno v6 Workflow Contract

This is the portable house workflow for new song packages. It takes priority over single-Style examples, genre defaults, and generic checklists in this skill. In this repository, keep it aligned with `core/methodology/suno-optimization.md` and `templates/suno-v6-song.md`. The skill remains usable when exported alone; no repository tools are required to read or follow this contract.

## Scope and creative freedom

Apply the complete package to new vocal songs and substantial production revisions. For a narrow request (one lyric fix, critique, mix advice, or one prompt), answer that request without inventing a complete song. Preserve approved lyrics and the established persona unless the user authorizes a change. Genre profiles supply options, not mandatory rhyme, tempo, structure, line counts, or emotional arcs. Do not impose a recurring arrangement or a default ambient build.

## Required package

Use level-two headings below. Put each copyable Style, Exclusions and Lyrics field in its own code block; keep heading labels outside the fences. Always keep Advanced Options, Changes and Next Changes visible in chat. No Canvas or writing blocks for tracks.

- Title as the document heading.
- **Vocal Identity**: one concise anchor covering register, timbre, phrasing and clean/harsh balance. Reuse the exact anchor in every Style Prompt and in `[Vocal Direction: ...]`. Keep identity stable while changing arrangement. If a saved Voice is used, retain the anchor for traceability; avoid contradictory instructions and test the rendered voice by listening.
- **Style Prompt A**, **Style Prompt B** (more if useful): at least two musically distinct alternatives before lock, each at most 1,000 characters. Front-load the defining sound and voice in the first 20–30 words; use at most two genre anchors, three or four named instruments and two mood/energy words. Vary tempo feel, rhythmic engine, instrument roles, ambience and section entry. Keep artist references outside the copyable prompts. These budgets are house policy, not verified Suno parser rules.
- **Intro Concept A**, **Intro Concept B**, **Intro Concept C**: three distinct proposals by default. Each records `Mechanism`, `First Sound`, `Groove` (including kick/snare behavior), `Vocal Entry`, `Envelope`, and `Transition`. Choose different mechanisms: immediate full-band, vocal-first, bass-led, guitar-signature, drum-led, cold verse, or a specific custom opening. Do not substitute three labels for the same opening. The repository validator's two-intro minimum is a compatibility floor, not the default creative deliverable.
- **Intro Differentiation Gate**: record `Window: 15–20 seconds`, `History: available` or `unavailable`, `Track 1` through `Track 3` for up to three recent tracks, a `Limitation` when fewer exist, `Comparison`, and `Decision: pass`, `revise` or `provisional`. Compare first sound, beat, vocal entry, envelopes and transitions; identify repeated fingerprints and the adjustment. Do not invent history or claim to have heard unavailable audio. Description-only comparisons stay provisional. Avoid recurring swells, pulses, risers and generic drum builds unless musically justified.
- **Production Lock**: `Status: draft` or `locked`, plus selected `Style` and `Intro` labels. Keep draft while choices or listening checks remain unresolved; do not silently lock. Preserve alternatives in the review record after selection.
- **Exclusions**: dedicated field, or explicit `none`.
- **Lyrics**: full lyrics with detailed section cues and the exact Vocal Direction anchor. Section-specific production belongs here, not in the global Style prompt. Tags are creative directions, not guaranteed commands.
- **Production Notes**: key, BPM, meter, chords when appropriate, vocal delivery, hook and vocal production notes, section energy map, rhyme and emotional arc. Explain musical choices without prescribing one formula. Include initial lyric QC and separate Similar Artists references when relevant.
- **Advanced Options**: Model (v6 family), Persona/Voice, Weirdness, Style Influence, Audio Influence, Exclude, Variety and Max Mode. Give a rationale or explicit unavailable/N/A. Verify controls against the user's current UI; recommendations are starting experiments, not guarantees.
- **Changes**: actual edits and reasons, or `None — initial draft`.
- **Next Changes**: visible, selectable revision choices and listening checks. Never silently rewrite locked lyrics.

## Instrumentals

Keep Style alternatives, three intro proposals, differentiation, selection, Advanced Options and Changes / Next Changes. Mark Vocal Identity and Vocal Entry `N/A — instrumental`; omit sung lyrics and voice checks and use structural tags. The current repository CLI targets vocal packages; do not fabricate a singer merely to pass it. Report instrumental checks manually.

## Pre-generation and lock

Run the existing lyrics, pronunciation, source, explicit-content and artist checks, plus this contract. Check every Style alternative, not only the selected one. In the repository run `python3 tools/validate-song.py <package.md>`; use `--legacy` only for historical single-prompt files, never as an escape from a failing new package.

Separate structural readiness from listening approval: text validation cannot hear singer continuity or the first 15–20 seconds. A draft can be ready for an exploratory generation with provisional history, but cannot be presented as production-locked until the required comparison passes. Without audio, disclose pending listening checks. Record the final selected copyable fields while retaining the complete alternatives and review record.

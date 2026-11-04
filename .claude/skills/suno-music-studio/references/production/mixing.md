# Mixing Suno Output

How to polish raw Suno audio (stems or a full stereo render) into a clean mix ready for mastering. This covers cleanup, EQ, dynamics and stem balance. It does not cover loudness normalization; for that, see `references/production/mastering.md`.

**Your position:** you cannot hear audio. Work from three things: what the user describes ("the vocal is harsh on the S's", "the low end is muddy"), measurements the user gives you, and measurements you take yourself with ffmpeg or Python when those tools exist in the environment. Turn a complaint into a likely frequency range and a conservative move, ask the user to A/B it, and repeat. If the user has stated mix preferences, follow them over every default here.

---

## Core principles

- **Use stems when you have them.** Processing each stem on its own beats processing a full mix, because a vocal-only fix can't dull the cymbals. Fall back to full-mix polish only when the user has no stems.
- **Stems are for balance, not surgery.** Level, pan, width and broad tone moves apply cleanly to a stem. De-essing, de-clicking and narrow notches don't, because of **stem bleed**: a cut on the vocal stem also lands on whatever leaked into that stem. If a de-esser on the vocal is dulling something else too, the cause is bleed, not a bad setting.
- **Solo the named element first.** When the user names an element ("the drums are harsh"), solo that stem and compare it raw against each processing stage before you touch any other stem, the full mix, or the master. A fix tested on the wrong layer wastes every experiment run there.
- **Preserve the performance.** Polish removes defects, not character. Over-processing sounds worse than under-processing. The defaults below are deliberately gentle.
- **Stay non-destructive.** Keep the original downloads untouched and write polished files under new names.
- **Split the work with mastering by frequency.** Mix presence boosts sit at about **3 kHz** and the mastering harshness cut sits at **3.5 kHz**. Because they have different center frequencies, they don't cancel each other.
- **Never touch the watermark.** Suno's Terms of Service (effective 2026-09-03) forbid removing, altering, obscuring or circumventing the fingerprint, watermark or metadata Suno adds to an output. Polish is tonal and dynamic cleanup only, and you must never describe any step as doing that.

### About Suno v6

The default settings below were calibrated on the previous Suno model generation and haven't been re-measured on v6. Early reports on v6 describe:
- de-essed or smeared sibilance
- less top-end harshness in most genres
- more artifacts in rock and metal, where vocals drift to a generic or grainy timbre
- a narrower stereo image than expected
- mixes that sometimes go muffled after about 2:30 in standard mode

Before you trust the presence and mud settings on v6 material, check them by ear. Don't widen by default. Widen only when the user hears a narrow image, and then run a mono check (see the QC section in mastering.md).

---

## Getting stems from Suno

Always download **WAV**, not MP3, because MP3 artifacts compound at every later step. Create-page WAVs are 44.1 kHz. Suno Studio exports are 32-bit float at 48 kHz. Both formats work.

Suno offers three split modes (More Actions (…) → Get Stems):

| Mode | Output | When to use |
|---|---|---|
| **Auto Split** | 12 stems: Vocals, Backing Vocals, Drums, Bass, Guitar, Keyboard, Strings, Brass, Woodwinds, Percussion, Synth, FX/Other | A full stem mix |
| **Split from Mix** | 2 stems: the target, plus everything else | One clean element (often cleaner than pulling all 12) |
| **Advanced Split** | 1 targeted stem chosen from about 100 instruments | A specific instrument (Premier tier, costs credits per extraction) |

What to expect from Auto Split in practice:
- bleed and crosstalk between stems
- reverb baked in and shared across several stems
- separation artifacts
- a file for **every** category, even when the song has no such instrument

The empty categories come back as a **near-silent placeholder at about −55 dBFS**, not true digital silence. Skip any stem whose peak is below **−40 dBFS** and pass it through unprocessed. Lower that gate per stem (for example to −80 dBFS) only when a genuinely quiet part, such as a distant pad or a fade-in intro, is being thrown away.

---

## Step 1: Diagnose before processing

Measure, or ask the user to describe, before you choose any settings. These checks are cheap and point straight at the fix. Run them per stem, or on the full mix when there are no stems.

| Check | How it's measured | Flag when | Suggested response |
|---|---|---|---|
| Noise floor | Mean absolute level of the quietest 10% of samples | > 0.005 linear (about −46 dBFS) | Apply noise reduction **only if the audio was imported or recorded** (see below) |
| Mud | Share of spectral energy at 150–400 Hz | > 35% | Cut −3 dB around 200–300 Hz |
| Harshness | Share of spectral energy at 2–5 kHz | > 25% | High-shelf cut −2 dB at about 7 kHz |
| Already dark | Share of spectral energy at 2–5 kHz | < 10% | **Remove** the default high-shelf cuts (set them to 0). Optionally add 1.5–2.5 dB of harmonic excitation. |
| Clicks | 10 ms windows whose peak-to-RMS ratio exceeds 15 | More than 10 windows | Apply click repair (drums, percussion and instrument stems only) |
| Sub rumble | Share of spectral energy below 30 Hz | > 15% | High-pass at 35 Hz |
| Empty stem | Peak level | < −40 dBFS | Skip it entirely |

**The analysis detects problems. It doesn't decide what to do about them.** If a check keeps flagging something that the defaults deliberately ignore (most often noise reduction on synthesized vocals), tell the user and let them decide. Don't quietly work around it.

---

## Step 2: Per-stem polish chains

The default processing order within each stem is: click repair → (noise reduction) → high-pass → mud cut → presence boost → high-shelf tame → stereo width → compression → (saturation / low-pass) → stem gain.

Filter and compressor conventions:
- High-passes are 2nd-order Butterworth.
- Presence boosts are peaking bells, Q ≈ 1.5 unless noted.
- Tames are high shelves.
- Compressor release is about 100 ms.
- Width multiplies the side signal in mid/side (1.0 = unchanged).

| Stem | High-pass | Mud cut | Presence | High tame (shelf) | Width | Compression (thr / ratio / attack) | Notes |
|---|---|---|---|---|---|---|---|
| **Lead vocals** | — | — | +2 dB @ 3 kHz | −2 dB @ 7 kHz | — | −15 dB / 2.5:1 / 10 ms | Click repair and noise reduction off by default |
| **Backing vocals** | — | — | +1 dB @ 3 kHz | −2.5 dB @ 7 kHz | 1.3× | −14 dB / 3:1 / 8 ms | Sits −1.5 dB under the lead in the remix |
| **Drums** | — | — | — | — | — | −12 dB / 2:1 / 5 ms | Click repair on (cubic-spline repair) |
| **Bass** | 30 Hz | −3 dB @ 200 Hz | — | — | — | −15 dB / 3:1 / 10 ms | Keep mono |
| **Guitar** | 80 Hz | −2.5 dB @ 250 Hz | +1.5 dB @ 3 kHz (Q 1.2) | −1.5 dB @ 8 kHz | 1.15× | −14 dB / 2.5:1 / 12 ms | 250 Hz is the boxiness zone |
| **Keyboard** | 40 Hz | −2 dB @ 300 Hz | +1 dB @ 2.5 kHz (Q 0.8) | −1.5 dB @ 9 kHz | 1.1× | −16 dB / 2:1 / 15 ms | Low HPF keeps piano bass notes; presence stays out of the vocal zone |
| **Strings** | 35 Hz | −1.5 dB @ 250 Hz (Q 0.8) | +1 dB @ 3.5 kHz | −1 dB @ 9 kHz | 1.25× | −18 dB / 1.5:1 / 20 ms | Lightest compression of any stem; keeps orchestral dynamics |
| **Brass** | 60 Hz | −2 dB @ 300 Hz | +1.5 dB @ 2 kHz | −2 dB @ 7 kHz | — | −14 dB / 2.5:1 / 10 ms | Bite below the vocal zone; brass is piercing up top |
| **Woodwinds** | 50 Hz | −1.5 dB @ 250 Hz (Q 0.8) | +1 dB @ 2.5 kHz | −1 dB @ 8 kHz | — | −16 dB / 2:1 / 15 ms | Keep the breathiness |
| **Percussion** | 60 Hz | — | +1 dB @ 4 kHz | −1 dB @ 10 kHz | 1.2× | −15 dB / 2:1 / 8 ms | Click repair on; highest presence of any stem, for shakers and tambourine |
| **Synth** | 80 Hz | — | +1 dB @ 2 kHz (wide, Q 0.8) | −1.5 dB @ 9 kHz | 1.2× | −16 dB / 2:1 / 15 ms | HPF avoids fighting the bass |
| **Other / FX** | — | −2 dB @ 300 Hz | — | −1.5 dB @ 8 kHz | — | — | Catch-all |

**Remix and bus:**
- Sum the stems at unity (0 dB), apart from backing vocals at −1.5 dB and the genre offsets below.
- Bus glue compression: −14 dB threshold, 2.5:1, 20 ms attack, 150 ms release.
- If the summed peak goes above 0.95 FS (about −0.4 dBFS), scale the whole mix down. Never clip.
- **No stem should come out louder than it went in.** Saturation and positive gain can raise peaks by 4–17%, so match each processed stem's peak back to its input peak.

**Noise reduction defaults to off on every stem.** Suno stems are synthesized, not recorded, so there is no steady noise floor to profile. Spectral gating removes consonants, breaths and sibilance decay instead of noise. Turn it on per stem only for **imported or recorded** audio with a real noise floor. Start at a strength of 0.3–0.5 and never exceed 0.8.

**Click repair defaults to off on vocals and on full mixes.** A peak/RMS detector can't reliably tell a clean synthetic consonant from a click, and a full mix contains the vocals. Still run detection on those, and report any clicks it finds so they surface before mastering. Raise the detection ratio from 15 to 20–25 if real transients are being flagged. Lower it to 10–12 only if genuine clicks are slipping through. Dense electronic genres use about 10.

### Full-mix fallback (no stems)

Use this chain:
1. High-pass at 35 Hz
2. Mud cut −2 dB at 250 Hz
3. Presence +1.5 dB at 3 kHz
4. High shelf −1.5 dB at 7 kHz
5. Compression at −15 dB threshold, 2:1
6. Width 1.0, click repair off, noise reduction off

This approach is less effective because it can't rebalance elements or target one sound. Recommend pulling stems when the problem is specific to one instrument.

---

## Common Suno artifacts and fixes

| Artifact | What it sounds like / where | Fix | Don't |
|---|---|---|---|
| **Harshness / sibilance** | Piercing 2–5 kHz content (tinny), sharp "s" sounds at 5–8 kHz | Vocal high shelf −2 to −3 dB at 7 kHz. On a bright mix, take −1 to −2 dB from the 3–4 kHz area on the instrument stems. Leave the rest to the mastering cut at 3.5 kHz. | Don't stack big cuts in mix and master. On v6, check first, because sibilance is often already smeared. |
| **Mud** | Thick, undefined low-mids at 150–400 Hz | −2 to −3 dB at 200 Hz (bass), 250 Hz (guitar), 300 Hz (keys and other). Go up to −3.5 to −4 dB for heavy guitars. | Don't over-cut warm genres (folk, jazz, soul). Reduce the cut there. |
| **Metallic shimmer / "watery" swirl** | Phasey, chirpy highs, mostly in cymbals, reverb tails and pad stems. Caused by separation or generation. | Gentle high shelf −1 to −2 dB at 8–10 kHz on the affected stem. Low-pass the stem at 14–16 kHz if the genre allows. Reduce that stem's width. Try **Split from Mix** for a cleaner pull. Regenerate or replace the section if it's severe. | Don't hunt for narrow notches on a bleeding stem. Don't widen it. |
| **Phasing / hollow mono** | The mix thins out or loses its vocal on a phone speaker or a mono Bluetooth speaker | Lower the width multipliers toward 1.0. Make the bass mono below about 120 Hz. Check that the L/R correlation stays above 0 (ideally above 0.5) and that mono-fold loss stays under 3 dB (ideally under 1 dB). | Don't add stereo wideners to v6 renders by default. |
| **Narrow image** (v6) | The whole mix sits in the middle | Modest per-stem width only: 1.1–1.3× on pads, backing vocals and strings. Keep bass, kick and lead vocal centered. Re-check mono afterward. | Don't try to fix this with style-prompt changes. It's a mix move. |
| **Noise / hiss** | Steady background noise | Only for imported or recorded audio: spectral noise reduction at 0.3–0.5 | Don't run it on Suno-synthesized stems. |
| **Clicks / pops** | Single-sample spikes in drums, percussion or instruments | Click repair: interpolate across the spike, using cubic spline on drums and percussion | Don't auto-declick vocals. Repair by hand if needed. |
| **Sub rumble** | Energy below 30 Hz that eats headroom | High-pass the bass at 30 Hz. Raise to 35–40 Hz if rumble is flagged. Lower to 20–25 Hz for sub-heavy genres. | — |
| **Dark / muffled sections** | Dull top end, sometimes only after about 2:30 | Remove the default high-shelf cuts. Optionally add 1.5–2.5 dB of harmonic excitation on vocals, keys and strings, but not on drums or bass. If only a later section is muffled, regenerate or replace that section in Suno. | Don't EQ-boost air onto artifacts. That brightens the swirl too. |
| **Empty stems** | A placeholder file at about −55 dBFS | Skip it (gate at −40 dBFS) | Don't process it or sum it with makeup gain. |

---

## Genre mix presets

These are offsets from the per-stem defaults above. Gains are remix levels. "Sat" is soft tanh saturation drive on a 0–1 scale, where 0.1 is subtle and 0.35 is obvious. "LP" is a low-pass for vintage or lo-fi character. "Bus" is the bus compressor ratio.

| Genre(s) | Vocals | Drums / percussion | Bass | Instruments / other | Bus / full-mix character |
|---|---|---|---|---|---|
| **Pop, K-pop** | Presence +2.5, gain +0.5. BVs −1.0 (K-pop −0.5), width 1.4. | Perc 2.5:1, +0.5 | — | Strings presence +1.5, 2:1. Brass 3:1, −0.5. Woodwinds 2.5:1. Synth tame −1. Other tame −2. | Width 1.1 |
| **Hyperpop** | Presence +3, tame −1.5, +0.5 | Drums 2.5:1 | — | — | Sat 0.15, width 1.2 |
| **Hip-hop / rap / grime / nerdcore** | Presence +2.5, gain +1 (grime +0.5), sat 0.1. BVs −2.5. | Drums +0.5, perc +0.5 (presence +1.5) | HPF 25 Hz, mud −2, gain +1 (nerdcore +0.5) | Strings −0.5. Brass presence +2, 3:1, −0.5. Synth −0.5. | Sat 0.1 |
| **Trap** | Presence +2, +0.5 | Drums +1 | HPF 25, +1.5, sat 0.15 | — | Bus 3:1, sat 0.1 |
| **Drill** | +0.5 | Drums +0.5, sat 0.1 | HPF 25, +1 | — | Sat 0.1 |
| **Phonk** | Tame −2.5, sat 0.4, LP 8 kHz | Drums +0.5, sat 0.35 | HPF 25, +1, sat 0.2 | — | Bus 3:1, sat 0.35, LP 10 kHz, width 0.9 |
| **R&B** | Presence +2, tame −1.5, +0.5, sat 0.1 | — | Mud −2, +0.5 | — | Sat 0.1 |
| **Soul / gospel** | Presence +1.5 (gospel +2), +0.5, sat 0.1–0.15 | — | — | Keys presence +1.5, sat 0.15. Guitar and brass sat 0.1. Other mud −1.5. | Sat 0.15 (soul) |
| **Funk** | — | Drums +0.5, sat 0.1. Perc +0.5, 2.5:1. | Mud −2, +0.5, sat 0.2 | Guitar presence +2, 3:1, sat 0.1. Keys (clav/organ) sat 0.2, 2.5:1. Brass +0.5, 3:1. | Sat 0.15 |
| **Disco** | — | Drums +0.5 | +0.5 | Other tame −1 | Sat 0.1, width 1.1 |
| **Rock** | Tame −2.5 | Drums +0.5, sat 0.15 | — | Guitar mud −3, +0.5, sat 0.15. Synth −0.5. Other mud −3. | Sat 0.15 |
| **Indie rock / alternative / indie** | Tame −2 (indie: presence +1.5, +0.5) | Drums +0.5 (indie rock) | — | Other mud −2 to −2.5 | Sat 0.1 |
| **Grunge / garage rock** | Tame −3 / −2.5, sat 0.3 / 0.25 | Drums sat 0.2 (grunge +0.5) | — | Other mud −3 / −2.5 | Sat 0.25 / 0.2, LP 14 kHz |
| **Surf / psychedelic / prog / post-rock** | Psych vocal sat 0.15. Post-rock presence +1.5. | Drums +0.5 (surf, prog) | — | Other tame −1, mud −2 (prog: mud −2.5) | Width 1.15 (surf) / 1.3 (psych, post-rock) / 1.2 (prog). Sat 0.1–0.15. |
| **Punk / hardcore** | Tame −3 | Drums +1, sat 0.2 / 0.25 | — | Guitar mud −3, sat 0.15. Other mud −3 / −3.5. | Sat 0.2 / 0.25 |
| **Ska-punk / Celtic punk / emo** | Celtic +0.5. Emo presence +2.5, +0.5, sat 0.1. | Ska drums +0.5, sat 0.1 | — | Other mud −2 to −2.5 | Sat 0.1–0.15 |
| **Metal / metalcore / thrash** | Tame −3 | Drums 2.5:1, +1, sat 0.2 (thrash 0.25) | Mud −4, +0.5, sat 0.15 | Guitar mud −4, presence +2, +0.5, sat 0.2. Other mud −3.5 to −4. Synth −0.5. | Sat 0.2–0.25 |
| **Black metal** | Tame −3.5, sat 0.2 | Drums +0.5 | — | Other mud −3 | Sat 0.2, LP 15 kHz |
| **Doom metal** | — | Drums 1.5:1 | HPF 25, mud −2, +1, sat 0.25 | Other mud −2.5 | Sat 0.2, width 1.1 |
| **Industrial** | Tame −3, sat 0.35 | Drums +1, sat 0.3 | +0.5, sat 0.2 | Other mud −3 | Sat 0.3 |
| **Electronic / EDM** | — | Drums +0.5 (EDM +1). Perc 2.5:1, +0.5. | HPF 25, +0.5 (EDM +1) | Synth +0.5, width 1.3. Other tame −1. | Width 1.1 (EDM 1.15, bus 3:1) |
| **House / techno / trance** | — | Drums +1 (techno 2.5:1, sat 0.1) | HPF 25, +0.5 (trance: HPF only) | Trance: other tame −1 | Width 1.1 (trance 1.2) |
| **Drum & bass / dubstep** | — | DnB drums +1.5, 2.5:1, sat 0.15. Dubstep drums +0.5. | HPF 25, +1 (dubstep +1.5, sat 0.2) | — | Bus 3:1. Width 1.1 / 1.15. |
| **Synthwave / new wave** | New wave presence +2 | — | Synthwave +0.5 | Synth +0.5, width 1.4, tame −1. Other tame −1 to −1.5, mud −1.5. | Synthwave sat 0.15, width 1.3. New wave sat 0.1, width 1.15. |
| **Dancehall / reggae** | Dancehall +0.5 | Drums +0.5. Reggae perc +0.5, sat 0.1. | HPF 25, +1, sat 0.1–0.15 | — | Width 1.1 / sat 0.1 |
| **Ambient** | Presence +1, 1.5:1. BVs 1.5:1, width 1.5. | — | — | Keys 1.5:1. Strings 1:1 (bypass), width 1.4. Synth 1.5:1, width 1.4. Other tame −1. | Bus bypass, width 1.3 |
| **Lo-fi** | Presence +1, tame −1, sat 0.3, LP 9 kHz. BVs sat 0.25, LP 8 kHz. | Drums sat 0.2. Perc sat 0.1. | Sat 0.2 | Guitar, keys, synth: sat 0.2, LP 10 kHz. Strings LP 12 kHz. | Bus 3:1, sat 0.25, LP 9 kHz, width 0.85 |
| **Chillwave / vaporwave / shoegaze / trip-hop** | Presence +1, sat 0.15–0.25 (vaporwave LP 10 kHz). Trip-hop presence +2, sat 0.1. | Trip-hop drums +0.5 | Trip-hop +0.5 | Other tame −1 (vaporwave LP 11 kHz) | Sat 0.15–0.2. LP 13 kHz (chillwave, trip-hop) / 11 kHz (vaporwave) / 14 kHz (shoegaze). Width 1.1 / 0.9 / 1.4. |
| **Folk / country / Americana / bluegrass** | Presence +2, +0.5 (bluegrass: +0.5 only) | Country drums +0.5 | — | Guitar presence +2, mud −1.5, width 1.0 (centered). Other mud −1.5. | Standard; don't squash |
| **Indie folk / singer-songwriter** | Presence +1.5 to +2, +0.5 | — | — | Other mud −1.5 | Light |
| **Jazz / bossa nova / swing** | Presence +1.5, 2:1, sat 0.1 | Drums 1.5:1. Perc 1.5:1, width 1.1. | Mud −2 | Guitar, keys, brass, woodwinds: 1.5:1, sat 0.1. Woodwinds presence +1.5, +0.5. Strings 1:1, width 1.2. Other mud −1.5. | Bus bypass (swing: none), sat 0.1 |
| **Blues** | Presence +1.5, +0.5, sat 0.2 | — | Sat 0.15 | Guitar sat 0.2, presence +1, 2:1. Keys sat 0.15, presence +1.5. Other mud −2. | Sat 0.15 |
| **Classical / opera** | Presence +1–1.5, 1.5:1 (opera +0.5) | Drums 1.5:1. Perc 1:1. | — | Strings, woodwinds, keys, brass: 1:1 (bypass). Strings and woodwinds tame 0. Brass tame −1. | Bus bypass |
| **Cinematic** | — | Drums +0.5. Perc 1:1. | +0.5 | Strings +0.5, width 1.3. Brass 1:1, tame −1. Other mud −2. | Width 1.3 |
| **Latin / Afrobeats** | +0.5 | Drums +0.5 (Afrobeats +1, sat 0.1). Perc +1, presence +1.5, 2.5:1. | +0.5 | Brass +0.5, presence +2 | Width 1.1 |
| **Piano pop / piano rock** | — | — | — | — | Width 1.05 / sat 0.1 |

Use these as starting points. If the user always hears the same problem (for example, every render too bright), adjust the relevant default for that user and say what changed.

---

## Workflow (DAW-agnostic)

1. **Gather.** Get WAV stems (Auto Split, or Split from Mix for a single element) plus the full-mix WAV as a reference. Confirm the genre so you can pick the preset.
2. **Pre-flight.** Check that every file is WAV at the same sample rate. Drop or mute stems that peak below −40 dBFS. Note any track with no stems; it gets the full-mix fallback.
3. **Diagnose** each stem against the table in Step 1. Report findings in plain English, for example: "The bass stem has 38% of its energy at 150–400 Hz, so it's muddy. I'll cut 3 dB at 200 Hz." Also tell the user which flags you're deliberately ignoring and why.
4. **Set up the session.** Import the stems at unity gain, aligned at zero. Suno stems are sample-aligned, so never nudge them. Put the full-mix render on a muted reference track.
5. **Insert per-stem chains** from the table above, then apply the genre offsets. Start with the stem the user complained about, and solo it.
6. **Balance.** Set the vocal level first, then drums and bass, then everything else. Pan only what the arrangement supports. Keep the kick, bass, lead vocal and snare centered.
7. **Glue.** On the mix bus, use about 2.5:1 at roughly 1–3 dB of gain reduction, 20 ms attack, 150 ms release. No limiter on the mix bus; leave limiting to mastering.
8. **Preview, then commit.** A/B against the raw full mix at matched loudness, because louder always sounds "better". Check on headphones and on a phone speaker.
9. **Export** a 24-bit (or 32-bit float) WAV at the source sample rate, with peaks around −3 to −6 dBFS, no clipping, no limiting, and no NaN or silent dropouts.
10. **Hand off to mastering.** Send the polished file to mastering, not the raw render. Pass along the genre and any per-track exceptions.

### Quality gate before mastering

- [ ] Every stem was processed, or the full-mix fallback was used. Don't do both on the same track.
- [ ] No clipping. Peak below 0.99 FS, ideally −3 to −6 dBFS.
- [ ] No NaN/inf samples, truncation, or silent gaps.
- [ ] No new artifacts: compare against the raw render at matched level.
- [ ] Mono fold sounds intact: the vocal survives and the bass doesn't vanish.
- [ ] Noise reduction was applied only to imported or recorded material, if at all.

### Common mistakes

- **Noise reduction on everything.** It strips musical detail from synthesized stems. Leave it at 0.
- **Skipping diagnosis.** Measure first, then process.
- **Mastering the raw files after polishing.** Master the polished output.
- **Polishing stems and then also polishing the full mix.** That double-processes. Pick one path.
- **Widening a v6 render by reflex.** Only widen on request, and check mono afterward.

---

## Optional: ffmpeg without a DAW

Use this when the user has no DAW, or when you can run commands yourself. All of these use standard ffmpeg filters (ffmpeg 5 or later recommended). Always write to a new file. Don't overwrite the original.

**Measure a stem or mix** (peak, RMS, DC offset, and loudness with true peak):
```bash
ffmpeg -hide_banner -i in.wav -af astats=metadata=0 -f null - 2>&1 | grep -E "Peak level|RMS level|DC offset"
ffmpeg -hide_banner -i in.wav -af ebur128=peak=true -f null - 2>&1 | tail -n 12
```

**Check whether a stem is an empty placeholder** (the max volume line reads below −40 dB):
```bash
ffmpeg -hide_banner -i "Brass.wav" -af volumedetect -f null - 2>&1 | grep max_volume
```

**Lead-vocal polish** (presence +2 dB at 3 kHz, high shelf −2 dB at 7 kHz, 2.5:1 compression at −15 dB):
```bash
ffmpeg -i vocals.wav -af "equalizer=f=3000:t=q:w=1.5:g=2,highshelf=f=7000:g=-2,acompressor=threshold=-15dB:ratio=2.5:attack=10:release=100" -c:a pcm_s24le vocals_polished.wav
```

**Bass polish** (high-pass 30 Hz, mud −3 dB at 200 Hz, 3:1 at −15 dB):
```bash
ffmpeg -i bass.wav -af "highpass=f=30:p=2,equalizer=f=200:t=q:w=1:g=-3,acompressor=threshold=-15dB:ratio=3:attack=10:release=100" -c:a pcm_s24le bass_polished.wav
```

**Drums** (gentle 2:1 at −12 dB with a fast attack):
```bash
ffmpeg -i drums.wav -af "acompressor=threshold=-12dB:ratio=2:attack=5:release=100" -c:a pcm_s24le drums_polished.wav
```

**Guitar or other instruments** (high-pass 80 Hz, −2.5 dB at 250 Hz, +1.5 dB at 3 kHz, shelf −1.5 dB at 8 kHz, slight widening):
```bash
ffmpeg -i guitar.wav -af "highpass=f=80:p=2,equalizer=f=250:t=q:w=1:g=-2.5,equalizer=f=3000:t=q:w=1.2:g=1.5,highshelf=f=8000:g=-1.5,extrastereo=m=1.15,acompressor=threshold=-14dB:ratio=2.5:attack=12:release=100" -c:a pcm_s24le guitar_polished.wav
```

**Tame shimmer or swirl on a pad or cymbal-heavy stem** (shelf down and a gentle low-pass):
```bash
ffmpeg -i synth.wav -af "highshelf=f=9000:g=-2,lowpass=f=15000:p=2" -c:a pcm_s24le synth_tamed.wav
```

**Remix polished stems** with per-stem gain and bus glue. `normalize=0` keeps amix from turning each input down. The final `volume` step is headroom, so check the peak afterward and lower it if the result peaks above about −1 dBFS.
```bash
ffmpeg -i vocals_polished.wav -i bvs_polished.wav -i drums_polished.wav -i bass_polished.wav -i guitar_polished.wav \
  -filter_complex "[1:a]volume=-1.5dB[bv];[0:a][bv][2:a][3:a][4:a]amix=inputs=5:normalize=0,acompressor=threshold=-14dB:ratio=2.5:attack=20:release=150,volume=-3dB[out]" \
  -map "[out]" -c:a pcm_s24le mix_polished.wav
```

**Full-mix fallback** (no stems):
```bash
ffmpeg -i full_mix.wav -af "highpass=f=35:p=2,equalizer=f=250:t=q:w=1:g=-2,equalizer=f=3000:t=q:w=1.5:g=1.5,highshelf=f=7000:g=-1.5,acompressor=threshold=-15dB:ratio=2:attack=10:release=100" -c:a pcm_s24le full_mix_polished.wav
```

**Mono-compatibility check.** Measure the stereo file, then a dual-mono fold. The fold puts the mid signal on both channels so the two loudness readings are comparable. A drop under 1 LU is fine. A drop of 1–3 LU calls for a listen. A drop above 3 LU, or a vanished vocal, means there are phase problems.
```bash
ffmpeg -hide_banner -i mix_polished.wav -af ebur128 -f null - 2>&1 | grep -A1 "Integrated loudness"
ffmpeg -hide_banner -i mix_polished.wav -af "pan=stereo|c0=0.5*c0+0.5*c1|c1=0.5*c0+0.5*c1,ebur128" -f null - 2>&1 | grep -A1 "Integrated loudness"
```

Notes on these commands:
- `acompressor` and `alimiter` take linear values, but the `dB` suffix converts for you, as shown.
- `extrastereo=m=1.0` leaves the image unchanged. Values above 1 widen.
- These are starting points. Tell the user to listen after each change.

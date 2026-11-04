# Mastering Suno Tracks

Taking polished mixes to release-ready masters: loudness, true peak, tonal balance, album consistency and platform delivery. Do mix cleanup first (see `references/production/mixing.md`). Release logistics are in `references/release/release.md`.

**Your position:** you cannot hear audio. Guide the user through the chain, interpret the numbers they paste (meter readouts, ffmpeg output), and when ffmpeg or Python is available, measure and process files yourself. Numbers are a safety net, and the user's ears decide. If the user has stated mastering preferences (target loudness, ceiling, bit depth, genre treatment), those override every default below.

Mastering is loudness, dynamics and tonal balance only. Suno's Terms of Service (effective 2026-09-03) prohibit removing, altering or obscuring the fingerprint, watermark or metadata Suno adds to an output. No step here does that, and never describe any step that way.

---

## Core principles

- **Loudness is not volume.** LUFS measures perceived loudness. Streaming services normalize playback to a reference, so a louder master just gets turned down, minus its dynamics. Too loud sounds squashed and fatiguing. Too quiet may not be turned up.
- **Universal target: −14 LUFS integrated, −1.0 dBTP true peak.** This works on every major platform. Use **−1.5 dBTP** for dense-transient genres (trap, punk, metal, industrial, EDM, drum & bass, dubstep, hardstyle), because their codec overshoot is larger.
- **Genre shapes the target.** Dynamic genres (classical, jazz, ambient, cinematic) sit at −16 to −18 LUFS. Loud club genres (hardstyle, gabber, reggaeton, rave) can sit at −12. For streaming, −14 is safe for nearly everything. See the genre table at the end of this file.
- **Preserve dynamics.** Don't crush a track to hit a number. If a track only reaches −14 by sounding lifeless, master it to −16 instead.
- **Master last.** Master after the tracks are generated, approved, polished and sequenced. Mastering cannot rescue a bad mix.
- **Use one master for every platform.** Make a single universal master for the distributor to send everywhere, not a separate version per service.

---

## Platform targets

| Platform | Normalization reference | True-peak ceiling | Behavior / strategy |
|---|---|---|---|
| **Spotify** | −14 LUFS | −1.0 dBTP (−2 if mastering louder than −14) | Turns louder tracks down. Quieter tracks are turned up only within peak headroom. Master to −14. |
| **Apple Music** | −16 LUFS (Sound Check) | −1.0 dBTP | Master to −14 anyway. It gets turned down slightly, keeps its dynamics, and stays consistent with other platforms. |
| **YouTube** | −14 LUFS (accepts about −13 to −15) | −1.0 dBTP | Only turns loud tracks down. 48 kHz is preferred for video. |
| **Tidal** | −14 LUFS | −1.0 dBTP | FLAC/lossless tiers. |
| **Amazon Music** | −14 LUFS | **−2.0 dBTP** | More conservative ceiling. Use −2 dBTP if Amazon matters to the user. |
| **Deezer** | about −15 LUFS | −1.0 dBTP | −14 is fine. |
| **SoundCloud** | No reliable normalization | −1.0 dBTP | Use −14 for consistency. Upload WAV or FLAC. |
| **Bandcamp** | None (the listener sets the volume) | −1.0 dBTP | −14, or −12 if the genre expects loud. |

**Delivery format:**
- **24-bit WAV** at the source sample rate is the safe universal deliverable.
- Suno Create-page WAVs are 44.1 kHz. Suno Studio exports are 32-bit float at 48 kHz. Spotify streams at 44.1 kHz regardless.
- To produce 16-bit, add **TPDF dither** at the final bit-depth reduction, and only there.

**Hi-res badges:** Apple Hi-Res Lossless requires 24-bit at **more than** 48 kHz. Tidal Max requires 24-bit above 44.1 kHz. Upsampling a 44.1 kHz Suno render to 96 kHz passes those gates but adds **no** audio information above about 22 kHz. If the user wants the badge, tell them this plainly and don't present the upsample as a quality gain.

---

## Measurement

### What the numbers mean

| Metric | Definition | Use |
|---|---|---|
| **Integrated loudness (LUFS)** | Gated average loudness over the whole track (ITU-R BS.1770 / EBU R128) | The number platforms normalize. Your main target. |
| **Short-term loudness** | Loudness over a 3 s window (1 s hop) | Section-to-section loudness. Its top 5% ("STL-95") shows how loud the choruses actually hit. |
| **Momentary loudness** | Loudness over a 400 ms window | Spot spikes. |
| **LRA (LU)** | Spread of short-term loudness, 10th to 95th percentile | Macro dynamics. About 8 LU suits balanced pop. Under 4 LU feels flat. Classical and ambient run 15 LU or more. |
| **True peak (dBTP)** | Peak after 4× oversampling (inter-sample peaks) | Must stay under the ceiling, or lossy encoding (AAC/MP3/Opus) can clip on playback. |
| **Sample peak (dBFS)** | Highest sample value | Not enough on its own. True peak can be 0.5–2 dB higher. |
| **Crest factor / PLR** | Peak-to-RMS ratio, or peak-to-loudness | A high value (above about 12 dB) means big transients, and the track may not reach target without compression. |
| **Tinniness ratio** | Energy at 2–6 kHz divided by energy at 500 Hz–2 kHz | Above 0.6 means a high-mid cut is needed. Above 0.8 means a clear spike. |

Typical dynamic range by genre: classical 15–25 dB, jazz/folk 10–15 dB, rock/pop 6–12 dB, EDM/hip-hop 4–8 dB.

### How to measure

**ffmpeg** (fast and available almost everywhere). This prints integrated loudness, LRA and true peak:
```bash
ffmpeg -hide_banner -i track.wav -af ebur128=peak=true -f null - 2>&1 | tail -n 12
ffmpeg -hide_banner -i track.wav -af loudnorm=print_format=summary -f null - 2>&1 | grep -E "Input (Integrated|True Peak|LRA)"
```

**Python** (`pyloudnorm`, `soundfile`, `scipy`):
```python
import numpy as np, soundfile as sf, pyloudnorm as pyln
from scipy.signal import resample_poly, welch
x, sr = sf.read("track.wav", always_2d=True)
lufs = pyln.Meter(sr).integrated_loudness(x)                     # BS.1770
tp = 20*np.log10(np.abs(resample_poly(x, 4, 1, axis=0)).max())    # ~true peak
f, p = welch(x.mean(axis=1), sr, nperseg=8192)
band = lambda lo, hi: p[(f >= lo) & (f < hi)].sum()
print(f"{lufs:.1f} LUFS | {tp:.2f} dBTP | tinniness {band(2000,6000)/band(500,2000):.2f}")
```

**Meters the user can run:**
- Free: Youlean Loudness Meter (plugin or standalone, with platform presets), TBProAudio dpMeter (true peak), Orban Loudness Meter (EBU R128), HOFA 4U+ Meter.
- Paid: iZotope Insight 2, Nugen MasterCheck Pro (codec preview).

### Reading the results

| Reading | Problem | Fix |
|---|---|---|
| Integrated louder than −12 LUFS (streaming target) | Too loud; it will be turned down and sound squashed | Lower the gain into the limiter |
| Integrated quieter than −16 (for a −14 genre) | Too quiet | More gain. If it won't get there, see "Track won't reach target" below. |
| True peak above −1.0 dBTP | Clipping risk after encoding | Set the ceiling to −1.5 dBTP |
| Album range above 2 LU | Inconsistent album | Re-master the outlier tracks |
| Tinniness above 0.6 | Harsh or tinny | High-mid cut of about `min((ratio − 0.5) × 6, 4)` dB at 3–5 kHz |
| Source peaks near 0 dBFS before mastering | Not enough headroom | Lower the mix by 3–6 dB first (gain only) |

Good result: integrated within ±0.5 LU of target, true peak between −1.0 and −1.5 dBTP, and less than 1 LU of spread across the album.

---

## The mastering chain

Apply the stages in this order. The values shown are the defaults, and each genre preset changes only the target loudness and the EQ cuts.

1. **DC/sub filter.** High-pass at 5 Hz to remove DC offset. Optionally add a sub-cut at 20–30 Hz for rumble.
2. **Low shelf** at 80 Hz (Q 0.7). Off by default. Use +1 dB at about 100 Hz if the bass feels thin after the high-mid cut.
3. **High-mid cut.** Peaking cut at **3.5 kHz, Q 1.5**, from 0 to −3 dB depending on the genre. This is the main fix for Suno brightness.
4. **High shelf** at **8 kHz** (Q 0.7). 0 by default. Use −1 dB for cymbal-wash genres.
5. *(Optional)* **Mid/side EQ.** Narrow the bass sides (shelf at 300 Hz) and widen the highs (shelf at 8 kHz). **Bass to mono** below about 120 Hz for club playback.
6. *(Optional)* **De-esser.** About 6.5 kHz center, 4 kHz detection band, −20 dB threshold, 4:1.
7. **Glue compression: 1.5:1, −18 dB threshold, 30 ms attack, 200 ms release.** This is gentle, with only 1–2 dB of gain reduction. Heavier genres can go to 2–2.5:1 with a −15 dB threshold and 10–15 ms attack. Ambient goes to about 1.2:1, and classical bypasses it. Parallel blends (wet/dry) and 3-band multiband (crossovers at 200 Hz and 5 kHz, 1.5:1 per band) are options, not defaults.
8. **Gain to target.** Measure integrated LUFS and apply the difference.
9. **True-peak limiter** with a −1.0 dBTP ceiling (−1.5 for dense-transient genres), 5 ms look-ahead and 50 ms release. Oversample, or else verify true peak afterward.
10. **Sample-rate conversion** (only if the delivery rate differs), then a **final true-peak check**, because resampling can re-introduce sub-dB overs.
11. **Dither** (TPDF) when reducing bit depth. Write a 24-bit WAV.

---

## Workflow

1. **Pre-flight.**
   - Confirm every file is WAV. If there are only MP3s, ask for WAV re-downloads from Suno.
   - Check that sample rates and bit depths are consistent.
   - Confirm the files aren't already mastered, to avoid double-processing.
   - Confirm the track order is final and that the user has backups of the originals.
2. **Confirm the genre treatment.** Name the preset you plan to use ("this is filed as synthwave, so I'll use the synthwave preset"), and ask whether any tracks differ in style (for example, "track 5 is really a ballad"). Master the main batch with the album preset, then re-master the exceptions with their own preset.
3. **Analyze the sources.** Measure integrated LUFS, true peak, LRA, crest factor and tinniness for each track. Red flags:
   - tracks varying by more than 2 LU
   - true peak above 0 dBTP
   - integrated LUFS below −20 or above −8
4. **Run pre-master QC** against the thresholds in the QC section below. Fix FAILs at the source (re-polish or regenerate) before you master.
5. **Choose settings.** Start from the genre preset. Adjust only if the user hears a problem: still harsh → deeper cut (−3 dB); too dull → shallower cut (−1 dB).
6. **Preview.** Work out the gain each track needs and show it to the user before committing. A huge gain (+8 dB or more) warns of a track that won't hit target cleanly.
7. **Master** all tracks with the same chain in one pass.
8. **Verify.** Every track should be within ±0.5 LU of target, true peak at or below the ceiling, no clipping, and less than 1 LU of spread across the album.
9. **Run post-master QC**, plus two listening artifacts:
   - **Codec preview.** Encode each master to 128 kbps AAC and have the user listen on earbuds or car Bluetooth. Compressed playback exposes warbly sibilance, lost sub-bass and pumping that the full-resolution file hides. The decoded preview should not clip.
   - **Mono fold.** Sum to mono and compare band by band. A drop of more than 6 dB in any band is a hard fail (phase cancellation). Ambient and cinematic music that relies on wide-stereo effects may tolerate 8–10 dB. Have the user check the mono file on a phone or smart speaker for missing elements.
10. **Listening tests:**
    - Shuffle the album to check for volume jumps.
    - Check translation on studio headphones, monitors, a laptop or phone, a car and earbuds.
    - Listen to the whole album front to back to check for fatigue.
    - A/B against 2–3 commercial references in the genre at matched loudness.
11. **Hand off to release.** Report the targets, measured results and QC verdicts per track, and note which files are the final masters. See `references/release/release.md`.

### ffmpeg mastering (no DAW)

Treat this as a starting point, verify with a meter, and keep the source files unchanged.

```bash
# 1) Tone + glue: DC filter, -2 dB @3.5 kHz (Q 1.5), gentle 1.5:1 compression. Float intermediate.
ffmpeg -i mix.wav -af "highpass=f=5,equalizer=f=3500:t=q:w=1.5:g=-2,acompressor=threshold=-18dB:ratio=1.5:attack=30:release=200" -c:a pcm_f32le stage1.wav

# 2) Measure integrated loudness of stage1 (read the "I:" line)
ffmpeg -hide_banner -i stage1.wav -af ebur128 -f null - 2>&1 | grep -A1 "Integrated loudness"

# 3) Gain to target (+X dB = -14 - measured), limit on a 4x-oversampled signal, back to 44.1 kHz, 24-bit
ffmpeg -i stage1.wav -af "volume=4.5dB,aresample=176400,alimiter=limit=-1.5dB:attack=5:release=50:level=0,aresample=44100" -c:a pcm_s24le master.wav

# 4) Verify, then re-nudge the gain if the integrated reading landed more than 0.5 LU off target
ffmpeg -hide_banner -i master.wav -af ebur128=peak=true -f null - 2>&1 | tail -n 12
```
- `alimiter` is a sample-peak limiter. Oversampling around it approximates true-peak limiting, and a −1.5 dB limit usually lands at or below −1.0 dBTP. Always confirm with the meter.
- For a 48 kHz source, use `aresample=192000` and then `aresample=48000`.
- `level=0` stops alimiter's auto-gain.

**Alternative: two-pass `loudnorm`.**
1. Run `loudnorm=I=-14:TP=-1:LRA=11:print_format=json` and collect the measured values.
2. Run it again with `measured_I`, `measured_TP`, `measured_LRA`, `measured_thresh`, `offset` and `linear=true`, and add `-ar 44100`, because loudnorm resamples internally to 192 kHz.

Linear mode is a clean gain-plus-limiter. If the target can't be reached without breaching TP, or if the input LRA is above the `LRA` setting, loudnorm silently switches to dynamic compression. In that case, raise `LRA` to the measured value, or use the manual chain above.

**Other useful commands:**
```bash
# 16-bit delivery with TPDF dither
ffmpeg -i master.wav -af "aresample=osf=s16:dither_method=triangular" -c:a pcm_s16le master_16bit.wav
# Codec preview (listen on Bluetooth), then confirm the decoded preview's true peak stays at or below 0 dBTP
ffmpeg -i master.wav -c:a aac -b:a 128k master_preview.m4a
ffmpeg -hide_banner -i master_preview.m4a -af ebur128=peak=true -f null - 2>&1 | tail -n 4
```

---

## QC thresholds

| Check | PASS | WARN | FAIL |
|---|---|---|---|
| Format | 2-channel WAV with consistent rate and depth | Mono file | Wrong format or channel count |
| Mono-fold energy loss | < 1 dB | 1–3 dB | > 3 dB |
| Mono-fold per band (master) | < 6 dB drop | Loudness delta > 3 LU, vocal band (1–4 kHz) delta > 2 dB, or correlation < 0.3 | Any band drops > 6 dB (8–10 dB allowed for ambient/cinematic) |
| L/R phase correlation (windowed) | > 0.5 | 0 to 0.5 | < 0 (out of phase) |
| Clipping (≥ 3 consecutive samples at ≥ 0.99 FS) | 0 regions | 1–3 regions | More |
| True peak vs ceiling | Below 95% of the ceiling | Within 95% of the ceiling | Above the ceiling |
| Clicks (10 ms windows with peak/RMS > 6) | 0 | 1–3 | > 3 |
| Silence (below −60 dBFS) | — | Trailing > 3 s | Leading > 0.5 s (1.5 s for electronic intros that open with builds); internal gaps ≥ 0.5 s |
| Spectral balance | Balanced | Sub-bass (20–60 Hz) < 1%; tinniness > 0.8; highs (6–20 kHz) < 1% | — |
| Post-master tinniness | — | > 0.6 **and** up by more than 0.10 from the pre-master value | — |

**Relax the click detector** for genres whose sharp transients are intentional: use a ratio of 10 and fail only above 30 clicks. The genre table marks these with *. Treat tinniness as a warning only, because the mastering EQ exists to fix it.

---

## Problem-solving

| Problem | Likely cause | Fix |
|---|---|---|
| **Track won't reach target** (e.g. stuck at −18.5 LUFS with −3.2 dBTP) | High dynamic range, big transients hitting the limiter | Compress in steps before limiting: −12 dB / 2.5:1, then −10 / 3.5:1, then −8 / 5:1. Stop when you're within ±0.5 LU. Or accept −16 to −18 if the genre suits it. |
| **Still harsh after EQ** | Several resonances, or Suno's bright vocals and highs | Deepen the 3.5 kHz cut to −3 or −4 dB, or spread cuts at 2.5, 4 and 5.5 kHz. Check whether the harshness is in a single stem, and fix that in the mix instead. |
| **Bass thinner after mastering** | A high-mid cut lowers perceived bass | Use a smaller cut, or add a +1 dB low shelf at about 100 Hz |
| **Bass too loud or muddy** | Suno can over-generate low end | Sub-cut at 25–30 Hz, or cut −1 to −2 dB around 200–300 Hz. Hip-hop, EDM and reggae need strong bass, so don't thin them. |
| **Clips on streaming playback** | True peak too close to 0 | Set the ceiling to −1.5 dBTP (−2.0 for Amazon or very loud masters) |
| **Squashed / lifeless** | Over-compressed to hit the number | Master to −16 LUFS and lighten the glue compression |
| **Album inconsistent** | Tracks mastered separately, or different source character | Master the whole album in one pass. Re-master the outliers with adjusted targets. See the album section below. |
| **Corrupt or truncated output** | Interrupted processing or a full disk | Delete the file, free up space, and re-run |

**Loudness myths:**
- *Louder is better.* Platforms normalize, so extra loudness only costs dynamics.
- *−14 is too quiet.* Platforms turn quieter tracks up, or other tracks down to match.
- *Mastering fixes the mix.* It can't. Fix the mix first.
- *Every track should be identical LUFS.* Small variations (under 1 LU) give the album natural flow, and exact matching can feel robotic.
- *True peak can touch 0 dBTP.* That clips after AAC/MP3 encoding. Keep headroom.

---

## Album-level consistency

1. **Master the album together** with one chain and one preset family, treating the per-track genre exceptions separately.
2. **Pick an anchor track.** This is the most representative track: its loudness and tone sit near the album median, its LRA is near the genre's ideal (about 8 LU for pop, higher for dynamic genres), and its spectrum is close to a sensible reference curve. Master it first, then match the rest to it.

   A rough pop reference curve, as a share of spectral energy:

   | Band | Share |
   |---|---|
   | Sub 20–60 Hz | 8% |
   | Bass 60–250 Hz | 18% |
   | Low-mid 250–500 Hz | 20% |
   | Mid 500 Hz–2 kHz | 25% |
   | High-mid 2–6 kHz | 14% |
   | High 6–12 kHz | 10% |
   | Air 12–20 kHz | 5% |

3. **Coherence tolerances** relative to the anchor:
   - Loudest-section loudness (STL-95): within ±0.5 LU
   - Low-band (20–200 Hz) RMS: within ±2 dB
   - Vocal-band (1–4 kHz) RMS: within ±2 dB
   - No track's short-term loudness range under 1 LU
   - Fix outliers with per-track target nudges and, at most, a ±0.5 dB spectral tilt. Don't re-EQ everything.
4. **Album ceiling guard.** Compare each master to the **median** album loudness, not the mean, because one hot outlier drags the mean toward itself.
   - Above median + 2 LU by 0.5 LU or less: pull it down with plain gain. Plain gain never raises peaks, so it needs no re-limiting.
   - Above median + 2 LU by more than 0.5 LU: something upstream didn't converge, so re-master that track.
5. **Allow intentional variation.** A quiet interlude or ballad can sit 1–2 LU under the album. Do it on purpose and keep it under 2 LU unless the user wants more contrast.
6. **Sequencing.** The default spacing is about 1.5 s between tracks, with a 100 ms fade on each tail and a 50 ms fade on each head. Gapless albums get 0 s and no fades. Distributors ingest tracks one at a time, so continuous playback depends on gapless support.
7. **Record what shipped.** For each track, note the target LUFS, ceiling, preset, anchor track and any overrides. Later bonus tracks or regenerated songs for a released album should be mastered against those recorded targets, not re-derived, so the catalog doesn't drift.

---

## Reference mastering

To match a commercial sound, compare against a professionally mastered reference in the **same genre** with similar instrumentation. Matching tools such as Matchering (Python), Ozone's Match EQ, or a manual A/B at matched loudness all work on the same idea: analyze the reference's frequency response and loudness, then match the track to it.

- **Legal sources:** CDs or purchases the user owns, and lossless Bandcamp downloads.
- **Not usable:** YouTube rips (lossy), streams (DRM), or pirated files.
- **Choosing a reference:** avoid loudness-war masters if the user wants dynamics. The reference should represent the target sound, not just any professional master.

Use reference mastering when the user wants a specific sound, is starting a new genre, or needs to match an existing catalog. Don't use genre presets on top of a reference match. Don't re-master files that are already mastered.

---

## Final checklist

- [ ] Sources are WAV, consistent in rate and depth, not already mastered, with peaks around −3 to −6 dBFS
- [ ] Genre preset confirmed with the user; per-track exceptions noted
- [ ] Pre-master QC: no FAILs
- [ ] Integrated loudness at target ±0.5 LU for every track (−14 unless the genre or user says otherwise)
- [ ] True peak at or below −1.0 dBTP (−1.5 for dense-transient genres; −2.0 if Amazon matters)
- [ ] Album spread under 1 LU; no track above median + 2 LU
- [ ] No clipping, clicks, truncation or unexpected silence; fades correct
- [ ] Mono fold and 128k AAC preview checked by ear
- [ ] Shuffle, translation, fatigue and reference tests passed
- [ ] Originals preserved; final masters clearly identified; settings recorded

---

## Genre presets (compact)

Use this legend to read the table:

| Column / mark | Meaning |
|---|---|
| **LUFS** | Streaming target. Variants for subgenres are in parentheses. |
| **Dyn** | Glue compression feel. **Min** = bypass or ≤ 1.2:1. **L** = light, about 1.2–1.5:1. **M** = moderate, 1.5–2:1. **H** = heavy, 2–3:1 with faster attack. Combined grades such as L–M or M–H sit between. |
| **HM** | High-mid peaking cut at 3.5 kHz, Q 1.5 |
| **HS** | High-shelf cut at 8 kHz, listed only when it isn't 0 |
| **†** | Use a −1.5 dBTP ceiling |
| **\*** | Relax the click QC (ratio 10, fail above 30) |
| **‡** | Allow 1.5 s of quiet lead-in |
| **k** | kHz |

Everything not listed uses the default chain above. Where a genre's own convention runs louder than its streaming target (for example, rock and hip-hop are often −12 to −14), stay at the streaming target unless the user asks.

### Pop & mainstream
| Genre(s) | LUFS | Dyn | EQ focus | Notes |
|---|---|---|---|---|
| pop, k-pop, synth-pop, bubblegum-pop, sophisti-pop | −14 | M | HM −1; vox 2–5k; sparkle 10k+ | Bright and radio-ready. K-pop is crisp and vocal-forward. |
| electropop | −14 (club −12, dark −15) | M–H | HM −1; vox 2–5k; pads 200–600; sub 40–80 | Keep synth sparkle |
| j-pop, anisong | −14 | M–H | HM −1; vox 2–6k; synth/guitar 1–4k; bass 60–100; air 10–14k | Dense; separate the competing layers |
| city-pop, kayokyoku | −14 | L–M / M | HM −1; bass 60–200; vox 2–4k; shimmer 4–8k | Warm, analog, vintage air |
| mandopop, cantopop, thai-pop, trot | −14 | M | HM −1; vox 2–5k; keys 200–500; strings 300–600 | Vocal sweetness first |
| art-pop, piano-pop | −14 | M | HM −1; vox 2–5k; piano body 200–600, attack 2–4k | Headroom for unusual arrangements |
| hyperpop\*, noise-pop\* | −14 | M | HM −1.5; vox 2–5k; noise 800–3k | Tame aggressive brightness; keep the noise/sweet contrast |
| twee-pop, jangle-pop | −14 | M | HM −1.5; chime 2–6k; sparkle 8–12k | Ringing guitars need headroom |
| turkish-pop, laiko | −14 | M | HM −1.5; vox 1–4k; saz/bouzouki 2–6k; darbuka 3–5k | Keep melisma |
| dream-pop, baroque-pop, chamber-pop | −16 | L | HM −1 | Reverb and orchestral room |
| enka | −16 | L | HM −1; vox 1–4k; shamisen/koto 2–6k; strings 200–600 | Kobushi ornaments need headroom |

### Hip-hop & rap
| Genre(s) | LUFS | Dyn | EQ focus | Notes |
|---|---|---|---|---|
| hip-hop, rap, east-coast-hip-hop, west-coast-rap, southern-hip-hop, gangsta-rap, underground-hip-hop, mumble-rap, pop-rap, chicano-rap, g-funk, bounce, nerdcore, christian-hip-hop | −14 (convention −12 to −14) | M, punchy | HM −1; sub 40–60; vox 2–4k | Strong low end, clear vocal, punchy kick and snare |
| boom-bap | −14 | M | HM −1; kick 60–100; snare 200–1k; vox 2–5k | Keep the dusty sampled drums; don't over-clean |
| cloud-rap, plugg | −14 | L–M | HM −1; vox 2–5k; pads 200–600; sub 30–60; shimmer 8–12k | Airy and spacious |
| conscious-hip-hop, jazz-rap, abstract-hip-hop | −14 | M | HM −1; vox 2–5k; sample warmth 200–600; bass 60–150 | Every word heard |
| trap\*†, drill\*, latin-trap | −14 | M | HM −1; 808 40–80; vox 2–5k; hats 8–12k | — |
| phonk\*, grime, horrorcore, emo-rap, country-rap | −14 | M | HM −1.5; bass 40–100; vox 2–5k | Phonk warm and lo-fi; grime punchy |
| crunk\* | −12 | H | HM −1.5 | Loud club energy |
| chopped-and-screwed | −16 | L | HM −1 | Slowed; leave room |

### R&B, soul & funk
| Genre(s) | LUFS | Dyn | EQ focus | Notes |
|---|---|---|---|---|
| r&b / rnb, soul, gospel, neo-soul, motown, northern-soul, psychedelic-soul | −14 (neo-soul optionally −16) | L–M to M | HM −1.5; vox 2–5k; bass 60–150; keys 200–600; tambourine 6–10k | Warm. Gospel needs choir clarity. Psych soul keeps its effects. |
| funk, p-funk | −14 | M | HM −1.5; bass 40–150; horns 1–4k; perc 3–6k | Punchy groove; the low end is the foundation |
| disco, nu-disco (cosmic −15), boogie, post-disco, new-jack-swing | −14 | M | HM −1; bass 60–200; kick 60–100; hats 8–12k | Bright but not harsh |
| alternative-rnb, trap-soul | −14 | L–M | HM −1; vox 2–5k; 808 40–100; shimmer | Intimate detail |
| doo-wop | −14 | L–M | HM −1; vocal group 2–5k; bass voice 80–200 | Keep the room sound |
| quiet-storm | −16 | L | HM −1; vox 2–4k; bass 60–150 | Late-night warmth |

### Rock
| Genre(s) | LUFS | Dyn | EQ focus | Notes |
|---|---|---|---|---|
| rock, grunge | −14 (convention −12 to −14) | Preserve peaks | HM −2.5; guitar 800–3k; avoid harsh highs | Guitar energy and drum impact |
| stoner-rock | −14 (stoner doom −16) | M | HM −2.5 (−2 to −2.5 max); low body 60–200; fuzz 800–3k | Fuzz overtones are the tone; warm master |
| indie-rock, alternative, garage-rock, arena-rock, heartland-rock, indie | −14 | M (arena M–H) | HM −2; guitar 800–3k; vox 2–5k | Arena: big drums and room |
| surf-rock, britpop, madchester, post-britpop, piano-rock, rockabilly | −14 | M | HM −1.5; vox 2–5k; guitar body 800–2k | Rockabilly slap at 80–200 plus 2–4k |
| math-rock | −14 (Japanese/atmospheric −15) | M | HM −1.5; guitar 1–4k; drums 3–5k | Keep the stop-start transients |
| psychobilly | −14 | M–H | HM −2; slap bass 60–200 plus 2–4k | — |
| psychedelic-rock, progressive-rock, post-rock, space-rock, jam-band | −16 | L | HM −1.5 | Builds and jams need room; don't push louder |
| krautrock, canterbury-scene, slowcore | −16 | L | HM −1 | Motorik and hypnotic; restraint |
| noise-rock\* | −14 (sludge-noise −12, art-noise −15) | Min | HM −2.5 (gentle); low body 60–200 | Harshness and feedback are intentional |

### Punk
| Genre(s) | LUFS | Dyn | EQ focus | Notes |
|---|---|---|---|---|
| punk†, pop-punk, ska-punk, celtic-punk, emo, riot-grrrl, oi | −14 | M | HM −2; vox 2–5k; guitar 800–2k; bass 80–200 | Raw but listenable. Lo-fi punk can take a −1 cut. |
| hardcore-punk\*, screamo | −14 | M–H | HM −2.5 | Keep the quiet/scream contrast |
| crust-punk\*, d-beat\*, powerviolence\* | −14 (neocrust −15) | M–H to H | HM −2.5, HS −1; low 40–200 | Tame blast-beat cymbal wash |
| no-wave | −14 | Min | HM −2.5, HS −1 | Abrasion is the point |
| post-punk (gothic −15), post-punk-revival, dance-punk | −14 | M | HM −1.5; bass 80–300; guitar 800–3k | Bass is the melodic center; reverb and delay are compositional |

### Metal
| Genre(s) | LUFS | Dyn | EQ focus | Notes |
|---|---|---|---|---|
| metal\*†, thrash-metal\*, metalcore\*, groove-metal\*, speed-metal\* | −14 | H | HM −3; low 60–200; vox 1–4k | Controlled aggression, not mush |
| death-metal\*, black-metal\*, deathcore\*, grindcore\* | −14 | H | HM −3, HS −1; low 40–200 | Cymbal wash causes fatigue. Raw black metal fans may prefer −1.5. |
| melodic-death-metal | −14 | H | HM −2.5, HS −1; melody 1–4k | — |
| nu-metal, doom-metal, power-metal, folk-metal, sludge-metal, nwobhm, viking-metal, crossover-thrash, trap-metal | −14 | M to H | HM −2.5; low 60–200; vox 2–5k | Nu-metal's scooped mids are intentional. Folk metal instruments sit at 1–6k. |
| djent\*, industrial\*† | −14 | M–H | HM −2.5; palm mute 800–3k; snare/ghosts 3–6k | Industrial is harsh by design |
| symphonic-metal, progressive-metal, hair-metal, visual-kei, christian-rock | −14 | M to M–H | HM −2; orchestra/keys 200–600; vox 2–5k | Prog: preserve the clean/heavy range |
| blackgaze, drone-metal, post-metal | −16 | L to L–M | HM −2 | Wash and sustain; keep the dynamic arc |

### Electronic & dance
| Genre(s) | LUFS | Dyn | EQ focus | Notes |
|---|---|---|---|---|
| edm\*†‡, electronic\*‡ | −14 (club convention −10 to −12) | H, consistent | HM −1; sub 30–50; sparkle 10k+ | For vinyl, go about 2 LU louder |
| house, tech-house, deep-house, french-house, vocal-house, future-house, lo-fi-house, afro-house, bass-house\* | −14 | M (deep house L–M; bass-house M–H) | HM −1; kick 40–80; bass 80–200; perc 2–5k | Rolling groove. Deep house keeps the air up top. |
| progressive-house (deep prog −15), trance, vocal-trance, goa-trance, psychedelic-trance | −14 | L–M | HM −1; pads 200–600; leads 1–4k; sub 40–80 | Breakdown-to-peak arcs need room |
| techno\*, minimal-techno, deep-techno | −14 | M / L–M | HM −1; kick 40–80; hats 8–12k | Power comes from micro-variation |
| eurodance, electroswing, future-bass, tropical-house, nightcore, complextro, moombahton, future-funk, italo-disco, jersey-club, baile-funk, electro, dancehall | −14 | M (tropical L) | HM −1; kick/808 40–100; leads 1–8k; hats 8–12k | Keep the sidechain pump and build dynamics |
| uk-garage, 2-step-garage, bassline, speed-garage, uk-funky, broken-beat | −14 | M | HM −1; bass 60–150; vox 2–5k; hats 8–12k | Keep the shuffled swing |
| drum-and-bass\*†, jungle\*, breakbeat\*, neurofunk\*, footwork\*, riddim\*, glitch-hop\*, glitch-pop\*, pc-music\* | −14 (big beat −12) | M | HM −1.5; sub 30–60; breaks 2–5k | Chopped breaks keep their punch |
| dubstep\*†, brostep | −14 | H | HM −1.5; growl 100–500; sub 30–60 | Drops must hit |
| synthwave, new-wave, darkwave, ebm, darksynth, hardwave, cyberpunk | −14 | M | HM −1.5; synth 1–4k; bass 40–100 | Retro brightness without harshness |
| dark-electro | −14 | M–H | HM −2; synth bass 60–200 | Weight and menace |
| hardstyle\*†, gabber\*, happy-hardcore\* | −12 (peak-time −10) | H | HM −2; kick 40–200; leads 1–4k | Intentionally loud |
| speedcore\* | −12 | H | HM −2, HS −1 | — |
| breakcore\*, chiptune\* | −14 | M | HM −2, HS −1 | — |
| glitch\*, deconstructed-club | −14 | M | HM −1.5, HS −1 | Glitches are intentional |
| rave, dembow, reggaeton | −12 (perreo −10) | H | HM −1.5; kick 40–100; bass 40–80; vox 2–5k | Built for big systems |
| guaracha | −12 | H | HM −1; kick 40–80; tribal perc 3–8k | — |
| post-dubstep, space-disco, wave, dub-techno, witch-house, folktronica, balearic | −16 | L to L–M | HM −1 | Texture and mood over impact |
| gqom, benga, gengetone, dangdut | −14 | M | HM −1.5; bass 40–100; perc 3–8k | Raw, minimal energy |
| coupe-decale, kuduro, kwaito, amapiano | −14 | M | HM −1; amapiano log drums 200–600; bass 60–150 | Laid-back bounce |

### Ambient & atmospheric
| Genre(s) | LUFS | Dyn | EQ focus | Notes |
|---|---|---|---|---|
| ambient, chillwave, vaporwave, downtempo, new-age, psybient, lounge | −16 | L / Min | HM −1; pads 200–600; gentle air | Spacious |
| shoegaze | −16 | L–M | HM −1.5 | Wall of sound |
| lo-fi / lofi | −14 | L | HM −1 (often none) | Warm and nostalgic |
| trip-hop | −14 | M | HM −1.5 | Dark and moody |
| idm\* | −14 | M | HM −1; micro-transients 3–8k; bass 40–100 | Artifacts are intentional |
| dark-ambient, drone, electroacoustic | −18 | Min | None; full spectrum; low body 20–200 | Minimal intervention |
| dungeon-synth | −18 | Min | HM −1; high-frequency rolloff | Keep the tape hiss |

### Folk, country & roots
| Genre(s) | LUFS | Dyn | EQ focus | Notes |
|---|---|---|---|---|
| folk, country, americana, indie-folk, outlaw-country, honky-tonk, red-dirt, bakersfield-sound, neotraditional-country | −14 (folk can sit −16; country convention −13) | Folk natural; country M | HM −2; vox 2–5k; warmth 200–500; steel 3–6k | Twangy guitars need taming. Live/raw recordings can take −2.5. |
| bluegrass, zydeco, bro-country, western-swing, cajun, swamp-pop, celtic, norteno | −14 | M | HM −1.5; accordion/fiddle 800–3k (zydeco rubboard 4–8k) | — |
| cowpunk | −14 | M–H | HM −2.5 | — |
| singer-songwriter | −16 | L | HM −1.5; vox 2–4k; sibilance 6–8k | Intimacy |
| polka | −14 | M | HM −1; accordion 800–3k; tuba 60–150 | — |

### Jazz & blues
| Genre(s) | LUFS | Dyn | EQ focus | Notes |
|---|---|---|---|---|
| jazz, bebop, cool-jazz, hard-bop, modal-jazz, gypsy-jazz, vocal-jazz, bossa-nova | −16 | L | None; horns 1–4k; ride/brush 6–12k | Natural dynamics; purists want no EQ |
| dark-jazz | −18 | Min | None | Nocturnal; very wide dynamics |
| big-band, delta-blues, piano-blues | −16 | M / L | HM −1 | Room ambience |
| swing, acid-jazz, jazz-fusion, smooth-jazz, nu-jazz, ethio-jazz, latin-jazz, soul-jazz, desert-blues | −14 | M | HM −1 | Watch brass brightness above 4 kHz |
| blues | −14 | M | HM −1.5 | Warm, classic tone |

### Classical, cinematic, stage & vocal
| Genre(s) | LUFS | Dyn | EQ focus | Notes |
|---|---|---|---|---|
| classical, opera, medieval, madrigal, gregorian-chant, choir | −18 | Min | None | Never compress classical; the reverb is the instrument |
| cinematic | −16 | L | None | Film-scoring dynamics |
| musicals, musical-theater, broadway, ragtime, spaghetti-western | −16 (rock musicals −14) | Wide | HM −1; vox 1–4k | Ballads stay quiet, showstoppers soar |
| soundtrack, film-theme, title-song | −14 (power ballad −13, intimate −15) | M | HM −1; vox 2–5k; orchestra 200–600 | Vocal always forward |
| musical-comedy, video-game-music, schlager | −14 (schlager party −11 to −12) | M / M–H | HM −1 | Comedy: every word heard |
| chanson, cabaret | −15 (modern/dark −14, traditional −16) | L / L–M | HM −1.5; chanson gentle high cut above 12k | Rubato and theatrical range |
| dark-cabaret | −14 | M | HM −1.5 | — |
| a-cappella, barbershop | −16 | L | HM −1; harmonies 1–5k; ring 2–6k | — |
| isicathamiya, throat-singing | −16 | Min / L | None | Keep the overtones |
| beatboxing | −14 | M | HM −1 | — |
| vocaloid | −14 | M | HM −1.5 | Tame digital harshness |
| spoken-word | −14 | L | None; rumble removal; sibilance 6–8k | The voice is everything |

### World
| Genre(s) | LUFS | Dyn | EQ focus | Notes |
|---|---|---|---|---|
| middle-eastern-pop, arabic-pop, rai, mizrahi, dabke, shaabi, gnawa, turbo-folk, manele | −14 | M (gnawa L–M) | HM −1.5; vox 1–4k; oud/qanun 200–600; darbuka 3–5k | Keep the ornamentation |
| mahraganat | −12 | H | HM −2 | Bass-forward |
| sufi, fado (novo −15), flamenco (nuevo −14), rebetiko, sevdah, morna | −16 | L | HM −1 | Dynamic vulnerability |
| klezmer | −14 | M | HM −1.5 | — |
| bollywood (filmi −15, item −13), bhangra, qawwali | −14 | M / M–H / L–M | HM −1.5; vox 2–5k; dhol 60–200; tabla 3–5k | Keep the meend and taan |
| chutney | −14 | M | HM −1 | — |
| ghazal | −16 | L | HM −1 | — |
| hindustani, carnatic, indian-classical | −18 | Min | None | The structure *is* the dynamics |
| latin, cumbia, samba, bachata, mambo, merengue, son-cubano, afro-cuban, boogaloo, corridos-tumbados, tejano, vallenato, axe, forro, mpb, pagode, calypso, mento, kompa, champeta, punta | −14 | M (mpb, mento L–M) | HM −1 | Keep the clave and percussion interplay |
| soca | −14 (power soca −12) | M–H | HM −1 | — |
| tropicalia, chicha, huayno, ranchera, mariachi, banda | −14 | M | HM −1.5; trumpet 1–4k | — |
| reggae, roots-reggae, lovers-rock, rocksteady, ragga, ska, dub | −14 | M (dub L–M) | HM −1.5; bass 40–200 | Dub: echo space and an analog top-end rolloff |
| bolero, tango (nuevo −15, electrotango −14) | −16 | L | HM −1 | — |
| afrobeats, afropop, afroswing, highlife, soukous, juju, fuji, mbalax, chimurenga, mbaqanga, maskandi, bongo-flava, sega, semba, zouk | −14 | M | HM −1; guitar 800–4k; perc 3–8k | — |
| kizomba | −14 | L–M | HM −1 | — |
| taarab | −16 | L | HM −1 | — |

### Faith, family & other
| Genre(s) | LUFS | Dyn | EQ focus | Notes |
|---|---|---|---|---|
| contemporary-christian / ccm, worship, praise | −14 (devotional −15, anthemic −13) | M | HM −1.5; vox 2–5k; pads 200–500 | Keep the swells |
| childrens-music, kinderlieder | −14 | L | HM −1.5; vox 2–4k | Consistent level for car and classroom playback |
| lullaby | −16 | Min | HM −1 | — |
| go-go, sea-shanties, music-hall | −14 | M | HM −1.5 | — |

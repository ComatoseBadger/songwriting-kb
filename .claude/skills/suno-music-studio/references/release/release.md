# Release: Readiness, Distribution, Metadata, Rights

Use this when mastered audio and cover art exist and the user wants the music on SoundCloud, Bandcamp or streaming services. It covers the release QA gate, choosing a distributor, platform-by-platform metadata, AI-music rights and disclosure, claims, timing, and catalog or bulk releases. A short appendix covers publishing sheet music.

> **Platform policies, prices, limits and AI rules change often.** Treat every number, price and policy below as a snapshot. Before the user submits anything, tell them to check the distributor's and platform's current help pages and terms, especially the AI-content rules and Suno's current Terms of Service.

If the user has stated release preferences (platform order, artist-name casing, tags to always include, extra QA checks, days between uploads), follow them. Do not drop the core QA gate, though. Preferences can add checks or reorder platforms. They cannot skip the rights, audio or metadata checks.

Related: `references/production/mastering.md` (loudness targets), `references/album/art.md` (cover art), `references/lyrics/compliance.md` (lyric and content screening), `references/release/promotion.md` (campaign copy and promo video).

---

## 1. Release Types and Timelines

| Type | Use for | Mastering to live |
|------|---------|-------------------|
| **Quick** | Demos, tests, non-commercial. SoundCloud and/or Bandcamp only | Same day |
| **Standard** | Commercial release with wide streaming distribution | 1–2 weeks |
| **Strategic** | A major release with a pre-save and a teaser campaign | 4–6 weeks |

**Quick (same day):** QA (0–2 h) → SoundCloud/Bandcamp upload (2–3 h) → verify.

**Standard (1–2 weeks):**
- Day 0: QA and distribution prep
- Day 1: distributor submission, SoundCloud and Bandcamp upload
- Days 4–10: distributor and store approval
- Day 10: verify every platform, then start the campaign

**Strategic (4–6 weeks):**
- Week 0: QA
- Week 1: distribution prep
- Week 2: submit to the distributor with a future release date and set up the pre-save
- Weeks 2–4: teaser campaign
- Week 4: approval confirmed and editorial pitch sent (Spotify needs it 4+ weeks ahead)
- Weeks 5–6: release and full campaign

---

## 2. Release Readiness Checklist (QA Gate)

Every item must pass before anything is uploaded. If one fails, fix it and run the whole list again.

### Audio
- [ ] Every track plays end to end, with no corruption, clicks or truncation
- [ ] Mastered to the target loudness: about −14 LUFS integrated ±0.5 dB for streaming, true peak below −1.0 dBTP (see `references/production/mastering.md`)
- [ ] Album loudness range across tracks under 1 LU
- [ ] No more than about 3 s of silence at the start or end of any track (a common rejection reason)
- [ ] Delivery format is lossless WAV/FLAC at 44.1 kHz or higher, 16- or 24-bit. Suno Studio exports at 48 kHz / 32-bit float are accepted
- [ ] File names are consistent and in order (`01-track-name.wav`)
- [ ] Track count matches the metadata

### Rights (AI-specific; re-verify against the current Suno terms)
- [ ] Every track's audio is a permitted download made on a **paid** Suno plan. Free or trial downloads are for personal use only and carry no commercial rights
- [ ] No track is a Suno Remix of another user's song. Those are never cleared for commercial use
- [ ] Nothing in the chain removes, alters or hides Suno's audio watermark, fingerprint or embedded metadata. That is prohibited by Suno's terms, and mastering or mixing must never be described as doing it
- [ ] The chosen distributor accepts tracks from the Suno model family used. Some distributors (Believe/TuneCore were reported this way) accept only tracks made on the current model family. Check before submitting
- [ ] No samples, interpolations or covers of other people's work, unless they are licensed (see §7)
- [ ] The creative process is documented: prompts, lyric drafts, selections, edits. This is your evidence if a claim comes in

### Metadata
- [ ] Album title under about 50 characters and track titles under about 40 (to avoid truncation)
- [ ] Artist name spelled and cased the same way everywhere
- [ ] Featured artists go in the featured-artist field, never in the title
- [ ] Version info ("Remix", "Live", "Acoustic") goes in the version field, not the title
- [ ] Primary and secondary genre and any subgenre chosen from the distributor's list
- [ ] Copyright (©) and phonographic (℗) year and holder filled in
- [ ] Lyrics language set
- [ ] Release date decided. Many distributors won't let you change it after submission
- [ ] Track order confirmed

### Lyrics and content
- [ ] Streaming lyrics prepared for each vocal track in the format in §3
- [ ] The explicit flag is set per track and matches the lyrics (§3)
- [ ] Lyrics screened for content and similarity issues (`references/lyrics/compliance.md`)
- [ ] If the album is based on real events, the sources are verified

### Artwork
- [ ] 3000×3000 px, square, RGB, JPG (Apple prefers JPG) or PNG
- [ ] Sharp, not upscaled mush, and readable as a 300×300 thumbnail
- [ ] No URLs, social handles, QR codes, prices or platform logos
- [ ] If the art is explicit, the release is flagged explicit
- [ ] Art is original, licensed or AI-generated by the user (see `references/album/art.md`)

### Promo (optional but recommended)
- [ ] Platform copy drafted and reviewed (`references/release/promotion.md`)
- [ ] `[Streaming Link]` placeholders listed so they can be filled in once the release is live

---

## 3. Streaming Lyrics and Explicit Content

### Streaming lyrics format (Spotify, Apple Music, Amazon, and most distributors)

Write these from the final sung lyrics. **Never paste Suno-prompt lyrics.** They contain phonetic respellings, meta tags and performance cues meant for the model.

- Lyrics only. No `[Verse]`/`[Chorus]` labels, no vocalist names, no performance notes
- Write every repeat out in full. Never use "x2" or "(repeat chorus)"
- Capitalise the first letter of each line
- No punctuation at the end of a line
- Use blank lines only between sections
- Don't censor explicit words. Set the explicit flag instead
- The lyrics must match what is actually sung, including ad-libs that are clearly sung

Platform formats: Spotify, Apple and Amazon take plain text, and timed (synced) lyrics are optional where offered. YouTube captions use SRT/VTT subtitles.

### Explicit flag

Set **Explicit = Yes** for any of these, including their variants and compounds:

| Category | Words |
|----------|-------|
| F-word | fuck, fucking, fucked, fucker, motherfucker |
| S-word | shit, shitty, bullshit |
| Other profanity | bitch, cunt, cock, dick, pussy, asshole, goddamn/goddammit |
| Slurs | any slur (racial, homophobic, misogynistic: whore, slut, etc.) |

These are usually **clean**: damn, hell, crap, ass, bastard, piss. "Damn" is clean, but "goddamn" is explicit.

Also flag tracks with graphic sexual content, graphic violence or drug-use glorification, even if no listed word appears. Check every track, report each match with its track name and count, and flag any mismatch in either direction. A track that is explicit but flagged clean gets rejected or pulled. A clean track flagged explicit is hidden from filtered accounts.

---

## 4. Choosing a Distributor

Spotify, Apple Music, Amazon, Tidal, Deezer, TikTok/Instagram libraries and most other stores accept music only through a distributor. SoundCloud, Bandcamp and YouTube accept direct uploads.

### Snapshot comparison (verify current pricing and tiers)

| Distributor | Pricing model | Revenue to artist | Stays live if you stop paying? | Best for |
|-------------|---------------|-------------------|-------------------------------|----------|
| **DistroKid** | Annual subscription, unlimited releases (~$23/yr base; higher tiers ~$40 and ~$80) | 100% | No, unless you pay the "Leave a Legacy" add-on | Frequent releasers, singles, experimenting |
| **TuneCore** | Historically per release (~$10 single / ~$30 album per year). Now offers subscription tiers, so verify | 100% | No, needs renewal | Selective releases, publishing admin |
| **CD Baby** | One-time fee per release (~$10 single / ~$30–50 album) | ~91% | Yes | "Finished" catalog, sync, no recurring fees |
| **Ditto Music** | Annual subscription, unlimited | 100% | No | Budget unlimited releases, UK/EU artists |

| Feature | DistroKid | TuneCore | CD Baby | Ditto |
|---------|-----------|----------|---------|-------|
| YouTube Content ID | Paid add-on per song | Included | Pro tier | Included |
| Spotify/Apple artist tools, lyrics, Shazam | Yes | Yes | Yes | Yes |
| Split payments to collaborators | Yes | No | Yes | Yes |
| Pre-save pages | Yes | Yes | Yes | Yes |
| Sync licensing | No | Pro tier | Pro tier | No |
| Publishing administration | No | Publishing tier | Pro tier | No |
| Cover licensing | Add-on (Easy Song Licensing) | Add-on (HFA) | Add-on (Songfile) | Third party |

All four deliver to roughly 150+ stores. That covers the major streamers (Spotify, Apple, Amazon, YouTube Music, Tidal, Deezer, Pandora), social libraries (TikTok, Instagram/Facebook, Snapchat), download stores (iTunes, Amazon) and some regional services (Tencent, NetEase, JioSaavn, Anghami, depending on the distributor).

### Processing time
Distributor approval usually takes 1–3 days (CD Baby 2–5). Most offer a paid rush option. The stores then add another 1–7 days, and Apple can take up to 14. Plan on at least 1–2 weeks. If there is a pre-save or editorial pitch, plan on 4+ weeks.

### AI-music acceptance (check this first)
Distributors differ on AI content and change their rules often. Before recommending one, have the user check its current AI policy for: whether fully AI-generated audio is accepted, any disclosure checkbox, model or tool restrictions (some accept only current-generation Suno output), and volume limits or anti-spam rules. Releasing very large numbers of near-identical tracks can get an account flagged or terminated.

### Quick decision guide

| Situation | Suggest |
|-----------|---------|
| First release, or experimenting | DistroKid base tier |
| 10+ releases a year | DistroKid mid tier (includes Content ID and a custom release date) |
| One or two albums total, no subscription wanted | CD Baby Standard |
| Interested in sync or publishing admin | CD Baby Pro or a TuneCore publishing tier |
| Budget, international, EU-based | Ditto |

### Cover songs
A cover needs a mechanical licence, usually around $12–15 per song plus per-stream royalties, arranged through the distributor's add-on. Original compositions made with AI need no cover licence. A track that recreates an existing song's melody or lyrics is a cover, or worse, and is not "original".

### Switching distributors
You can switch, but a re-upload gets new ISRCs. The algorithms then treat it as a new song, and stream counts and playlist placements are lost unless the new distributor reuses the old ISRCs. If switching, keep the old release live until the new one is approved and overlap them by 2+ weeks. Don't switch for minor reasons.

---

## 5. Platforms

### Overview

| Platform | Upload | Monetisation | Strength |
|----------|--------|--------------|----------|
| SoundCloud | Direct | Fan-powered royalties, Pro | Instant release, DJ/remix and electronic/hip-hop communities |
| Spotify | Distributor only | Pro-rata stream pool | Largest audience, playlists, algorithmic discovery |
| Apple Music | Distributor only | Per stream (pays more than Spotify) | Quality-focused listeners, strict metadata |
| YouTube Music | Distributor (Art Tracks) or direct video | Ads and Premium | Search, video, developing markets |
| Bandcamp | Direct | Direct sales, roughly 82–85% to artist | Superfans, downloads, pay-what-you-want, fee-free "Bandcamp Fridays" |

Rough per-stream figures (they vary by country and subscription): Apple about $0.007–0.01, Spotify about $0.003–0.005, SoundCloud about $0.002–0.005, YouTube about $0.002–0.004.

| Feature | SoundCloud | Spotify | Apple | YouTube Music | Bandcamp |
|---------|-----------|---------|-------|---------------|----------|
| Lyrics display | No | Yes | Yes | Yes | Optional |
| Pre-save | No | Via distributor | Via distributor | No | No |
| Download sales | Pro | No | No | No | Yes |
| Pay-what-you-want | No | No | No | No | Yes |
| Analytics | Pro | Yes | Yes | Yes | Yes |

### Upload specs

| Platform | Audio | Art | Notes |
|----------|-------|-----|-------|
| SoundCloud | WAV, FLAC, AIFF, or MP3 at 320 kbps+ | 800×800 min, JPG/PNG, ≤2 MB recommended | Free accounts have upload-size and time limits, so check the current tier. Up to 5 tags. Live within minutes |
| Spotify (via distributor) | WAV/FLAC, 16-bit/44.1 kHz min | 3000×3000, JPG/PNG | ISRC per track and UPC per release (the distributor issues both) |
| Apple Music (via distributor) | WAV/AIFF, 24-bit preferred | 3000×3000, RGB, JPG preferred | Strictest formatting; 3–14 days |
| YouTube Music | WAV, FLAC or high-quality MP3 | Art Track works; 2048×2048 or larger | Hours if uploaded direct, days via a distributor |
| Bandcamp | Lossless only (WAV, FLAC, AIFF) | 1400×1400 min, 3000×3000 recommended | Instant. Set your own price, free, or pay-what-you-want |

### Suggested platform order

- **Quick or demo:** SoundCloud first, Bandcamp the same day, distributor the next day if wanted.
- **Standard:** distributor, SoundCloud and Bandcamp all on day 1. Wait 3–14 days for the stores, then verify.
- **Maximum reach:** distributor for all stores, SoundCloud for direct engagement, Bandcamp for superfans, and YouTube with a visualizer or lyric video.

Tips:
- Spotify: pitch to editorial through Spotify for Artists 4+ weeks ahead, verify the artist profile, and add a Canvas loop.
- Apple Music: clean formatting is critical. Most rejections are about formatting.
- SoundCloud: tags drive discovery, and reposts and groups help.
- YouTube: lyric videos and visualizers drive engagement.
- Bandcamp: add bonus content (stems, lyric booklet, sheet music) to reward buyers.

---

## 6. Metadata by Platform

### Title limits

| Platform | Album title max | Notes |
|----------|-----------------|-------|
| Spotify | 200 | Avoid special characters |
| Apple Music | 255 | Clean formatting is enforced |
| YouTube Music | 100 | Display truncates early |
| SoundCloud | 100 | |
| Bandcamp | ~200 | |
| Distributors | 100–200 | Varies, so check |

Track titles allow 100–200 characters but display at about 30–40. Keep album titles under 50 and track titles under 40.

### Required fields

| Field | Spotify | Apple | YouTube | SoundCloud | Bandcamp |
|-------|---------|-------|---------|------------|----------|
| Title / Artist / Genre | Yes | Yes | Yes | Yes | Yes |
| Release date | Yes | Yes | Yes | Optional | Optional |
| UPC | Via distributor | Via distributor | Via distributor | No | No |
| Copyright | Via distributor | Yes | Via distributor | Optional | Yes |
| Explicit flag | Yes | Yes | Yes | No | Optional |

Per track: title (no "feat." in it), primary artist, featured artist (as a separate field), sequential track number with no gaps, ISRC (issued by the distributor and unique per track), explicit flag, and lyrics (recommended).

### Description and bio limits

| Platform | Release description | Artist bio |
|----------|---------------------|------------|
| Spotify | None (bio only) | 1,500 |
| Apple Music | 4,000 (editorial notes) | 1,000 |
| YouTube | 5,000 | n/a |
| SoundCloud | 4,000 | 4,000 |
| Bandcamp | Unlimited | Unlimited |

### Artwork

| Platform | Min | Recommended | Max | Format | Max file |
|----------|-----|-------------|-----|--------|----------|
| Spotify | 640² | 3000² | 3000² | JPG/PNG | 20 MB |
| Apple Music | 3000² | 3000² | 4000² | JPG | 40 MB |
| YouTube Music | 1400² | 3000² | n/a | JPG/PNG | 20 MB |
| SoundCloud | 800² | 800²+ | 8000² | JPG/PNG | 2 MB |
| Bandcamp | 1400² | 3000² | n/a | JPG/PNG/GIF | 10 MB |

Use one 3000×3000 RGB JPG everywhere, and export a smaller copy under 2 MB for SoundCloud if needed. Allowed: original art, licensed images, AI-generated art (disclose where required), and the album title or artist name as text. Not allowed: blurry or pixelated images, heavy text, contact info, URLs or QR codes, platform logos, explicit imagery without the flag, or infringing content.

### Genre and tags
- Spotify and Apple pick genres from a fixed dropdown, and Apple is strict about it. YouTube uses free text plus a category. SoundCloud and Bandcamp combine a dropdown with tags.
- Distributor genre fields: **Primary** is the broad family (Electronic, Hip-Hop/Rap, Rock…). **Secondary** or **subgenre** narrows it (House, Trap, Alternative…). Use the distributor's list exactly.
- Tags: SoundCloud allows 5 at about 25 characters each. Bandcamp is unlimited. YouTube allows about 500 characters in total. Good tags cover genre, subgenre, mood, tempo/feel, and a "sounds like" described by style rather than by naming another artist.

### Pre-save lead times

| Store | Lead time | Via |
|-------|-----------|-----|
| Spotify | 4+ weeks | Distributor and a smart-link service |
| Apple Music | 4+ weeks | Distributor (pre-add) |
| Deezer | 2+ weeks | Distributor |

A pre-save needs a future release date, final art and basic metadata in place.

### Common rejection reasons
- **Metadata:** "feat." or version info in the title, special characters, ALL CAPS, metadata that doesn't match the audio (wrong language, wrong artist), or a misspelled artist name that creates a duplicate profile.
- **Artwork:** wrong size, blurry, contains a URL or QR code, explicit without the flag, or a copyright issue.
- **Audio:** more than 3 s of silence at either end, clipping or distortion, a low-quality or transcoded source, a mismatched track count, or near-duplicates of tracks already released.
- **Content:** lyrics with prohibited content, or an unlicensed cover or sample.

If rejected: read the reason, fix that specific issue, and resubmit. The second attempt usually passes.

### Pre-submission metadata checklist
- [ ] Album title ≤50 chars, track titles ≤40
- [ ] Art 3000×3000 JPG, RGB
- [ ] Explicit flags correct per track
- [ ] Lyrics formatted (no labels, repeats written out)
- [ ] Genres match the content
- [ ] Release date set (and in the future if there is a pre-save)
- [ ] © and ℗ information accurate
- [ ] Featured artists in the correct field
- [ ] No problem characters or ALL CAPS

---

## 7. Submission Walkthroughs

### Distributor
1. Create a new release (single, EP or album).
2. Upload the artwork.
3. Enter release metadata: title, artist, primary/secondary genre and subgenre, release date, UPC (auto-generate unless the user has one), language, © and ℗ year and holder, and the AI-content disclosure if the form asks.
4. Upload tracks in order, each with its WAV, title, explicit flag, ISRC (auto), streaming lyrics, and credits (songwriter, producer).
5. Review everything once more against §6, then submit. The release date usually can't be changed afterwards.
6. After approval, confirm the release on each store and claim the Spotify for Artists and Apple Music for Artists profiles.

### SoundCloud
1. Upload the tracks in order, then create the playlist or album "[Album] by [Artist]" and set its order.
2. Add the artwork, description, genre and up to 5 tags. The description can include the AI-process note.
3. Set privacy (public, private or scheduled) and decide whether downloads are enabled.
4. Verify: every track plays, the order is right, the art displays, and the links work.

### Bandcamp
Upload lossless files, set the price (fixed, free, or pay-what-you-want with a minimum), and add credits, liner notes and lyrics. Bandcamp rewards rich album pages. Optionally add bonus files: stems, a PDF lyric book, sheet music.

---

## 8. AI Music: Ownership, Copyright and Disclosure

### What can be owned (the legal picture as of 2025–2026, and still unsettled)
- **Pure AI output**, meaning raw audio with no meaningful human authorship, is generally not copyrightable in the US and many other jurisdictions.
- **Human contributions** usually are: lyrics the user wrote, melodies or toplines they composed or substantially directed, the selection and arrangement of outputs, post-production editing, mixing and arrangement, and the album concept and sequencing.
- The more documented human creative control there is, the stronger the claim. Advise the user to keep prompts, lyric drafts, iteration logs, edit notes and timestamps.
- Suno's terms decide what the user may do with outputs: commercial use only for permitted downloads on paid plans, no Remixes of other users' songs, and no watermark removal. Copyright eligibility is a separate question from those permissions. Being allowed to sell a track is not the same as owning a registrable copyright in it.

### Disclosure
- YouTube requires disclosure of realistic synthetic or altered content. TikTok labels AI-generated content. Streaming services and distributors are adding AI tags, disclosure fields (including DDEX AI credits) and anti-spam or anti-impersonation rules. All of these change, so check each platform's current policy at release time.
- **Never** imply that a real artist performed, endorsed or is featured on the track. Don't use soundalike artist names in titles, tags or metadata. Impersonation is the fastest way to a takedown.
- Recommended practice even where it isn't required: a short, factual note in the release description or artist bio about how AI tools were used, plus honest answers when asked. That builds trust and gets ahead of future rules.
- For how to talk about AI in promo copy, see `references/release/promotion.md`.

---

## 9. Rights, Royalties, Content ID and Claims

### Content ID and fingerprinting
YouTube Content ID, platform audio fingerprinting and Audible Magic (used by Facebook, Twitch and others) match uploads against registered audio. Registration goes through the distributor, as a paid add-on or included in some tiers. Once registered, matches elsewhere can be **tracked**, **monetised** (ads on the other upload, with revenue to the user) or **blocked**.

**AI caution:** enroll in Content ID only tracks the user clearly owns and that are clearly distinct. Generative output can resemble other material, and Content ID on near-generic AI audio can wrongly claim other creators. Distributors may refuse or revoke Content ID for AI tracks. Also make sure the user's own channels and videos are allow-listed so their own uploads don't get claimed.

### When the user's music gets claimed
Possible causes: an accidental resemblance to an existing song, a match against similar material, a fraudulent claim, or a legitimate claim (an uncleared sample or cover, or Remix-derived audio).
1. Read the claim: what portion, who the claimant is, and which policy applies.
2. If it is invalid, dispute it with evidence: generation logs, prompts, timestamps, project files.
3. If it is valid, acknowledge it and remove or replace the content.
4. Keep a record of all communication. Filing false disputes can lead to strikes.

| Platform | Process | Typical time |
|----------|---------|--------------|
| YouTube | Dispute, then appeal, then legal (copyright takedown). The claimant has 30 days at each step | 30–90 days |
| Spotify/Apple | Through the distributor | Varies |
| SoundCloud | Online form | 7–14 days |
| Bandcamp | Directly with Bandcamp | 7–14 days |

### Royalties
- **Mechanical royalties** are paid for reproducing the *composition* (streams, downloads, physical copies). In the US the MLC collects them, and registration is free. Elsewhere, local collecting societies do. Publishing administration through a distributor's publishing tier collects them worldwide. They apply only where there is a copyrightable composition, such as human-written lyrics or melody.
- **Performance royalties** are paid for public performance (radio, streaming, venues, TV). Collect them by joining a performing-rights organisation (US: ASCAP, BMI, SESAC; UK: PRS; Canada: SOCAN; Australia: APRA) and registering the songs. PROs require human-authored works. Register only the parts the user authored and describe them accurately.
- **Master or neighbouring rights** are paid to the recording owner (for example SoundExchange in the US for non-interactive digital radio). Eligibility for AI-generated masters varies.

### Avoiding problems
**Before release:** document the process, check for accidental similarity to existing songs (especially melody and hook), clear any samples, and decide on a Content ID policy.
**During distribution:** keep artist and album metadata consistent, register with a PRO and the MLC where eligible, and keep the distributor account in good standing.
**If claimed:** stay calm. Most claims can be resolved. Gather evidence and use the proper channel.

### When to recommend a lawyer
Multiple disputes or strikes, legal threats, significant revenue at stake, or label, sync or publishing contracts. Low-cost options include Volunteer Lawyers for the Arts, the Future of Music Coalition and the EFF for digital-rights questions.

---

## 10. Timing and Scheduling

- **Release day:** Friday is the global industry release day and lines up with New Music Friday editorial playlists. Schedule a specific future date rather than "as soon as possible" whenever there is promotion.
- **Lead time:** 1–2 weeks minimum through a distributor. 4+ weeks if you want an editorial pitch or a pre-save.
- **Staggering:** SoundCloud and Bandcamp can go live the same day as submission or be held to match the store date. Stagger the announcements across platforms (see `promotion.md`).
- **Singles strategy:** releasing singles every 4–8 weeks ahead of an album keeps algorithmic momentum going. Each single can carry over to the album if it uses the same ISRC.
- **Don't rush QA.** Leave a buffer of 1–3 days between finishing and submitting for a final listen on several devices (headphones, monitors, phone, car).

### After release: verification
- [ ] Every store and platform is live, every track plays, the art displays and the order is correct
- [ ] Lyrics are showing where they were supplied
- [ ] Artist profiles claimed (Spotify for Artists, Apple Music for Artists, YouTube Official Artist Channel if eligible)
- [ ] Release date and platform URLs recorded and every link tested
- [ ] Promo copy updated with the real streaming links, then the campaign started

### Common problems
- **QA fails:** fix the specific item (re-master, re-flag, correct lyrics) and re-run the full gate. Don't proceed while anything is unresolved.
- **Distributor rejects:** see "Common rejection reasons" above. Fix the issue and resubmit.
- **Streaming lyrics missing at submission:** pause, write them in the §3 format, then resume. Don't submit without them and plan to add them later.

---

## 11. Bulk and Catalog Releases

Releasing several singles or albums in a short window works only if quality holds. Recommend doing the first 2–3 releases one at a time before batching.

### Approaches
| Approach | When |
|----------|------|
| Sequential | First 2–3 releases, while learning the workflow |
| Parallel planning | Plan several albums, then write and generate one at a time |
| Batch generation | Generate all tracks for one album in one session |
| Pipeline | Advanced. Different albums sit at different stages at the same time |

### Batching that works
1. **Plan in a batch:** concept, tracklist and sonic direction for 3–5 releases before writing any lyrics (see `references/album/concept.md`).
2. **Write album by album** for a consistent voice. Batching by track type (all intros, then all closers) only helps when the albums share themes.
3. **Generate one album per session:** have all style prompts ready, generate in order, and log keepers and their links as you go (for example, "Album A, track 02, take 2: keeper"). Plan sessions around credit refreshes and be selective about regenerating.
4. **Master album by album**, then check loudness consistency within each album (see `references/production/mastering.md`).
5. **Batch the art prompts**, generate the images in one session, then check each against the spec in §6.
6. **Run the full QA gate on each release on its own.** Batching never skips it.

### Staged release schedule
| Strategy | Pattern |
|----------|---------|
| All at once | Everything on one day. Maximum splash, but the releases compete with each other |
| Weekly / bi-weekly | Steady content flow with lessons carried forward between releases |
| Monthly | Sustained presence, which the algorithms favour |

Per release: QA gate, record the release date and status, upload to SoundCloud/Bandcamp, submit to the distributor, then announce.

**Sample 4-week bulk timeline:** week 1 plan albums A–C, week 2 write A–C, week 3 generate A–C, week 4 master everything, make the art, run QA, release A, and schedule B and C.

### Catalog hygiene and AI-volume caution
- Keep the artist name, genres and credits consistent across the catalog. One artist name maps to one profile.
- Avoid flooding stores with many near-identical tracks. Distributors and stores have anti-spam rules for mass uploads and low-effort content, and AI catalogs get extra scrutiny. Quality beats quantity.
- If quality starts slipping across albums, go back to one release at a time.

---

## Appendix: Publishing Sheet Music and Lead Sheets (Optional)

Some fans, cover artists, teachers and sync supervisors want notation. This is optional and is best for melodic, sparse tracks.

### Getting notation
- **Automatic transcription** (audio-to-MIDI or notation tools, sometimes after stem separation to isolate vocal and bass) gives a draft. Expect roughly 90–95% accuracy on solo piano, singer-songwriter, folk and classical material, 75–90% on vocal-led pop, country and jazz heads, 60–80% on rock, blues, gospel and musical theatre, and 50–70% on hip-hop hooks, metal and melodic EDM. Ambient, drone, noise and dubstep mostly fail. Skip those.
- **Always polish** in a notation editor (MuseScore is free): fix the rhythm, key and time signatures, enharmonics and octaves, and simplify for playability.
- **Lead sheets** are often the better deliverable: melody, chord symbols and lyrics. They can be written from the known chords and melody without full transcription.
- Tips: transcribe the memorable sections (hook, theme) rather than dense full tracks. For jazz, transcribe the head only. For hip-hop, only the sung hooks. Aim for a playable piano reduction, not a replica of the production.

| Use | Accuracy needed | Effort |
|-----|-----------------|--------|
| Personal reference | 60–70% | Low |
| Cover performers | 80–90% | Medium |
| Licensing package | 90%+ | High |
| Selling | 95%+ | Very high |

### What to publish
Per track: **PDF** (to view and print), **MusicXML** (editable in MuseScore, Finale or Sibelius) and **MIDI** (for playback and practice). Use clean titles with no track-number prefixes. Optionally add a combined songbook PDF with a title page (with album art), a copyright page, a table of contents and the tracks in album order. Use US Letter for home printing or 9×12 for a professional look.

### Where
- **The user's website or Bandcamp** (recommended): a free download page or bonus content with an album purchase. Include a credit line, a listen link and a download for each track.
- **Marketplaces:** Sheet Music Plus (roughly 70% to the creator) and Musicnotes (may require approval).
- **Print-on-demand** (optional): Amazon KDP, Lulu, Blurb.

### Rights
The user may publish notation only for compositions they own. Never publish notation for covers or samples without a licence. Add a copyright notice, for example "© 2026 [Artist]. Free companion to the album. Share freely with credit", or a Creative Commons licence (CC BY, BY-NC or BY-SA). The authorship caveats in §8 apply to AI-generated melodies too.

**Checklist:** clean titles, all three formats per track, PDFs checked for readability, copyright notice, links tested, and the sheet music mentioned in the album description and on social posts.

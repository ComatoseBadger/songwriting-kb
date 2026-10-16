# Lyric Compliance

Three checks that protect the release rather than the craft:

1. **Explicit content**: the content flag must match what's actually in the lyrics.
2. **Originality**: catch unintentional borrowing from existing songs.
3. **Documentary and real-people standards**: avoid defamation and fabrication when you write about real people and events.

When to run them:

| Check | When |
|-------|------|
| Explicit content | Before generation, and again before release (see `references/release/release.md`) |
| Originality | Before release. It's too slow and depends too much on search to gate generation. |
| Documentary standards | While writing every line about a real person or event, and again in review (`references/lyrics/review.md`, checks 7–8) |

---

## 1. Explicit Content

Scan the lyrics for explicit words, count them per track, and flag any mismatch between the content and the explicit flag. Produce a summary suitable for distributor submission.

### Explicit Words (require Explicit = Yes)

| Category | Words |
|----------|-------|
| **F-word** | fuck, fucking, fucked, fucker, motherfuck, motherfucker |
| **S-word** | shit, shitting, shitty, bullshit |
| **B-word** | bitch, bitches |
| **C-words** | cunt, cock, cocks |
| **D-word** | dick, dicks |
| **P-word** | pussy, pussies |
| **A-word** | asshole, assholes |
| **Slurs** | whore, slut, the n-word, the f-slur |
| **Profanity** | goddamn, goddammit |

### Clean Words (no flag needed)

damn, hell, crap, ass, bastard, piss

"damn" alone is clean, but "goddamn" is explicit.

### Matching Rules

- Match case-insensitively (Fuck = fuck = FUCK).
- Catch the variations (fucking, fucked, fucker).
- Count intentional phonetic or obfuscated spellings (fuk, sh1t).
- Presence matters more than context: if the word is there, flag it.
- If any track is explicit, the album is explicit.
- **User word lists win.** If the user names extra explicit words (regional slang, genre-specific profanity), add them. If they exempt base words for a specific context (e.g. "hell" and "damn" in a historical narrative or period-accurate dialogue), remove those. Scan with the merged list.

### Mismatch Handling

**Flag says No, content is explicit:**
```
⚠️ MISMATCH: Track contains explicit content but Explicit flag is "No"
ACTION: Set Explicit: Yes
```

**Flag says Yes, content is clean:**
```
ℹ️ NOTE: Track flagged explicit but no explicit words found
This is OK — the artist may want the explicit flag for themes/context
No action required (conservative flagging is fine)
```

### Distributor Requirements

Most distributors (DistroKid, TuneCore, CD Baby) require:
- **track-level flags**: every track marked explicit or clean;
- **an album-level flag**: explicit if ANY track is explicit;
- **consistent metadata**: each flag matches the actual content.

**Consequences of a wrong flag:**
- explicit content marked clean → possible removal from platforms and account issues;
- clean content marked explicit → reduced reach (filtered from some playlists), but no penalty.

**Rule: when in doubt, mark it explicit.** Under-flagging is worse than over-flagging.

### Report Format

```
EXPLICIT CONTENT SCAN
Album: [Album Name]
Date: [Scan Date]

TRACK RESULTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Track 01: [Title]
  Flag: No
  Content: Clean
  Status: ✓ OK

Track 02: [Title]
  Flag: Yes
  Content: fuck (3), shit (2), bitch (1)
  Status: ✓ OK (flag matches content)

Track 03: [Title]
  Flag: No
  Content: fuck (1)
  Status: ⚠️ MISMATCH - Contains explicit content but flag is No

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUMMARY:
  Total tracks: 10
  Clean tracks: 7
  Explicit tracks: 3
  Mismatches: 1

ALBUM EXPLICIT FLAG: Yes (any track explicit = album explicit)

ACTION REQUIRED:
  - Track 03: Set Explicit flag to Yes
```

---

## 2. Originality (Plagiarism Check)

Scan the lyrics for phrases that may unintentionally echo existing songs. This is a quality check, not a legal tool. It catches likely borrowing early so the writer can revise before release; only a lawyer can determine infringement.

### Method

1. **Use the streaming lyrics** (standard spelling). Suno lyrics contain phonetic respellings (e.g. "Seh-KYOOR-ih-tee" for "security") that produce garbage search results. Fall back to the Suno lyrics only if no streaming version exists.
2. **Extract the distinctive phrases.** Pick about 15 distinctive 4–7-word n-grams, chorus/hook lines first, then bridge, then verses. Leave out ubiquitous clichés ("break my heart", "falling in love", and the like); they are too common to flag, so count them as filtered.
3. **Search the web** if search is available. Query each phrase in quotes plus the word `lyrics`. Search 10–15 phrases, or 5–8 for short lyrics (under 100 words). Look for results that name a specific song and artist. Skip:
   - lyric aggregator pages listing hundreds of matches (too generic);
   - dictionary or reference pages;
   - the user's own published work.
4. **Compare in depth.** For each result that names a specific song, open its lyrics and compare the matching section:
   - exact consecutive matching words (5+) → HIGH;
   - a partial 4-word overlap → MEDIUM;
   - thematic similarity only → LOW.
5. **Run a knowledge check.** Independently scan ALL lines, not just the extracted phrases, against the songs you know. Flag any line that closely resembles a well-known lyric, name the suspected source song and artist, and say whether the similarity is in the words, the hook phrasing, or the concept.
6. **Report.** If web search is unavailable or rate-limited, run the knowledge check alone and say so in the report.

For a full album, check every track that has lyrics and aggregate the results into one report with a section per track.

### Risk Levels

| Level | Criteria | Action |
|-------|----------|--------|
| **HIGH** | 5+ consecutive words matching a known song, especially a chorus/hook | Rewrite the line immediately |
| **MEDIUM** | A 4-word match with a known song, or a structural similarity you've flagged | Review and consider rewording |
| **LOW** | Common phrasing overlap, likely coincidence | Note for awareness; no action needed |

### Verdicts

| Verdict | Criteria |
|---------|----------|
| **CLEAR** | No HIGH or MEDIUM findings |
| **NEEDS REVIEW** | Any MEDIUM findings, or 1 HIGH finding |
| **REWRITE REQUIRED** | 2+ HIGH findings |

### Report Format

```
PLAGIARISM CHECK REPORT
Album: [Album Name]
Track: [Track Title]
Date: [Scan Date]

PHRASES SEARCHED: [N]
WEB MATCHES FOUND: [N]
KNOWLEDGE FLAGS: [N]

FINDINGS:
------------------------------------------------------------------------

[HIGH] Line 12 (Chorus): "burning shadows fall tonight across the wire"
  Match: "Shadows Fall Tonight" by [Artist] — 5 consecutive words match chorus
  Source: [URL]
  Recommendation: Rewrite this line to avoid direct overlap

[MEDIUM] Line 24 (Verse 2): "walking through the ruins of the empire"
  Similarity: Resembles "Empire" by [Artist] — similar phrasing in bridge
  Source: Model knowledge
  Recommendation: Consider rewording if concerned

[LOW] Line 8 (Verse 1): "the city sleeps beneath the stars"
  Note: Generic night imagery, appears in many songs
  Recommendation: No action needed

------------------------------------------------------------------------

SUMMARY:
  HIGH risk findings: 1
  MEDIUM risk findings: 1
  LOW risk findings: 1

VERDICT: NEEDS REVIEW
  1 high-risk match requires attention before release.

COMMON PHRASES FILTERED: [N] (not searched — too generic to flag)
```

Related: an artist name in a Suno style prompt is a separate problem (generation failure, not originality). See `references/lyrics/review.md` check 14.

---

## 3. Documentary and Real-People Standards

Use these legal-safety standards whenever lyrics describe real people or events.

### When They Apply

- **True crime** (criminal cases, trials, investigations)
- **Documentary storytelling** (real events, real people)
- **Biographical work** (profiles of real people)
- **Historical narratives** (factual events)
- **Any work built on cited sources or research notes**

### The Five Rules

1. **No impersonation.** Use a third-person narrator only and never speak *as* the person. The narrator describes; it doesn't impersonate.
2. **No fabricated quotes.** Put words in quotation marks only when they appear verbatim in the sources (testimony, transcript, recorded statement), and cite them.
3. **No internal-state claims.** Never claim to know what someone thought, felt, believed, or feared unless a source (interview, statement, court record) affirms it.
4. **No speculative actions.** Stick to documented events. Don't invent daily activities, scenes, or beats.
5. **No negative factual claims.** Don't claim "nobody saw" or "nobody heard": you can't prove a negative, and a gap in the record is not evidence. Such a line needs a source that asserts it.

### High Risk: Avoid

**Internal-state claims:**
- "She was afraid"
- "He felt angry"
- "She believed him"
- "He knew it was wrong"
- "She wanted to escape"
- "Living in fear"
- "Tried to disappear"
- "Can't believe what's real"
- "Didn't know where to go"

**Fabricated quotes:**
- "I need help," she cried
- "We'll start the process," they said
- any direct speech without a documented source

**Speculative actions:**
- "She finally made the call" (unless *how* is documented)
- "Goes to sleep that night" (an undocumented private action)
- "Waiting for the call" (a speculative daily activity)
- "June 21st she waited" (an invented, specific, undocumented timeline)

**Negative factual claims:**
- "Nobody heard her scream"
- "Nobody saw what happened"
- "No one knew the truth"

### Legally Safer: Use

**Pattern-based language:**
- "The pattern started" (not "the first time")
- "The cycle repeated" (not "the second time")
- "Years of documented abuse" (a pattern, not specific incidents)

**Observable, documented behavior:**
- "She called 911" (a documented action)
- "Court records show" (attributed to a source)
- "Testimony revealed" (documented at trial)
- "The walls kept her screams in" (describes the situation without claiming "nobody heard")

**Documented psychiatric or medical states:**
- "Brief reactive psychosis" (a doctor's diagnosis)
- "PTSD confirmed" (a documented diagnosis)
- "Testimony says she lost her mind" (attributed to testimony)

**Narrator description vs. internal claim:**

| Safe (observable/documented) | Unsafe (internal state/intention) |
|------------------------------|-----------------------------------|
| "She asked for protection" | "She felt desperate" |
| "Reality hitting hard" (narrator's observation of the situation) | "She couldn't process" |
| "Four years of violence" (documented pattern) | "Four years of hiding" (internal intention) |

**Timing without speculation:**
- Safe: "Two days before June 23rd" (documented timing)
- Unsafe: "June 21st she waited, June 22nd still nothing" (speculative daily actions)

### Attribution Techniques

When a line has to come close to an internal state, **attribute it to a source**:
- "Doctors diagnosed PTSD"
- "Testimony revealed years of abuse"
- "Court records documented the pattern"
- "She testified 'You hurt me again and again'" (an actual quote, attributed)
- "According to trial testimony" (explicit attribution)

### Before/After

| Problem | Before | After |
|---------|--------|-------|
| Internal state | "She was living in dread, trying to survive" | "Years of documented abuse, the pattern escalating" |
| Fabricated quote | "'I need protection,' she begged" | "She asked for protection, asked to get away" |
| Speculative action | "She finally made the call, hiding in the bathroom" | "She reached out for help, contacted the authorities" |
| Negative claim | "Nobody heard her scream, nobody saw" | "The walls kept her screams in, the world couldn't see within" |
| Pattern vs. specific | "The first time he hit her, the second time worse" | "The pattern started, the cycle repeated, years of escalation" |

### The Line-by-Line Test

Ask these for EVERY line about a real person or event:
1. Can I cite this claim to a specific source?
2. Am I claiming internal knowledge I can't have?
3. Am I inventing quotes or dialogue?
4. Am I speculating about undocumented actions?
5. Am I making negative claims I can't prove?

If any answer is a problem, rewrite the line.

Then verify the facts: names spelled correctly, dates, numbers and amounts, event order, and key facts all match the sources. A wrong name, date, or major fact is critical.

### Why It Matters

Getting this wrong can:
- expose the artist to defamation claims;
- undermine the credibility of the whole work;
- force expensive revisions or takedowns;
- damage the artist's reputation as a documentary storyteller.

**The standard:** if you can't cite it, don't write it. If you can't prove it, don't claim it. If it's internal, don't assume it.

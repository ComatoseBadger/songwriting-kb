"""Structural contract and regressions; no generated-audio claims."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validator', ROOT / 'tools/validate-song.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
VOICE = 'warm baritone with rhythmic clean phrasing and restrained grit'
PACKAGE = f'''# Test
## Vocal Identity
{VOICE}
## Style Prompt A
Alternative metal, {VOICE}, clipped guitar riff, syncopated drums, dry space
## Style Prompt B
Alternative metal, {VOICE}, melodic bass, swinging drums, wide guitars
## Intro Concept A
- Mechanism: guitar-signature
- First Sound: muted guitar pickup
- Groove: syncopated kick and backbeat snare
- Vocal Entry: bar three, intimate
- Envelope: short dry attacks
- Transition: drums stop before verse
## Intro Concept B
- Mechanism: bass-led
- First Sound: sliding bass phrase
- Groove: swung kick, rim clicks
- Vocal Entry: first downbeat, clean
- Envelope: long resonant notes
- Transition: guitar answers into verse
## Intro Differentiation Gate
- Window: 15–20 seconds
- History: unavailable
- Limitation: No prior track audio or descriptions supplied
- Comparison: Compare the planned dry guitar pickup with sustained bass; listen after rendering
- Decision: provisional
## Production Lock
- Status: draft
- Style: A
- Intro: B
## Exclusions
beatboxing
## Lyrics
[Title: Test]
[Production Direction: contrasting rhythms]
[Vocal Direction: {VOICE}]
[Verse 1]
I took the call and let it ring
[Chorus]
You never heard me say a thing
[end]
## Production Notes
Key Em; 96 BPM; 4/4; i–VI Em–C; baritone; guitar/bass/drums; sparse to full; title hook; AA; confession to resolve
## Advanced Options
- Model: v6
- Persona/Voice: unavailable
- Weirdness: 40, starting comparison only
- Style Influence: 60, starting comparison only
- Audio Influence: N/A
- Exclude: beatboxing
- Variety: 0, keep Style controlled
- Max Mode: off for sketch
## Changes
Initial draft
## Next Changes
Listen for voice continuity and intro contrast
'''


class PackageTests(unittest.TestCase):
    def validate(self, text=PACKAGE, legacy=False):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'song.md'
            path.write_text(text)
            return v.validate_file(str(path), legacy=legacy)

    def failed(self, text, name):
        result = self.validate(text)
        self.assertTrue(any(c['status'] == 'FAIL' and name in c['name'] for c in result['checks']), result)

    def test_valid_package(self):
        self.assertEqual(self.validate()['result'], 'PASS')

    def test_missing_style_alternative(self):
        self.failed(PACKAGE.replace('## Style Prompt B', '## Unused Prompt'), 'Style Alternatives')

    def test_duplicate_styles(self):
        s = v.package_sections(PACKAGE)
        self.failed(PACKAGE.replace(s['style prompt b'], s['style prompt a']), 'Style Alternatives')

    def test_each_style_length_checked(self):
        self.failed(PACKAGE.replace('melodic bass', 'x' * 1001), 'Style B: Style Prompt Characters')

    def test_same_intro_mechanism(self):
        self.failed(PACKAGE.replace('Mechanism: bass-led', 'Mechanism: guitar-signature'), 'Intro Architectures')

    def test_missing_groove(self):
        self.failed(PACKAGE.replace('- Groove: swung kick, rim clicks\n', ''), 'Intro B Fields')

    def test_voice_drift(self):
        self.failed(PACKAGE.replace(f'Alternative metal, {VOICE}, melodic', 'Alternative metal, bright tenor, melodic'), 'Vocal Identity Reuse')

    def test_review_window(self):
        self.failed(PACKAGE.replace('Window: 15–20 seconds', 'Window: 5 seconds'), 'Intro Review Window')

    def test_unavailable_requires_reason(self):
        self.failed(PACKAGE.replace('- Limitation: No prior track audio or descriptions supplied\n', ''), 'Intro History')

    def test_history_three_tracks(self):
        text = PACKAGE.replace('History: unavailable', 'History: available').replace('- Limitation: No prior track audio or descriptions supplied', '- Track 1: One, guitar vs drums\n- Track 2: Two, bass vs piano\n- Track 3: Three, dry vs swelling')
        self.assertEqual(self.validate(text)['result'], 'PASS')

    def test_partial_history_requires_limitation(self):
        text = PACKAGE.replace('History: unavailable', 'History: available').replace('- Limitation: No prior track audio or descriptions supplied', '- Track 1: One, guitar vs drums')
        self.failed(text, 'Intro History')
        self.assertEqual(self.validate(text.replace('- Track 1:', '- Limitation: Only one prior track available\n- Track 1:'))['result'], 'PASS')

    def test_locked_cannot_skip_failed_gate(self):
        self.failed(PACKAGE.replace('Status: draft', 'Status: locked').replace('Decision: provisional', 'Decision: revise'), 'Gate Decision')

    def test_lock_ids_exist(self):
        self.failed(PACKAGE.replace('- Style: A', '- Style: C'), 'Production Selection')

    def test_advanced_options_required(self):
        self.failed(PACKAGE.replace('## Advanced Options', '## Settings'), 'Advanced Options')

    def test_missing_next_changes(self):
        self.failed(PACKAGE.replace('## Next Changes', '## Future'), 'Changes / Next Changes')

    def test_combined_changes_heading(self):
        self.assertEqual(self.validate(PACKAGE.replace('## Changes', '## Changes / Next Changes').replace('## Next Changes\n', 'Next: '))['result'], 'PASS')

    def test_lyrics_stop_at_package_metadata(self):
        self.assertNotIn('Advanced Options', v.package_sections(PACKAGE)['lyrics'])
        self.assertNotIn('Production Notes', v.package_sections(PACKAGE)['lyrics'])

    def test_fenced_style_counts_only_payload(self):
        text = PACKAGE.replace(f'Alternative metal, {VOICE}, clipped guitar riff, syncopated drums, dry space', f'```text\nAlternative metal, {VOICE}, clipped guitar riff, syncopated drums, dry space\n```')
        self.assertEqual(self.validate(text)['result'], 'PASS')

    def test_existing_section_isolation_check(self):
        self.failed(PACKAGE.replace('[Verse 1]\n', '[Verse 1] '), 'Section Tag Isolation')

    def test_existing_named_layers_check(self):
        self.failed(PACKAGE.replace('I took the call', '(robotic layer: hello)\nI took the call'), 'Layer Declarations')

    def test_existing_lyrics_budget(self):
        self.failed(PACKAGE.replace('I took the call', 'x' * 5001 + '\nI took the call'), 'Lyrics Field Characters')

    def test_legacy_single_prompt(self):
        text = '## Style Prompt\nAlternative metal, warm baritone, guitar, drums\n## Lyrics\n[Title: Test]\n[Production Direction: sparse]\n[Vocal Direction: baritone]\n[Verse]\nA line\n[end]\n## Production Notes\n' + 'x' * 6000
        self.assertEqual(self.validate(text, legacy=True)['result'], 'PASS')
        self.failed(text, 'Style Alternatives')

    def test_legacy_heading_levels(self):
        for level in ("#", "##", "###"):
            text = f"{level} Style Prompt:\nAlternative metal, guitar, drums\n{level} Lyrics:\n[Title: Test]\n[Production Direction: sparse]\n[Vocal Direction: warm]\n[end]"
            self.assertEqual(self.validate(text, legacy=True)['result'], 'PASS')

    def test_cli_json_exit_codes(self):
        for text, expected in [(PACKAGE, 0), (PACKAGE.replace('## Advanced Options', '## Other'), 1)]:
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / 'song.md'
                path.write_text(text)
                result = subprocess.run([sys.executable, str(ROOT / 'tools/validate-song.py'), '--json', str(path)], capture_output=True, text=True)
                self.assertEqual(result.returncode, expected, result.stderr)
                import json
                self.assertEqual(json.loads(result.stdout)[0]['failures'] > 0, expected == 1)

    def test_unfilled_template_fails(self):
        self.assertEqual(self.validate((ROOT / 'templates/suno-v6-song.md').read_text())['result'], 'FAIL')


if __name__ == '__main__':
    unittest.main()

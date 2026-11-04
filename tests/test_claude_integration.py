"""Portable Claude routing and three-intro package regressions.

Text checks protect load paths; they do not prove creative quality or audio identity.
"""
from pathlib import Path
import re
import tempfile
import unittest
from test_validate_song import v

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / '.claude/skills/suno-music-studio'
FIXTURE = (ROOT / 'tests/fixtures/claude-v6-package.md').read_text()


class ClaudeIntegrationTests(unittest.TestCase):
    def validate(self, text):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'package.md'
            path.write_text(text)
            return v.validate_file(str(path))

    def assertFails(self, text, check):
        result = self.validate(text)
        self.assertTrue(any(c['status'] == 'FAIL' and check in c['name']
                            for c in result['checks']), result)

    def test_copyable_three_intro_package(self):
        self.assertEqual(self.validate(FIXTURE)['result'], 'PASS')

    def test_third_intro_fields_checked(self):
        self.assertFails(FIXTURE.replace('- Envelope: dry close vocal', '- Missing: dry close vocal'),
                         'Intro C Fields')

    def test_third_intro_duplicate_mechanism(self):
        self.assertFails(FIXTURE.replace('Mechanism: vocal-first', 'Mechanism: bass-led'),
                         'Intro Architectures')

    def test_third_intro_selection_must_exist(self):
        self.assertFails(FIXTURE.replace('## Intro Concept C', '## Unused Concept C'),
                         'Production Selection')

    def test_unselected_style_budget_checked(self):
        self.assertFails(FIXTURE.replace('melodic bass', 'x' * 1001),
                         'Style B: Style Prompt Characters')

    def test_saved_voice_does_not_bypass_identity(self):
        changed = FIXTURE.replace('Persona/Voice: unavailable', 'Persona/Voice: saved test voice')
        changed = changed.replace('Alternative metal, warm baritone', 'Alternative metal, bright tenor', 1)
        self.assertFails(changed, 'Vocal Identity Reuse')

    def test_provisional_cannot_be_final_lock(self):
        self.assertFails(FIXTURE.replace('Status: draft', 'Status: locked'), 'Gate Decision')

    def test_explicit_pass_can_lock(self):
        changed = FIXTURE.replace('Status: draft', 'Status: locked')
        changed = changed.replace('History: unavailable', 'History: available\n- Track 1: prior take, sustained synth opening; current vocal pickup is dry')
        changed = changed.replace('Decision: provisional', 'Decision: pass')
        self.assertEqual(self.validate(changed)['result'], 'PASS')

    def test_portable_routes_load_contract(self):
        for relative in ['SKILL.md', 'references/suno/prompting.md',
                         'references/suno/pre-generation-check.md',
                         'references/album/personas-and-covers.md']:
            with self.subTest(route=relative):
                self.assertIn('v6-workflow.md', (SKILL / relative).read_text())

    def test_contract_relative_links_resolve(self):
        # Only follow local Markdown links; exported skill must not need repo files.
        for relative in ['references/suno/prompting.md',
                         'references/suno/pre-generation-check.md',
                         'references/album/personas-and-covers.md']:
            path = SKILL / relative
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if '://' not in target and not target.startswith('#'):
                    self.assertTrue((path.parent / target.split('#')[0]).exists(), target)

    def test_router_no_longer_delivers_single_box(self):
        text = (SKILL / 'SKILL.md').read_text()
        self.assertNotIn('Deliver a finished generation in this order', text)
        self.assertIn('multiple Style alternatives', text)
        self.assertIn('three distinct intro concepts', text)

    def test_gate_cannot_skip_workflow_for_instrumentals(self):
        text = (SKILL / 'references/suno/pre-generation-check.md').read_text()
        self.assertIn('Do not skip Gate 0', text)
        self.assertIn('READY FOR EXPLORATORY GENERATION', text)

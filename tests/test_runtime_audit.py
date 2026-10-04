import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('runtime_audit', ROOT / 'scripts/audit_runtime.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class RuntimeAuditTests(unittest.TestCase):
    def test_original_description_reintroduced_in_skill_or_ui_is_rejected(self):
        inventory = json.loads((ROOT / 'research/upstream-inventory.json').read_text())
        stale = next(item['purpose_ko'] for item in inventory['skills'] if item['upstream'] == 'setup-pstack')
        for path in ['skills/setup-jstack/SKILL.md', 'skills/setup-jstack/agents/openai.yaml']:
            self.assertTrue(module.audit_text(path, stale))

    def test_legacy_tools_rejected_without_platform_word(self):
        rules = [r for r in module.POLICY['patterns'] if r['id'] == 'legacy-tool']
        self.assertEqual(len(rules), 1)
        # 직접 도구 의존을 검사하고 일반 작업을 뜻하는 소문자 task는 허용한다.
        for value in ['AskQuestion', 'Task', 'control-ui', 'control-cli', 'create-skill', 'deslop']:
            self.assertTrue(module.audit_text('skills/how/SKILL.md', value))
        self.assertFalse(module.audit_text('skills/how/SKILL.md', '독립 task를 내부 Codex agent에 맡긴다.'))

    def test_history_exception_does_not_hide_execution_section(self):
        stale = next(item['purpose_ko'] for item in json.loads((ROOT / 'research/upstream-inventory.json').read_text())['skills'] if item['upstream'] == 'setup-pstack')
        self.assertFalse(module.audit_text('README.md', '## pstack와 달라진 점\n' + stale))
        self.assertTrue(module.audit_text('README.md', '## pstack와 달라진 점\n' + stale + '\n## 설치\n' + stale))

    def test_pagination_exception_does_not_hide_new_dependency(self):
        path = 'skills/jstack-mode/scripts/watch-pr.py'
        original = (ROOT / path).read_text()
        self.assertFalse(module.audit_text(path, original))
        stale = next(item['purpose_ko'] for item in json.loads((ROOT / 'research/upstream-inventory.json').read_text())['skills'] if item['upstream'] == 'setup-pstack')
        self.assertTrue(module.audit_text(path, original + '\n# ' + stale))
        for new_dependency in ['import cursor', 'from cursor import launch_agent', 'cursor.launch_agent()', 'import endCursor']:
            self.assertTrue(module.audit_text(path, original + '\n' + new_dependency))
        self.assertTrue(module.audit_text(path, original.replace("pagination_after=page['pageInfo']['endCursor']", "pagination_after=page['pageInfo']['endCursor']; import endCursor")))

    def test_complete_current_execution_surface_passes(self):
        report = module.audit()
        self.assertGreaterEqual(report['files_checked'], 130)
        self.assertEqual(report['findings'], [])

#!/usr/bin/env python3
"""현재 실행 지시와 역사 자료를 구분하는 정적 이식 감사. 모델 행동 보장은 아님."""
import ast
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
POLICY = json.loads((ROOT / 'research/runtime-audit-policy.json').read_text())


def executable_text(path, text):
    if str(path) == 'README.md':
        historical = False
        rows = []
        for row in text.splitlines(keepends=True):
            if row.startswith('## '):
                historical = row[3:].strip() in POLICY['historical_readme_sections']
            rows.append('\n' if historical else row)
        text = ''.join(rows)
        text = re.sub(r'\[pstack\]\(https://github\.com/cursor/plugins/[^)]*\)', '[원본 출처]', text)
    if str(path) == 'skills/jstack-mode/scripts/watch-pr.py':
        # API field는 실제 read_pr query/응답 index의 문자열에서만 구분한다.
        tree = ast.parse(text)
        parents = {child: node for node in ast.walk(tree) for child in ast.iter_child_nodes(node)}
        function = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'read_pr')
        lines = text.splitlines(keepends=True)
        for node in ast.walk(function):
            if not isinstance(node, ast.Constant) or not isinstance(node.value, str):
                continue
            parent = parents.get(node)
            query = (isinstance(parent, ast.Assign)
                     and any(isinstance(target, ast.Name) and target.id == 'query' for target in parent.targets)
                     and node.value.startswith('query(') and 'reviewThreads(' in node.value)
            index = (isinstance(parent, ast.Subscript) and parent.slice is node
                     and node.value == 'endCursor' and isinstance(parent.value, ast.Subscript)
                     and isinstance(parent.value.slice, ast.Constant) and parent.value.slice.value == 'pageInfo')
            if query or index:
                for row in range(node.lineno - 1, node.end_lineno):
                    line = lines[row].encode('utf-8')
                    start = node.col_offset if row == node.lineno - 1 else 0
                    end = node.end_col_offset if row == node.end_lineno - 1 else len(line)
                    segment = line[start:end].decode('utf-8')
                    lines[row] = (line[:start].decode('utf-8')
                                  + re.sub(r'\bendCursor\b', '         ', segment)
                                  + line[end:].decode('utf-8'))
        text = ''.join(lines)
    return text


def audit_text(path, text):
    text = executable_text(path, text)
    findings = []
    for rule in POLICY['patterns']:
        pattern = re.compile(rule['regex'], re.IGNORECASE if rule['ignore_case'] else 0)
        for number, line in enumerate(text.splitlines(), 1):
            if pattern.search(line):
                findings.append({'path': str(path), 'line': number, 'rule': rule['id']})
    return findings


def audit(root=ROOT):
    paths = [p for p in (root / 'skills').rglob('*')
             if p.is_file() and p.suffix in {'.md', '.yaml', '.yml', '.py', '.json'}]
    paths += [root / 'README.md', root / 'plugin.json',
              root / '.agents/plugins/marketplace.json', root / 'scripts/test-install.py']
    findings = []
    for path in sorted(paths):
        findings.extend(audit_text(path.relative_to(root), path.read_text(encoding='utf-8')))
    return {'files_checked': len(paths), 'findings': findings,
            'scope': '실행 지시의 정적 잔재 검사. 원본 조사·귀속·감사 어휘·검증 기록은 역사 자료. 의미 검토와 model 행동 검증을 대체하지 않음.'}


if __name__ == '__main__':
    report = audit()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(bool(report['findings']))

#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
text = SKILL.read_text(encoding="utf-8")

errors = []

if not text.startswith("---\n"):
    errors.append("SKILL.md must start with YAML frontmatter")

m = re.search(r"^name:\s*([a-z0-9-]+)\s*$", text, re.M)
if not m:
    errors.append("missing or invalid 'name' in frontmatter")
else:
    name = m.group(1)
    if name != ROOT.name:
        errors.append(f"name '{name}' must match directory '{ROOT.name}'")

if not re.search(r"^description:\s*>?", text, re.M):
    errors.append("missing 'description' in frontmatter")

required = [
    "# Grounded Reality Essay",
    "## When to Use",
    "## Core Model: 六镜头现实拆解",
    "## Workflow",
    "## Output Contract",
    "## Quality Gate",
]
for section in required:
    if section not in text:
        errors.append(f"missing required section: {section}")

# Ensure excluded source domains/topics are explicitly guarded, not silently forgotten.
for keyword in ["征婚", "相亲", "恋爱", "婚姻", "怀孕"]:
    if keyword not in text:
        errors.append(f"missing exclusion keyword in SKILL.md: {keyword}")

if errors:
    print("INVALID")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("VALID")
print(f"skill: {ROOT.name}")
print(f"files: {sum(1 for p in ROOT.rglob('*') if p.is_file())}")

"""Validate the portable-agent guide package; no native profile is modified."""
from pathlib import Path
import re
import sys

root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
required = ["README.md", "SPEC.md", "SETUP.md", "VERIFICATION.md", "LICENSE", "templates/AGENT.md", "templates/LAUNCH-GUIDE.md", "examples/bob/AGENT.md", "examples/bob/skills/cite-sources/SKILL.md"]
required += [f"surfaces/{name}.md" for name in ("claude-code", "codex", "cursor", "grok", "hermes", "t3-code")]
errors = []
for name in required:
    path = root / name
    if not path.is_file() or not path.read_text(encoding="utf-8-sig").strip():
        errors.append(f"Missing or empty package file: {name}")
if (root / "SPEC.md").is_file():
    spec = (root / "SPEC.md").read_text(encoding="utf-8-sig")
    for path in required[-6:]:
        if path not in spec:
            errors.append(f"Surface guide missing from specification: {path}")
for document in [root / "README.md", root / "SPEC.md", root / "SETUP.md", root / "VERIFICATION.md", *sorted((root / "surfaces").glob("*.md"))]:
    if not document.is_file():
        continue
    text = re.sub(r"```[\s\S]*?```", "", document.read_text(encoding="utf-8-sig"))
    for target in re.findall(r"\[[^\]]+\]\(([^\s)]+)", text):
        if target.startswith(("http:", "https:", "mailto:", "#", "/")) or "{" in target:
            continue
        local = target.split("#", 1)[0]
        if local and not (document.parent / local).exists():
            errors.append(f"Broken local link in {document.relative_to(root)}: {target}")
if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)
print(f"PASS: {len(required)} required documents, six surface references and local links")

#!/usr/bin/env python3
"""Verify that the canonical skill behavior survives every runtime projection.

Structural parity only: this does not assert live model behavior or host capabilities.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import re
import zipfile

SKILLS = ("presentationsplanering", "bildproduktion", "presentationsexport", "kvalitetsgranskning")
ARCHIVES = {
    "chat": "assistant/instructions.md",
    "claude-project": "project/instructions.md",
    "opencode": "AGENTS.md",
}
SKILL_ARCHIVES = {
    "chat": "assistant/skills",
    "plugin": "skills",
    "claude-skills": "skills",
}

def headings(text: str) -> list[str]:
    return re.findall(r"^## (.+)$", text, flags=re.MULTILINE)

def verify(root: Path, version: str, dist: Path) -> list[str]:
    errors: list[str] = []
    originals = {}
    for skill in SKILLS:
        source = root / "canonical" / "skills" / skill / "behavior.md"
        originals[skill] = [h for h in headings(source.read_text(encoding="utf-8")) if h != "Ansvarsgränser"]
    for target in ("chat", "plugin", "claude-project", "claude-skills", "opencode"):
        archive = dist / f"presentationsbyggaren-{target}-{version}.zip"
        if not archive.is_file():
            errors.append(f"Missing archive: {archive.name}")
            continue
        with zipfile.ZipFile(archive) as z:
            names = set(z.namelist())
            for skill in SKILLS:
                if target in ARCHIVES:
                    entry = ARCHIVES[target]
                    if entry not in names:
                        errors.append(f"{target}: missing {entry}")
                        continue
                    text = z.read(entry).decode("utf-8")
                else:
                    entry = f"{SKILL_ARCHIVES[target]}/{skill}/SKILL.md"
                    if entry not in names:
                        errors.append(f"{target}: missing {entry}")
                        continue
                    text = z.read(entry).decode("utf-8")
                for heading in originals[skill]:
                    if f"## {heading}" not in text:
                        errors.append(f"{target}/{skill}: missing behavior section {heading}")
    return errors

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--project-root", default=".")
    p.add_argument("--dist", default="dist")
    p.add_argument("--version", required=True)
    a = p.parse_args()
    errors = verify(Path(a.project_root), a.version, Path(a.dist))
    for e in errors:
        print("ERROR:", e)
    print("RUNTIME BEHAVIOR PROJECTION:", "FAIL" if errors else "PASS")
    return bool(errors)

if __name__ == "__main__":
    raise SystemExit(main())

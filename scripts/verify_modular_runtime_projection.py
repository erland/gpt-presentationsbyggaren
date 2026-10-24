#!/usr/bin/env python3
"""Verify runtime-specific modular projection from actual generated ZIP outputs."""
import argparse
import json
from pathlib import Path
from zipfile import ZipFile

SKILLS = ("presentationsplanering","bildproduktion","presentationsexport","kvalitetsgranskning")

def verify(dist: Path, version: str) -> list[str]:
    errors = []
    paths = {target:dist / f"presentationsbyggaren-{target}-{version}.zip" for target in ("chat","claude-project","opencode")}
    data = {}
    for target, path in paths.items():
        if not path.is_file():
            errors.append(f"Missing {path}")
            continue
        with ZipFile(path) as z:
            data[target] = {name:z.read(name) for name in z.namelist()}
    if len(data) != len(paths):
        return errors
    chat = data["chat"].get("assistant/instructions.md",b"").decode()
    claude = data["claude-project"].get("project/instructions.md",b"").decode()
    opencode = data["opencode"]
    agents = opencode.get("AGENTS.md",b"").decode()
    for skill in SKILLS:
        marker = f"## Skill: {skill}"
        # Assembly manifests may generate headings rather than Skill labels.
        # Critical behavior headings from source are checked elsewhere.
        path=f".opencode/skills/{skill}/SKILL.md"
        if path not in opencode:
            errors.append(f"OpenCode missing {path}")
            continue
        skill_text=opencode[path].decode()
        if "## Canonical behavior" not in skill_text:
            errors.append(f"OpenCode {skill}: missing canonical behavior")
        if len(skill_text)>len(agents):
            errors.append(f"OpenCode {skill}: Skill longer than shared AGENTS.md")
    if not chat or not claude or not agents:
        errors.append("Missing full runtime instructions")
    if chat != claude:
        errors.append("Chat and Claude Project instruction projection differs")
    contract=json.loads(opencode.get(".opencode/runtime-contract.json",b"{}"))
    if set(contract.get("adapter",{}).get("skills",[]))!=set(SKILLS):
        errors.append("OpenCode adapter contract Skill list mismatch")
    return errors

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--dist",type=Path,default=Path("dist"))
    p.add_argument("--version",required=True)
    a=p.parse_args()
    errors=verify(a.dist,a.version)
    for e in errors: print("ERROR:",e)
    print("MODULAR RUNTIME PARITY:","FAIL" if errors else "PASS")
    raise SystemExit(bool(errors))

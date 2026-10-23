#!/usr/bin/env python3
"""Regression guard for the generated OpenCode distribution."""
import argparse
from pathlib import Path
from zipfile import ZipFile

def verify(archive: Path) -> list[str]:
    errors=[]
    if not archive.is_file():
        return [f"Missing: {archive}"]
    with ZipFile(archive) as z:
        files=set(z.namelist())
        for name in (".opencode/tools/gpt_presentation_plan_validate.ts", ".opencode/tools/gpt_pptx_validate.ts"):
            if name not in files:
                errors.append(f"Missing OpenCode tool: {name}")
                continue
            wrapper=z.read(name).decode("utf-8")
            for required in ('file: tool.schema.string().min(1)', 'const cmd = ["python3", script, file]', 'path.relative(projectRoot, file)'):
                if required not in wrapper:
                    errors.append(f"{name}: missing {required}")
        if "README.md" not in files:
            errors.append("Missing OpenCode README")
        else:
            readme=z.read("README.md").decode("utf-8")
            if "GPT Byggarens runtime, inte det GPT-projekt" in readme:
                errors.append("OpenCode README incorrectly describes generic builder runtime")
    return errors

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--archive",required=True,type=Path)
    args=parser.parse_args()
    errors=verify(args.archive)
    for error in errors:
        print("ERROR:",error)
    print("OPENCODE WRAPPER REGRESSION:","FAIL" if errors else "PASS")
    return 1 if errors else 0

if __name__=="__main__":
    raise SystemExit(main())

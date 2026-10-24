#!/usr/bin/env python3
"""Selftest for the portable Presentationsbyggaren Engine ZIP."""
from pathlib import Path
import importlib.util
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts"

def load(name):
    path = SCRIPT / (name + ".py")
    if not path.is_file():
        raise RuntimeError(f"Missing engine script: {path}")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    plan = load("validate_presentation_plan")
    pptx = load("validate_pptx")
    with tempfile.TemporaryDirectory() as temp:
        base = Path(temp)
        if not plan.validate(base / "missing-plan.md"):
            raise RuntimeError("Plan validator must reject missing file")
        with zipfile.ZipFile(base / "invalid.pptx", "w") as z:
            z.writestr("invalid.txt", "not a PowerPoint presentation")
        if pptx.validate_pptx(str(base / "invalid.pptx"))["valid"]:
            raise RuntimeError("PPTX validator must reject invalid package")
    print("PRESENTATION ENGINE SELFTEST: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())

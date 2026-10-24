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
    project = load("presentation_project")
    with tempfile.TemporaryDirectory() as temp:
        base = Path(temp)
        (base / "invalid-plan.md").write_text("not a presentation plan", encoding="utf-8")
        if not plan.validate(base / "invalid-plan.md"):
            raise RuntimeError("Plan validator must reject missing file")
        with zipfile.ZipFile(base / "invalid.pptx", "w") as z:
            z.writestr("invalid.txt", "not a PowerPoint presentation")
        if pptx.validate_pptx(str(base / "invalid.pptx"))["valid"]:
            raise RuntimeError("PPTX validator must reject invalid package")
        source = base / "source"
        (source / "project").mkdir(parents=True)
        (source / "slides").mkdir()
        (source / "project/presentation-plan.md").write_text("# Test", encoding="utf-8")
        (source / "project/project-state.json").write_text('{"slides":{"01":{"status":"approved"}}}', encoding="utf-8")
        (source / "project/design-system.json").write_text('{"palette":["navy"]}', encoding="utf-8")
        (source / "slides/slide-01.png").write_bytes(b"test-image")
        archive = base / "project.zip"
        project.pack(source, archive)
        assert project.verify(archive)["slides"] == 1
        restored = base / "restored"
        project.restore(archive, restored)
        assert (restored / "slides/slide-01.png").read_bytes() == b"test-image"
    print("PRESENTATION ENGINE SELFTEST: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())

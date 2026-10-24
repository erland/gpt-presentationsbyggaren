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
    renderer = load("render_slide_layers")
    two_stage = load("validate_two_stage_project")
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
        from PIL import Image
        (source / "slides/slide-02-background.png").parent.mkdir(parents=True, exist_ok=True)
        Image.new("RGB", (1280, 720), "#15243B").save(source / "slides/slide-02-background.png")
        layers = {"schema_version":1, "background":"slides/slide-02-background.png",
                  "output":"slides/slide-02.png",
                  "layers":[{"type":"text","text":"Rubrik 1","box":[0.1,0.1,0.8,0.25],"font_size":48,"color":"#FFFFFF"}]}
        (source / "slides/slide-02.layers.json").write_text(__import__("json").dumps(layers), encoding="utf-8")
        import hashlib
        digest = hashlib.sha256((source / "slides/slide-02-background.png").read_bytes()).hexdigest()
        first = renderer.render(source,"02").read_bytes()
        layers["layers"][0]["text"] = "Rubrik 2"
        (source / "slides/slide-02.layers.json").write_text(__import__("json").dumps(layers), encoding="utf-8")
        second = renderer.render(source,"02").read_bytes()
        assert first != second, "Text update must change composite"
        assert hashlib.sha256((source / "slides/slide-02-background.png").read_bytes()).hexdigest() == digest
        project_state = {"slides":{"03":{
            "render_mode":"ai_two_stage", "status":"approved",
            "background":"slides/slide-03-background.png",
            "final":"slides/slide-03-final.png",
            "text":{"headline":"Testbudskap"},
            "generation":{"background_prompt":"A standalone text-free scene",
                          "final_prompt":"Use exact copy integrated into reference scene",
                          "reference_background":"slides/slide-03-background.png"},
            "approval_recorded":True}}}
        import json
        (source / "project/project-state.json").write_text(json.dumps(project_state), encoding="utf-8")
        (source / "slides/slide-03-background.png").write_bytes(b"background original")
        (source / "slides/slide-03-final.png").write_bytes(b"composited final")
        assert two_stage.validate(source)["validated_two_stage_slides"] == 1
        (source / "slides/slide-03-final.png").unlink()
        try:
            two_stage.validate(source)
        except ValueError as exc:
            assert "final asset missing" in str(exc)
        else:
            raise AssertionError("Missing final must fail validation")
    print("PRESENTATION ENGINE SELFTEST: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())

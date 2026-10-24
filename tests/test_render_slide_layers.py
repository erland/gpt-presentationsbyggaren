"""Executable layered-slide regression tests."""
import importlib.util
import hashlib
import json
from pathlib import Path
import pytest
from PIL import Image

MODULE = Path(__file__).resolve().parents[1] / "scripts/render_slide_layers.py"
spec = importlib.util.spec_from_file_location("render_slide_layers", MODULE)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def setup(tmp_path):
    slides = tmp_path / "slides"
    slides.mkdir()
    bg = slides / "slide-01-background.png"
    Image.new("RGB", (1280, 720), "#12213C").save(bg)
    data = {"schema_version": 1, "background": "slides/slide-01-background.png",
            "output": "slides/slide-01.png",
            "layers": [{"type":"text","text":"Första rubriken","box":[0.08,0.08,0.84,0.20],
                        "font_size":54,"color":"#FFFFFF"}]}
    layers = slides / "slide-01.layers.json"
    layers.write_text(json.dumps(data), encoding="utf-8")
    return bg, layers, data

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def test_text_change_preserves_background(tmp_path):
    bg, layers, data = setup(tmp_path)
    original = sha(bg)
    first = mod.render(tmp_path, "01")
    first_digest = sha(first)
    data["layers"][0]["text"] = "En ny rubrik"
    layers.write_text(json.dumps(data), encoding="utf-8")
    second = mod.render(tmp_path, "01")
    assert sha(bg) == original
    assert sha(second) != first_digest
    assert Image.open(second).size == (1280, 720)

def test_deterministic_and_reject_overwrite(tmp_path):
    bg, layers, data = setup(tmp_path)
    path = mod.render(tmp_path,"01")
    h = sha(path)
    mod.render(tmp_path,"01")
    assert sha(path) == h
    data["output"] = data["background"]
    layers.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(ValueError,match="overwritten"):
        mod.render(tmp_path,"01")

def test_invalid_paths_and_overflow(tmp_path):
    bg,layers,data = setup(tmp_path)
    data["background"] = "../escape.png"
    layers.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(ValueError,match="Unsafe"):
        mod.render(tmp_path,"01")
    data["background"] = "slides/slide-01-background.png"
    data["layers"][0]["box"] = [0.01,0.01,0.02,0.02]
    layers.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(ValueError,match="overflow|exceeds"):
        mod.render(tmp_path,"01")

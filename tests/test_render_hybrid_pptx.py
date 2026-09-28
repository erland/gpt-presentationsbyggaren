from __future__ import annotations

import struct
import sys
import zlib
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from render_hybrid_pptx import parse_presentation_plan, render_hybrid_pptx, render_plan_hybrid_pptx
from validate_pptx import validate_pptx

A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
P_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"


def _png_chunk(kind: bytes, data: bytes) -> bytes:
    return (
        struct.pack(">I", len(data))
        + kind
        + data
        + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
    )


def _write_png(path: Path, width: int = 16, height: int = 9) -> None:
    # Small deterministic RGB PNG; enough to prove image-backed rendering without Pillow.
    raw_rows = []
    for _ in range(height):
        raw_rows.append(b"\x00" + (b"\xe8\xec\xf2" * width))
    payload = b"".join(raw_rows)
    png = (
        b"\x89PNG\r\n\x1a\n"
        + _png_chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
        + _png_chunk(b"IDAT", zlib.compress(payload))
        + _png_chunk(b"IEND", b"")
    )
    path.write_bytes(png)


def test_hybrid_renderer_creates_background_image_and_editable_text(tmp_path: Path) -> None:
    background = tmp_path / "background.png"
    output = tmp_path / "hybrid.pptx"
    _write_png(background)

    spec = {
        "slides": [
            {
                "background": str(background),
                "text": [
                    {
                        "text": "Redigerbar rubrik",
                        "box": {
                            "x_pct": 8,
                            "y_pct": 18,
                            "w_pct": 40,
                            "h_pct": 20,
                        },
                        "font_size_pt": 30,
                        "bold": True,
                        "color": "#223344",
                    }
                ],
            }
        ]
    }

    render_hybrid_pptx(spec, output)

    result = validate_pptx(output)
    assert result["valid"], result["errors"]

    with zipfile.ZipFile(output) as zf:
        names = set(zf.namelist())
        assert any(name.startswith("ppt/media/") for name in names)

        slide_xml = zf.read("ppt/slides/slide1.xml")
        root = ET.fromstring(slide_xml)

        texts = [
            node.text
            for node in root.findall(f".//{{{A_NS}}}t")
            if node.text
        ]
        assert "Redigerbar rubrik" in texts

        # The slide must contain a picture plus at least one ordinary shape/textbox.
        assert root.find(f".//{{{P_NS}}}pic") is not None
        assert root.find(f".//{{{P_NS}}}sp") is not None


def test_presentation_plan_projects_hybrid_slide_to_renderer_spec(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    assets = tmp_path / "assets"
    assets.mkdir()
    _write_png(assets / "slide-02.png")

    spec = parse_presentation_plan(root / "tests" / "presentation-plan-example.md", assets)

    assert len(spec["slides"]) == 1
    slide = spec["slides"][0]
    assert slide["slide_id"] == "02"
    assert slide["text"][0]["text"] == "AI ger information. Du utför arbetet."
    assert slide["text"][0]["box"] == {
        "x_pct": 58.0,
        "y_pct": 24.0,
        "w_pct": 34.0,
        "h_pct": 24.0,
    }
    assert slide["text"][0]["bold"] is True


def test_presentation_plan_renders_editable_text_pptx(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    assets = tmp_path / "assets"
    assets.mkdir()
    _write_png(assets / "slide-02.png")
    output = tmp_path / "from-plan.pptx"

    render_plan_hybrid_pptx(root / "tests" / "presentation-plan-example.md", assets, output)

    result = validate_pptx(output)
    assert result["valid"], result["errors"]

    with zipfile.ZipFile(output) as zf:
        root_xml = ET.fromstring(zf.read("ppt/slides/slide1.xml"))
        texts = [
            node.text
            for node in root_xml.findall(f".//{{{A_NS}}}t")
            if node.text
        ]
        assert "AI ger information. Du utför arbetet." in texts
        assert root_xml.find(f".//{{{P_NS}}}pic") is not None
        assert root_xml.find(f".//{{{P_NS}}}sp") is not None

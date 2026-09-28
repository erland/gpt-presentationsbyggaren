from __future__ import annotations

import struct
import sys
import zlib
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from approve_slide_asset import approve_slide
from render_hybrid_pptx import assert_packaging_ready, parse_presentation_plan, render_hybrid_pptx, render_plan_hybrid_pptx, render_plan_pptx
from validate_pptx import validate_pptx
from validate_presentation_plan import validate as validate_presentation_plan

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



def _approved_plan(source: Path, target: Path) -> Path:
    text = source.read_text(encoding="utf-8")
    text = text.replace("- Next slide: 01", "- Next slide: none")
    text = text.replace("- Slide 01: next", "- Slide 01: approved")
    text = text.replace("- Slide 02: pending", "- Slide 02: approved")
    text = text.replace("- Slide 03: pending", "- Slide 03: approved")
    text = text.replace(
        "- Generation group: anchor-1",
        "- Generation group: anchor-1\n- Approved asset: slide-01-v3.png",
    )
    text = text.replace(
        "- Generation group: slide-02",
        "- Generation group: slide-02\n- Approved asset: slide-02-v2.png",
    )
    text = text.replace(
        "- Generation group: anchor-2",
        "- Generation group: anchor-2\n- Approved asset: slide-03-v4.png",
    )
    target.write_text(text, encoding="utf-8")
    return target

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

    spec = parse_presentation_plan(
        root / "tests" / "presentation-plan-example.md",
        assets,
        {"hybrid-slide"},
    )

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


def test_mixed_plan_packages_image_and_hybrid_slides_in_order(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    assets = tmp_path / "assets"
    assets.mkdir()
    for name in ("slide-01-v3.png", "slide-02-v2.png", "slide-03-v4.png"):
        _write_png(assets / name)

    approved_plan = _approved_plan(
        root / "tests" / "presentation-plan-example.md",
        tmp_path / "approved-plan.md",
    )
    spec = parse_presentation_plan(approved_plan, assets)
    assert [slide["slide_id"] for slide in spec["slides"]] == ["01", "02", "03"]
    assert [slide["render_mode"] for slide in spec["slides"]] == [
        "image-slide",
        "hybrid-slide",
        "image-slide",
    ]
    assert spec["slides"][0]["text"] == []
    assert spec["slides"][1]["text"][0]["text"] == "AI ger information. Du utför arbetet."
    assert spec["slides"][2]["text"] == []

    assert assert_packaging_ready(approved_plan, assets) == {
        "01": "approved",
        "02": "approved",
        "03": "approved",
    }

    output = tmp_path / "mixed.pptx"
    render_plan_pptx(approved_plan, assets, output)

    result = validate_pptx(output)
    assert result["valid"], result["errors"]

    with zipfile.ZipFile(output) as zf:
        slide_names = sorted(
            name
            for name in zf.namelist()
            if name.startswith("ppt/slides/slide") and name.endswith(".xml")
        )
        assert slide_names == [
            "ppt/slides/slide1.xml",
            "ppt/slides/slide2.xml",
            "ppt/slides/slide3.xml",
        ]

        roots = [ET.fromstring(zf.read(name)) for name in slide_names]
        assert all(root.find(f".//{{{P_NS}}}pic") is not None for root in roots)

        texts_per_slide = [
            [node.text for node in root.findall(f".//{{{A_NS}}}t") if node.text]
            for root in roots
        ]
        assert texts_per_slide[0] == []
        assert "AI ger information. Du utför arbetet." in texts_per_slide[1]
        assert texts_per_slide[2] == []


def test_packaging_is_blocked_until_all_visual_slides_are_approved(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    plan = root / "tests" / "presentation-plan-example.md"

    try:
        assert_packaging_ready(plan)
    except ValueError as exc:
        message = str(exc)
        assert "Slide 01: next" in message
        assert "Slide 02: pending" in message
        assert "Slide 03: pending" in message
    else:
        raise AssertionError("Packaging should be blocked for unapproved slides")


def test_render_plan_pptx_does_not_consume_assets_before_approval(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    assets = tmp_path / "assets"
    assets.mkdir()
    for slide_id in ("01", "02", "03"):
        _write_png(assets / f"slide-{slide_id}.png")

    output = tmp_path / "should-not-exist.pptx"
    try:
        render_plan_pptx(root / "tests" / "presentation-plan-example.md", assets, output)
    except ValueError as exc:
        assert "not ready for PPTX packaging" in str(exc)
    else:
        raise AssertionError("Packaging should fail before reading approved assets")

    assert not output.exists()


def test_packaging_requires_explicit_approved_asset_binding(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    source = root / "tests" / "presentation-plan-example.md"
    plan = tmp_path / "approved-without-assets.md"
    text = source.read_text(encoding="utf-8")
    text = text.replace("- Next slide: 01", "- Next slide: none")
    text = text.replace("- Slide 01: next", "- Slide 01: approved")
    text = text.replace("- Slide 02: pending", "- Slide 02: approved")
    text = text.replace("- Slide 03: pending", "- Slide 03: approved")
    plan.write_text(text, encoding="utf-8")

    try:
        assert_packaging_ready(plan)
    except ValueError as exc:
        message = str(exc)
        assert "Slide 01: missing-approved-asset" in message
        assert "Slide 02: missing-approved-asset" in message
        assert "Slide 03: missing-approved-asset" in message
    else:
        raise AssertionError("Approved slides must bind to explicit approved assets")


def test_packaging_uses_exact_approved_asset_version(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    assets = tmp_path / "assets"
    assets.mkdir()
    for name in ("slide-01-v3.png", "slide-02-v2.png", "slide-03-v4.png"):
        _write_png(assets / name)

    # Distractor files must not be picked once Approved asset is present.
    for name in ("slide-01.png", "slide-02.png", "slide-03.png"):
        _write_png(assets / name, width=8, height=8)

    approved_plan = _approved_plan(
        root / "tests" / "presentation-plan-example.md",
        tmp_path / "approved-versioned-plan.md",
    )
    spec = parse_presentation_plan(approved_plan, assets)

    assert [Path(slide["background"]).name for slide in spec["slides"]] == [
        "slide-01-v3.png",
        "slide-02-v2.png",
        "slide-03-v4.png",
    ]
    assert [slide["approved_asset"] for slide in spec["slides"]] == [
        "slide-01-v3.png",
        "slide-02-v2.png",
        "slide-03-v4.png",
    ]


def test_end_to_end_approval_sequence_builds_final_mixed_pptx(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    source_plan = root / "tests" / "presentation-plan-example.md"
    plan = tmp_path / "presentation-plan.md"
    plan.write_text(source_plan.read_text(encoding="utf-8"), encoding="utf-8")

    assets = tmp_path / "assets"
    assets.mkdir()
    for name in ("slide-01-v1.png", "slide-02-v2.png", "slide-03-v1.png"):
        _write_png(assets / name)

    # Simulate the actual user approval flow across all slides.
    approve_slide(plan, "01", "slide-01-v1.png", "02")
    approve_slide(plan, "02", "slide-02-v2.png", "03")
    approve_slide(plan, "03", "slide-03-v1.png", None)

    final_text = plan.read_text(encoding="utf-8")
    assert "- Next slide: none" in final_text
    assert "- Slide 01: approved" in final_text
    assert "- Slide 02: approved" in final_text
    assert "- Slide 03: approved" in final_text
    assert "- Approved asset: slide-01-v1.png" in final_text
    assert "- Approved asset: slide-02-v2.png" in final_text
    assert "- Approved asset: slide-03-v1.png" in final_text
    assert validate_presentation_plan(plan) == []

    # Packaging readiness must now pass using the exact approved versions.
    assert assert_packaging_ready(plan, assets) == {
        "01": "approved",
        "02": "approved",
        "03": "approved",
    }

    spec = parse_presentation_plan(plan, assets)
    assert [Path(slide["background"]).name for slide in spec["slides"]] == [
        "slide-01-v1.png",
        "slide-02-v2.png",
        "slide-03-v1.png",
    ]
    assert [slide["render_mode"] for slide in spec["slides"]] == [
        "image-slide",
        "hybrid-slide",
        "image-slide",
    ]

    output = tmp_path / "presentation.pptx"
    render_plan_pptx(plan, assets, output)

    result = validate_pptx(output)
    assert result["valid"], result["errors"]

    with zipfile.ZipFile(output) as zf:
        slide_names = [
            "ppt/slides/slide1.xml",
            "ppt/slides/slide2.xml",
            "ppt/slides/slide3.xml",
        ]
        roots = [ET.fromstring(zf.read(name)) for name in slide_names]

        # Every slide is image-backed.
        assert all(root.find(f".//{{{P_NS}}}pic") is not None for root in roots)

        # Only the hybrid slide keeps editable presentation text.
        texts_per_slide = [
            [node.text for node in root.findall(f".//{{{A_NS}}}t") if node.text]
            for root in roots
        ]
        assert texts_per_slide[0] == []
        assert "AI ger information. Du utför arbetet." in texts_per_slide[1]
        assert texts_per_slide[2] == []

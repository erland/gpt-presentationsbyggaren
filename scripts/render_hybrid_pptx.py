#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt

SLIDE_WIDTH_IN = 13.333333
SLIDE_HEIGHT_IN = 7.5


def _pct(value: float, total_inches: float):
    return Inches(total_inches * value / 100.0)


def _rgb(hex_value: str) -> RGBColor:
    value = hex_value.strip().lstrip("#")
    if len(value) != 6:
        raise ValueError(f"Expected 6-digit RGB hex color, got: {hex_value}")
    return RGBColor.from_string(value.upper())


def render_hybrid_pptx(spec: dict[str, Any], output_path: str | Path) -> Path:
    """Render image-backed slides with editable native PowerPoint text overlays."""
    output_path = Path(output_path)
    prs = Presentation()
    prs.slide_width = Inches(SLIDE_WIDTH_IN)
    prs.slide_height = Inches(SLIDE_HEIGHT_IN)

    # Remove the default slide if a producer/library ever adds one.
    while prs.slides:
        r_id = prs.slides._sldIdLst[-1].rId
        prs.part.drop_rel(r_id)
        del prs.slides._sldIdLst[-1]

    blank_layout = prs.slide_layouts[6]

    for slide_spec in spec.get("slides", []):
        slide = prs.slides.add_slide(blank_layout)

        background = slide_spec.get("background")
        if background:
            background_path = Path(background)
            if not background_path.is_file():
                raise FileNotFoundError(background_path)
            slide.shapes.add_picture(
                str(background_path),
                0,
                0,
                width=prs.slide_width,
                height=prs.slide_height,
            )

        for item in slide_spec.get("text", []):
            box = item["box"]
            shape = slide.shapes.add_textbox(
                _pct(float(box["x_pct"]), SLIDE_WIDTH_IN),
                _pct(float(box["y_pct"]), SLIDE_HEIGHT_IN),
                _pct(float(box["w_pct"]), SLIDE_WIDTH_IN),
                _pct(float(box["h_pct"]), SLIDE_HEIGHT_IN),
            )
            frame = shape.text_frame
            frame.clear()
            frame.word_wrap = True

            paragraph = frame.paragraphs[0]
            paragraph.text = str(item["text"])

            align = str(item.get("align", "left")).lower()
            from pptx.enum.text import PP_ALIGN
            paragraph.alignment = {
                "left": PP_ALIGN.LEFT,
                "center": PP_ALIGN.CENTER,
                "right": PP_ALIGN.RIGHT,
            }.get(align, PP_ALIGN.LEFT)

            font = paragraph.runs[0].font
            font.name = item.get("font_name", "Aptos")
            font.size = Pt(float(item.get("font_size_pt", 28)))
            font.bold = bool(item.get("bold", False))
            font.color.rgb = _rgb(item.get("color", "#000000"))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    prs.save(output_path)
    return output_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render a reference hybrid PPTX with image backgrounds and editable text overlays."
    )
    parser.add_argument("spec", help="JSON spec containing slides, backgrounds and text boxes")
    parser.add_argument("output", help="Output .pptx path")
    args = parser.parse_args()

    spec_path = Path(args.spec)
    spec = json.loads(spec_path.read_text(encoding="utf-8"))

    # Resolve relative backgrounds from the spec file directory.
    for slide in spec.get("slides", []):
        background = slide.get("background")
        if background and not Path(background).is_absolute():
            slide["background"] = str((spec_path.parent / background).resolve())

    render_hybrid_pptx(spec, args.output)
    print(f"HYBRID PPTX: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

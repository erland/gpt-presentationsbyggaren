#!/usr/bin/env python3
"""Render editable text layers over a preserved image background.

Project-relative paths only. Source background is never edited.
Usage: python scripts/render_slide_layers.py --project DIR --slide 01
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path, PurePosixPath
from PIL import Image, ImageDraw, ImageFont

def safe_path(root: Path, name: str) -> Path:
    p = PurePosixPath(name)
    if (not name or p.is_absolute() or ".." in p.parts or "\\" in name
            or p.as_posix() != name):
        raise ValueError(f"Unsafe project path: {name}")
    target = (root / name).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError("Path leaves project root")
    return target

def validate_layer(layer: dict) -> None:
    if not isinstance(layer, dict) or layer.get("type") != "text":
        raise ValueError("Only text layers are supported")
    if not isinstance(layer.get("text"), str):
        raise ValueError("Text must be a string")
    box = layer.get("box")
    if (not isinstance(box, list) or len(box) != 4 or
        any(not isinstance(v, (float, int)) or isinstance(v, bool) for v in box)):
        raise ValueError("box must be [x,y,width,height] normalized to 0..1")
    x,y,w,h = box
    if min(x,y) < 0 or min(w,h) <= 0 or x+w > 1 or y+h > 1:
        raise ValueError("Text box outside image")
    if layer.get("align", "left") not in ("left", "center", "right"):
        raise ValueError("Invalid alignment")
    if not isinstance(layer.get("font_size", 44), (float, int)) or not 6 <= layer.get("font_size", 44) <= 240:
        raise ValueError("Invalid font size")
    color = layer.get("color", "#FFFFFF")
    if not isinstance(color, str) or len(color) not in (7, 9) or not color.startswith("#"):
        raise ValueError("Invalid color")
    try:
        int(color[1:], 16)
    except ValueError as exc:
        raise ValueError("Invalid color") from exc

def wrap(draw: ImageDraw.ImageDraw, words: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines = []
    for paragraph in words.split("\n"):
        current = ""
        for word in paragraph.split():
            candidate = (current + " " + word).strip()
            if current and draw.textbbox((0,0), candidate, font=font)[2] > max_width:
                lines.append(current)
                current = word
            else:
                current = candidate
        lines.append(current)
    return lines

def render(project: Path, slide: str) -> Path:
    root = project.resolve()
    data = json.loads(safe_path(root, f"slides/slide-{slide}.layers.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        raise ValueError("Unsupported layer schema")
    background = safe_path(root, data["background"])
    output = safe_path(root, data.get("output", f"slides/slide-{slide}.png"))
    if background == output:
        raise ValueError("Background cannot be overwritten")
    with Image.open(background) as source:
        image = source.convert("RGB")
    draw = ImageDraw.Draw(image)
    width, height = image.size
    for layer in data.get("layers", []):
        validate_layer(layer)
        x,y,w,h = layer["box"]
        x0, y0 = round(x*width), round(y*height)
        max_width, max_height = round(w*width), round(h*height)
        # Bundled Pillow commonly finds DejaVuSans; explicit font file is optional.
        font_name = layer.get("font", "DejaVuSans.ttf")
        if "/" in font_name or "\\" in font_name or ".." in font_name:
            raise ValueError("Font must be an installed font name, not a path")
        font = ImageFont.truetype(font_name, round(layer.get("font_size", 44)))
        lines = wrap(draw, layer["text"], font, max_width)
        gap = round(layer.get("line_spacing", 1.15) * font.size)
        if len(lines)*gap > max_height:
            raise ValueError("Text overflows declared box; reduce font or text")
        color = layer.get("color", "#FFFFFF")
        for index, line in enumerate(lines):
            bbox = draw.textbbox((0,0), line, font=font)
            text_width = bbox[2] - bbox[0]
            if text_width > max_width:
                raise ValueError("Unbreakable text exceeds box width")
            align = layer.get("align", "left")
            sx = x0 + (max_width-text_width)//2 if align == "center" else (x0+max_width-text_width if align == "right" else x0)
            draw.text((sx,y0+index*gap), line, font=font, fill=color)
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output, "PNG")
    return output

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--slide", required=True, help="Slide ID such as 01")
    args = parser.parse_args()
    print("RENDER: PASS", render(Path(args.project), args.slide))

if __name__ == "__main__":
    main()

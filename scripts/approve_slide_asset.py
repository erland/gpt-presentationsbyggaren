#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import tempfile
from pathlib import Path

from validate_presentation_plan import validate


def _slide_block_bounds(text: str, slide_id: str) -> tuple[int, int]:
    pattern = re.compile(rf"^### Slide\s+{re.escape(slide_id)}\s+—\s+.+$", re.M)
    match = pattern.search(text)
    if not match:
        raise ValueError(f"Slide {slide_id} does not exist")
    next_match = re.search(r"^### Slide\s+\d{2,3}\s+—\s+.+$", text[match.end():], re.M)
    end = match.end() + next_match.start() if next_match else text.find("## Sources and assumptions", match.end())
    if end < 0:
        end = len(text)
    return match.start(), end


def _replace_rendering_status(text: str, slide_id: str, status: str) -> str:
    pattern = re.compile(rf"^- Slide\s+{re.escape(slide_id)}:\s*[a-z-]+\s*$", re.M)
    if not pattern.search(text):
        raise ValueError(f"Rendering status is missing Slide {slide_id}")
    return pattern.sub(f"- Slide {slide_id}: {status}", text, count=1)


def _replace_next_pointer(text: str, next_slide: str | None) -> str:
    value = next_slide if next_slide is not None else "none"
    pattern = re.compile(r"^- Next slide:\s*(?:\d{2,3}|none)\s*$", re.M)
    if not pattern.search(text):
        raise ValueError("Rendering status is missing '- Next slide: NN|none'")
    return pattern.sub(f"- Next slide: {value}", text, count=1)


def _set_approved_asset(block: str, asset_name: str) -> str:
    if Path(asset_name).is_absolute() or ".." in Path(asset_name).parts:
        raise ValueError("Approved asset must be a safe relative path")
    if not re.search(r"^\*\*Image asset\*\*\s*$", block, re.M):
        raise ValueError("Slide is missing **Image asset** section")

    approved = re.compile(r"^- Approved asset:\s*.+$", re.M)
    if approved.search(block):
        return approved.sub(f"- Approved asset: {asset_name}", block, count=1)

    anchor = re.search(r"^- Generation group:\s*.+$", block, re.M)
    if anchor:
        insert_at = anchor.end()
        return block[:insert_at] + f"\n- Approved asset: {asset_name}" + block[insert_at:]

    image_heading = re.search(r"^\*\*Image asset\*\*\s*$", block, re.M)
    assert image_heading is not None
    insert_at = image_heading.end()
    return block[:insert_at] + f"\n- Approved asset: {asset_name}" + block[insert_at:]


def approve_slide(
    plan_path: str | Path,
    slide_id: str,
    approved_asset: str,
    next_slide: str | None,
) -> Path:
    path = Path(plan_path)
    text = path.read_text(encoding="utf-8")

    if next_slide == slide_id:
        raise ValueError("next_slide must not be the slide being approved")

    # Update exact slide asset binding.
    start, end = _slide_block_bounds(text, slide_id)
    block = _set_approved_asset(text[start:end], approved_asset)
    text = text[:start] + block + text[end:]

    # Update rendering status and next pointer.
    text = _replace_rendering_status(text, slide_id, "approved")
    text = _replace_next_pointer(text, next_slide)

    # Clear any previous next marker before assigning the new one.
    text = re.sub(r"^- Slide\s+(\d{2,3}):\s*next\s*$", r"- Slide \1: pending", text, flags=re.M)
    text = _replace_rendering_status(text, slide_id, "approved")

    if next_slide is not None:
        if not re.search(rf"^### Slide\s+{re.escape(next_slide)}\s+—\s+.+$", text, re.M):
            raise ValueError(f"Next slide {next_slide} does not exist")
        text = _replace_rendering_status(text, next_slide, "next")

    # Validate before replacing the canonical file.
    with tempfile.NamedTemporaryFile("w", suffix=".md", encoding="utf-8", delete=False) as tmp:
        tmp.write(text)
        tmp_path = Path(tmp.name)
    try:
        errors = validate(tmp_path)
    finally:
        tmp_path.unlink(missing_ok=True)

    if errors:
        raise ValueError("Updated presentation plan is invalid: " + "; ".join(errors))

    path.write_text(text, encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Approve a generated slide, bind its exact asset version and advance rendering status."
    )
    parser.add_argument("plan", help="presentation-plan.md to update in place")
    parser.add_argument("--slide", required=True, help="Slide id, e.g. 02")
    parser.add_argument("--asset", required=True, help="Approved relative asset path")
    parser.add_argument("--next", dest="next_slide", help="Next slide id; omit after the final slide")
    args = parser.parse_args()

    approve_slide(args.plan, args.slide, args.asset, args.next_slide)
    print(
        f"APPROVED Slide {args.slide}: {args.asset}; "
        f"next={args.next_slide or 'none'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

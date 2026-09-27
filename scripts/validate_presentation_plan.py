#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
import yaml

REQUIRED_SECTIONS = [
    "# Presentation Plan",
    "## Brief",
    "## Storyline",
    "## Design direction",
    "## Visual system",
    "## Rendering status",
    "## Slides",
    "## Sources and assumptions",
]
REQUIRED_SLIDE_FIELDS = [
    "**Purpose:**",
    "**Message:**",
    "**Pattern:**",
    "**Render mode:**",
    "**Visual priority:**",
    "**Visible text**",
    "**Visual concept**",
    "**Image asset**",
    "**Composition**",
    "**Speaker notes**",
    "**Sources**",
]
VALID_OUTPUTS = {"visual-first", "copilot-handoff", "both"}
VALID_STATUS = {"draft", "planned", "approved", "rendered"}
VALID_RENDERING_STATUS = {"pending", "next", "generated", "approved", "redo", "not-applicable"}


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise ValueError("Missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("Unclosed YAML frontmatter")
    data = yaml.safe_load(text[4:end]) or {}
    return data, text[end + 5:]


def _validate_rendering_status(body: str, slide_ids: list[str]) -> list[str]:
    errors: list[str] = []
    start = body.find("## Rendering status")
    end = body.find("## Slides", start + 1)
    if start < 0 or end < 0:
        return errors
    block = body[start:end]
    declared_next_match = re.search(r"^- Next slide:\s*(\d{2,3}|none)\s*$", block, re.M)
    if not declared_next_match:
        errors.append("Rendering status: missing '- Next slide: NN|none'")
        declared_next = None
    else:
        declared_next = declared_next_match.group(1)

    entries = re.findall(r"^- Slide\s+(\d{2,3}):\s*([a-z-]+)\s*$", block, re.M)
    statuses = {slide_id: status for slide_id, status in entries}

    for slide_id in slide_ids:
        if slide_id not in statuses:
            errors.append(f"Rendering status: missing Slide {slide_id}")
    for slide_id, status in statuses.items():
        if slide_id not in slide_ids:
            errors.append(f"Rendering status: unknown Slide {slide_id}")
        if status not in VALID_RENDERING_STATUS:
            errors.append(f"Rendering status: invalid status for Slide {slide_id}: {status}")

    next_ids = [slide_id for slide_id, status in entries if status == "next"]
    if len(next_ids) > 1:
        errors.append("Rendering status: at most one slide may be 'next'")
    if declared_next == "none" and next_ids:
        errors.append("Rendering status: Next slide is none but a slide is marked next")
    if declared_next not in {None, "none"}:
        if declared_next not in slide_ids:
            errors.append(f"Rendering status: Next slide {declared_next} does not exist")
        if next_ids != [declared_next]:
            errors.append("Rendering status: '- Next slide' must match the single slide marked next")

    active_review = [status for status in statuses.values() if status in {"generated", "redo"}]
    pending = [status for status in statuses.values() if status == "pending"]
    if pending and not active_review and not next_ids:
        errors.append("Rendering status: pending slides require one 'next' slide unless a generated/redo slide awaits user review")

    return errors


def validate(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    try:
        fm, body = parse_frontmatter(text)
    except Exception as exc:
        return [str(exc)]

    for key in ["schema_version", "title", "language", "target_slides", "primary_output", "status"]:
        if key not in fm:
            errors.append(f"Missing frontmatter field: {key}")
    if fm.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if fm.get("primary_output") not in VALID_OUTPUTS:
        errors.append("primary_output must be visual-first, copilot-handoff or both")
    if fm.get("status") not in VALID_STATUS:
        errors.append("status must be draft, planned, approved or rendered")
    if not isinstance(fm.get("target_slides"), int) or fm.get("target_slides", 0) < 1:
        errors.append("target_slides must be a positive integer")

    for section in REQUIRED_SECTIONS:
        if section not in body:
            errors.append(f"Missing section: {section}")

    slide_matches = list(re.finditer(r"^### Slide\s+(\d{2,3})\s+—\s+.+$", body, re.M))
    if not slide_matches:
        errors.append("No slide sections found")
        return errors

    target = fm.get("target_slides")
    if isinstance(target, int) and len(slide_matches) != target:
        errors.append(f"target_slides is {target} but plan contains {len(slide_matches)} slides")

    slide_ids = [match.group(1) for match in slide_matches]
    errors.extend(_validate_rendering_status(body, slide_ids))

    for idx, match in enumerate(slide_matches):
        start = match.start()
        end = slide_matches[idx + 1].start() if idx + 1 < len(slide_matches) else body.find("## Sources and assumptions", start)
        if end < 0:
            end = len(body)
        block = body[start:end]
        title = match.group(0)
        for field in REQUIRED_SLIDE_FIELDS:
            if field not in block:
                errors.append(f"{title}: missing {field}")
        mode_match = re.search(r"\*\*Render mode:\*\*\s*(\S+)", block)
        if mode_match and mode_match.group(1) not in {"image-slide", "hybrid-slide", "native-slide", "copilot-only"}:
            errors.append(f"{title}: invalid Render mode")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("plan")
    args = parser.parse_args()
    errors = validate(Path(args.plan))
    if errors:
        print("PRESENTATION PLAN VALIDATION: FAIL")
        for err in errors:
            print("ERROR:", err)
        return 1
    print("PRESENTATION PLAN VALIDATION: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

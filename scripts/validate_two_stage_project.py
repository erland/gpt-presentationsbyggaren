#!/usr/bin/env python3
"""Validate two-stage slide assets and their declared generation metadata.

Checks file/state consistency, not whether a particular image model truly used a reference.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath

STAGES = {"pending", "background_ready", "final_ready", "approved"}
def _asset(root: Path, name: str) -> Path:
    if not isinstance(name, str) or not name or "\\" in name:
        raise ValueError("Invalid image path")
    p = PurePosixPath(name)
    if p.is_absolute() or ".." in p.parts or p.as_posix() != name or not name.startswith("slides/"):
        raise ValueError("Image path must be project-relative and inside slides/")
    result = (root / name).resolve()
    if not result.is_relative_to(root.resolve()):
        raise ValueError("Image path escapes project")
    if result.suffix.lower() != ".png":
        raise ValueError("Slide image must be PNG")
    return result

def validate(root: Path) -> dict:
    state = json.loads((root / "project/project-state.json").read_text(encoding="utf-8"))
    slides = state.get("slides")
    if not isinstance(slides, dict):
        raise ValueError("Missing slides object")
    checked = 0
    for slide_id, slide in slides.items():
        if not isinstance(slide, dict):
            raise ValueError(f"Invalid slide {slide_id}")
        if slide.get("render_mode") != "ai_two_stage":
            continue  # Earlier or explicitly alternative slide modes remain supported.
        checked += 1
        stage = slide.get("status")
        if stage not in STAGES:
            raise ValueError(f"{slide_id}: unknown stage")
        bg_name = slide.get("background")
        final_name = slide.get("final")
        if not isinstance(bg_name, str) or not isinstance(final_name, str):
            raise ValueError(f"{slide_id}: both asset paths must be declared")
        bg, final = _asset(root, bg_name), _asset(root, final_name)
        if bg == final:
            raise ValueError(f"{slide_id}: background and final must differ")
        if stage in {"background_ready", "final_ready", "approved"} and not bg.is_file():
            raise ValueError(f"{slide_id}: background asset missing")
        if stage in {"final_ready", "approved"} and not final.is_file():
            raise ValueError(f"{slide_id}: final asset missing")
        if stage in {"final_ready", "approved"}:
            gate = slide.get("background_gate")
            if not isinstance(gate, dict):
                raise ValueError(f"{slide_id}: missing background quality gate")
            for key in ("checked", "text_free", "no_text_containers", "single_scene"):
                if gate.get(key) is not True:
                    raise ValueError(f"{slide_id}: background quality gate failed: {key}")
            digest = gate.get("sha256")
            if not isinstance(digest, str) or len(digest) != 64:
                raise ValueError(f"{slide_id}: background checksum missing")
            if hashlib.sha256(bg.read_bytes()).hexdigest() != digest:
                raise ValueError(f"{slide_id}: background checksum mismatch")
        metadata = slide.get("generation")
        if not isinstance(metadata, dict):
            raise ValueError(f"{slide_id}: generation metadata missing")
        if not isinstance(metadata.get("background_prompt"), str) or not metadata["background_prompt"].strip():
            raise ValueError(f"{slide_id}: background prompt missing")
        if not isinstance(metadata.get("final_prompt"), str) or not metadata["final_prompt"].strip():
            raise ValueError(f"{slide_id}: final prompt missing")
        if metadata.get("reference_background") != bg_name:
            raise ValueError(f"{slide_id}: final generation must reference original background")
        if not isinstance(slide.get("text"), dict):
            raise ValueError(f"{slide_id}: structured text missing")
        if "headline" not in slide["text"] or not isinstance(slide["text"]["headline"], str):
            raise ValueError(f"{slide_id}: text headline missing")
        if stage == "approved" and not slide.get("approval_recorded", False):
            raise ValueError(f"{slide_id}: approval record missing")
    return {"validated_two_stage_slides": checked, "total_slides": len(slides)}

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    args = parser.parse_args()
    print("TWO-STAGE VALIDATE: PASS", validate(Path(args.project)))

if __name__ == "__main__":
    main()

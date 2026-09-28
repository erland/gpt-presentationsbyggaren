from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_presentation_plan import validate


def test_example_plan_is_valid() -> None:
    root = Path(__file__).resolve().parents[1]
    assert validate(root / "tests" / "presentation-plan-example.md") == []


def test_missing_visual_system_is_rejected(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    text = (root / "tests" / "presentation-plan-example.md").read_text(encoding="utf-8")
    path = tmp_path / "bad.md"
    path.write_text(text.replace("## Visual system", "## Visual language"), encoding="utf-8")
    assert any("Visual system" in error for error in validate(path))


def test_multiple_next_slides_are_rejected(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    text = (root / "tests" / "presentation-plan-example.md").read_text(encoding="utf-8")
    text = text.replace("- Slide 02: pending", "- Slide 02: next")
    path = tmp_path / "multiple-next.md"
    path.write_text(text, encoding="utf-8")
    errors = validate(path)
    assert any("at most one slide may be 'next'" in error for error in errors)


def test_next_slide_pointer_must_match_status(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    text = (root / "tests" / "presentation-plan-example.md").read_text(encoding="utf-8")
    text = text.replace("- Next slide: 01", "- Next slide: 02")
    path = tmp_path / "mismatch.md"
    path.write_text(text, encoding="utf-8")
    errors = validate(path)
    assert any("must match" in error for error in errors)


def test_generated_slide_can_wait_without_next(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    text = (root / "tests" / "presentation-plan-example.md").read_text(encoding="utf-8")
    text = text.replace("- Next slide: 01", "- Next slide: none")
    text = text.replace("- Slide 01: next", "- Slide 01: generated")
    path = tmp_path / "waiting-review.md"
    path.write_text(text, encoding="utf-8")
    assert validate(path) == []


def test_hybrid_slide_requires_text_layout(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    text = (root / "tests" / "presentation-plan-example.md").read_text(encoding="utf-8")
    text = text.replace(
        "**Text layout**\n- Title: x=58%, y=24%, width=34%, height=24%, style=title-large\n\n",
        "",
    )
    path = tmp_path / "missing-text-layout.md"
    path.write_text(text, encoding="utf-8")
    errors = validate(path)
    assert any("hybrid-slide requires **Text layout**" in error for error in errors)


def test_hybrid_slide_requires_text_free_image_asset(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    text = (root / "tests" / "presentation-plan-example.md").read_text(encoding="utf-8")
    text = text.replace("- Text in image: no\n", "")
    path = tmp_path / "text-in-image.md"
    path.write_text(text, encoding="utf-8")
    errors = validate(path)
    assert any("Text in image: no" in error for error in errors)


def test_hybrid_slide_requires_text_safe_area(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    text = (root / "tests" / "presentation-plan-example.md").read_text(encoding="utf-8")
    text = text.replace("- Text-safe area: right 42% kept visually calm for title overlay\n", "")
    path = tmp_path / "missing-safe-area.md"
    path.write_text(text, encoding="utf-8")
    errors = validate(path)
    assert any("Text-safe area" in error for error in errors)

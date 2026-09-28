from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from approve_slide_asset import approve_slide
from validate_presentation_plan import validate


def _copy_example(tmp_path: Path) -> Path:
    root = Path(__file__).resolve().parents[1]
    target = tmp_path / "presentation-plan.md"
    target.write_text(
        (root / "tests" / "presentation-plan-example.md").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    return target


def test_approve_slide_binds_asset_and_advances_next(tmp_path: Path) -> None:
    plan = _copy_example(tmp_path)

    approve_slide(plan, "01", "slide-01-v3.png", "02")

    text = plan.read_text(encoding="utf-8")
    assert "- Next slide: 02" in text
    assert "- Slide 01: approved" in text
    assert "- Slide 02: next" in text
    assert "- Slide 03: pending" in text

    slide_01 = text[text.index("### Slide 01"):text.index("### Slide 02")]
    assert "- Approved asset: slide-01-v3.png" in slide_01
    assert validate(plan) == []


def test_approve_slide_final_sets_next_to_none(tmp_path: Path) -> None:
    plan = _copy_example(tmp_path)
    text = plan.read_text(encoding="utf-8")
    text = text.replace("- Next slide: 01", "- Next slide: 03")
    text = text.replace("- Slide 01: next", "- Slide 01: approved")
    text = text.replace("- Slide 02: pending", "- Slide 02: approved")
    text = text.replace("- Slide 03: pending", "- Slide 03: next")
    text = text.replace(
        "- Generation group: anchor-1",
        "- Generation group: anchor-1\n- Approved asset: slide-01-v1.png",
    )
    text = text.replace(
        "- Generation group: slide-02",
        "- Generation group: slide-02\n- Approved asset: slide-02-v2.png",
    )
    plan.write_text(text, encoding="utf-8")

    approve_slide(plan, "03", "slide-03-v4.png", None)

    result = plan.read_text(encoding="utf-8")
    assert "- Next slide: none" in result
    assert "- Slide 03: approved" in result
    assert "- Approved asset: slide-03-v4.png" in result
    assert validate(plan) == []


def test_reapproval_replaces_approved_asset_version(tmp_path: Path) -> None:
    plan = _copy_example(tmp_path)

    approve_slide(plan, "01", "slide-01-v1.png", "02")
    approve_slide(plan, "01", "slide-01-v2.png", "02")

    text = plan.read_text(encoding="utf-8")
    slide_01 = text[text.index("### Slide 01"):text.index("### Slide 02")]
    assert "- Approved asset: slide-01-v2.png" in slide_01
    assert "slide-01-v1.png" not in slide_01
    assert validate(plan) == []


def test_approve_slide_rejects_unsafe_asset_path(tmp_path: Path) -> None:
    plan = _copy_example(tmp_path)

    try:
        approve_slide(plan, "01", "../slide-01.png", "02")
    except ValueError as exc:
        assert "safe relative path" in str(exc)
    else:
        raise AssertionError("Unsafe asset path should be rejected")


def test_approve_slide_rejects_unknown_next_slide_without_mutating_plan(tmp_path: Path) -> None:
    plan = _copy_example(tmp_path)
    before = plan.read_text(encoding="utf-8")

    try:
        approve_slide(plan, "01", "slide-01-v1.png", "99")
    except ValueError as exc:
        assert "Next slide 99 does not exist" in str(exc)
    else:
        raise AssertionError("Unknown next slide should be rejected")

    assert plan.read_text(encoding="utf-8") == before

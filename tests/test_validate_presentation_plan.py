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

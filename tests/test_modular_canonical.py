"""Spårbarhetskontroll för föreslagna modulära canonical-källor.

Kör: python -m pytest tests/test_modular_canonical.py -q
Kontrollerar exakt bevarade avsnitt från originalet; detta testar inte runtime-paritet.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assistant/instructions.md"
TARGETS = [ROOT / "canonical/core.md", *(ROOT / "canonical/skills" / n / "behavior.md" for n in (
    "presentationsplanering", "bildproduktion", "presentationsexport", "kvalitetsgranskning"
))]

def sections(text):
    result = {}
    for part in re.split(r"(?=^## )", text, flags=re.M):
        match = re.match(r"## (.+)\n", part)
        if match:
            result[match.group(1)] = part.strip()
    return result

def test_original_sections_preserved_once():
    expected = sections(SOURCE.read_text(encoding="utf-8"))
    # Visual-first was intentionally superseded by the two-stage AI image workflow.
    # All other original canonical sections remain exact-match migration invariants.
    expected.pop("Visual-first", None)
    actual = {}
    for path in TARGETS:
        assert path.is_file(), path
        for heading, section in sections(path.read_text(encoding="utf-8")).items():
            if heading == "Visual-first":
                continue
            if heading not in expected:
                continue
            assert heading not in actual, f"Duplicerat originalavsnitt: {heading}"
            actual[heading] = section
    assert actual == expected, f"Saknade eller ändrade avsnitt: {set(expected) ^ set(actual)}"

def test_no_duplicate_skill_ownership():
    names = [p.parent.name for p in TARGETS[1:]]
    assert len(names) == len(set(names)) == 4


def test_visual_first_intentional_migration_to_two_stage():
    skill=(ROOT/"canonical/skills/bildproduktion/behavior.md").read_text(encoding="utf-8")
    core=(ROOT/"canonical/core.md").read_text(encoding="utf-8")
    assert "bakgrunden som bildreferens" in skill
    assert "inga förberedda" in core.lower() or "utan text, textbehållare" in core
    assert "render_mode: ai_two_stage" in core

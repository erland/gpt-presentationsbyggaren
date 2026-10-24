"""Static regression guards for separate-turn prompt contracts."""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SKILL=(ROOT/"canonical/skills/bildproduktion/behavior.md").read_text(encoding="utf-8")
CORE=(ROOT/"canonical/core.md").read_text(encoding="utf-8")
WORKFLOW=(ROOT/"knowledge/visual-first-workflow.md").read_text(encoding="utf-8")
A=(ROOT/"templates/background-generation.md.tpl").read_text(encoding="utf-8")
B=(ROOT/"templates/text-overlay-edit.md.tpl").read_text(encoding="utf-8")

def test_distinct_prompt_templates_and_inputs():
    assert "{{visual_concept}}" in A and "{{visual_style}}" in A
    assert "{{exact_text}}" not in A
    assert "{{exact_text}}" in B
    assert "{{visual_concept}}" not in B and "{{visual_style}}" not in B
    assert "bifogade ursprungliga bakgrundsbilden" in B

def test_turn_boundary_and_approved_command():
    assert "nytt användarmeddelande" in SKILL
    assert "Lägg på texten enligt planen" in SKILL
    assert "background_ready" in SKILL
    assert "text-overlay-edit.md.tpl" in SKILL
    assert "background-generation.md.tpl" in SKILL
    assert "nytt användarmeddelande" in WORKFLOW

def test_no_claimed_edit_without_evidence():
    assert "PARTIAL" in SKILL
    assert "edit_confirmed" in SKILL
    assert "faktisk bildindata" in SKILL
    assert "separata användarmeddelanden" in CORE

def test_legacy_text_layer_option_retained():
    assert "render_slide_layers.py" in SKILL

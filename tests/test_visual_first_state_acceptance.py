"""Deterministiska scenarier för visual-first state enligt dokumenterat godkännandeflöde.

Verifierar planfilens tillstånd, inte faktisk bildgenerering eller PPTX/PDF.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_presentation_plan import validate

SOURCE=Path(__file__).resolve().parent/"presentation-plan-example.md"

def plan(tmp_path, statuses, pointer):
    text=SOURCE.read_text(encoding="utf-8")
    text=text.replace("- Next slide: 01", f"- Next slide: {pointer}")
    for idx,status in enumerate(statuses,1):
        before="next" if idx==1 else "pending"
        text=text.replace(f"- Slide {idx:02d}: {before}",f"- Slide {idx:02d}: {status}")
    target=tmp_path/"presentation-plan.md"
    target.write_text(text,encoding="utf-8")
    return validate(target)

def test_initial_plan_and_one_generated_slide_waiting(tmp_path):
    assert plan(tmp_path,["next","pending","pending"],"01")==[]
    assert plan(tmp_path,["generated","pending","pending"],"none")==[]

def test_explicit_approval_sets_next_slide(tmp_path):
    assert plan(tmp_path,["approved","next","pending"],"02")==[]
    assert plan(tmp_path,["approved","generated","pending"],"none")==[]
    assert plan(tmp_path,["approved","approved","next"],"03")==[]
    assert plan(tmp_path,["approved","approved","generated"],"none")==[]
    assert plan(tmp_path,["approved","approved","approved"],"none")==[]

def test_change_or_redo_keeps_current_slide_active(tmp_path):
    assert plan(tmp_path,["redo","pending","pending"],"none")==[]

def test_cannot_skip_user_approval(tmp_path):
    errors=plan(tmp_path,["generated","next","pending"],"02")
    assert any("awaiting review cannot coexist" in error for error in errors)

def test_cannot_have_two_outstanding_slide_reviews(tmp_path):
    errors=plan(tmp_path,["generated","generated","pending"],"none")
    assert any("at most one slide may await review" in error for error in errors)

def test_stale_next_pointer_rejected(tmp_path):
    errors=plan(tmp_path,["approved","next","pending"],"03")
    assert any("must match" in error for error in errors)

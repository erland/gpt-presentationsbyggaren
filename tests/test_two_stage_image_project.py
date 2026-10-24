"""Two-stage image workflow contract: files, approval, references, legacy."""
import importlib.util
import hashlib
import json
from pathlib import Path
import pytest
SPEC=importlib.util.spec_from_file_location("two_stage",Path(__file__).resolve().parents[1]/"scripts/validate_two_stage_project.py")
mod=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(mod)

def project(tmp_path,stage="approved"):
    (tmp_path/"project").mkdir()
    (tmp_path/"slides").mkdir()
    (tmp_path/"slides/slide-01-background.png").write_bytes(b"pure background, no text")
    (tmp_path/"slides/slide-01-final.png").write_bytes(b"AI final based on background")
    data={"slides":{"01":{"render_mode":"ai_two_stage","status":stage,
        "background":"slides/slide-01-background.png",
        "final":"slides/slide-01-final.png",
        "text":{"headline":"Ett budskap"},
        "generation":{"background_prompt":"Create a text-free scene; no panels or placeholders",
                      "final_prompt":"Use background as reference; integrate exact copy",
                      "reference_background":"slides/slide-01-background.png"},
        "background_gate":{"checked":True,"text_free":True,"no_text_containers":True,
                           "single_scene":True, "sha256":hashlib.sha256(
                               (tmp_path/"slides/slide-01-background.png").read_bytes()).hexdigest()},
        "approval_recorded":True}}}
    path=tmp_path/"project/project-state.json"
    path.write_text(json.dumps(data),encoding="utf-8")
    return data,path

def test_approved_two_stage_project(tmp_path):
    project(tmp_path)
    assert mod.validate(tmp_path)["validated_two_stage_slides"]==1

def test_background_only_stage_does_not_require_final(tmp_path):
    data,path=project(tmp_path,"background_ready")
    (tmp_path/"slides/slide-01-final.png").unlink()
    assert mod.validate(tmp_path)["validated_two_stage_slides"]==1

def test_final_requires_background(tmp_path):
    project(tmp_path)
    (tmp_path/"slides/slide-01-background.png").unlink()
    with pytest.raises(ValueError,match="background asset missing"):
        mod.validate(tmp_path)

def test_reference_must_match_background(tmp_path):
    data,path=project(tmp_path)
    data["slides"]["01"]["generation"]["reference_background"]="slides/other.png"
    path.write_text(json.dumps(data))
    with pytest.raises(ValueError,match="reference original background"):
        mod.validate(tmp_path)

def test_unapproved_cannot_claim_approved(tmp_path):
    data,path=project(tmp_path)
    data["slides"]["01"]["approval_recorded"]=False
    path.write_text(json.dumps(data))
    with pytest.raises(ValueError,match="approval record missing"):
        mod.validate(tmp_path)

def test_original_background_is_preserved_after_final_change(tmp_path):
    data,path=project(tmp_path)
    bg=tmp_path/"slides/slide-01-background.png"
    old=bg.read_bytes()
    (tmp_path/"slides/slide-01-final.png").write_bytes(b"new text in AI generated final")
    data["slides"]["01"]["text"]["headline"]="Nytt budskap"
    data["slides"]["01"]["status"]="final_ready"
    path.write_text(json.dumps(data))
    assert mod.validate(tmp_path)["validated_two_stage_slides"]==1
    assert bg.read_bytes()==old

def test_legacy_slide_is_supported(tmp_path):
    data,path=project(tmp_path)
    data["slides"]={"01":{"status":"approved","image_asset":"slides/slide-01.png"}}
    path.write_text(json.dumps(data))
    assert mod.validate(tmp_path)["validated_two_stage_slides"]==0

def test_path_traversal_rejected(tmp_path):
    data,path=project(tmp_path)
    data["slides"]["01"]["background"]="../private.png"
    path.write_text(json.dumps(data))
    with pytest.raises(ValueError,match="project-relative"):
        mod.validate(tmp_path)

def test_unchecked_background_blocks_final(tmp_path):
    data,path=project(tmp_path)
    data["slides"]["01"]["background_gate"]["checked"]=False
    path.write_text(json.dumps(data))
    with pytest.raises(ValueError,match="background quality gate failed"):
        mod.validate(tmp_path)

def test_unchecked_text_containers_block_final(tmp_path):
    data,path=project(tmp_path)
    data["slides"]["01"]["background_gate"]["no_text_containers"]=False
    path.write_text(json.dumps(data))
    with pytest.raises(ValueError,match="no_text_containers"):
        mod.validate(tmp_path)

def test_changed_background_blocks_final(tmp_path):
    data,path=project(tmp_path)
    (tmp_path/"slides/slide-01-background.png").write_bytes(b"changed")
    with pytest.raises(ValueError,match="checksum mismatch"):
        mod.validate(tmp_path)

def test_final_without_gate_is_rejected(tmp_path):
    data,path=project(tmp_path)
    del data["slides"]["01"]["background_gate"]
    path.write_text(json.dumps(data))
    with pytest.raises(ValueError,match="missing background quality gate"):
        mod.validate(tmp_path)

import json
from pathlib import Path
import jsonschema

ROOT=Path(__file__).resolve().parents[1]

def test_installed_acceptance_template_and_required_case_coverage():
    schema=json.loads((ROOT/"schemas/installed-plugin-acceptance.schema.json").read_text())
    data=json.loads((ROOT/"tests/fixtures/installed-plugin-acceptance.template.json").read_text())
    jsonschema.Draft202012Validator(schema).validate(data)
    assert len({c["id"] for c in data["cases"]})==10
    assert all(c["status"]=="NOT_RUN" for c in data["cases"])

def test_pass_requires_observation_and_evidence():
    schema=json.loads((ROOT/"schemas/installed-plugin-acceptance.schema.json").read_text())
    data=json.loads((ROOT/"tests/fixtures/installed-plugin-acceptance.template.json").read_text())
    data["cases"][0]["status"]="PASS"
    assert not jsonschema.Draft202012Validator(schema).is_valid(data)
    data["cases"][0]["observed"]="Installerad assistent läste planfilen"
    data["cases"][0]["evidence"]=["Körningslogg från test"]
    assert jsonschema.Draft202012Validator(schema).is_valid(data)

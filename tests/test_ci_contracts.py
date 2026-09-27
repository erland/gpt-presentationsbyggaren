from pathlib import Path
import json, yaml, jsonschema
ROOT=Path(__file__).resolve().parents[1]

def test_canonical_instruction_markers_and_limit():
    cfg=yaml.safe_load((ROOT/'gpt-project.yaml').read_text())
    text=(ROOT/cfg['instructions']['canonical']).read_text()
    assert len(text)<=cfg['runtime']['custom_gpt']['instruction']['max_characters']
    for marker in cfg['instructions']['core_contract']['required_markers']:
        assert marker in text

def test_eval_cases_validate():
    schema=json.loads((ROOT/'schemas/eval-case.schema.json').read_text())
    files=list((ROOT/'evals').rglob('*.yaml'))
    assert len(files)>=9
    for p in files:
        jsonschema.Draft202012Validator(schema).validate(yaml.safe_load(p.read_text()))

def test_runtime_parity_report_validates():
    schema=json.loads((ROOT/'schemas/runtime-parity.schema.json').read_text())
    report=json.loads((ROOT/'reports/runtime-parity.json').read_text())
    jsonschema.Draft202012Validator(schema).validate(report)
    assert report['runtimes']['chatgpt_chat']['release_recommendation']!='do_not_publish'
    assert report['runtimes']['chatgpt_custom']['release_recommendation']!='do_not_publish'

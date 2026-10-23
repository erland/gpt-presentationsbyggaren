from pathlib import Path
import json, yaml, jsonschema
ROOT=Path(__file__).resolve().parents[1]

def test_canonical_instruction_markers_and_limit():
    cfg=yaml.safe_load((ROOT/'gpt-project.yaml').read_text())
    text=(ROOT/cfg['instructions']['canonical']).read_text()
    custom = cfg.get('runtime', {}).get('custom_gpt', {})
    max_chars = custom.get('instruction', {}).get('max_characters')
    if isinstance(max_chars, int):
        assert len(text) <= max_chars
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
    # Historical Custom GPT is no longer an active distribution.
    assert report['runtimes']['openai_plugin']['release_recommendation']!='do_not_publish'

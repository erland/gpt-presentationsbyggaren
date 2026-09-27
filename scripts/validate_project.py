#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
import yaml,jsonschema

def validate_instance(path,schema):
    obj=json.loads(path.read_text()) if path.suffix=='.json' else yaml.safe_load(path.read_text())
    sch=json.loads(schema.read_text())
    jsonschema.Draft202012Validator(sch).validate(obj)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--project-root',default='.')
    root=Path(ap.parse_args().project_root).resolve()
    cfg=yaml.safe_load((root/'gpt-project.yaml').read_text())
    instr=(root/cfg['instructions']['canonical']).read_text()
    for marker in cfg['instructions']['core_contract']['required_markers']:
        assert marker in instr, f'Missing core marker: {marker}'
    assert len(instr)<=cfg['runtime']['custom_gpt']['instruction']['max_characters']
    pairs=[
      ('tests/fixtures/presentation-brief.example.json','schemas/presentation-brief.schema.json'),
      ('tests/fixtures/storyline.example.json','schemas/storyline.schema.json'),
      ('tests/storyboard-example.json','schemas/storyboard.schema.json'),
      ('tests/presentation-generation-example.json','schemas/presentation-generation.schema.json'),
      ('tests/presentation-review-example.json','schemas/presentation-review.schema.json'),
      ('tests/test-manifest.yaml','schemas/test-manifest.schema.json'),
    ]
    for a,b in pairs: validate_instance(root/a,root/b)
    es=json.loads((root/'schemas/eval-case.schema.json').read_text())
    for p in sorted((root/'evals').rglob('*.yaml')):
        jsonschema.Draft202012Validator(es).validate(yaml.safe_load(p.read_text()))
    if (root/'reports/runtime-parity.json').exists():
        validate_instance(root/'reports/runtime-parity.json',root/'schemas/runtime-parity.schema.json')
    print('PROJECT VALIDATION: PASS')
if __name__=='__main__': main()

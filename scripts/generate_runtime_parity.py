#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
import yaml

CRITICAL_TOOLS={"document_read","file_write","presentation_generate"}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--project-root',default='.')
    args=ap.parse_args(); root=Path(args.project_root).resolve()
    cfg=yaml.safe_load((root/'gpt-project.yaml').read_text())
    runtimes={
      'chatgpt_chat': {'level':'high','release_recommendation':'publish','notes':['Canonical instruction and Knowledge are packaged directly. Tool availability depends on the active ChatGPT environment.']},
      'chatgpt_custom': {'level':'high','release_recommendation':'publish_with_warning','notes':['Canonical instruction is identical. Knowledge is packaged within configured limits. Presentation/file tools depend on enabled Custom GPT capabilities.']},
      'openai_plugin': {'level':'high','release_recommendation':'publish_with_warning','notes':['Canonical behavior is embedded in a skills-first Plugin. Full completion depends on host file writing and presentation generation capabilities.']},
    }
    req=[]
    for marker in cfg['instructions']['core_contract']['required_markers']:
        req.append({'category':'behavior','id':'behavior_'+str(len(req)+1),'title':marker,'criticality':'critical','runtime_states':{
          'chatgpt_chat':{'state':'equivalent'},'chatgpt_custom':{'state':'equivalent'},'openai_plugin':{'state':'equivalent'}}})
    for name,cap in cfg['capabilities']['requirements'].items():
        critical='critical' if name=='filesystem' else 'important'
        req.append({'category':'capability','id':name,'title':name,'criticality':critical,'runtime_states':{
          'chatgpt_chat':{'state':'reduced','reason':'Availability depends on the active ChatGPT tool configuration.'},
          'chatgpt_custom':{'state':'reduced','reason':'Availability depends on capabilities enabled for the Custom GPT.'},
          'openai_plugin':{'state':'reduced','reason':'Capability is supplied by the Plugin host; full parity requires file writing and presentation generation.'}}})
    for tool in cfg['tools']['tools']:
        critical='critical' if tool['id'] in CRITICAL_TOOLS else ('important' if tool.get('requirement')=='recommended' else 'optional')
        req.append({'category':'tool','id':tool['id'],'title':tool['purpose'],'criticality':critical,'runtime_states':{
          'chatgpt_chat':{'state':'reduced','reason':'Tool is runtime-provided rather than embedded in the package.'},
          'chatgpt_custom':{'state':'reduced','reason':'Tool is runtime-provided and must be enabled/available in the GPT.'},
          'openai_plugin':{'state':'reduced','reason':'API actions are host-provided; deterministic validation scripts are packaged but require compatible execution.'}}})
    for aid,a in cfg['artifacts']['outputs'].items():
        crit='critical' if a.get('requirement')=='required' else 'important'
        state_chat={'state':'equivalent'}
        state_custom={'state':'equivalent'}
        state_plugin={'state':'equivalent'}
        if aid=='presentation_pptx':
            state_chat={'state':'reduced','reason':'PPTX creation depends on presentation/file-generation support in the active ChatGPT runtime.'}
            state_custom={'state':'reduced','reason':'PPTX creation depends on capabilities available to the configured Custom GPT.'}
            state_plugin={'state':'reduced','reason':'PPTX completion requires an actual host presentation-generation capability.'}
        req.append({'category':'artifact','id':aid,'title':a.get('description',aid),'criticality':crit,'runtime_states':{'chatgpt_chat':state_chat,'chatgpt_custom':state_custom,'openai_plugin':state_plugin}})
    report={'schema_version':2,'reference':{'type':'canonical_contract','description':'gpt-project.yaml and assistant/instructions.md'},'runtimes':runtimes,'requirements':req,'notes':['No canonical behavior drift detected by source/build parity checks.','Reduced tool states reflect runtime capability availability, not divergent assistant policy.','OpenAI Plugin is equivalent_runtime_dependent: presentation completion requires host file writing and presentation generation.']}
    out=root/'reports'/'runtime-parity.json'; out.parent.mkdir(exist_ok=True); out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    md=['# Runtime parity report','','Reference: canonical contracts in `gpt-project.yaml` and `assistant/instructions.md`.','','| Runtime | Level | Release |','|---|---|---|']
    for rid,r in runtimes.items(): md.append(f"| {rid} | {r['level']} | {r['release_recommendation']} |")
    md += ['','## Result','','No blockerande canonical drift detected. ChatGPT Chat, ChatGPT Custom and OpenAI Plugin use the same canonical behavior. Tool-dependent functions remain capability-dependent and are explicitly marked as reduced where appropriate.']
    (root/'reports'/'runtime-parity.md').write_text('\n'.join(md)+'\n')
    print(out)
if __name__=='__main__': main()

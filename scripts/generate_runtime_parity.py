#!/usr/bin/env python3
"""Conservative declared-runtime parity inventory; NOT a host acceptance result."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import yaml

def generate(root: Path):
    cfg=yaml.safe_load((root/"gpt-project.yaml").read_text(encoding="utf-8"))
    candidates=cfg["analysis"]["runtime"]["candidates"]
    enabled={x["runtime_id"]:x for x in candidates if x.get("activate_by_default")}
    actual=set(cfg["runtime_parity"]["registered_runtimes"])
    assert set(enabled)==actual, f"Candidates differ from registered runtimes: {set(enabled) ^ actual}"
    targets={v["runtime_id"] for k,v in cfg["build_system"]["runtime_targets"].items() if k in cfg["build_system"]["targets"]}
    assert targets==actual, f"Build targets differ from registered runtimes: {targets ^ actual}"
    runtimes={rid:{"level":"moderate","release_recommendation":"publish_with_warning",
      "notes":["Declared build target; functionality in this host is not verified."]} for rid in sorted(actual)}
    requirements=[]
    def add(category, key, title, criticality, states):
        requirements.append(dict(category=category,id=key,title=title,criticality=criticality,runtime_states=states))
    def states(kind):
        return {rid:{"state":"reduced","reason":f"{kind} requires functional host-specific verification; packaging alone is insufficient."} for rid in runtimes}
    for ix, marker in enumerate(cfg["instructions"]["core_contract"]["required_markers"],1):
        add("behavior",f"behavior_{ix}",marker,"critical",states("Canonical behavior"))
    for key in cfg["capabilities"]["requirements"]:
        add("capability",key,key,"critical" if key=="filesystem" else "important",states("Capability"))
    for item in cfg["tools"]["tools"]:
        add("tool",item["id"],item["purpose"],"critical" if item["id"] in {"document_read","file_write","presentation_generate"} else "important",states("Tool"))
    for key,item in cfg["artifacts"]["outputs"].items():
        add("artifact",key,item.get("description",key),"critical" if item.get("requirement")=="required" else "important",states("Artifact"))
    report={"schema_version":2,"reference":{"type":"canonical_contract","description":"gpt-project.yaml canonical/core.md and modular Skills"},
       "runtimes":runtimes,"requirements":requirements,
       "notes":["This is a conservative declaration audit, NOT empirical runtime parity or release readiness.",
                "Release requires actual host acceptance tests, slide-level behavior and PPTX/PDF delivery."]}
    out=root/"reports";out.mkdir(exist_ok=True)
    (out/"runtime-parity.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    md=["# Runtime-paritet (deklarativ kontroll)","","**Ingen runtime är funktionellt accepterad enbart genom denna rapport.**","","| Runtime | Status |","|---|---|"]
    for rid in runtimes: md.append(f"| {rid} | Hosttest återstår |")
    md.extend(["","Kör praktiska, värdspecifika tester för plan, bildgodkännande och PPTX/PDF innan release."])
    (out/"runtime-parity.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    return report

def main():
    p=argparse.ArgumentParser();p.add_argument("--project-root",default=".")
    root=Path(p.parse_args().project_root).resolve()
    generate(root)
    print(root/"reports/runtime-parity.json")
if __name__=="__main__":
    main()

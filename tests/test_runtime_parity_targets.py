from pathlib import Path
import json
import yaml

ROOT=Path(__file__).resolve().parents[1]

def test_parity_report_covers_exactly_the_active_build_runtimes():
    cfg=yaml.safe_load((ROOT/"gpt-project.yaml").read_text(encoding="utf-8"))
    report=json.loads((ROOT/"reports/runtime-parity.json").read_text(encoding="utf-8"))
    expected=set(cfg["runtime_parity"]["registered_runtimes"])
    built={v["runtime_id"] for k,v in cfg["build_system"]["runtime_targets"].items() if k in cfg["build_system"]["targets"]}
    assert expected==built==set(report["runtimes"])
    assert "chatgpt_custom" not in expected
    for requirement in report["requirements"]:
        assert set(requirement["runtime_states"])==expected
    for runtime in report["runtimes"].values():
        assert runtime["release_recommendation"]!="publish"

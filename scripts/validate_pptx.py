#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import posixpath
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
REQUIRED_PARTS = {"[Content_Types].xml", "_rels/.rels", "ppt/presentation.xml"}


def _source_part_for_rels(rels_path: str) -> str:
    if rels_path == "_rels/.rels":
        return ""
    directory, name = posixpath.split(rels_path)
    if not directory.endswith("/_rels") or not name.endswith(".rels"):
        return ""
    source_dir = directory[: -len("/_rels")]
    source_name = name[: -len(".rels")]
    return posixpath.join(source_dir, source_name)


def _resolve_target(rels_path: str, target: str) -> str:
    source_part = _source_part_for_rels(rels_path)
    base_dir = posixpath.dirname(source_part)
    if target.startswith("/"):
        return target.lstrip("/")
    return posixpath.normpath(posixpath.join(base_dir, target))


def validate_pptx(path: str | Path) -> dict:
    path = Path(path)
    errors: list[str] = []
    warnings: list[str] = []

    if not zipfile.is_zipfile(path):
        return {"valid": False, "errors": ["Not a readable ZIP/Open XML package"], "warnings": []}

    with zipfile.ZipFile(path) as zf:
        names = set(zf.namelist())
        for required in sorted(REQUIRED_PARTS - names):
            errors.append(f"Missing required package part: {required}")

        if "[Content_Types].xml" in names:
            try:
                root = ET.fromstring(zf.read("[Content_Types].xml"))
                for node in root.findall(f"{{{CT_NS}}}Override"):
                    part = (node.attrib.get("PartName") or "").lstrip("/")
                    if part and part not in names:
                        errors.append(f"Content-Type Override references missing part: {part}")
            except ET.ParseError as exc:
                errors.append(f"Invalid [Content_Types].xml: {exc}")

        for rels_path in sorted(n for n in names if n.endswith(".rels")):
            try:
                root = ET.fromstring(zf.read(rels_path))
            except ET.ParseError as exc:
                errors.append(f"Invalid relationships XML {rels_path}: {exc}")
                continue
            for rel in root.findall(f"{{{REL_NS}}}Relationship"):
                if rel.attrib.get("TargetMode") == "External":
                    continue
                target = rel.attrib.get("Target")
                if not target:
                    warnings.append(f"Relationship without Target in {rels_path}")
                    continue
                resolved = _resolve_target(rels_path, target)
                if resolved not in names:
                    rid = rel.attrib.get("Id", "?")
                    errors.append(
                        f"Relationship {rid} in {rels_path} references missing part: {resolved}"
                    )

    return {"valid": not errors, "errors": errors, "warnings": warnings}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate PPTX Open XML package integrity")
    parser.add_argument("pptx")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    result = validate_pptx(args.pptx)
    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("PPTX VALIDATION:", "PASS" if result["valid"] else "FAIL")
        for item in result["errors"]:
            print("ERROR:", item)
        for item in result["warnings"]:
            print("WARNING:", item)
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())

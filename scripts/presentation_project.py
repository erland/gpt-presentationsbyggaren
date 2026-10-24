#!/usr/bin/env python3
"""Deterministic, portable presentation project ZIP with safe extraction."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import zipfile

REQUIRED = {"project/presentation-plan.md", "project/project-state.json", "project/design-system.json"}
MAX_FILES = 500
MAX_TOTAL = 500 * 1024 * 1024
FIXED_DATE = (2020, 1, 1, 0, 0, 0)

def valid_name(name: str) -> bool:
    p = PurePosixPath(name)
    return bool(name) and not p.is_absolute() and ".." not in p.parts and "\\" not in name and not name.startswith("/") and p.as_posix() == name

def project_files(folder: Path) -> dict[str, bytes]:
    result = {}
    for p in sorted(folder.rglob("*")):
        if not p.is_file():
            continue
        if p.is_symlink():
            raise ValueError("Symlinks are forbidden")
        name = p.relative_to(folder).as_posix()
        if not valid_name(name) or name == "manifest.json":
            raise ValueError(f"Unsafe/reserved path: {name}")
        result[name] = p.read_bytes()
    if not REQUIRED <= result.keys():
        raise ValueError(f"Missing project files: {sorted(REQUIRED - result.keys())}")
    if len(result) > MAX_FILES or sum(map(len, result.values())) > MAX_TOTAL:
        raise ValueError("Project exceeds size limits")
    state = json.loads(result["project/project-state.json"])
    json.loads(result["project/design-system.json"])
    if not isinstance(state, dict) or not isinstance(state.get("slides"), dict):
        raise ValueError("project-state.json requires slides object")
    return result

def pack(folder: Path, output: Path) -> None:
    files = project_files(folder)
    manifest = {"schema_version": 1, "format": "presentationsbyggaren-project",
                "files": {n: hashlib.sha256(data).hexdigest() for n, data in files.items()}}
    with zipfile.ZipFile(output, "w") as z:
        for name, data in [*files.items(), ("manifest.json", (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode())]:
            info = zipfile.ZipInfo(name, FIXED_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data)

def verify(archive: Path) -> dict:
    with zipfile.ZipFile(archive) as z:
        infos = z.infolist()
        names = [i.filename for i in infos]
        if len(names) != len(set(names)) or any(not valid_name(n) for n in names):
            raise ValueError("Unsafe or duplicate ZIP entries")
        if len(infos) > MAX_FILES + 1 or sum(i.file_size for i in infos) > MAX_TOTAL:
            raise ValueError("Archive exceeds size limits")
        for info in infos:
            if info.is_dir() or (info.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError("Directory and symlink entries are not supported")
        manifest = json.loads(z.read("manifest.json"))
        if manifest.get("schema_version") != 1 or manifest.get("format") != "presentationsbyggaren-project":
            raise ValueError("Unknown project format")
        files = manifest.get("files", {})
        if set(files) != set(names) - {"manifest.json"} or not REQUIRED <= set(files):
            raise ValueError("Manifest inventory mismatch")
        for name, digest in files.items():
            if hashlib.sha256(z.read(name)).hexdigest() != digest:
                raise ValueError(f"Checksum mismatch: {name}")
        state = json.loads(z.read("project/project-state.json"))
        json.loads(z.read("project/design-system.json"))
        if not isinstance(state, dict) or not isinstance(state.get("slides"), dict):
            raise ValueError("Invalid project state")
        return {"files": len(files), "slides": len(state["slides"])}

def restore(archive: Path, destination: Path) -> None:
    verify(archive)
    if destination.exists() and any(destination.iterdir()):
        raise ValueError("Destination must be empty")
    destination.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as z:
        for name in z.namelist():
            if name == "manifest.json":
                continue
            p = destination / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(z.read(name))

def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="action", required=True)
    for cmd in ("pack", "verify", "restore"):
        sub.add_parser(cmd)
    parser.add_argument("--source", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()
    if args.action == "verify":
        print("PROJECT VERIFY: PASS", verify(Path(args.source)))
    elif args.action == "pack":
        if not args.output:
            parser.error("--output required")
        pack(Path(args.source), Path(args.output))
        print("PROJECT PACK: PASS", args.output)
    else:
        if not args.output:
            parser.error("--output required")
        restore(Path(args.source), Path(args.output))
        print("PROJECT RESTORE: PASS", args.output)

if __name__ == "__main__":
    main()

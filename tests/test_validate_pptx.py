from __future__ import annotations

import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_pptx import validate_pptx

CT = """<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
</Types>"""
ROOT_RELS = """<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="x" Target="ppt/presentation.xml"/>
</Relationships>"""


def make_package(path: Path, content_types: str = CT, root_rels: str = ROOT_RELS) -> None:
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr("[Content_Types].xml", content_types)
        zf.writestr("_rels/.rels", root_rels)
        zf.writestr("ppt/presentation.xml", "<p:presentation xmlns:p='urn:p'/>")


def test_valid_minimal_package(tmp_path: Path) -> None:
    path = tmp_path / "valid.pptx"
    make_package(path)
    result = validate_pptx(path)
    assert result["valid"], result


def test_missing_content_type_part_is_blocking(tmp_path: Path) -> None:
    path = tmp_path / "missing-part.pptx"
    ct = CT.replace("</Types>", '<Override PartName="/ppt/slideMasters/slideMaster2.xml" ContentType="x"/></Types>')
    make_package(path, content_types=ct)
    result = validate_pptx(path)
    assert not result["valid"]
    assert any("slideMaster2.xml" in error for error in result["errors"])


def test_missing_relationship_target_is_blocking(tmp_path: Path) -> None:
    path = tmp_path / "missing-rel.pptx"
    rels = ROOT_RELS.replace("</Relationships>", '<Relationship Id="rId2" Type="x" Target="ppt/missing.xml"/></Relationships>')
    make_package(path, root_rels=rels)
    result = validate_pptx(path)
    assert not result["valid"]
    assert any("ppt/missing.xml" in error for error in result["errors"])

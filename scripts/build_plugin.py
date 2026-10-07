#!/usr/bin/env python3
"""Build a distribution ZIP containing only public plugin payload files."""
from pathlib import Path
import argparse
import json
import zipfile

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output", type=Path)
args = parser.parse_args()
version = json.loads((root / "plugin.json").read_text())["version"]
output = args.output or root / "dist" / f"anti-defensive-writing-{version}.zip"
output.parent.mkdir(parents=True, exist_ok=True)
files = [root / p for p in ("plugin.json", ".codex-plugin/plugin.json", "LICENSE", "PRIVACY.md")]
files += sorted((root / "skills").rglob("SKILL.md"))
files += sorted((root / "assets").glob("*.svg"))
with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
    for file in files:
        archive.write(file, file.relative_to(root).as_posix())
with zipfile.ZipFile(output) as archive:
    assert archive.testzip() is None
print(output.resolve())

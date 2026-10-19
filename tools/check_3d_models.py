#!/usr/bin/env python3
"""Check footprint 3D model references without changing KiCad files."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
footprints = sorted(root.rglob("*.kicad_mod"))
missing = []
external = []
checked = 0
pattern = re.compile(r'\(model\s+"?([^"\s)]+)"?')
for footprint in footprints:
    text = footprint.read_text(encoding="utf-8", errors="replace")
    for raw in pattern.findall(text):
        checked += 1
        if raw.startswith("${"):
            external.append((footprint.relative_to(root), raw))
            continue
        target = (footprint.parent / raw).resolve()
        if not target.is_file():
            missing.append((footprint.relative_to(root), raw))
print(f"Footprints: {len(footprints)}; 3D references: {checked}")
print(f"External-variable references (manual review): {len(external)}")
print(f"Missing local models: {len(missing)}")
for path, model in missing:
    print(f"MISSING {path}: {model}")
for path, model in external:
    print(f"EXTERNAL {path}: {model}")
sys.exit(1 if missing else 0)

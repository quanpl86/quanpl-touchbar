#!/usr/bin/env python3
"""Deterministic SVG rect pixel-art exporter. Needs Pillow: pip install Pillow."""
import json
import sys
from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "assets/manifest/asset-catalog.json"

def export_item(item):
    src = ROOT / item["source"]
    dst = ROOT / item["target"]
    doc = ET.parse(src).getroot()
    w, h = item["logicalArtPx"]
    scale = 4
    canvas = Image.new("RGBA", (w * scale, h * scale), (0, 0, 0, 0))
    from PIL import ImageDraw
    draw = ImageDraw.Draw(canvas)
    for node in doc:
        if not node.tag.endswith("rect"):
            continue
        x, y = int(node.attrib["x"]), int(node.attrib["y"])
        rw, rh = int(node.attrib["width"]), int(node.attrib["height"])
        if not (x >= 0 and y >= 0 and x + rw <= w and y + rh <= h):
            raise ValueError(f"outside canvas: {src}")
        draw.rectangle((x * scale, y * scale, (x + rw) * scale - 1, (y + rh) * scale - 1), fill=node.attrib["fill"])
    if canvas.size != tuple(item["physicalPx"]):
        raise ValueError("wrong output size")
    dst.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(dst, format="PNG", optimize=False)
    return dst

def main():
    items = json.loads(CATALOG.read_text(encoding="utf-8"))["entries"]
    generated = [export_item(i) for i in items]
    print(f"Exported {len(generated)} transparent pixel PNGs at 4x source resolution")
    if "--check" in sys.argv:
        for i in items:
            with Image.open(ROOT / i["target"]) as im:
                if im.mode != "RGBA" or im.size != tuple(i["physicalPx"]):
                    raise ValueError(f"bad PNG: {i['target']}")
        print("Asset PNG validation passed")

if __name__ == "__main__":
    main()

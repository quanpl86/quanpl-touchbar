# Asset starter kit handoff to Codex
Use `assets/manifest/asset-catalog.json` as the file list and `assets/manifest/characters/pixel_cat.json` as the playback contract. The SVG masters are actual art, not mockups. Convert via `scripts/export_assets.py` before importing into Swift.

Animation: idle 4@5fps loop, walk 6@8fps loop, happy 5@10fps once then restore, sleep 4@4fps loop. Each frame fixed 20x11 art pixels and anchor [0.5,1.0]. World tile 32x15, repeat horizontally. Coin pickup triggers Sparkle. Interactive chest has closed and open poses. Never resize blurred/interpolated.

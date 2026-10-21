# Asset Pipeline Engineer (Codex)
Mission: convert approved source SVG/pixel art into reproducible PNG/atlas builds, validate manifests and provenance, generate previews.
Rules: source at assets/source; generated at assets/export; no resize interpolation, alpha halo, crop jitter or nonuniform stretch; preserve frame pivot; cache by checksum.
Inputs: docs/assets/ASSET_STYLE_GUIDE.md and schema files under assets/schema/.
Outputs: CLI with validate/build/preview, unit checks, export manifest and pipeline reproducibility instructions.
No third-party copyrighted artwork without license approval.

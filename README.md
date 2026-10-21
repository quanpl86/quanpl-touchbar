# QuanPL TouchBar — Character & Interactive Pixel World

A native macOS Touch Bar character companion: choose a pixel-art character and environment, play pre-authored animations, and react to physical touch. Collectibles, interactive props and compact UI extend the world without distracting from normal keyboard use.

> Project state: **Phase 0 — repository and production pipeline bootstrap.** No runnable macOS application has been built or tested yet. This repository contains original project assets/specifications and a Codex engineering backlog.

## Current product scope
- Selectable character packs: first production prototype **Pixel Cat**; Robot and Dino are next.
- Animation controller: idle/walk/run/jump/sleep/happy/special and touch interrupt/return.
- Viewport-aware Touch Bar scene with optional ambient/background mode.
- Terrain/background tiling, pickups, interactive props, VFX and a compact HUD.
- Local settings, bundled and user-imported asset packs, no network dependency for runtime.

## Source of truth
- [Project charter](docs/product/PROJECT_CHARTER.md)
- [Master plan and milestones](docs/management/MASTER_PLAN.md)
- [Decisions and upstream licensing](docs/architecture/ADR-0001-UPSTREAM-AND-LICENSE.md)
- [Touch Bar hardware and rendering constraints](docs/technical/TOUCHBAR_DISPLAY_AND_ASSETS.md)
- [Asset production standards](docs/assets/ASSET_STYLE_GUIDE.md)
- [Codex handoff](docs/engineering/CODEX_HANDOFF.md)
- [Agent instructions](AGENTS.md)
- [Asset registry](assets/manifest/asset-catalog.json)
- [GitHub Issues](https://github.com/quanpl86/quanpl-touchbar/issues)

## Technology decision
Native **Swift 6 + AppKit/NSTouchBar**; start with a small custom pixel-art renderer to validate Touch Bar behavior. SpriteKit remains optional for later game logic. **macOS 13+ is a tentative target, not a tested compatibility claim.** Intel vs Apple Silicon support requires hardware verification.

## Important upstream notice
The reference [Heaaaaaaaa/TouchBar-Pet](https://github.com/Heaaaaaaaa/TouchBar-Pet) is **not copied into this repository**. Its public repository currently does not present a clear reusable license. Public visibility is not permission to relicense, publish or redistribute derivatives. See ADR-0001. Reimplement concepts from scratch or obtain explicit permission before code reuse.

## Asset pipeline
SVG source masters in `assets/source/`; JSON descriptors in `assets/manifest/`; deterministic exported PNG sheets and metadata will be produced by Codex in `assets/export/` when its render pipeline is implemented. Never stretch backgrounds or claim 2170px as guaranteed app viewport width.

## Engineering workflow
1. Read `AGENTS.md` and role instructions under `.agents/roles/`.
2. Implement one scoped GitHub Issue per feature branch; make tests and preview evidence.
3. Open a PR against `main` and include risks, performance measurements and screenshots.
4. Project Director reviews; Project Owner approves release scope. Never auto-merge by default.

Copyright in original project-authored materials remains with their respective authors until a repository-wide license is explicitly selected.

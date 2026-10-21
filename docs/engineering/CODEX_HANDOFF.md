# Codex engineering handoff (2026-10-21)
Open this repository as the active Codex workspace (repository: quanpl86/quanpl-touchbar). At start read AGENTS.md, architecture ADRs, technical measurements, asset style guide and your assigned Issue.

## Team agents and coordination
Agent role configs live in .codex/agents/: engineering_lead, rendering_engineer, animation_engineer, interaction_qa, asset_pipeline. Human-readable instructions also live in .agents/roles/. These are prepared Codex project-side configurations; they are not evidence that remote Codex workspaces or subagents have already executed.
Assign one editing owner per file/folder in any parallel work. Prefer sequential P1->P2 dependency; QA review can parallelize read-only.

## First sprint order
1. P0: confirm hardware/macOS matrix and upstream license policy. Do not copy reference code.
2. P1: scaffold a native SwiftPM/AppKit executable and structured logging (no external deps).
3. P1: Touch Bar presenter public NSTouchBar + preview window, dynamic bounds and backing-scale logger.
4. P2: manifest loader/validation for original assets; SVG -> PNG nearest neighbor export.
5. P2: FSM and renderer; Cat idle/walk/happy/sleep.
6. P3: X-aware hit routing, settings panel, persistence; real device validation.
Each issue = one feature branch = one PR. No skipping acceptance checks.

## PR handoff template
- Issue number & scope
- Exact implementation changes
- Tests run and results (with machine/OS/Xcode)
- Screenshots/recording, comparison to design at 60px physical height
- License/provenance notes
- Known gaps and hardware dependent checks
- Reviewer requests and resulting decisions

## Build/test commands
No Swift app or pipeline has been built yet. Codex must document commands added in its P1 PR; do not claim `swift test` passes until source exists and CI actually runs.

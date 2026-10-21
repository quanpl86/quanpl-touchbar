# Codex project instructions — QuanPL TouchBar

Read README.md, docs/management/MASTER_PLAN.md, docs/technical/TOUCHBAR_DISPLAY_AND_ASSETS.md and docs/architecture/ADR-0001-UPSTREAM-AND-LICENSE.md before modifying code.

## Chain of command
- Project Owner approves scope/release. ChatGPT acts as Product/Design/Architecture/QA reviewer; Codex performs implementation in scoped GitHub Issues.
- Follow GitHub Issues and docs/engineering/CODEX_HANDOFF.md. Do not silently broaden scope.
- For focused work adopt appropriate role specification under .codex/agents/ or .agents/roles/; notify review owner on cross-cutting changes.
- Implementation branch `feat/<issue>-...` or `fix/<issue>-...`; PR into main; do not merge your own PR or bypass review.
- Existing `main` must remain recoverable; no force-push, secrets, credentials, or unreviewed external downloads.

## Nonnegotiable safety/legal
- Upstream Heaaaaaaaa/TouchBar-Pet is reference-only while no explicit redistribution license is verified. DO NOT copy/paste its Swift sources or bundled PNGs into this repo without explicit authorization. Reimplement from APIs/specs independently. Keep provenance of any imported third-party asset.
- Private Touch Bar APIs are experimental and opt-in, behind an isolated adapter with a documented public NSTouchBar fallback. Never claim guaranteed always-on support.
- Never fabricate real-hardware tests. Intel 2020, M1 2020, app bounds, latency, gesture behavior all require evidence.
- Favor offline/local-only behavior. Do not add analytics/network or start on login without explicit product approval.

## Architecture
- Native Swift 6, AppKit, NSTouchBar. Prefer pure Swift models, minimal AppKit boundary; SwiftUI optional for settings.
- Separate CharacterCatalog, AnimationStateMachine, SceneRenderer, TouchInteractionRouter, AssetLoader, SettingsStore and TouchBarPresentation.
- Dynamic view bounds in points; @2x physical reference only. Do not hardcode full width 1085pt or assume 2170px drawing region.
- Pixel art: nearest-neighbor, identical canvas/anchor per animation, transparent RGBA sprites, sRGB, bottom-center anchor; deterministic exports.
- UI touch target width >= 22pt desired, >= 30pt for important controls when possible; X-first hit testing; prefer usable viewport over visual density.

## Definition of done
- Include unit tests for state transitions, manifest validation, hit routing, persistence and viewport layout as relevant.
- Explain tested machine and toolchain; screenshot or log for physical Touch Bar claims.
- Include before/after screenshot or preview GIF for visual PRs, asset source/master + metadata + provenance.
- Update docs/management/STATUS.md and Issue checkboxes; identify unverified cases and risks.
- Do not invent build outcomes. CI is planned but not yet installed.

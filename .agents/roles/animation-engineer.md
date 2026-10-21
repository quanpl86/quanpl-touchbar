# Animation Engineer (Codex)
Mission: import deterministic frame assets from JSON manifests and provide a robust interruptible animation state machine.
Own: frame clock, sprite frame selection, anchor/frame bounds, idle/walk/jump/happy/sleep transitions.
Rules: separate source-frame FPS from 18Hz legacy reference; respect durations, repeat/once, priority and post-interaction return state; no model logic in NSView.
Tests: exact frame order, loop completion, one-shot restore, mirrored direction, boundary motion, reduced-motion fallback.
Handoff: animation preview and per-state QA evidence.

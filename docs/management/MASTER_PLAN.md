# Master Plan & milestone gates
Start 2026-10-21; schedule is sequence-based, **no promised calendar delivery dates**. Owner approval required for major scope changes.

| Phase | Main deliverable | Gate / evidence | Owner |
|---|---|---|---|
| P0 — Bootstrap | repo, technical docs, original asset kit, Issues, Codex rules, license decision | files live on main; ADR and backlog linked | ChatGPT |
| P1 — Platform | minimal Swift macOS executable; Touch Bar view and metrics probe | macOS build; emulator preview; machine identity recorded | Codex |
| P2 — Character | metadata loader; PNG exporter; Cat animation FSM | 4 states deterministic; no frame jitter; tests | Codex + ChatGPT assets |
| P3 — Interactivity | gesture router, settings, persistence | tap/hold/swipe simulated tests and real Touch Bar evidence | Codex |
| P4 — Pixel world | terrain layers, coin/star, chest/portal, particle and HUD | object interactions, no clipped labels, keyboard fallback | Codex + ChatGPT assets |
| P5 — Release candidate | packaging, QA matrix, release notes | owner signs off; regression complete | Codex/ChatGPT |

## Repo policy
main = reviewed integration; working branches = feat/<issue>-topic and fix/<issue>-topic. PR template documents screenshots and tests. All user-visible asset work includes source masters + technical manifest + export validations. Codex owns code; ChatGPT owns product design, asset definitions, review. `main` currently documentation/assets only, not a runnable app.

## Gate P0 blockers
- Upstream TouchBar-Pet license not established: do not copy upstream code/assets.
- Intel or M1 2020 and macOS version unknown: platform compatibility remains unverified.
- Codex workspace not connected/started for this repo: issues are prepared as engineering handoff, not a claim that an agent executed them.

## Reporting
STATUS.md updated after every merged phase PR; ADR required for major architecture changes. No automated merges; project owner approves milestone acceptance.

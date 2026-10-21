# Hardware and QA Evidence Matrix
Status: all entries NOT TESTED until an operator provides device measurements.

| Model | Architecture | macOS | TouchBar physical | NSView bounds | Tested? | Evidence |
|---|---|---|---|---|---|---|
| MacBook Pro 2020 13-inch Intel | Intel x86_64 | TBD | reference 2170×60 | unknown | NO | pending |
| MacBook Pro 2020 13-inch M1 | Apple M1 arm64 | TBD | reference 2170×60 | unknown | NO | pending |
| Preview window (simulated) | any Mac | TBD | 60px simulated | 340/580/800pt cases | NO | pending |

## Acceptance checklist
- view bounds/backing scale logged
- ESC and Control Strip remain accessible as intended
- animation not clipped at edges/corners
- tap/long press/swipe event and interactions do not collide with UI
- no visible scaling blur or frame jitter
- acceptable CPU/energy profile in idle mode
- app restore/quit behavior, private-API failure graceful fallback

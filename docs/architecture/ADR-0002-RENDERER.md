# ADR-0002 — Start with small native AppKit renderer
Status: PROPOSED; 2026-10-21.

Primary: Swift 6 + AppKit + NSTouchBar. PixelRenderer draws pixel-perfect PNG frames onto dynamic NSView bounds with nearest-neighbor. Frame FSM and interaction router remain UIKit/AppKit-independent pure Swift models. SwiftUI may implement settings window only.

Rationale: tiny 30pt Touch Bar does not need game physics. SpriteKit may be added only after documented requirements (physics, high object count, particle collisions) justify integration.

Layers back to front: 0 clear/background, 1 far scenery, 2 far particles, 3 terrain, 4 props, 5 pickups, 6 character, 7 interaction FX, 8 HUD, 9 modal/gesture overlay. Each object has a z and X range for independent hit testing; decoration is not tappable.

Always-on: optional private adapter; report failure and fallback to foreground-app NSTouchBar. No hardcoded screen-wide size.

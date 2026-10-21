# Touch Bar — hardware reference and source-audit measurements (DRAFT)
Reference hardware commonly described as **2170 × 60 physical pixels**, ~1085 × 30 points at @2x. Apple supports 30pt tall Touch Bar content. Width allocated to app is NOT fixed; Escape and Control Strip can consume horizontal space. Verify variant, scale and bounds on target 2020 Mac.
Sources: https://developer.apple.com/documentation/appkit/nstouchbar and https://developer.apple.com/documentation/appkit/creating-and-customizing-the-touch-bar

## Source audit of Heaaaaaaaa/TouchBar-Pet (2026-10-21)
- `PetTouchBarSceneView.intrinsicContentSize`: 640×30pt preference (not guaranteed actual).
- Track: min(max(340,bounds.width-4),580) ×28pt at y=1.
- Status HUD: 122×22pt, at track right; motion zone typically 200..440pt depending on track width.
- 12 invisible NSButton zones for food, separate character touch button and rest button.
- Timer at 1/18s (18Hz target, not measured FPS).
- 5 characters × 3 PNG *poses* each; not complete multiframe animation sheets.
- 4 stretch-to-view backgrounds and 5 food PNGs. Private DFRFoundation bridge for persistent mode.
- NOTE: No source file copied; observations only.

## Production design constraints
1. Call convertToBacking and log view.bounds, scale and pixel rect during runtime.
2. Height must fit 30pt; safe placement baseline y~26pt, scene margin 2pt where feasible.
3. Art grid proposal: 1 logical art px = 2pt = 4 physical px. Character 20×11 art px -> 80×44 physical PNG -> 40×22pt rendered.
4. Max normal character height 12 art px / 48px / 24pt to preserve room for effects; anchors consistently bottom-center.
5. PNG RGBA, sRGB, no resampling blur; nearest neighbor only. Sprite animation frames have identical fixed canvas and pivot; never auto-crop per frame.
6. Treat Touch Bar as a 1D interaction space predominantly X; y useful for visuals, not a robust small hit target.
7. Split UI mode: AMBIENT prioritizes actor; CONTROLS shows buttons; COLLECTION shows pickups; auto-hide HUD or reserve dynamic width.
8. Test three simulated view widths >= 340, 580, 800pt, and actual measured bound on target Mac; do not presume these are exact Apple allocations.

## Proposed asset dimensions at 4× pixel export
| Asset class | Logical art px | PNG physical px | Display pt |
|---|---:|---:|---:|
| small character | 16×10 | 64×40 | 32×20 |
| standard character | 20×11 | 80×44 | 40×22 |
| large character | 24×12 | 96×48 | 48×24 |
| collectible small | 6×6 | 24×24 | 12×12 |
| collectible standard | 8×8 | 32×32 | 16×16 |
| interactive prop | 12×10 | 48×40 | 24×20 |
| terrain tile | 32×15 | 128×60 | 64×30 |
| particle | 4×4 to 8×8 | 16..32 square | 8..16 square |
UI icons can use Retina-native drawings at 2× independent of art grid. Physical Tap target should expand to >=22pt width when possible, even for a visual sprite narrower than 22pt.

## Runtime probe required
Log: model identifier, architecture, OS, NSView.bounds, backingScaleFactor, convertToBacking, Control Strip mode user selection, active frame duration, gesture hit response. Collect screenshots and known test path in docs/qa/DEVICE_MATRIX.md; hardware remains unverified until evidence.

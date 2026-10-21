# TOUCHBAR CHARACTER STUDIO — ASSET & RENDERING SPECIFICATION v1.0 (DRAFT)

**Base repository:** https://github.com/Heaaaaaaaa/TouchBar-Pet  
**Target:** MacBook Pro 2020 with Touch Bar (verify Intel vs M1)  
**Audit date:** 2026-10-21  
**Status:** Source-audited; hardware-dependent values pending real-device validation.  
**Scope:** Character, Terrain, Collectible, Interactive objects, UI, Effects, Animation and interaction hit testing.

## 1. Evidence and confidence levels

- **Hardware reference:** 2170×60 physical pixels, corresponding to 1085×30 points on Retina @2x. Supported by the open-source Touch Bar Preview project and Apple's 30pt/60px asset guidance. Do **not** equate screen-wide width with an app's usable drawing width.
- **Apple platform behavior:** macOS may reserve Escape and the Control Strip; application content width changes with layout and control strip visibility; touch gestures supply primarily meaningful **horizontal X** coordinates. Source: https://developer.apple.com/documentation/appkit/nstouchbar and https://developer.apple.com/documentation/appkit/nstouchbaritem
- **App source:** `Sources/TouchBarPet/*.swift` and `Scripts/extract-pixel-sprites.py` on repo `main` inspected directly. Values marked as current-source facts below.
- **Proposals:** All asset sizes, hitboxes, animation FPS, interaction thresholds and layer conventions in sections 4–10 are **design decisions** for our derivative, not Apple requirements or existing repo behavior.

## 2. Hardware and coordinate units

| Parameter | Reference | Status |
|---|---:|---|
| Touch Bar native strip | 2170 × 60 physical pixels | Reference; verify hardware variant |
| Retina logical dimensions | 1085 × 30 pt | Reference @2x |
| Backing scale | 2 physical px per point | Standard reference; verify actual `convertToBacking` |
| Art unit proposal | 1 art px = 4 physical px = 2 pt | Proposed pixel-art grid |
| Max asset/view height | 30 pt = 60 px | Apple documented |
| Working vertical band | ~2–28 pt, 26pt tall | Proposed 2pt safe insets; legacy track = 1–29pt |
| Physical x-axis | Horizontal | Apple gesture documentation |
| Physical y-axis | Too small to be dependable for direct gesture gameplay | Apple guidance |
| Color/alpha | PNG RGBA, sRGB, transparency | Proposed authoring convention |

**Important warning:** 16 art pixels tall at 4× is 64 physical px / 32pt and therefore too tall for a 30pt Touch Bar. Standard character height should be <= 12 art px (48 physical px / 24pt), with any jumping effects clipped or controlled to stay inside the view.

**Coordinate conventions:** App viewport (not entire screen) has `x=0` at left, `y=0` at top in flipped AppKit view. World entities store normalized X in [0,1] and optional virtual world-Y; actor's anchor defaults bottom-center `[0.5,1]` in PNG. Keep measured point and physical pixel values separate. `renderPt = exportPhysicalPx/2` unless specific scaling policy applies.

## 3. Current TouchBar-Pet source audit (verified in code)

| Code / behavior | Current value / implementation | Notes |
|---|---|---|
| `PetTouchBarSceneView.intrinsicContentSize` | 640 × 30 pt | Preferred NSView size, **not** guaranteed active hardware width |
| `trackRect` | `width=min(max(340,bounds.width-4),580)`, `y=1`, `h=28` pt | At bounds=640pt, 580×28pt / 1160×56 px |
| `statsRect` | 122 × 22pt, x=`trackWidth -130`, y=4 | HUD occupies a large fixed width |
| `motionRect` | `width=max(190,trackWidth-140)`, height 28pt | At track 580pt => 440pt; track 340pt => 200pt |
| Pet hit area | Sprite bounding rectangle expanded 12pt X each side and 8pt Y each side | Overlap must be re-tested in crowded layout |
| Food touch zones | 12 invisible NSButtons distributed equally through motionRect | Coarse touch-position selection, not real item hit testing |
| Update loop | `Timer` at `1/18` sec (~18Hz) | `AppDelegate.startPetLoop()`; actual hardware may differ |
| Character image | Upstream extracted PNG per pose; code fallback pixel drawing | 5 species × 3 poses = 15 PNG sprites |
| Motion | per-species affine/procedural bob, stretch, rotation, opacity | No full multi-frame sprite sheet state machine |
| Background | four PNG images drawn via AppKit with `.interpolation=.none` | Current source stretches image to trackRect, potentially distorting ratio |
| Foods | 5 PNG files; maximum draw size varies by species | Render in points, values below |
| Persistent Touch Bar | Private `DFRFoundation` bridge plus public fallback | Not App Store safe, risks macOS incompatibility |
| Minimum OS in Package.swift | macOS 13 | Upstream README requires Apple Silicon, local target Mac must be confirmed |

### Current image draw boxes by pet (computed from source, point values)

| Pet | Current stable image slot (width × height pt, approximate) |
|---|---|
| Cat | 40.70 × 23.65 |
| Puffer Fish (normal) | 40.20 × 25.80 |
| Ghost | 34.81 × 25.37 |
| Dragon | 40.29 × 22.19 |
| Plant Buddy | 29.15 × 23.06 |

These sizes are *renderer slots*, **not** the pixel dimensions of upstream cropped PNGs. Source PNG dimensions vary because crop/extraction removes surrounding background. Correct final asset format requires fixed-frame exports with normalized pivots to avoid jitter.

### Current food drawing maximum slots (point)

| Pet | Max size pt |
|---|---|
| Cat | 28×18 |
| Puffer Fish | 30×21 |
| Ghost | 25×22 |
| Dragon | 25×21 |
| Plant Buddy | 18×15 |

### Content currently present

- Characters (5): Cat, Puffer Fish, Ghost, Dragon, Plant Buddy.
- Character PNGs (15 poses): `cat-idle`, `cat-walk`, `cat-sleep`, `puffer-idle`, `puffer-swim`, `puffer-puff`, `ghost-idle`, `ghost-dash`, `ghost-sleep`, `dragon-idle`, `dragon-run`, `dragon-fire`, `plant-sprout`, `plant-flower`, `plant-thirsty`.
- Backgrounds (4): `aquarium`, `night`, `grass`, `cozy`.
- Food (5): `cat-fish`, `puffer-pellets`, `ghost-star`, `dragon-meat`, `plant-water`.
- Source concept sheets: 1254×1254px each; `Scripts/extract-pixel-sprites.py` uses defined crop regions. Four background source crop boxes are **1194×82px**; this is **not** the runtime display dimensions.
- Existing small effects: bubbles, flame, sparkle, sun, shadow via AppKit drawing.

**Source correctness issues to fix:** `trackWidth` minimum of 340pt can exceed an NSView narrower than ~344pt; content may clip. Current 12-zone touch mapping ignores individual interactive-object stacking. Current pixel backgrounds may be stretched with nonuniform ratios. Code enumerations and `switch` cases make adding new characters costly.

## 4. Proposed asset standards (v1)

| Asset | Art grid px | Export @4× physical px | Onscreen @2× pt | Alpha |
|---|---:|---:|---:|---|
| Character small | 16×10 | 64×40 | 32×20 | Transparent |
| Character standard | 20×11 | 80×44 | 40×22 | Transparent |
| Character large | 24×12 | 96×48 | 48×24 | Transparent |
| Collectible small | 6×6 | 24×24 | 12×12 | Transparent |
| Collectible standard | 8×8 | 32×32 | 16×16 | Transparent |
| Interactable object | 12×10 | 48×40 | 24×20 | Transparent |
| Terrain tile | 32×15 | 128×60 | 64×30 | Opaque/transparent by layer |
| Particle small | 4×4 | 16×16 | 8×8 | Transparent |
| Particle large | 8×8 | 32×32 | 16×16 | Transparent |

**Pixel art:** nearest-neighbor only; no resampling between non-integer sizes for source art. Use fixed canvas per frame, same anchor across every state, strict 1-frame=1-cell. Keep important contour within ~20–24pt character height. Larger poses need explicit jump offset and clip policy. Store sources in Aseprite/PSD/ase format if available; export PNG RGBA sRGB with unique filenames.

**Scene-specific export:** Use physical 2170×60px full-width *mockup only*. Until macOS actual view width is measured, backgrounds should be designed as tileable segments. For current `trackRect 580×28pt` the bitmap raster reference is **1160×56px**, and for default custom view `640×30pt` it is **1280×60px**; these are distinct values. Avoid using 2170×60 as if the app automatically controlled the full physical strip.

## 5. Asset families and requirements

### A. Character

Required per character: ID, displayName, author/license metadata, category, scale, `anchorNormalized=[0.5,1]`, uniform frame size, idle default, animation descriptions, hitbox/collisionbox, allowed backgrounds, sound toggle, interaction triggers.

Suggested animation frame packs (modifiable after prototype): Idle 6 frames at 6 FPS loop, Walk 8 frames at 10 FPS loop, Run 8 at 12 FPS loop, Jump 6 at 12 FPS once, Sleep 4 at 4 FPS loop, Happy 6 at 12 FPS once, Surprised 4 at 10 FPS once, Hurt 4 at 10 FPS once. Export: `character_id/<animation>.png`, strip of N frames, per frame consistent source grid and metadata. For a standard 80×44px frame, Walk 8 frames horizontally => 640×44px sprite strip. PNG transparent.

Modes: `idle`, `autonomous`, `manual`, `interaction`, `disabled`. State priorities: `critical > touch reaction > special > movement > idle`. One-shot animation returns to previous mode. Separate state transitions from movement speed/time-based updates.

### B. Terrain

Four initial families: Aquarium, Night, Grass, Cozy Room. Each contains (1) background/sky; (2) distant decor/parallax; (3) ground/walkable track with logical collision height; (4) foreground decor; (5) optional ambient effects. Recommend horizontal 128×60 physical tiles as source, repeat/crop without distortion; adapt/crop height to legacy 56px. Do not bake items or UI labels into background images. Use X seam tests at tile boundaries and test variations of viewport width.

### C. Collectible Items

Coins / stars / crystals; 24–32px physical, alpha, 4–8 frames optional. Each item defines ID, rarity/theme, world X, speed (optional), `collectOnOverlap`, `collectOnTap`, pickup hitbox, activation cooldown, triggered effects, persistence policy and sound. Visual collision ≠ touch hit zone. Do not create invisible tap targets that mask the character.

### D. Interactive Items

Food / chest / portal / toy / lamp; 48×40px physical starting format, at least 2–3 pose states (idle, active, disabled). Define triggers such as tap, long press, drag; results can be open, feed, change mood, start animation, transform scene. Use larger invisible horizontal hit box 32–44pt where space allows, **not** a tiny touch target matching icon bounds.

### E. Labels, buttons, badges, status HUD

- Interactive button height 26–28pt (Touch Bar constrained), horizontal hit region ideally 36–44pt, visible icon 16–20pt. A 44×28pt control equals 88×56 physical px. Do not apply general iOS 44×44pt as if 30pt Touch Bar could contain it.
- Labels: short, one-line, preferred 11–12pt; essential text should not fall below Apple's general macOS 10pt guidance. Prefer graphic and number over long localized strings. Stats badge legacy 122×22pt is acceptable only when overall scene width allows it.
- Feedback badges/toasts: max 1 short line, display ~0.6–1.2s, opacity + slide or fade, no modal alerts. Ensure enough foreground/background contrast.
- Settings/character and animation selection should live in the main Mac app; the Touch Bar only presents compact direct interactions. Keep Escape/system controls accessible.

### F. Effects

Spark, heart, puff, star, bubble, dust, shine, pickup flash; 16×16 to 32×32 physical px; 4–8 animation frames for short transient effects; no blur on pixel edges, alpha supported. Draw after gameplay sprites but before HUD. Pool allocations; spawn short life effects and expire promptly.

## 6. Proposed rendering and event order

Layers in descending background-to-foreground z order:

1. Background / sky
2. Parallax
3. Terrain / ground
4. Rear objects
5. Collectibles
6. Characters
7. Foreground interactive objects
8. Particle effects
9. HUD and labels
10. Transparent interaction hit regions (not visually drawn)

Render scene based on measured `bounds`, not screen-wide pixels. Use `NSView` with `isFlipped=true`. Time-based animation engine should decouple source animation FPS from redraw heartbeat; preload/cached images and draw only when needed.

Hit-test priority proposal: UI > dragged item > interactive item > collectible > character > terrain. Tap=default, doubleTap=special (disambiguate from single tap), longPress ~500ms, horizontal swipe distance ~30pt (all thresholds tentative, hardware QA mandatory). Apple guidance says horizontal x is meaningful for gestures; simulate virtual y for gameplay but do **not** require users to identify narrow vertical lanes by finger position.

## 7. Performance profiles (targets, not measured facts)

- Existing code timer is 18Hz. Retain as known functional baseline. For redesign, start with 18–20 redraw Hz; test 30Hz interactive mode on real Mac (CPU/GPU and responsiveness) before committing. Individual animation packs may run at 4–12 frame changes per second. No claim that physical Touch Bar refresh rate equals any of these software rates.
- Pause/reduce work when bar is hidden; cap particle counts; predecode/crop sprite frames once; avoid `NSImage(contentsOf:)` inside drawing loop; debounce persistence rather than writing every frame.
- Test while using Chrome/IDE, waking Touch Bar, resizing available strip, switching apps, and Control Strip changes. Private persistent method may fail by macOS version; retain official `NSTouchBar` fallback.

## 8. Suggested folder layout

```text
TouchBarCharacterStudio/
  Assets/
    Characters/<character-id>/character.json
    Characters/<character-id>/animations/{idle,walk,jump,happy,...}.png
    Terrain/<terrain-id>/{background,parallax,ground,foreground}.png
    Items/Collectibles/<item-id>/{idle,collect}.png
    Items/Interactive/<item-id>/{idle,active,disabled}.png
    Effects/<effect-id>/spritesheet.png
    UI/{icons,badges,states}/
  Engine/{CharacterCatalog,AnimationPlayer,SceneRenderer,TouchHitTester}.swift
  Core/{AssetManifest,AssetValidator,SceneState}.swift
  TouchBar/{TouchBarController,TouchBarSceneView}.swift
  Debug/{DeviceCalibration,BoundsOverlay}.swift
```

See `TouchBar_Asset_Manifest_V1_DRAFT.json` for usable schema example and `TouchBar_Asset_Inventory_V1.csv` for first asset backlog. These files are draft contracts for a redesigned app, **not** manifests already understood by the upstream source.

## 9. Device calibration that must be completed on MacBook 2020

First collect chip/macos/SDK:

```bash
system_profiler SPHardwareDataType | grep -E 'Model Identifier|Chip:|Processor Name:'
sw_vers
xcodebuild -version
```

Then temporarily add the following diagnostic in `PetTouchBarSceneView.layout()` after `super.layout()`:

```swift
let b = self.bounds
let scale = self.window?.backingScaleFactor ?? 2.0
let physicalSize = self.convertToBacking(b).size
NSLog("TBP geometry: view=%0.2fx%0.2f pt, backing=%0.2fx%0.2f px, scale=%0.2f", b.width, b.height, physicalSize.width, physicalSize.height, scale)
```

If the view is not yet attached to a backing window, log only point `bounds` and repeat in `viewDidMoveToWindow()` after attachment. **This is an instrumentation suggestion, not proof that the machine has been measured.** Observe 3 modes: Control Strip visible, Control Strip hidden, forced persistent; record clipping and escaping. Also log redraw/touch latency and test single/double/long press/swipe on physical hardware. Do not infer useable width from 1085pt physical screen reference.

## 10. Source locations and critical migration tickets

- `PetTouchBarSceneView.swift` — replace hardcoded/minmax track widths with adaptive viewport + object hit tests; avoid hidden overlapping buttons.
- `PetBitmapArt.swift` — replace species switch statement/static pose map with package-based sprite atlas/animation descriptors; align pivots.
- `PetEngine.swift` — separate care/pet stats from deterministic animation state machine, make it optional for character-only mode.
- `PetState.swift` — character ID not closed enum; store animation and current state metadata.
- `PetBitmapBackground.swift` — tile/crop horizontally, never stretch pixel terrain to unmatched aspect ratio.
- `PetTouchBarController.swift` — retain public NSTouchBar fallback; isolate private persistent API behind adapter and feature flag.
- `AppDelegate.swift` — retain menu-bar integration, replace hard-coded species menus with loaded character catalog and Settings.
- `Scripts/extract-pixel-sprites.py` — original 1254² concept crops only; new build pipeline needs validated export of frame-based sprite sheets.

**Legal/platform QA:** Public repository presently has no identifiable license in repo root/metadata; explicitly obtain license or permission before redistributing source-derived work. Upstream targets Apple Silicon/macOS 13+; build and run on target Intel/M1 MacBook 2020 before committing to this codebase. Always-present mode uses private APIs; keep it opt-in with fallback and expect compatibility changes.

## 11. Release acceptance criteria

- Sprite sheets aligned/pivot fixed, pure alpha, nearest-neighbor; visual test at 100% physical Touch Bar size.
- Each Character has Idle, Walk, interaction response, Sleep minimum; no frame jitter.
- Terrain seamless at 250, 340, 500, 640pt available widths; no stretched pixels, excessive clipping, missing HUD icons.
- Collectible and interactive item hit regions distinct, priority tested; at least 95% intentional taps successful in representative manual tests (project QA target, not OS guarantee).
- 18Hz baseline passes; no obvious UI jank in foreground/background; CPU/profile results documented before raising frame rate.
- Tap/long press/swipe do not interfere with Escape/System controls; visible physical touch bar tests conducted.
- Source/license/compatibility requirements documented for target hardware and macOS.

## References

- Apple NSTouchBar https://developer.apple.com/documentation/appkit/nstouchbar
- Apple NSTouchBarItem https://developer.apple.com/documentation/appkit/nstouchbaritem
- Apple HIG Accessibility https://developer.apple.com/design/human-interface-guidelines/accessibility
- Hardware pixel preview/reference https://github.com/touchbar/Touch-Bar-Preview
- Base source https://github.com/Heaaaaaaaa/TouchBar-Pet
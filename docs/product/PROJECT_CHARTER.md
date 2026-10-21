# Project Charter — TouchBar Character Studio
Status: APPROVED DIRECTION / engineering acceptance pending. 2026-10-21.

## Product mission
Transform the MacBook Pro 2020 Touch Bar into a tiny, expressive character world. Users select a character, background and allowed animations in an accessible macOS UI, then interact with the character directly on Touch Bar.

## Users, jobs and boundaries
- Solo owner/personal use first, offline and self-buildable.
- Main tasks: choose character -> configure idle sequence -> observe -> tap/swipe -> get visual response -> resume normal.
- Later: world scenes, collectibles and usable props.
- Not in MVP: game currency, online sync, accounts, paid marketplace, public App Store delivery.

## MVP acceptance
1. Device probe records macOS, CPU architecture, physical/backing scale, viewport bounds and Control Strip mode.
2. Render original Pixel Cat with at least idle/walk/happy/sleep frame animations and one configurable background.
3. Tap character -> Happy one-shot, then resume prior idle/walk. Touch-empty should not fire character action.
4. Settings switch animation enable/disable, playback speed and character selection; saved locally.
5. App survives being hidden/minimized; public Touch Bar availability documented; persistent support is an optional experiment.
6. First preview demonstrable without physical device; real device validation documented separately.

## Roadmap
P0 foundations/legal + specs; P1 app skeleton/renderer; P2 character/animation; P3 interaction and settings; P4 scenes/items/UI; P5 export/QA packaging.

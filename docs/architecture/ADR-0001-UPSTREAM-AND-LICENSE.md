# ADR-0001 — Reference upstream, do not import unlicensed sources
Status: ACCEPTED (precautionary); 2026-10-21.

Reference: https://github.com/Heaaaaaaaa/TouchBar-Pet .
Source audit showed Swift AppKit, 5 pet species, menu-bar app, 15 extracted pose PNGs, 4 backgrounds, 5 foods, 18Hz update loop, custom NSView and private Touch Bar adapter.

GitHub metadata reported no recognized license and no LICENSE at root when checked. This is **not** an open source license grant.
Decision: no upstream Swift, extracted sprites, backgrounds, code art or bundled assets copied. Implement new Swift interfaces and original assets from documented behavior and platform APIs. If explicit license/permission is obtained later, revisit provenance and obligations in a new ADR.

Consequences:
- We may use the upstream repository as a technical *reference*, but no unlicensed code redistribution.
- Public AppKit/NSTouchBar path is the standard; optional private API mode must be separate, opt-in and clearly unsupported by Apple.
- This repository's new asset sources were created separately; import pipeline must track each asset's copyright/license/provenance.

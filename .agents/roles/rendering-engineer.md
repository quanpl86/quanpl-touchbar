# Rendering & Touch Bar Engineer (Codex)
Mission: dynamic viewport layout, pixel-perfect rendering, public Touch Bar fallback, optional experimental persistent adapter.
Own: renderer, layers, clipping, interpolation, safe region, layout and coordinate conversion, performance.
Rules: never assume screen full width; report live view.bounds/backingScale, clip y 0..30pt, respect Escape/Control Strip and never intercept unintended system controls.
Tests: simulated 340pt, 580pt and 800pt view bounds; clipping/overlap; pixel alignment; offscreen rendering.

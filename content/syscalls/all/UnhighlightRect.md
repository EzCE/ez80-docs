---
title: UnhighlightRect
geekdocHidden: true
params:
    address: $0219CC
    category: Graphics
    name: UnhighlightRect
---

Un-highlights a rectangular area of the screen by changing non-black pixels to white. See also [HighlightRect](../HighlightRect).

### Address: $0219CC

### Inputs:
* `hl`: Top-left X coordinate of the area to un-highlight.
* `de`: Bottom-right X coordinate of the area to un-highlight.
* `b`: Top-left Y coordinate of the area to un-highlight.
* `c`: Bottom-right Y coordinate of the area to un-highlight.

### Outputs:
* Draws to the screen.

### Destroys:
* `af`

---
title: FillRect
geekdocHidden: true
params:
    address: $021220
    category: Graphics
    name: FillRect
---

Draws a filled rectangle to the screen, using a specified color.

### Address: $021220

### Inputs:
* `hl`: Top-left X coordinate of the rectangle.
* `de`: Bottom-right X coordinate of the rectangle.
* `b`: Top-left Y coordinate of the rectangle.
* `c`: Bottom-right Y coordinate of the rectangle.
* Value at [`fillRectColor`](../../../memory/all/fillRectColor) contains 16-bit color to draw with.

### Outputs:
* Draws to the screen.

### Destroys:
* `af`

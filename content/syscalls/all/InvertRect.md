---
title: InvertRect
geekdocHidden: true
params:
    address: $02121C
    category: Graphics
    name: InvertRect
---

### Address: $02121C

Inverts the colors of a rectangular area on the screen.

### Inputs:
* `hl`: Top-left X coordinate of the rectangle.
* `de`: Bottom-right X coordinate of the rectangle.
* `b`: Top-left Y coordinate of the rectangle.
* `c`: Bottom-right Y coordinate of the rectangle.

### Outputs:
* Draws to the screen.

### Destroys:
* `af`

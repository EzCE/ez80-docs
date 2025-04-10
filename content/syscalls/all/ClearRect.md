---
title: ClearRect
geekdocHidden: true
params:
    address: $021218
    category: Graphics
    name: ClearRect
---

Draws a solid white filled rectangle to the screen.

This call behaves the same as:
```plain
push hl
ld.sis hl, $FFFF
ld.sis (fillRectColor), hl
pop hl
call FillRect
```

### Address: $021218

### Inputs:
* `hl`: Top-left X coordinate of the rectangle.
* `de`: Bottom-right X coordinate of the rectangle.
* `b`: Top-left Y coordinate of the rectangle.
* `c`: Bottom-right Y coordinate of the rectangle.

### Outputs:
* Value at [`fillRectColor`](../../../memory/all/fillRectColor) is loaded with `$FFFF`.
* Draws to screen.

### Destroys:
* `af`

---
title: DrawThickRectBorder
geekdocHidden: true
params:
    address: $021B04
    category: Graphics
    name: DrawThickRectBorder
---

### Address: $021B04

Draws a two-pixel rectangular border by drawing the specified outline and a second outline one pixel farther out on each side. See also [DrawRectBorder](../DrawRectBorder). Note that calling this routine also disables interrupts.

{{< hint type=note >}}
Pass ordered corners (hl, b) and (de, c) with hl ≤ de and b ≤ c. Reversed coordinates can cause drawing artifacts or screen corruption.
{{< /hint >}}

### Inputs:
* `hl`: Top-left X coordinate of the inner rectangle.
* `de`: Bottom-right X coordinate of the inner rectangle.
* `b`: Top-left Y coordinate of the inner rectangle.
* `c`: Bottom-right Y coordinate of the inner rectangle.
* Value at [`drawFGColor`](../../../memory/all/drawFGColor) contains the 16-bit color to draw with.

### Outputs:
* Draws to the screen.
* `hl` and `b` are decremented by one.
* `de` and `c` are incremented by one.

### Destroys:
* `af`

{{< hint type=note >}}
With `bufferOnly` set, no writes to the LCD framebuffer, `plotSScreen`, or `saveSScreen` were observed.
{{< /hint >}}
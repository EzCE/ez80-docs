---
title: DrawRectBorder
geekdocHidden: true
params:
    address: $02123C
    category: Graphics
    name: DrawRectBorder
---

### Address: $02123C

Draws a one-pixel rectangular border to the screen, using a specified color. See also [DrawThickRectBorder](../DrawThickRectBorder). Note that calling this routine also disables interrupts.

{{< hint type=note >}}
Pass ordered corners (hl, b) and (de, c) with hl ≤ de and b ≤ c. Reversed coordinates can cause drawing artifacts or screen corruption.
{{< /hint >}}

`_DrawRectBorder_` (`$0216DC`) and `_DrawRectBorder__` (`$021BE0`) jump to the same implementation as `_DrawRectBorder`.

### Inputs:
* `hl`: Top-left X coordinate of the rectangle.
* `de`: Bottom-right X coordinate of the rectangle.
* `b`: Top-left Y coordinate of the rectangle.
* `c`: Bottom-right Y coordinate of the rectangle.
* Value at [`drawFGColor`](../../../memory/all/drawFGColor) contains the 16-bit color to draw with.

### Outputs:
* Draws to the screen.

### Destroys:
* `af`

{{< hint type=note >}}
With `bufferOnly` set, no writes to the LCD framebuffer, `plotSScreen`, or `saveSScreen` were observed.
{{< /hint >}}
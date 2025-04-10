---
title: DrawTILogo
geekdocHidden: true
params:
    address: $021B00
    category: Graphics
    name: DrawTILogo
---

Draws the Texas Instruments logo and text, along with copyright info if specified.

### Address: $021B00

### Inputs:
* `a`: Set to 0 to display copyright info.
* `c`: Distance (in pixels) from the bottom of the screen to the top coordinate to begin drawing at.
* `OP1`: Data for displaying copyright info.

### Outputs:
* Draws to the screen.

### Destroys:
* `af`, `bc`, `de`, `hl`, `ix`.

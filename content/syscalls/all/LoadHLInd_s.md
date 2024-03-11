---
title: LoadHLInd_s
geekdocHidden: true
params:
    address: $020138
    category: Load
    name: LoadHLInd_s
---

Loads the 16-bit value pointed to by the address in `hl` into `hl`, and loads `hlu` with $00.

### Address: $020138

### Inputs:
* `hl`: Contains address.

### Outputs:
* `hl`: Contains 16-bit value pointed to by address.

### Destroys:
* `a`

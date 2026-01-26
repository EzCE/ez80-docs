---
title: ArcChk
geekdocHidden: true
params:
    address: $022040
    category: System
    name: ArcChk
---

### Address: $022040

Finds the amount of free archive space and stores it to [tempFreeArc](../../../memory/all/tempFreeArc).

### Inputs:
* None

### Outputs:
* [tempFreeArc](../../../memory/all/tempFreeArc): Contains 3 bytes with the number amount of free bytes of Archive remaining.

### Destroys:
* `af`, `bc`, `de`, `hl`

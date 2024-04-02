---
title: SizeWind
geekdocHidden: true
params:
    address: $020180
    category: Context
    name: SizeWind
---

This routine calls the current context's [Window Size Change](../../../memory/all/cxSizeWind) vector.

### Address: $020180

### Inputs:
* [`cxSizeWind`](../../../memory/all/cxSizeWind): Context's current Window Size Change vector.

### Outputs:
* Calls the vector.

### Destroys:
* Depends on the vector.

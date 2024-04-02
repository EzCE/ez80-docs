---
title: ErrorEP
geekdocHidden: true
params:
    address: $020184
    category: Context
    name: ErrorEP
---

This routine calls the current context's [Error EP](../../../memory/all/cxErrorEP) vector.

### Address: $020184

### Inputs:
* [`cxErrorEP`](../../../memory/all/cxErrorEP): Context's current Error EP vector.

### Outputs:
* Calls the vector.

### Destroys:
* Depends on the vector.


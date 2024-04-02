---
title: PPutawayPrompt
geekdocHidden: true
params:
    address: $020174
    category: Context
    name: PPutawayPrompt
---

This routine calls the current context's [Partial PutAway](../../../memory/all/cxPPutAway) vector, [PutAway](../../../memory/all/cxPutAway) vector, and then resets the `promptEdit` flag. It is equivalent to this:

```asm
call PPutAway
call PutAway
res promptEdit, (iy + promptFlags)
```

### Address: $020174

### Inputs:
* [`cxPPutAway`](../../../memory/all/cxPPutAway): Context's current Partial PutAway vector.
* [`cxPutAway`](../../../memory/all/cxPutAway): Context's current PutAway vector.

### Outputs:
* Calls the listed vectors and resets `prompEdit`.

### Destroys:
* Depends on vectors.

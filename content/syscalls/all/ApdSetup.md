---
title: ApdSetup
geekdocHidden: true
params:
    address: $021144
    category: System
    name: ApdSetup
---

Resets the APD counter. The value loaded depends on the status of the flag at bit 1 of `ti.flags + $41` (`$D000C1`). If the flag is reset, the value is loaded with `$49`. If the flag is set, the value is loaded with `$1E1`.

### Address: $021144

### Inputs:
* None

### Outputs:
* Value at [apdTimer](../../../memory/all/apdTimer) contains the reset value.

### Destroys:
* `hl`

---
title: monFlags
geekdocHidden: true
params:
    address: $D00081 (ti.flags + $01)
    name: monFlags
---

Monitor flags.

### Address: $D00081 (ti.flags + $01)

### Size: 1 byte

#### Bit 4 - monAbandon:
Appears to be set if the calculator is about to turn off. It is also set to prohibit starting any long process in PutAway.

---
title: tblFlags
geekdocHidden: true
params:
    address: $D00093 (ti.flags + $13)
    name: tblFlags
---

Table flags.

### Address: $D00093 (ti.flags + $13)

### Size: 1 byte

#### Bit 4 - autoFill:
Set for prompt, reset for FillAuto.

#### Bit 5 - autoCalc:
Set for prompt, reset for CalcAuto.

#### Bit 6 - reTable:
Set if table needs to be recomputed, reset if not.

---
title: ParsFlag
geekdocHidden: true
params:
    address: $D00086 (ti.flags + $06)
    name: ParsFlag
---

#### Bit 5 - listOpen:
Set by the parser when currently inside a `{...}` (list) block, then unset once outside.

#### Bit 6 - matrixOpen1:
Set by the parser when currently inside a `[[...]]` (matrix) block, then unset once outside.

#### Bit 7 - matrixOpen2:
Set by the parser when currently inside a `[...]` (matrix) block, then unset once outside.

### Address: $D00086 (ti.flags + $06)

### Size: 1 byte

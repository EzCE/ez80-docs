---
title: fmtFlags
geekdocHidden: true
params:
    address: $D0008A (ti.flags + $0A)
    name: fmtFlags
---

This section also has a related section at `$D0008B` (`ti.flags + $0B`) called `fmtOverride`, which is a copy of `fmtFlags` with conversion override.

#### Bit 0 - fmtExponent:
Set to show exponent, reset for no exponent.

#### Bit 1 - fmtEng:
Set for engineering notation, reset for scientific notation.

#### Bit 5 - fmtReal:
Set for real number format.

#### Bit 6 - fmtRect:
Set for rectangular graph mode.

#### Bit 7 - fmtPolar:
Set for polar graph mode.

### Address: $D0008A (ti.flags + $0A)

### Size: 1 byte

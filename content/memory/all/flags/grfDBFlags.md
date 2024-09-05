---
title: grfDBFlags
geekdocHidden: true
params:
    address: $D00084 (ti.flags + $04)
    name: grfDBFlags
---

### Address: $D00084 (ti.flags + $04)

### Size: 1 byte

#### Bit 0 - grfDot:
Set for dot, reset for line.

#### Bit 1 - grfSimul:
Set for simultaneous, reset for sequential.

#### Bit 2 - grfGrid:
Set if grid is on, reset if grid is off.

#### Bit 3 - grfPolar:
Set for polar coordinates, reset for rectangular coordinates

#### Bit 4 - grfNoCoord:
Set to not display coordinates, reset if coordinates are displayed.

#### Bit 5 - grfNoAxis:
Set to not display an axis, reset if axis is displayed.

#### Bit 6 - grfLabel:
Set for axis labels, reset if axis labels are off.

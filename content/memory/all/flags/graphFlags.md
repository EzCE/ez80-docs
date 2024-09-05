---
title: graphFlags
geekdocHidden: true
params:
    address: $D00083 (ti.flags + $03)
    name: graphFlags
---

### Address: $D00083 (ti.flags + $03)

### Size: 1 byte

#### Bit 0 - graphDraw:
Set if the graph is dirty, reset if valid.

#### Bit 2 - graphCursor:
Set if the cursor is currently being displayed on the graph, reset otherwise.

---
title: sGrFlags
geekdocHidden: true
params:
    address: $D00094 (ti.flags + $14)
    name: sGrFlags
---

Graph split flags.

### Address: $D00094 (ti.flags + $14)

### Size: 1 byte

#### Bit 0 - grfSplit:
Set for split graph, reset for normal.

#### Bit 1 - vertSplit:
Set for vertical (left - right) graph split.

#### Bit 2 - grfSChanged:
Set if graph has just changed from split mode <-> normal mode.

#### Bit 3 - grfSplitOverride:
Set to ignore grfSplit flag if set.

#### Bit 4 - write_on_graph:
Set if text or equ is writing to the graph screen.

#### Bit 5 - g_style_active:
Set if graph styles are enabled and should be used.

#### Bit 6 - cmp_mod_box:
Set if doing mod box plot computation.

#### Bit 7 - textWrite

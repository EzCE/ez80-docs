---
title: plotFlag3
geekdocHidden: true
params:
    address: $D000BC (ti.flags + $3C)
    name: plotFlag3
---

### Address: $D000BC (ti.flags + $3C)

### Size: 1 byte

#### Bit 0 - bufferOnly:
Reset by [`AppSetup`](../../../../syscalls/all/AppSetup).

#### Bit 4 - useFastCirc:
Set to use fast circle algorithm, reset otherwise.

---
title: kbdFlags
geekdocHidden: true
params:
    address: $D00080 (ti.flags + $00)
    name: kbdFlags
---

#### Bit 3 - kbdSCR:
Set if a keypress has been scanned and is ready for [`GetCSC`](../../../../syscalls/all/GetCSC) to return. This flag is then reset after [`GetCSC`](../../../../syscalls/all/GetCSC) is called.

#### Bit 4 - kbdKeyPress:
Set if a key has been pressed.

### Address: $D00080 (ti.flags + $00)

### Size: 1 byte

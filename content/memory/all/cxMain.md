---
title: cxMain
geekdocHidden: true
params:
    address: $D007CA
    name: cxMain
---

This section of memory holds a pointer to the current context's Main vector. It is usually set with [`AppInit`](../../../syscalls/all/AppInit). The Main vector is usually called by the system monitor to handle keypresses.

### Address: $D007CA

### Size: 3 bytes

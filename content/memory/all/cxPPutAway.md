---
title: cxPPutAway
geekdocHidden: true
params:
    address: $D007CD
    name: cxPPutAway
---

### Address: $D007CD

This section of memory holds a pointer to the current context's Partial PutAway vector. It is usually set with [`AppInit`](../../../syscalls/all/AppInit). The Partial PutAway vector is used for exiting edit buffers.

### Size: 3 bytes

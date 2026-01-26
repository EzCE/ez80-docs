---
title: cxErrorEP
geekdocHidden: true
params:
    address: $D007D6
    name: cxErrorEP
---

### Address: $D007D6

This section of memory holds a pointer to the current context's Error EP vector. It is usually set with [`AppInit`](../../../syscalls/all/AppInit). The Error EP vector is used to process errors.

### Size: 3 bytes

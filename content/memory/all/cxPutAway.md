---
title: cxPutAway
geekdocHidden: true
params:
    address: $D007D0
    name: cxPutAway
---

This section of memory holds a pointer to the current context's PutAway vector. It is usually set with [`AppInit`](../../../syscalls/all/AppInit). The PutAway vector is used to clean up the context / app right before exiting. In the OS, this is usually as a response to <kbd>2nd</kbd> + <kbd>on</kbd> (turning the calculator off) or <kbd>2nd</kbd> + <kbd>mode</kbd> (quit).

### Address: $D007D0

### Size: 3 bytes

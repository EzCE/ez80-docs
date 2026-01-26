---
title: cxSizeWind
geekdocHidden: true
params:
    address: $D007D9
    name: cxSizeWind
---

### Address: $D007D9

This section of memory holds a pointer to the current context's Window Size Change vector. It is usually set with [`AppInit`](../../../syscalls/all/AppInit). The Window Size Change vector is called when the window size changes, for example if <kbd>2nd</kbd> + <kbd>sto→</kbd> (rcl) is used.

### Size: 3 bytes

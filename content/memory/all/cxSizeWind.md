---
title: cxSizeWind
geekdocHidden: true
params:
    address: $D007D9
    name: cxSizeWind
---

This section of memory holds a pointer to the current context's Window Size Change vector. It is usually set with [`AppInit`](../../../syscalls/all/AppInit). The Window Size Change vector is called when the window size changes, for example if <kbd>2nd</kbd> + <kbd>sto→</kbd> (rcl) is used.

### Address: $D007D9

### Size: 3 bytes

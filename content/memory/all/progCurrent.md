---
title: progCurrent
geekdocHidden: true
params:
    address: $D0082D
    name: progCurrent
---

Holds the name of the currently selected program in the OS programs menu, or app in the OS apps menu. The first byte is a variable type, such as `ProgObj`, `ProtProgObj`, or `AppObj`, and the the remaining 8 bytes are the file name. The name is zero terminated as long as it is under 8 bytes.

If the name is exactly 8 bytes long, it will not always be zero terminated. This is because the two bytes after `progCurrent` are a 16-bit value that seems to be modified by the <kbd>alpha</kbd> + function keys.

This is also used when launching apps with `NewContext0`.

### Address: $D0082D

### Size: 9 bytes

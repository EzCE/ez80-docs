---
title: shiftFlags
geekdocHidden: true
params:
    address: $D00092 (ti.flags + $12)
    name: shiftFlags
---

Flags for <kbd>2nd</kbd> and <kbd>alpha</kbd>.

### Address: $D00092 (ti.flags + $12)

### Size: 1 byte

#### Bit 3 - shift2nd:
Set if <kbd>2nd</kbd> has been pressed.

#### Bit 4 - shiftAlpha:
Set if <kbd>alpha</kbd> has been pressed.

#### Bit 5 - shiftLwrAlph:
Set for lowercase, reset for uppercase.

#### Bit 6 - shiftALock:
Set for alpha-lock.

#### Bit 7 - shiftKeepAlph:
Set if alpha shift cannot be canceled.

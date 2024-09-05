---
title: textFlags
geekdocHidden: true
params:
    address: $D00085 (ti.flags + $05)
    name: textFlags
---

### Address: $D00085 (ti.flags + $05)

### Size: 1 byte

#### Bit 1 - textEraseBelow:
Set to erase line below small font characters.

#### Bit 2 - textScrolled:
Set if screen is scrolled.

#### Bit 3 - textInverse:
Set to display inverse font bitmap.

#### Bit 4 - textInsMode:
Set for insert mode, reset for overstrike.

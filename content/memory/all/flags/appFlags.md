---
title: appFlags
geekdocHidden: true
params:
    address: $D0008D (ti.flags + $0D)
    name: appFlags
---

#### Bit 0 - appWantIntrpt:
Set to want on key interrupts.

#### Bit 1 - appTextSave:
Set to save characters in textShadow.

#### Bit 2 - appAutoScroll:
Set to auto-scroll text on last line.

#### Bit 3 - appMenus:
Set to process keys that bring up menus, reset to check lock menu flag.

#### Bit 4 - appLockMenus:
Set to ignore menu keys, reset to switch to home screen and bring up menu.

#### Bit 5 - appCurGraphic:
Set for graphic cursor.

#### Bit 6 - appCurWord:
Set for text cursor to cover entire word.

#### Bit 7 - appExit:
Set for application to handle exit key itself.

### Address: $D0008D (ti.flags + $0D)

### Size: 1 byte

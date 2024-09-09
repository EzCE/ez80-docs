---
title: APIFlg
geekdocHidden: true
params:
    address: $D000A8 (ti.flags + $28)
    name: APIFlg
---

### Address: $D000A8 (ti.flags + $28)

### Size: 1 byte

#### Bit 0 - appAllowContext:
Set if app wants context changes to happen.

#### Bit 4 - appRunning:
Set if app is currently running.

#### Bit 7 appRetKeyOff:
Set for GetKey to return kOff when <kbd>2nd</kbd> + <kbd>on</kbd> is pressed.

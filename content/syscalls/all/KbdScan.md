---
title: KbdScan
geekdocHidden: true
params:
    address: $020148
    category: Keyboard
    name: KbdScan
---

### Address: $020148

Scans the keyboard for any key presses and updates the value at [`kbdScanCode`](../../../memory/all/kbdScanCode) accordingly. An interactive keypad with all key values (including scan codes) can be found [here](../../../other/keypad).

### Inputs:
* None.

### Outputs:
* Value at [`kbdScanCode`](../../../memory/all/kbdScanCode) contains scan code.

### Destroys:
* `hl`, `bc`, `a`

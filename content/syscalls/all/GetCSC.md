---
title: GetCSC
geekdocHidden: true
params:
    address: $02014C
    category: Keyboard
    name: GetCSC
---

This routine loads the current keyboard scancode from [`kbdScanCode`](../../../memory/all/kbdScanCode) into `a`, then clears [`kbdScanCode`](../../../memory/all/kbdScanCode). If no key is pressed, `a` is loaded with $00. Note that calling this routine will also enable interrupts. An interactive keypad with all key values (including scan codes) can be found [here](../../../other/keypad).

### Address: $02014C

### Inputs:
* None.

### Outputs:
* `a`: Current scancode.
* `hl`: [`kbdScanCode`](../../../memory/all/kbdScanCode) address.
* [`kbdScanCode`](../../../memory/all/kbdScanCode): Loaded with $00.
* [`kbdSCR`](../../../memory/all/flags/kbdFlags#bit-3---kbdscr) flag reset.

### Destroys:
* `a`, `hl`

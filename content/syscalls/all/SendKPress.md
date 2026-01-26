---
title: SendKPress
geekdocHidden: true
params:
    address: $02015C
    category: System
    name: SendKPress
---

### Address: $02015C

This routine performs very similarly to [`Mon`](../Mon), with the exception that it allows an initial key to be sent to [`cxMain`](../../../memory/all/cxMain). Unlike [`MonForceKey`](../MonForceKey), which handles special keys and runs through the raw key hook, `SendKPress` passes the keypress directly to `cxMain`.

{{< hint type=caution >}}
If this routine is called, it will not return.
{{< /hint >}}

### Inputs:
* `a`: [Keypress](../../../other/keypad) to simulate.
* [`AppAllowContext`](../../../memory/all/flags/APIFlg#bit-0---appallowcontext): Set to allow [`Mon`](../Mon) to pass context keys, to the [`cxMain`](../../../memory/all/cxMain) routine.
* [`curLock`](../../../memory/all/flags/curFlags#bit-4---curlock): Set to lock the cursor off.

### Outputs:
* None.

### Destroys:
* This routine does not return.

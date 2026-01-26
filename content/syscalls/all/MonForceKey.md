---
title: MonForceKey
geekdocHidden: true
params:
    address: $020158
    category: System
    name: MonForceKey
---

### Address: $020158

This routine performs very similarly to [`Mon`](../Mon), with the exception that it allows an initial key to be sent to [`cxMain`](../../../memory/all/cxMain).

{{< hint type=caution >}}
If this routine is called, it will not return.
{{< /hint >}}

### Inputs:
* `a`: Initial [keypress](../../../other/keypad) to send.
* [`AppAllowContext`](../../../memory/all/flags/APIFlg#bit-0---appallowcontext): Set to allow `Mon` to pass context keys, to the [`cxMain`](../../../memory/all/cxMain) routine.
* [`curLock`](../../../memory/all/flags/curFlags#bit-4---curlock): Set to lock the cursor off.

### Outputs:
* None.

### Destroys:
* This routine does not return.

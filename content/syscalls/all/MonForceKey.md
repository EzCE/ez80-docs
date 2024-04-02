---
title: MonForceKey
geekdocHidden: true
params:
    address: $020158
    category: System
    name: MonForceKey
---

This routine performs very similarly to [`Mon`](../Mon), with the exception that it allows an initial key to be sent to [`cxMain`](../../../memory/all/cxMain).

{{< hint type=caution >}}
If this routine is called, it will not return.
{{< /hint >}}

### Address: $020158

### Inputs:
* `a`: Initial keypress to send.
* `AppAllowContext`: Set to allow `Mon` to pass context keys, to the [`cxMain`](../../../memory/all/cxMain) routine.
* `CurLock`: Set to lock the cursor off.

### Outputs:
* None.

### Destroys:
* This routine does not return.

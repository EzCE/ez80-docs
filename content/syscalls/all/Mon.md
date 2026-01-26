---
title: Mon
geekdocHidden: true
params:
    address: $020154
    category: System
    name: Mon
---

### Address: $020154

This routine starts the system monitor. The system monitor takes over the system, and reports events to the active application via the monitor vectors. These vectors can be set prior to the `Mon` routine using [`AppInit`](../AppInit).

{{< hint type=caution >}}
If this routine is called, it will not return.
{{< /hint >}}

### Inputs:
* [`AppAllowContext`](../../../memory/all/flags/APIFlg#bit-0---appallowcontext): Set to allow `Mon` to pass context keys, to the [`cxMain`](../../../memory/all/cxMain) routine.
* [`curLock`](../../../memory/all/flags/curFlags#bit-4---curlock): Set to lock the cursor off.

### Outputs:
* System monitor takes over the system.

### Destroys:
* This routine does not return.

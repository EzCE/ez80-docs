---
title: Mon
geekdocHidden: true
params:
    address: $020154
    category: System
    name: Mon
---

This routine starts the system monitor. The system monitor takes over the system, and reports events to the active application via the monitor vectors. These vectors can be set prior to the `Mon` routine using [`AppInit`](../AppInit).

{{< hint type=caution >}}
If this routine is called, it will not return.
{{< /hint >}}

### Address: $020154

### Inputs:
* `AppAllowContext`: Set to allow `Mon` to pass context keys, to the [`cxMain`](../../../memory/all/cxMain) routine.
* `CurLock`: Set to lock the cursor off.

### Outputs:
* System monitor takes over the system.

### Destroys:
* This routine does not return.

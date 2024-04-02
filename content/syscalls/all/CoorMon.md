---
title: CoorMon
geekdocHidden: true
params:
    address: $020150
    category: System
    name: CoorMon
---

This routine performs very similarly to [`Mon`](../Mon), with the exception that it does the following first:

```asm
res g_style_active, (iy + sGrFlags)
call CursorOff
call CoorDisp
```

Afterwards, [`Mon`](../Mon) is run.

It appears that this routine is used in menu contexts, such as the programs, math, or catalog menus. It is triggered when the menu is entered or exited, along with when the cursor is moved.

{{< hint type=caution >}}
If this routine is called, it will not return.
{{< /hint >}}

### Address: $020150

### Inputs:
* `AppAllowContext`: Set to allow `Mon` to pass context keys, to the [`cxMain`](../../../memory/all/cxMain) routine.
* `CurLock`: Set to lock the cursor off.
* Possibly more?

### Outputs:
* System monitor takes over the system.

### Destroys:
* This routine does not return.

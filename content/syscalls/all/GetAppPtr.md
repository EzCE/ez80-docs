---
title: GetAppPtr
geekdocHidden: true
params:
    address: $022224
    category: Apps
    name: GetAppPtr
---

Gets the pointer of an app with the name specified in [`progCurrent + 1`](../../../memory/all/progCurrent). It is likely that the first byte of [`progCurrent`](../../../memory/all/progCurrent) will be `ti.AppObj`, though this call doesn't care about it.

{{< hint type=caution >}}
This call expects the name to be zero terminated, but the name in [`progCurrent`](../../../memory/all/progCurrent) will not always be zero terminated if it is 8 bytes long. It is recommended to load [`progCurrent + 9`](../../../memory/all/progCurrent) with 0 just to be safe.
{{< /hint >}}

### Address: $022224

### Inputs:
* [`progCurrent + 1`](../../../memory/all/progCurrent): Name of app to find pointer for.

### Outputs:
* `hl`: Contains pointer to app if found, otherwise 0.
* [Carry Flag](../../../instructions/flags#c-carry): Reset if app is found, set otherwise.

### Destroys:
* `af`, `bc`, `de`, `hl`.

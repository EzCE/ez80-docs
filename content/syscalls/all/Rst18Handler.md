---
title: Rst18Handler
geekdocHidden: true
params:
    address: $020114
    category: System
    name: Rst18Handler
---

This routine is jumped to following `di \ rsmix` as a result of the [`rst 18`](../../../instructions/processor-control/#rst) instruction.

{{< hint type=warning >}}
Using this call will cause a crash.
{{< /hint >}}

### Address: $020114

### Inputs:
* None.

### Outputs:
* Causes the calculator to crash.

### Destroys:
* All RAM is reset.

---
title: Rst30Handler
geekdocHidden: true
params:
    address: $020120
    category: System
    name: Rst30Handler
---

This routine is jumped to following `di \ rsmix` as a result of the [`rst 30`](../../../instructions/processor-control/#rst) instruction.

{{< hint type=warning >}}
Using this call will cause a crash.
{{< /hint >}}

### Address: $020120

### Inputs:
* None.

### Outputs:
* Causes the calculator to crash.

### Destroys:
* All RAM is reset.

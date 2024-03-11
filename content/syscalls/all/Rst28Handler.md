---
title: Rst28Handler
geekdocHidden: true
params:
    address: $02011C
    category: System
    name: Rst28Handler
---

This routine is jumped to following `di \ rsmix` as a result of the [`rst 28`](../../../instructions/processor-control/#rst) instruction.

{{< hint type=warning >}}
Using this call will cause a crash.
{{< /hint >}}

### Address: $02011C

### Inputs:
* None.

### Outputs:
* Causes the calculator to crash.

### Destroys:
* All RAM is reset.

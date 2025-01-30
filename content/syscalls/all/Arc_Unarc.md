---
title: Arc_Unarc
geekdocHidden: true
params:
    address: $021448
    category: Variables
    name: Arc_Unarc
---

Swaps a specified variable between RAM and Archive.

{{< hint type=note >}}
Throws an OS error if any problem is encountered, including attempting to pass a variable which cannot be archived / unarchived.
{{< /hint >}}

### Address: $021448

### Inputs:
* OP1: Type and name of the variable to swap.

### Outputs:
* Swaps variable between RAM and Archive.

### Destroys:
* `af`, `bc`, `de`, `hl`
* OP3

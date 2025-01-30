---
title: ArchiveVar
geekdocHidden: true
params:
    address: $02144C
    category: Variables
    name: ArchiveVar
---

Archives a specified variable. This is a subroutine of [Arc_Unarc](../Arc_Unarc).

### Address: $02144C

### Inputs:
* Uses the outputs of [ChkFindSym](../ChkFindSym).

### Outputs:
* Archives the variable.

### Destroys:
* `af`, `bc`, `de`, `hl`

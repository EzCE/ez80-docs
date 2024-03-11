---
title: CpHLDE
geekdocHidden: true
params:
    address: $02013C
    category: Arithmetic
    name: CpHLDE
---

Compares a 24-bit value in `hl` to a 24-bit value in `de`. The output is similar to the [`cp`](../../../instructions/arithmetic/#cp) instruction.

### Address: $02013C

### Inputs:
* `hl`: Value.
* `de`: Comparison value.

### Outputs:
* Z flag: Set if `hl` and `de` are equal.
* C flag: Set if `hl` is less than or equal to `de`, reset if `hl` is greater than `de`.

### Destroys:
* None.

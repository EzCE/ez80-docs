---
title: AdjMath
geekdocHidden: true
params:
    address: $020578
    category: System
    name: AdjMath
---


{{< hint type=note >}}
WikiTI also calls this [UpdatePointers](https://wikiti.brandonw.net/index.php?title=83Plus:BCALLs:4345&oldid=10999).
{{< /hint >}}

Updates 27 pointers after memory has been inserted or deleted.

{{< expand "Pointers Updated" "..." >}}
| Address | Equate Name   |
|---------|---------------|
| $D0066F | iMathPtr1     |
| $D00672 | iMathPtr2     |
| $D00675 | iMathPtr3     |
| $D00678 | iMathPtr4     |
| $D0067B | iMathPtr5     |
| $D0067E | asm_data_ptr1 |
| $D00681 | asm_data_ptr2 |
| $D00684 | Unknown       |
| $D0069F | Unknown       |
| $D006A2 | Unknown       |
| $D0256A | fmtMatMem     |
| $D025A0 | newDataPtr    |
| $D0256D | Unknown       |
| $D022CE | Unknown       |
| $D022BA | ES            |
| $D0068D | Unknown       |
| $D022BF | Unknown       |
| $D022CB | Unknown       |
| $D02695 | Unknown       |
| $D02451 | editDat       |
| $D00687 | asm_ram       |
| $D01FED | Unknown       |
| $D01FF3 | Unknown       |
| $D00693 | Unknown       |
| $D00696 | Unknown       |
| $D01FF9 | Unknown       |
| $D0068A | Unknown       |
{{< /expand >}}

### Address: $020578

### Inputs:
* `de`: Location in RAM where memory was inserted or deleted.
* `bc`: Number of bytes to decrease each pointer (use signed integer to increase).

### Outputs:
* None

### Destroys:
* `f`, `hl`

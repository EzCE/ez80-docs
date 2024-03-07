---
title: Block Transfer and Compare
weight: -10
---

{{< toc >}}

## CPD



## CPDR



## CPI



## CPIR



## LDD

{{< expand "ldd" "..." >}}
Transfers the byte of memory pointed to by `hl` to the memory location pointed to by `de`. Then `hl`, `de`, and `bc` are decremented.
* Opcode: `11101101` `10101000`
* Bytes: 2
* Flags:
    * H: Reset
    * N: Reset
    * P/V: Reset if `bc` becomes zero
* Cycles: 2F+1R+1W+1
{{< /expand >}}

## LDDR

{{< expand "lddr" "..." >}}
Transfers the byte of memory pointed to by `hl` to the memory location pointed to by `de`. Then `hl`, `de`, and `bc` are decremented. If `bc` is not zero, this operation is repeated. Interrupts can trigger between repetitions.
* Opcode: `11101101` `10111000`
* Bytes: 2
* Flags:
    * H: Reset
    * N: Reset
    * P/V: Reset
* Cycles: 2F+(1R+1W+1)*bc
{{< /expand >}}

## LDI

{{< expand "ldi" "..." >}}
Transfers the byte of memory pointed to by `hl` to the memory location pointed to by `de`. Then `hl` and `de` are incremented and `bc` is decremented.
* Opcode: `11101101` `10100000`
* Bytes: 2
* Flags:
    * H: Reset
    * N: Reset
    * P/V: Reset if `bc` becomes zero
* Cycles: 2F+1R+1W+1
{{< /expand >}}

## LDIR

{{< expand "ldir" "..." >}}
Transfers the byte of memory pointed to by `hl` to the memory location pointed to by `de`. Then `hl` and `de` are incremented and `bc` is decremented. If `bc` is not zero, this operation is repeated. Interrupts can trigger between repetitions.
* Opcode: `11101101` `10110000`
* Bytes: 2
* Flags:
    * H: Reset
    * N: Reset
    * P/V: Reset
* Cycles: 2F+(1R+1W+1)*bc
{{< /expand >}}

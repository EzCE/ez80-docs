---
title: Block Transfer and Compare
weight: -10
---

{{< toc >}}

## CPD

{{< expand "cpd" "..." >}}
Compares (via subtraction) the value in `a` with the 8-bit value pointed to by `hl`. Then, both `hl` and `bc` are decremented by one.
* Opcode: `11101101` `10101001`
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Set if the value in `a` is equal to the 8-bit value pointed to by `hl`, reset otherwise
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Set while `bc` is not 0, otherwise reset if `bc` is decremented to 0
    * N: Set
* Cycles: 2F + 1R
{{< /expand >}}

## CPDR

{{< expand "cpdr" "..." >}}
Compares (via subtraction) the value in `a` with the 8-bit value pointed to by `hl`. Then, both `hl` and `bc` are decremented by one. This operation is then repeated until either `a` is equal to the 8-bit value pointed to by `hl`, or the P/V flag is reset (bc is decremented to 0).
* Opcode: `11101101` `10111001`
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Set if the value in `a` is equal to the 8-bit value pointed to by `hl`, reset otherwise
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Set while `bc` is not 0, otherwise reset if `bc` is decremented to 0
    * N: Set
* Cycles: 2F + (1R + 2 ) * bc - 1
{{< /expand >}}

## CPI

{{< expand "cpi" "..." >}}
Compares (via subtraction) the value in `a` with the 8-bit value pointed to by `hl`. Then, `hl` is incremented and `bc` is decremented by one.
* Opcode: `11101101` `10100001`
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Set if the value in `a` is equal to the 8-bit value pointed to by `hl`, reset otherwise
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Set while `bc` is not 0, otherwise reset if `bc` is decremented to 0
    * N: Set
* Cycles: 2F + 1R
{{< /expand >}}

## CPIR

{{< expand "cpir" "..." >}}
Compares (via subtraction) the value in `a` with the 8-bit value pointed to by `hl`. Then, `hl` is incremented and `bc` is decremented by one. This operation is then repeated until either `a` is equal to the 8-bit value pointed to by `hl`, or the P/V flag is reset (bc is decremented to 0).
* Opcode: `11101101` `10110001`
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Set if the value in `a` is equal to the 8-bit value pointed to by `hl`, reset otherwise
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Set while `bc` is not 0, otherwise reset if `bc` is decremented to 0
    * N: Set
* Cycles: 2F + (1R + 2 ) * bc - 1
{{< /expand >}}

## LDD

{{< expand "ldd" "..." >}}
Transfers the byte of memory pointed to by `hl` to the memory location pointed to by `de`. Then `hl`, `de`, and `bc` are decremented.
* Opcode: `11101101` `10101000`
* Bytes: 2
* Flags:
    * H: Reset
    * P/V: Reset if `bc` becomes zero
    * N: Reset
* Cycles: 2F + 1R + 1W + 1
{{< /expand >}}

## LDDR

{{< expand "lddr" "..." >}}
Transfers the byte of memory pointed to by `hl` to the memory location pointed to by `de`. Then `hl`, `de`, and `bc` are decremented. If `bc` is not zero, this operation is repeated. Interrupts can trigger between repetitions.
* Opcode: `11101101` `10111000`
* Bytes: 2
* Flags:
    * H: Reset
    * P/V: Reset
    * N: Reset
* Cycles: 2F + (1R + 1W + 1) * bc
{{< /expand >}}

## LDI

{{< expand "ldi" "..." >}}
Transfers the byte of memory pointed to by `hl` to the memory location pointed to by `de`. Then `hl` and `de` are incremented and `bc` is decremented.
* Opcode: `11101101` `10100000`
* Bytes: 2
* Flags:
    * H: Reset
    * P/V: Reset if `bc` becomes zero
    * N: Reset
* Cycles: 2F+1R+1W+1
{{< /expand >}}

## LDIR

{{< expand "ldir" "..." >}}
Transfers the byte of memory pointed to by `hl` to the memory location pointed to by `de`. Then `hl` and `de` are incremented and `bc` is decremented. If `bc` is not zero, this operation is repeated. Interrupts can trigger between repetitions.
* Opcode: `11101101` `10110000`
* Bytes: 2
* Flags:
    * H: Reset
    * P/V: Reset
    * N: Reset
* Cycles: 2F + (1R + 1W + 1) * bc
{{< /expand >}}

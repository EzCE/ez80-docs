---
title: Arithmetic
weight: -20
---

{{< toc >}}

## ADC

{{< expand "adc a, (hl)" "..." >}}
Adds the 8-bit value in `hl` and the carry flag to `a`.
* Opcode: `10001110`
* Bytes: 1
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 1F + 1R
{{< /expand >}}

{{< expand "adc a, reg8" "..." >}}
Adds `reg8` and the carry flag to `a`.
* Opcode: `10001` `reg8`
    | Register | Bit Field |
    |----------|-----------|
    | `a`      | `111`     |
    | `b`      | `000`     |
    | `c`      | `001`     |
    | `d`      | `010`     |
    | `e`      | `011`     |
    | `h`      | `100`     |
    | `l`      | `101`     |
    | `(hl)`   | `110`     |
* Bytes: 1
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 1F
{{< /expand >}}

## ADD



## CP



## DAA



## DEC



## INC



## MLT



## NEG



## SBC



## SUB



## BIT



## RES



## SET

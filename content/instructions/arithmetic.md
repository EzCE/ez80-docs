---
title: Arithmetic
weight: -10
---

{{< toc >}}

## ADC

{{< expand "adc a, reg8" "..." >}}
Adds the value in `reg8` and the carry flag to the value in `a`. Also includes 1R cycle if `reg8` is `(hl)`.
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

{{< expand "adc a, imm8" "..." >}}
Adds the immediate value `imm8` and the carry flag to the value in `a`.
* Opcode: `11001110` `imm8`
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 2F
{{< /expand >}}

{{< expand "adc hl, reg24" "..." >}}
Adds the value in `reg24` and the carry flag to the value in `hl`.
* Opcode: `11101101` `01` `reg24` `1010`
    | Register | Bit Field |
    |----------|-----------|
    | `bc`     | `00`      |
    | `de`     | `01`      |
    | `hl`     | `10`      |
    | `sp`     | `11`      |
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 2F
{{< /expand >}}

{{< expand "adc a, reg8i" "..." >}}
Adds the value in `reg8i` and the carry flag to the value in `a`.
* Opcode: `regi` `1000110` `reg8i`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |

    | Register | Bit Field |
    |----------|-----------|
    | `l`      | `0`       |
    | `h`      | `1`       |
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 2F
{{< /expand >}}

{{< expand "adc a, (regi + ofs8)" "..." >}}
Adds the value pointed to by `regi` + `ofs8` and the carry flag to the value in `a`.
* Opcode: `regi` `10001110` `ofs8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 3
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 3F + 1R
{{< /expand >}}

## ADD

{{< expand "add hl, reg24" "..." >}}
Adds the value in `reg24` to the value in `hl`.
* Opcode: `00` `reg24` `1001`
    | Register | Bit Field |
    |----------|-----------|
    | `bc`     | `00`      |
    | `de`     | `01`      |
    | `hl`     | `10`      |
    | `sp`     | `11`      |
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

{{< expand "add a, reg8" "..." >}}
Adds the value in `reg8` to the value in `a`. Also includes 1R cycle if `reg8` is `(hl)`.
* Opcode: `10000` `reg8`
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

{{< expand "add a, imm8" "..." >}}
Adds the immediate value `imm8` to the value in `a`.
* Opcode: `11000110` `imm8`
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 2F
{{< /expand >}}

{{< expand "add regi, reg24" "..." >}}
Adds the value in `reg24` to the value in `regi`.
* Opcode: `regi` `00` `reg24` `1001`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |

    | Register  | Bit Field |
    |-----------|-----------|
    | `bc`      | `00`      |
    | `de`      | `01`      |
    | `ix`/`iy` | `10`      |
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 2F
{{< /expand >}}

{{< expand "add a, reg8i" "..." >}}
Adds the value in `reg8i` to the value in `a`.
* Opcode: `regi` `10000100` `reg8i`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |

    | Register | Bit Field |
    |----------|-----------|
    | `l`      | `0`       |
    | `h`      | `1`       |
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 2F
{{< /expand >}}

{{< expand "add a, (regi + ofs8)" "..." >}}
Adds the value pointed to by `regi` + `ofs8` to the value in `a`.
* Opcode: `regi` `10000110` `ofs8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 3
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 3F + 1R
{{< /expand >}}

## CP

{{< expand "cp a, reg8" "..." >}}
Compares (via subtraction) the value in `reg8` with the value in `a`. Also includes 1R cycle if `reg8` is `(hl)`.
* Opcode: `10111` `reg8`
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
* Cycles: 1F + 1R
{{< /expand >}}

{{< expand "cp a, imm8" "..." >}}
Compares (via subtraction) the immediate value `imm8` with the value in `a`.
* Opcode: `11111110` `imm8`
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 2F
{{< /expand >}}

{{< expand "cp a, reg8i" "..." >}}
Compares (via subtraction) the value in `reg8i` with the value in `a`.
* Opcode: `regi` `1011110` `reg8i`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |

    | Register | Bit Field |
    |----------|-----------|
    | `l`      | `0`       |
    | `h`      | `1`       |
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 2F
{{< /expand >}}

{{< expand "cp a, (regi + ofs8)" "..." >}}
Compares (via subtraction) the value pointed to by `regi` + `ofs8` with the value in `a`.
* Opcode: `regi` `10111110` `ofs8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 3
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 3F + 1R
{{< /expand >}}

## DAA

{{< expand "daa" "..." >}}
This instruction is meant to be used after an addition or subtraction instruction on binary-coded-decimal values, specifically [`add`](#add), [`adc`](#adc), [`inc`](#inc), [`sub`](#sub), [`sbc`](#sbc), [`dec`](#dec), or [`neg`](#neg). Following one of these specific instructions, `daa` adjusts the value in `a` according to this table:
| Operation             | C flag prior to DAA | H flag prior to DAA | Upper digit of `a` | Lower digit of `a` | Number added to `a` | C flag after DAA | H flag after DAA |
|-----------------------|---------------------|---------------------|--------------------|--------------------|---------------------|------------------|------------------|
| ADD, ADC, or INC      | 0                   | 0                   | 0 - 9              | 0 - 9              | 00                  | 0                | 0                |
|                       | 0                   | 0                   | 0 - 8              | A - F              | 06                  | 0                | 1                |
|                       | 0                   | 1                   | 0 - 9              | 0 - 3              | 06                  | 0                | 0                |
|                       | 0                   | 0                   | A - F              | 0 - 9              | 60                  | 1                | 0                |
|                       | 0                   | 0                   | 9 - F              | A - F              | 66                  | 1                | 1                |
|                       | 0                   | 1                   | A - F              | 0 - 3              | 66                  | 1                | 0                |
|                       | 1                   | 0                   | 0 - 2              | 0 - 9              | 60                  | 1                | 0                |
|                       | 1                   | 0                   | 0 - 2              | A - F              | 66                  | 1                | 1                |
|                       | 1                   | 1                   | 0 - 3              | 0 - 3              | 66                  | 1                | 0                |
| SUB, SBC, DEC, or NEG | 0                   | 0                   | 0 - 9              | 0 - 9              | 00                  | 0                | 0                |
|                       | 0                   | 1                   | 0 - 8              | 6 - F              | FA                  | 0                | 0                |
|                       | 1                   | 0                   | 7 - F              | 0 - 9              | A0                  | 1                | 0                |
|                       | 1                   | 1                   | 6 - F              | 6 - F              | 9A                  | 1                | 0                |
* Opcode: `00100111`
* Bytes: 1
* Flags:
    * S: Set if msb of the result is 1, reset otherwise
    * Z: Set if result is 0, reset otherwise
    * H: See above table
    * P/V: Detects parity
    * C: See above table
* Cycles: 1F
{{< /expand >}}

## DEC

{{< expand "dec reg24" "..." >}}
Subtracts one from the value in `reg24`.
* Opcode: `00` `reg24` `1011`
    | Register | Bit Field |
    |----------|-----------|
    | `bc`     | `00`      |
    | `de`     | `01`      |
    | `hl`     | `10`      |
    | `sp`     | `11`      |
* Bytes: 1
* Flags:
    * None
* Cycles: 1F
{{< /expand >}}

{{< expand "dec (hl)" "..." >}}
Subtracts one from the value pointed to by `hl`.
* Opcode: `00110101`
* Bytes: 1
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 1F + 1R + 1W + 1
{{< /expand >}}

{{< expand "dec reg8" "..." >}}
Subtracts one from the value in `reg8`.
* Opcode: `00` `reg8` `101`
    | Register | Bit Field |
    |----------|-----------|
    | `a`      | `111`     |
    | `b`      | `000`     |
    | `c`      | `001`     |
    | `d`      | `010`     |
    | `e`      | `011`     |
    | `h`      | `100`     |
    | `l`      | `101`     |
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

{{< expand "dec regi" "..." >}}
Subtracts one from the value in `regi`.
* Opcode: `regi` `00101011`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 2
* Flags:
    * None
* Cycles: 2F
{{< /expand >}}

{{< expand "dec reg8i" "..." >}}
Subtracts one from the value in `reg8i`.
* Opcode: `regi` `0010` `reg8i` `101`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |

    | Register | Bit Field |
    |----------|-----------|
    | `l`      | `0`       |
    | `h`      | `1`       |
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 2F
{{< /expand >}}

{{< expand "dec (regi + ofs8)" "..." >}}
Subtracts one from the 8-bit value pointed to by `regi` + `ofs8`.
* Opcode: `regi` `00110101` `ofs8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 3
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 3F + 1R + 1W + 1
{{< /expand >}}

## INC

{{< expand "inc reg24" "..." >}}
Adds one to the value in `reg24`.
* Opcode: `00` `reg24` `0011`
    | Register | Bit Field |
    |----------|-----------|
    | `bc`     | `00`      |
    | `de`     | `01`      |
    | `hl`     | `10`      |
    | `sp`     | `11`      |
* Bytes: 1
* Flags:
    * None
* Cycles: 1F
{{< /expand >}}

{{< expand "inc (hl)" "..." >}}
Adds one to the 8-bit value pointed to by `hl`.
* Opcode: `00110100`
* Bytes: 1
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 1F + 1R + 1W + 1
{{< /expand >}}

{{< expand "inc reg8" "..." >}}
Adds one to the value in `reg8`.
* Opcode: `00` `reg8` `100`
    | Register | Bit Field |
    |----------|-----------|
    | `a`      | `111`     |
    | `b`      | `000`     |
    | `c`      | `001`     |
    | `d`      | `010`     |
    | `e`      | `011`     |
    | `h`      | `100`     |
    | `l`      | `101`     |
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

{{< expand "inc regi" "..." >}}
Adds one to the value in `regi`.
* Opcode: `regi` `00100011`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 2
* Flags:
    * None
* Cycles: 2F
{{< /expand >}}

{{< expand "inc reg8i" "..." >}}
Adds one to the value in `reg8i`.
* Opcode: `regi` `0010` `reg8i` `100`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |

    | Register | Bit Field |
    |----------|-----------|
    | `l`      | `0`       |
    | `h`      | `1`       |
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 2F
{{< /expand >}}

{{< expand "inc (regi + ofs8)" "..." >}}
Adds one to the 8-bit value pointed to by `regi` + `ofs8`.
* Opcode: `regi` `00110100` `ofs8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 3
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 3F + 1R + 1W + 1
{{< /expand >}}

## MLT

{{< expand "mlt reg24" "..." >}}
Multiplies the low byte of `reg24` by the high byte of `reg24`. The 16-bit result is stored back into the register pair.
* Opcode: `11101101` `01` `reg24` `1100`
    | Register | Bit Field |
    |----------|-----------|
    | `bc`     | `00`      |
    | `de`     | `01`      |
    | `hl`     | `10`      |
    | `sp`     | `11`      |
* Bytes: 2
* Flags:
    * None
* Cycles: 2F + 4
{{< /expand >}}

## NEG

{{< expand "neg" "..." >}}
Negates the value of `a`. The result is identical to subtracting the value in `a` from 0.
* Opcode: `11101101` `01000100`
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 2F
{{< /expand >}}

## SBC

{{< expand "sbc a, reg8" "..." >}}
Subtracts the value in `reg8` and the carry flag from the value in `a`. Also includes 1R cycle if `reg8` is `(hl)`.
* Opcode: `10011` `reg8`
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

{{< expand "sbc a, imm8" "..." >}}
Subtracts the immediate value `imm8` and the carry flag from the value in `a`.
* Opcode: `11011110` `imm8`
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 2F
{{< /expand >}}

{{< expand "sbc hl, reg24" "..." >}}
Subtracts the value in `reg24` and the carry flag from the value in `hl`.
* Opcode: `11101101` `01` `reg24` `0010`
    | Register | Bit Field |
    |----------|-----------|
    | `bc`     | `00`      |
    | `de`     | `01`      |
    | `hl`     | `10`      |
    | `sp`     | `11`      |
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 2F
{{< /expand >}}

{{< expand "sbc a, reg8i" "..." >}}
Subtracts the value in `reg8i` and the carry flag from the value in `a`.
* Opcode: `regi` `1001110` `reg8i`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |

    | Register | Bit Field |
    |----------|-----------|
    | `l`      | `0`       |
    | `h`      | `1`       |
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 2F
{{< /expand >}}

{{< expand "sbc a, (regi + ofs8)" "..." >}}
Subtracts the value pointed to by `regi` + `ofs8` and the carry flag from the value in `a`.
* Opcode: `regi` `10011110` `ofs8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 3
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 3F + 1R
{{< /expand >}}

## SUB

{{< expand "sub a, reg8" "..." >}}
Subtracts the value in `reg8` from the value in `a`. Also includes 1R cycle if `reg8` is `(hl)`.
* Opcode: `10010` `reg8`
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
* Cycles: 1F + 1R
{{< /expand >}}

{{< expand "sub a, imm8" "..." >}}
Subtracts the immediate value `imm8` from the value in `a`.
* Opcode: `11010110` `imm8`
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 2F
{{< /expand >}}

{{< expand "sub a, reg8i" "..." >}}
Subtracts the value in `reg8i` from the value in `a`.
* Opcode: `regi` `1001010` `reg8i`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |

    | Register | Bit Field |
    |----------|-----------|
    | `l`      | `0`       |
    | `h`      | `1`       |
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 2F
{{< /expand >}}

{{< expand "sub a, (regi + ofs8)" "..." >}}
Subtracts the value pointed to by `regi` + `ofs8` from the value in `a`.
* Opcode: `regi` `10010110` `ofs8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 3
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Affected as [defined](../flags/#h-half-carry)
    * P/V: Detects overflow
    * N: Reset
    * C: Affected as [defined](../flags/#c-carry)
* Cycles: 3F + 1R
{{< /expand >}}

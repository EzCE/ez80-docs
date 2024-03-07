---
title: Bit Manipulation
weight: -20
---

{{< toc >}}

## BIT

{{< expand "bit imm3, reg8" "..." >}}
Checks bit `imm3` of the value in `reg8`. Also includes 1R cycle if `reg8` is `(hl)`.
* Opcode: `11001011` `01` `imm3` `reg8`
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
* Bytes: 2
* Flags:
    * S: Undefined
    * Z: Set if bit `imm3` is 0, reset otherwise
    * H: Set
    * P/V: Undefined
    * N: Reset
* Cycles: 2F
{{< /expand >}}

{{< expand "bit imm3, (regi + ofs8)" "..." >}}
Checks bit `imm3` of the 8-bit value pointed to by `regi` + `ofs8`.
* Opcode: `regi` `11001011` `ofs8` `01` `imm3` `110`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 4
* Flags:
    * S: Undefined
    * Z: Set if bit `imm3` is 0, reset otherwise
    * H: Set
    * P/V: Undefined
    * N: Reset
* Cycles: 4F + 1R
{{< /expand >}}

## RES

{{< expand "res imm3, reg8" "..." >}}
Resets bit `imm3` of the value in `reg8`. Also includes 1R + 1W + 1 cycles if `reg8` is `(hl)`.
* Opcode: `11001011` `10` `imm3` `reg8`
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
* Bytes: 2
* Flags:
    * None
* Cycles: 2F
{{< /expand >}}

{{< expand "res imm3, (regi + ofs8)" "..." >}}
Resets bit `imm3` of the 8-bit value pointed to by `regi` + `ofs8`.
* Opcode: `regi` `11001011` `ofs8` `10` `imm3` `110`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 4
* Flags:
    * None
* Cycles: 4F + 1R + 1W + 1
{{< /expand >}}

## SET

{{< expand "set imm3, reg8" "..." >}}
Sets bit `imm3` of the value in `reg8`. Also includes 1R + 1W + 1 cycles if `reg8` is `(hl)`.
* Opcode: `11001011` `11` `imm3` `reg8`
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
* Bytes: 2
* Flags:
    * None
* Cycles: 2F
{{< /expand >}}

{{< expand "set imm3, (regi + ofs8)" "..." >}}
Sets bit `imm3` of the 8-bit value pointed to by `regi` + `ofs8`.
* Opcode: `regi` `11001011` `ofs8` `11` `imm3` `110`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 4
* Flags:
    * S: Undefined
    * Z: Set if bit `imm3` is 0, reset otherwise
    * H: Set
    * P/V: Undefined
    * N: Reset
* Cycles: 4F + 1R + 1W + 1
{{< /expand >}}

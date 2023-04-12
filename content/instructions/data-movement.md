---
title: Data Movement
weight: -20
---

{{< toc >}}

## EX

{{< expand "ex af, af'" "..." >}}
Exchanges the contents of `af` and `af'`.
* Opcode: `00001000`
* Bytes: 1
* Flags: None
* Cycles: 1F
{{< /expand >}}

{{< expand "ex (sp), hl" "...">}}
Exchanges the word of memory pointed to by `sp` with `hl`.
* Opcode: `11100011`
* Bytes: 1
* Flags: None
* Cycles: 1F+3R+3W
{{< /expand >}}

{{< expand "ex de, hl" "..." >}}
Exchanges the contents of `de` and `hl`.
* Opcode: `11101011`
* Bytes: 1
* Flags: None
* Cycles: 1F
{{< /expand >}}

{{< expand "ex (sp), ix" "..." >}}
Exchanges the word of memory pointed to by `sp` with `ix`.
* Opcode: `1101110111100011`
* Bytes: 2
* Flags: None
* Cycles: 2F+3R+3W
{{< /expand >}}

{{< expand "ex (sp), iy" "..." >}}
Exchanges the word of memory pointed to by `sp` with `iy`.
* Opcode: `1111110111100011`
* Bytes: 2
* Flags: None
* Cycles: 2F+3R+3W
{{< /expand >}}

## EXX

{{< expand "exx" "..." >}}
Exchanges the contents of `af`, `bc`, `de`, and `hl` with `af'`, `bc'`, `de'`, and `hl'`, respectively.
* Opcode: `11011001`
* Bytes: 1
* Flags: None
* Cycles: 1F
{{< /expand >}}

## LD

{{< expand "ld reg8D, reg8S" "..." >}}
The contents of register `reg8S` are stored into `reg8D`.
* Opcode: `01` `reg8D` `reg8S`
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
* Flags: None
* Cycles: 1F
{{< /expand >}}

{{< expand "ld reg8, imm8" "..." >}}
Stores an immediate value `imm8` into `reg8`.
* Opcode: `01` `reg8` `110` `imm8`
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
* Flags: None
* Cycles: 2F
{{< /expand >}}

{{< expand "ld reg8, (regi + ofs8)" "..." >}}
Stores the byte of memory pointed to by `regi` + `ofs8` into `reg8`.
* Opcode: `regi` `01` `reg8` `110` `ofs8`
    | Index   | Bit Field  |
    |---------|------------|
    | `ix`    | `11011101` |
    | `iy`    | `11111101` |

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
* Bytes: 3
* Flags: None
* Cycles: 3F+1R
{{< /expand >}}

{{< expand "ld  (regi + ofs8), reg8" "..." >}}
Stores `reg8` into the address pointed to by `regi` + `ofs8`.
* Opcode: `regi` `01110` `reg8` `ofs8`
    | Index   | Bit Field  |
    |---------|------------|
    | `ix`    | `11011101` |
    | `iy`    | `11111101` |

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
* Bytes: 3
* Flags: None
* Cycles: 3F+1W
{{< /expand >}}

{{< expand "ld  (regi + ofs8), imm8" "..." >}}
Stores `imm8` into the address pointed to by `regi` + `ofs8`.
* Opcode: `regi` `00110110` `ofs8` `imm8`
    | Index   | Bit Field  |
    |---------|------------|
    | `ix`    | `11011101` |
    | `iy`    | `11111101` |
* Bytes: 4
* Flags: None
* Cycles: 4F+1W
{{< /expand >}}

{{< expand "ld  a, (reg24)" "..." >}}
Stores the byte of memory pointed to by `reg24` into `reg8`.
* Opcode: `000` `reg24` `1010`
    | Register | Bit Field |
    |----------|-----------|
    | `bc`     | `0`       |
    | `de`     | `1`       |
* Bytes: 1
* Flags: None
* Cycles: 1F+1R
{{< /expand >}}

{{< expand "ld  a, (imm24)" "..." >}}
Stores the byte of memory pointed to by `imm24` into `reg8`.
* Opcode: `00111010` `imm24`
* Bytes: 4
* Flags: None
* Cycles: 4F+1R
{{< /expand >}}

{{< expand "ld  (reg24), a" "..." >}}
Stores `reg8` into the address pointed to by `reg24`.
* Opcode: `000` `reg24` `0010`
    | Register | Bit Field |
    |----------|-----------|
    | `bc`     | `0`       |
    | `de`     | `1`       |
* Bytes: 1
* Flags: None
* Cycles: 1F+1W
{{< /expand >}}

{{< expand "ld  (imm24), a" "..." >}}
Stores `reg8` into the address pointed to by `imm24`.
* Opcode: `00110010` `imm24 (little endian)`
* Bytes: 4
* Flags: None
* Cycles: 4F+1W
{{< /expand >}}

{{< expand "ld  a, regir" "..." >}}
Stores the value of `regir` into `reg8`
* Opcode: `11101101` `0101` `regir` `111`
    | Register | Bit Field |
    |----------|-----------|
    | `i`      | `0`       |
    | `r`      | `1`       |
* Bytes: 2
* Flags: 
    * S: Affected by the loaded value
    * Z: Affected by the loaded value
    * P: Interrupt flag state
* Cycles: 2F
{{< /expand >}}

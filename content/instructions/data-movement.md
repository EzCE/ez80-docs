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
* Opcode: `11011101` `11100011`
* Bytes: 2
* Flags: None
* Cycles: 2F+3R+3W
{{< /expand >}}

{{< expand "ex (sp), iy" "..." >}}
Exchanges the word of memory pointed to by `sp` with `iy`.
* Opcode: `11111101` `11100011`
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
Stores the value of `regir` into `reg8`.
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

{{< expand "ld  regir, a" "..." >}}
Stores the value of `reg8` into `regir`.
* Opcode: `11101101` `0100` `regir` `111`
    | Register | Bit Field |
    |----------|-----------|
    | `i`      | `0`       |
    | `r`      | `1`       |
* Bytes: 2
* Flags: None
* Cycles: 2F
{{< /expand >}}

{{< expand "ld  reg24, imm24" "..." >}}
Stores `imm24` into `reg24`.
* Opcode: `00` `reg24` `0001` `imm24`
    | Register | Bit Field |
    |----------|-----------|
    | `bc`     | `00`      |
    | `de`     | `01`      |
    | `hl`     | `10`      |
    | `sp`     | `11`      |
* Bytes: 4
* Flags: None
* Cycles: 4F
{{< /expand >}}

{{< expand "ld  regi, imm24" "..." >}}
Stores `imm24` into `regi`.
* Opcode: `regi` `00100001` `imm24`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 5
* Flags: None
* Cycles: 5F
{{< /expand >}}

{{< expand "ld  hl, (imm24)" "..." >}}
Stores the value pointed to by `imm24` into `hl`.
* Opcode: `00101010` `imm24`
* Bytes: 4
* Flags: None
* Cycles: 4F+3R
{{< /expand >}}

{{< expand "ld  reg24, (imm24)" "..." >}}
Stores the value pointed to by `imm24` into `reg24`.
* Opcode: `11101101` `01` `reg24` `1011` `imm24`
    | Register | Bit Field |
    |----------|-----------|
    | `bc`     | `00`      |
    | `de`     | `01`      |
    | `hl`     | `10`      |
    | `sp`     | `11`      |
* Bytes: 5
* Flags: None
* Cycles: 5F+3R
{{< /expand >}}

{{< expand "ld  regi, (imm24)" "..." >}}
Stores the value pointed to by `imm24` into `regi`.
* Opcode: `regi` `00101010` `imm24`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 5
* Flags: None
* Cycles: 5F+3R
{{< /expand >}}

{{< expand "ld  (imm24), hl" "..." >}}
Stores `hl` to the address pointed to by `imm24`.
* Opcode: `00100010` `imm24`
* Bytes: 4
* Flags: None
* Cycles: 4F+3W
{{< /expand >}}

{{< expand "ld  (imm24), reg24" "..." >}}
Stores `reg24` to the address pointed to by `imm24`.
* Opcode: `11101101` `01` `reg24` `0011` `imm24`
    | Register | Bit Field |
    |----------|-----------|
    | `bc`     | `00`      |
    | `de`     | `01`      |
    | `hl`     | `10`      |
    | `sp`     | `11`      |
* Bytes: 5
* Flags: None
* Cycles: 5F+3W
{{< /expand >}}

{{< expand "ld  (imm24), regi" "..." >}}
Stores `regi` to the address pointed to by `imm24`.
* Opcode: `regi` `00100010` `imm24`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 5
* Flags: None
* Cycles: 5F+3W
{{< /expand >}}

{{< expand "ld  sp, hl" "..." >}}
Stores `hl` into `sp`.
* Opcode: `11111001`
* Bytes: 1
* Flags: None
* Cycles: 1F
{{< /expand >}}

{{< expand "ld  sp, regi" "..." >}}
Stores `regi` into `sp`.
* Opcode: `regi` `11111001`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 2
* Flags: None
* Cycles: 2F
{{< /expand >}}

{{< expand "ld  regih, imm8" "..." >}}
Stores `imm8` into the high byte of `regi`.
* Opcode: `regi` `00100110` `imm8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 3
* Flags: None
* Cycles: 3F
{{< /expand >}}

{{< expand "ld  regil, imm8" "..." >}}
Stores `imm8` into the low byte of `regi`.
* Opcode: `regi` `00101110` `imm8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 3
* Flags: None
* Cycles: 3F
{{< /expand >}}

{{< expand "ld  reg8, regih" "..." >}}
Stores the high byte of `regi` into `reg8`.
* Opcode: `regi` `01100` `reg8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |

    | Register | Bit Field |
    |----------|-----------|
    | `a`      | `111`     |
    | `b`      | `000`     |
    | `c`      | `001`     |
    | `d`      | `010`     |
    | `e`      | `011`     |
* Bytes: 2
* Flags: None
* Cycles: 2F
{{< /expand >}}

{{< expand "ld  reg8, regil" "..." >}}
Stores the low byte of `regi` into `reg8`.
* Opcode: `regi` `01101` `reg8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |

    | Register | Bit Field |
    |----------|-----------|
    | `a`      | `111`     |
    | `b`      | `000`     |
    | `c`      | `001`     |
    | `d`      | `010`     |
    | `e`      | `011`     |
* Bytes: 2
* Flags: None
* Cycles: 2F
{{< /expand >}}

{{< expand "ld  regih, reg8" "..." >}}
Stores `reg8` into the high byte of `regi`.
* Opcode: `regi` `01100` `reg8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |

    | Register | Bit Field |
    |----------|-----------|
    | `a`      | `111`     |
    | `b`      | `000`     |
    | `c`      | `001`     |
    | `d`      | `010`     |
    | `e`      | `011`     |
    | `ixh`    | `100`     |
    | `ixl`    | `101`     |
* Bytes: 2
* Flags: None
* Cycles: 2F
{{< /expand >}}

{{< expand "ld  regil, reg8" "..." >}}
Stores `reg8` into the low byte of `regi`.
* Opcode: `regi` `01101` `reg8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |

    | Register | Bit Field |
    |----------|-----------|
    | `a`      | `111`     |
    | `b`      | `000`     |
    | `c`      | `001`     |
    | `d`      | `010`     |
    | `e`      | `011`     |
    | `ixh`    | `100`     |
    | `ixl`    | `101`     |
* Bytes: 2
* Flags: None
* Cycles: 2F
{{< /expand >}}

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

## POP

{{< expand "pop reg24" "..." >}}
The word of memory pointed to by `sp` is stored into `reg24` and `sp` is incremented by the word size.
* Opcode: `11` `reg24` `0001`
    | Register | Bit Field |
    |----------|-----------|
    | `bc`     | `00`      |
    | `de`     | `01`      |
    | `hl`     | `10`      |
    | `af`     | `11`      |
* Bytes: 1
* Flags: None
* Cycles: 1F+3R
{{< /expand >}}

{{< expand "pop regi" "..." >}}
The word of memory pointed to by `sp` is stored into `regi` and `sp` is incremented by the word size.
* Opcode: `regi` `11100001`
    | Register | Bit Field  |
    |----------|------------|
    | `ix`     | `11011101` |
    | `iy`     | `11111101` |
* Bytes: 2
* Flags: None
* Cycles: 2F+3R
{{< /expand >}}

## PUSH

{{< expand "push reg24" "..." >}}
`sp` is decremented by the word size and `reg24` is stored into the word of memory pointed to by `sp`.
* Opcode: `11` `reg24` `0101`
    | Register | Bit Field |
    |----------|-----------|
    | `bc`     | `00`      |
    | `de`     | `01`      |
    | `hl`     | `10`      |
    | `af`     | `11`      |
* Bytes: 1
* Flags: None
* Cycles: 1F+3W
{{< /expand >}}

{{< expand "push regi" "..." >}}
`sp` is decremented by the word size and `regi` is stored into the word of memory pointed to by `sp`.
* Opcode: `regi` `11100101`
    | Register | Bit Field  |
    |----------|------------|
    | `ix`     | `11011101` |
    | `iy`     | `11111101` |
* Bytes: 2
* Flags: None
* Cycles: 2F+3W
{{< /expand >}}

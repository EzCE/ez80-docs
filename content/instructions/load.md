---
title: Load
weight: -10
---

{{< toc >}}

## LD

### 8 bit

#### Load register

{{< expand "ld reg8D, reg8S" "..." >}}
The contents of register `reg8S` are stored into `reg8D`. Includes `1R` cycle for `ld reg8D, (hl)` or `1W` cycle for `ld (hl), reg8S`.
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
* Cycles: 1F (+1R/1W)
{{< /expand >}}

{{< expand "ld  reg8, regih" "..." >}}
Stores the high byte of `regih` into `reg8`.
* Opcode: `regih` `01100` `reg8`
    | Index | Bit Field  |
    |-------|------------|
    | `ixh` | `11011101` |
    | `iyh` | `11111101` |

    | Register | Bit Field |
    |----------|-----------|
    | `a`      | `111`     |
    | `b`      | `000`     |
    | `c`      | `001`     |
    | `d`      | `010`     |
    | `e`      | `011`     |
    | `ixh/iyh`| `100`     |
    | `ixl/iyl`| `101`     |
* Bytes: 2
* Flags: None
* Cycles: 2F
{{< /expand >}}

{{< expand "ld  reg8, regil" "..." >}}
Stores the low byte of `regil` into `reg8`.
* Opcode: `regil` `01101` `reg8`
    | Index | Bit Field  |
    |-------|------------|
    | `ixl` | `11011101` |
    | `iyl` | `11111101` |

    | Register | Bit Field |
    |----------|-----------|
    | `a`      | `111`     |
    | `b`      | `000`     |
    | `c`      | `001`     |
    | `d`      | `010`     |
    | `e`      | `011`     |
    | `ixh/iyh`| `100`     |
    | `ixl/iyl`| `101`     |
* Bytes: 2
* Flags: None
* Cycles: 2F
{{< /expand >}}

{{< expand "ld  regih, reg8" "..." >}}
Stores `reg8` into the high byte of `regih`.
* Opcode: `regih` `01100` `reg8`
    | Index | Bit Field  |
    |-------|------------|
    | `ixh` | `11011101` |
    | `iyh` | `11111101` |

    | Register | Bit Field |
    |----------|-----------|
    | `a`      | `111`     |
    | `b`      | `000`     |
    | `c`      | `001`     |
    | `d`      | `010`     |
    | `e`      | `011`     |
    | `ixh/iyh`| `100`     |
    | `ixl/iyl`| `101`     |
* Bytes: 2
* Flags: None
* Cycles: 2F
{{< /expand >}}

{{< expand "ld  regil, reg8" "..." >}}
Stores `reg8` into the low byte of `regil`.
* Opcode: `regil` `01101` `reg8`
    | Index | Bit Field  |
    |-------|------------|
    | `ixl` | `11011101` |
    | `iyl` | `11111101` |

    | Register | Bit Field |
    |----------|-----------|
    | `a`      | `111`     |
    | `b`      | `000`     |
    | `c`      | `001`     |
    | `d`      | `010`     |
    | `e`      | `011`     |
    | `ixh/iyh`| `100`     |
    | `ixl/iyl`| `101`     |
* Bytes: 2
* Flags: None
* Cycles: 2F
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

{{< expand "ld  regih, imm8" "..." >}}
Stores `imm8` into the high byte of `regih`.
* Opcode: `regih` `00100110` `imm8`
    | Index | Bit Field  |
    |-------|------------|
    | `ixh` | `11011101` |
    | `iyh` | `11111101` |
* Bytes: 3
* Flags: None
* Cycles: 3F
{{< /expand >}}

{{< expand "ld  regil, imm8" "..." >}}
Stores `imm8` into the low byte of `regil`.
* Opcode: `regil` `00101110` `imm8`
    | Index | Bit Field  |
    |-------|------------|
    | `ixl` | `11011101` |
    | `iyl` | `11111101` |
* Bytes: 3
* Flags: None
* Cycles: 3F
{{< /expand >}}

#### Load pointer

{{< expand "ld  a, (imm24)" "..." >}}
Stores the byte of memory pointed to by `imm24` into `reg8`.
* Opcode: `00111010` `imm24`
* Bytes: 4
* Flags: None
* Cycles: 4F+1R
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

#### Store pointer

{{< expand "ld  (imm24), a" "..." >}}
Stores `reg8` into the address pointed to by `imm24`.
* Opcode: `00110010` `imm24 (little endian)`
* Bytes: 4
* Flags: None
* Cycles: 4F+1W
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

### 24 bit

#### Load register

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

#### Load pointer

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

{{< expand "ld reg24, (hl)" "..." >}}
Loads `reg24` with the word of memory pointed to by `hl`.
* Opcode: `11101101` `00` `reg24` `0111`
    | Register | Bit Field |
    |----------|-----------|
    | `bc`     | `00`      |
    | `de`     | `01`      |
    | `hl`     | `10`      |
* Bytes: 2
* Flags: None
* Cycles: 2F + 3R
{{< /expand >}}

{{< expand "ld regi, (hl)" "..." >}}
Loads `regi` with the word of memory pointed to by `hl`.
* Opcode: `11101101` `regi`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `00110111` |
    | `iy`  | `00110001` |
* Bytes: 2
* Flags: None
* Cycles: 2F + 3R
{{< /expand >}}

{{< expand "ld reg24, (regi + ofs8)" "..." >}}
Loads the word of memory pointed to by `regi` + `ofs8` into `reg24`.
* Opcode: `regi` `00` `reg24` `0111` `ofs8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |

    | Register | Bit Field |
    |----------|-----------|
    | `bc`     | `00`      |
    | `de`     | `01`      |
    | `hl`     | `10`      |
* Bytes: 3
* Flags: None
* Cycles: 3F + 3R
{{< /expand >}}

{{< expand "ld regi, (ix + ofs8)" "..." >}}
Loads `regi` with the word of memory pointed to by `ix` plus `ofs8`.
* Opcode: `11011101` `regi` `ofs8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `00110111` |
    | `iy`  | `00110001` |
* Bytes: 3
* Flags: None
* Cycles: 3F + 3R
{{< /expand >}}

{{< expand "ld regi, (iy + ofs8)" "..." >}}
Loads `regi` with the word of memory pointed to by `iy` plus `ofs8`.
* Opcode: `11111101` `regi` `ofs8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `00110111` |
    | `iy`  | `00110001` |
* Bytes: 3
* Flags: None
* Cycles: 3F + 3R
{{< /expand >}}

#### Store pointer

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

{{< expand "ld (regi + ofs8), reg24" "..." >}}
Stores `reg24` into the word of memory pointed to by `regi` + `ofs8`.
* Opcode: `regi` `00` `reg24` `1111` `ofs8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |

    | Register | Bit Field |
    |----------|-----------|
    | `bc`     | `00`      |
    | `de`     | `01`      |
    | `hl`     | `10`      |
* Bytes: 3
* Flags: None
* Cycles: 3F + 3W
{{< /expand >}}

{{< expand "ld (ix + ofs8), regi" "..." >}}
Loads the word of memory at `ix` plus `ofs8` with `regi`.
* Opcode: `11011101` `regi` `ofs8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `00111111` |
    | `iy`  | `00111110` |
* Bytes: 3
* Flags: None
* Cycles: 3F + 3W
{{< /expand >}}

{{< expand "ld (iy + ofs8), regi" "..." >}}
Loads the word of memory at `iy` plus `ofs8` with `regi`.
* Opcode: `11111101` `regi` `ofs8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `00111111` |
    | `iy`  | `00111110` |
* Bytes: 3
* Flags: None
* Cycles: 3F + 3W
{{< /expand >}}

### Memory / Interrupts

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

{{< expand "ld  a, regir" "..." >}}
Stores the value of `regir` into `reg8`.
* Opcode: `11101101` `0101` `regir` `111`
    | Register | Bit Field |
    |----------|-----------|
    | `i`      | `0`       |
    | `r`      | `1`       |
* Bytes: 2
* Flags: 
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected by [defined](../flags/#z-zero)
    * H: Reset
    * N: Reset
    * P/V: Interrupt flag state
* Cycles: 2F
{{< /expand >}}

{{< expand "ld  mb, a" "..." >}}
Stores the value of `a` into `mb`.
* Opcode: `11101101` `01101101`
* Bytes: 2
* Flags: None
* Cycles: 2F
{{< /expand >}}

{{< expand "ld  a, mb" "..." >}}
Stores the value of `mb` into `a`.
* Opcode: `11101101` `01101110`
* Bytes: 2
* Flags: None
* Cycles: 2F
{{< /expand >}}

## LEA

{{< expand "lea regi, ix + ofs8" "..." >}}
Loads `regi` with the value of `ix` plus `ofs8`.
* Opcode: `11101101` `regi` `ofs8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `01010100` |
    | `iy`  | `00110011` |
* Bytes: 3
* Flags: None
* Cycles: 3F
{{< /expand >}}

{{< expand "lea regi, iy + ofs8" "..." >}}
Loads `regi` with the value of `iy` plus `ofs8`.
* Opcode: `11101101` `regi` `ofs8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `00110010` |
    | `iy`  | `01010101` |
* Bytes: 3
* Flags: None
* Cycles: 3F
{{< /expand >}}

{{< expand "lea reg24, regi + ofs8" "..." >}}
Loads `reg24` with the value of `regi` + `ofs8`.
* Opcode: `regi` `00` `reg24` `001` `regi` `ofs8`
    | Index | Bit Field       |
    |-------|-----------------|
    | `ix`  | `11011101`, `0` |
    | `iy`  | `11111101`, `1` |

    | Register | Bit Field |
    |----------|-----------|
    | `bc`     | `00`      |
    | `de`     | `01`      |
    | `hl`     | `10`      |
* Bytes: 3
* Flags: None
* Cycles: 3F
{{< /expand >}}

## PEA

{{< expand "pea regi + ofs8" "..." >}}
The value of `regi` plus `ofs8` is pushed to the stack.
* Opcode: `11101101` `011001` `regi` `ofs8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `01`       |
    | `iy`  | `10`       |
* Bytes: 3
* Flags: None
* Cycles: 3F + 3W
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

---
title: Logical
weight: -10
---

{{< toc >}}

## AND

{{< expand "and a, reg8" "..." >}}
A bitwise AND operation is performed on the value in `reg8` with the value in `a`. The result is then stored in `a`. Also includes 1R cycle if `reg8` is `(hl)`.
* Opcode: `10100` `reg8`
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
    * H: Set
    * P/V: Detects parity
    * N: Reset
    * C: Reset
* Cycles: 1F
{{< /expand >}}

{{< expand "and a, imm8" "..." >}}
A bitwise AND operation is performed on `imm8` with the value in `a`. The result is then stored in `a`.
* Opcode: `11100110` `imm8`
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Set
    * P/V: Detects parity
    * N: Reset
    * C: Reset
* Cycles: 2F
{{< /expand >}}

{{< expand "and a, reg8i" "..." >}}
A bitwise AND operation is performed on the value in `reg8i` with the value in `a`. The result is then stored in `a`.
* Opcode: `regi` `1010010` `reg8i`
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
    * H: Set
    * P/V: Detects parity
    * N: Reset
    * C: Reset
* Cycles: 2F
{{< /expand >}}

{{< expand "and a, (regi + ofs8)" "..." >}}
A bitwise AND operation is performed on the value pointed to by `regi` + `ofs8` with the value in `a`. The result is then stored in `a`.
* Opcode: `regi` `10100110` `ofs8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 3
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Set
    * P/V: Detects parity
    * N: Reset
    * C: Reset
* Cycles: 3F + 1R
{{< /expand >}}

## CPL

{{< expand "cpl" "..." >}}
All bits in the `a` are inverted (one's complemented).
* Opcode: `00101111`
* Bytes: 1
* Flags:
    * H: Set
    * N: Set
* Cycles: 1F
{{< /expand >}}

## OR

{{< expand "or a, reg8" "..." >}}
A bitwise OR operation is performed on the value in `reg8` with the value in `a`. The result is then stored in `a`. Also includes 1R cycle if `reg8` is `(hl)`.
* Opcode: `10110` `reg8`
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
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Reset
* Cycles: 1F
{{< /expand >}}

{{< expand "or a, imm8" "..." >}}
A bitwise OR operation is performed on `imm8` with the value in `a`. The result is then stored in `a`.
* Opcode: `11110110` `imm8`
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Reset
* Cycles: 2F
{{< /expand >}}

{{< expand "or a, reg8i" "..." >}}
A bitwise OR operation is performed on the value in `reg8i` with the value in `a`. The result is then stored in `a`.
* Opcode: `regi` `1011010` `reg8i`
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
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Reset
* Cycles: 2F
{{< /expand >}}

{{< expand "or a, (regi + ofs8)" "..." >}}
A bitwise OR operation is performed on the value pointed to by `regi` + `ofs8` with the value in `a`. The result is then stored in `a`.
* Opcode: `regi` `10110110` `ofs8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 3
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Reset
* Cycles: 3F + 1R
{{< /expand >}}

## TST

{{< expand "tst a, reg8" "..." >}}
A bitwise AND operation is performed on the value in `reg8` with the value in `a`. Unlike the `and` instruction, the result is not stored in `a`. However, the flags are updated according to the result. Also includes 1R cycle if `reg8` is `(hl)`.
* Opcode: `11101101` `00` `reg8` `100`
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
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Set
    * P/V: Detects parity
    * N: Reset
    * C: Reset
* Cycles: 2F
{{< /expand >}}

{{< expand "tst a, imm8" "..." >}}
A bitwise AND operation is performed on `imm8` with the value in `a`. Unlike the `and` instruction, the result is not stored in `a`. However, the flags are updated according to the result.
* Opcode: `11101101` `01100100` `imm8`
* Bytes: 3
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Set
    * P/V: Detects parity
    * N: Reset
    * C: Reset
* Cycles: 3F
{{< /expand >}}

## XOR

{{< expand "xor a, reg8" "..." >}}
A bitwise XOR operation is performed on the value in `reg8` with the value in `a`. The result is then stored in `a`. Also includes 1R cycle if `reg8` is `(hl)`.
* Opcode: `10101` `reg8`
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
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Reset
* Cycles: 1F
{{< /expand >}}

{{< expand "xor a, imm8" "..." >}}
A bitwise XOR operation is performed on `imm8` with the value in `a`. The result is then stored in `a`.
* Opcode: `11101110` `imm8`
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Reset
* Cycles: 2F
{{< /expand >}}

{{< expand "xor a, reg8i" "..." >}}
A bitwise XOR operation is performed on the value in `reg8i` with the value in `a`. The result is then stored in `a`.
* Opcode: `regi` `1010110` `reg8i`
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
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Reset
* Cycles: 2F
{{< /expand >}}

{{< expand "xor a, (regi + ofs8)" "..." >}}
A bitwise XOR operation is performed on the value pointed to by `regi` + `ofs8` with the value in `a`. The result is then stored in `a`.
* Opcode: `regi` `10101110` `ofs8`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 3
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Reset
* Cycles: 3F + 1R
{{< /expand >}}

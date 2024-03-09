---
title: Rotate and Shift
weight: -10
---

{{< toc >}}

## RL

{{< expand "rl reg8" "..." >}}
The value in `reg8` is rotated left by one bit position. Bit 7 is then copied into the [carry flag](../flags/#c-carry) and the previous contents of the carry flag are copied into bit 0 of `reg8`. Also includes 1R + 1W + 1 cycle if `reg8` is `(hl)`.
* Opcode: `11001011` `00010` `reg8`
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
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Data from bit 7 of `reg8`
* Cycles: 2F
{{< /expand >}}

{{< expand "rl (regi + ofs8)" "..." >}}
The 8-bit value pointed to by `regi` + `ofs8` is rotated left by one bit position. Bit 7 is then copied into the [carry flag](../flags/#c-carry) and the previous contents of the carry flag are copied into bit 0 of the value pointed to by `regi` + `ofs8`.
* Opcode: `regi` `11001011` `ofs8` `00010110`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 4
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Data from bit 7 of the value pointed to by `regi` + `ofs8`
* Cycles: 4F + 1R + 1W + 1
{{< /expand >}}

## RLA

{{< expand "rla" "..." >}}
The value in `a` is rotated left by one bit position. Bit 7 is then copied into the [carry flag](../flags/#c-carry) and the previous contents of the carry flag are copied into bit 0 of `a`.
* Opcode: `00010111`
* Bytes: 1
* Flags:
    * H: Reset
    * N: Reset
    * C: Data from bit 7 of `a`
* Cycles: 1F
{{< /expand >}}

## RLC

{{< expand "rlc reg8" "..." >}}
The value in `reg8` is rotated left by one bit position. Bit 7 is then copied into the [carry flag](../flags/#c-carry) and is copied into bit 0 of `reg8` as well. Also includes 1R + 1W + 1 cycle if `reg8` is `(hl)`.
* Opcode: `11001011` `00000` `reg8`
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
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Data from bit 7 of `reg8`
* Cycles: 2F
{{< /expand >}}

{{< expand "rlc (regi + ofs8)" "..." >}}
The 8-bit value pointed to by `regi` + `ofs8` is rotated left by one bit position. Bit 7 is then copied into the [carry flag](../flags/#c-carry) and is copied into bit 0 of the value pointed to by `regi` + `ofs8` as well.
* Opcode: `regi` `11001011` `ofs8` `00000110`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 4
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Data from bit 7 of the value pointed to by `regi` + `ofs8`
* Cycles: 4F + 1R + 1W + 1
{{< /expand >}}

## RLCA

{{< expand "rlca" "..." >}}
The value in `a` is rotated left by one bit position. Bit 7 is then copied into the [carry flag](../flags/#c-carry) and is copied into bit 0 of `a` as well.
* Opcode: `00000111`
* Bytes: 1
* Flags:
    * H: Reset
    * N: Reset
    * C: Data from bit 7 of `a`
* Cycles: 1F
{{< /expand >}}

## RLD

{{< expand "rld" "..." >}}
The contents of the low-order four bits of the 8-bit value pointed to by `hl` are copied into the high-order four bits of the 8-bit value pointed to by `hl`. The CPU then copies the previous contents of the high-order four bits of the 8-bit value pointed to by `hl` into the low-order four bits of `a`. Finally, the previous contents of the low-order four bits of `a` are copied into the low-order four bits of the value pointed to by `hl`.
* Opcode: `11101101` `01101111`
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Reset
    * P/V: Detects parity
    * N: Reset
* Cycles: 2F + 1R + 1W + 1
{{< /expand >}}

## RR

{{< expand "rr reg8" "..." >}}
The value in `reg8` is rotated right by one bit position. Bit 0 is then copied into the [carry flag](../flags/#c-carry) and the previous contents of the carry flag are copied into bit 7 of `reg8`. Also includes 1R + 1W + 1 cycle if `reg8` is `(hl)`.
* Opcode: `11001011` `00011` `reg8`
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
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Data from bit 0 of `reg8`
* Cycles: 2F
{{< /expand >}}

{{< expand "rr (regi + ofs8)" "..." >}}
The 8-bit value pointed to by `regi` + `ofs8` is rotated right by one bit position. Bit 0 is then copied into the [carry flag](../flags/#c-carry) and the previous contents of the carry flag are copied into bit 7 of the value pointed to by `regi` + `ofs8`.
* Opcode: `regi` `11001011` `ofs8` `00011110`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 4
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Data from bit 0 of the value pointed to by `regi` + `ofs8`
* Cycles: 4F + 1R + 1W + 1
{{< /expand >}}

## RRA

{{< expand "rra" "..." >}}
The value in `a` is rotated right by one bit position. Bit 0 is then copied into the [carry flag](../flags/#c-carry) and the previous contents of the carry flag are copied into bit 7 of `a`.
* Opcode: `00011111`
* Bytes: 1
* Flags:
    * H: Reset
    * N: Reset
    * C: Data from bit 0 of `a`
* Cycles: 1F
{{< /expand >}}

## RRC

{{< expand "rrc reg8" "..." >}}
The value in `reg8` is rotated right by one bit position. Bit 0 is then copied into the [carry flag](../flags/#c-carry) and is copied into bit 7 of `reg8` as well. Also includes 1R + 1W + 1 cycle if `reg8` is `(hl)`.
* Opcode: `11001011` `00001` `reg8`
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
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Data from bit 0 of `reg8`
* Cycles: 2F
{{< /expand >}}

{{< expand "rrc (regi + ofs8)" "..." >}}
The 8-bit value pointed to by `regi` + `ofs8` is rotated right by one bit position. Bit 0 is then copied into the [carry flag](../flags/#c-carry) and is copied into bit 7 of the value pointed to by `regi` + `ofs8` as well.
* Opcode: `regi` `11001011` `ofs8` `00001110`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 4
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Data from bit 0 of the value pointed to by `regi` + `ofs8`
* Cycles: 4F + 1R + 1W + 1
{{< /expand >}}

## RRCA

{{< expand "rrca" "..." >}}
The value in `a` is rotated right by one bit position. Bit 0 is then copied into the [carry flag](../flags/#c-carry) and is copied into bit 7 of `a` as well.
* Opcode: `00001111`
* Bytes: 1
* Flags:
    * H: Reset
    * N: Reset
    * C: Data from bit 0 of `a`
* Cycles: 1F
{{< /expand >}}

## RRD

{{< expand "rrd" "..." >}}
The contents of the low-order four bits of the 8-bit value pointed to by `hl` are copied into the low-order four bits of `a`. The CPU then copies the previous contents of the low-order four bits of `a` into the high-order four bits of the 8-bit value pointed to by `hl`. Finally, the previous contents of the high-order four bits of the 8-bit value pointed to by `hl` are copied into the low-order four bits of the value pointed to by `hl`.
* Opcode: `11101101` `01100111`
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Reset
    * P/V: Detects parity
    * N: Reset
* Cycles: 2F + 1R + 1W + 1
{{< /expand >}}

## SLA

{{< expand "sla reg8" "..." >}}
The 8-bit value in `reg8` is shifted left by one bit. Bit 7 is stored in the [carry flag](../flags#c-carry), and 0 is stored in bit 0. Also includes 1R + 1W + 1 cycle if `reg8` is `(hl)`.
* Opcode: `11001011` `00100` `reg8`
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
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Data from bit 7 of `reg8`
* Cycles: 2F
{{< /expand >}}

{{< expand "sla (regi + ofs8)" "..." >}}
The 8-bit value pointed to by `regi` + `ofs8` is shifted left by one bit. Bit 7 is stored in the [carry flag](../flags#c-carry), and 0 is stored in bit 0.
* Opcode: `regi` `11001011` `ofs8` `00100110`
* Bytes: 4
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Data from bit 7 of the value pointed to by `regi` + `ofs8`
* Cycles: 4F + 1R + 1W + 1
{{< /expand >}}

## SRA

{{< expand "sra reg8" "..." >}}
The 8-bit value in `reg8` is shifted right by one bit. Bit 0 is stored in the [carry flag](../flags#c-carry), and bit 7 is unchanged. Also includes 1R + 1W + 1 cycle if `reg8` is `(hl)`.
* Opcode: `11001011` `00101` `reg8`
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
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Data from bit 0 of `reg8`
* Cycles: 2F
{{< /expand >}}

{{< expand "sra (regi + ofs8)" "..." >}}
The 8-bit value pointed to by `regi` + `ofs8` is shifted right by one bit. Bit 0 is stored in the [carry flag](../flags#c-carry), and bit 7 is unchanged.
* Opcode: `regi` `11001011` `ofs8` `00101110`
* Bytes: 4
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Data from bit 0 of the value pointed to by `regi` + `ofs8`
* Cycles: 4F + 1R + 1W + 1
{{< /expand >}}

## SRL

{{< expand "srl reg8" "..." >}}
The 8-bit value in `reg8` is shifted right by one bit. Bit 0 is stored in the [carry flag](../flags#c-carry), and 0 is stored in bit 7. Also includes 1R + 1W + 1 cycle if `reg8` is `(hl)`.
* Opcode: `11001011` `00111` `reg8`
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
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Data from bit 0 of `reg8`
* Cycles: 2F
{{< /expand >}}

{{< expand "srl (regi + ofs8)" "..." >}}
The 8-bit value pointed to by `regi` + `ofs8` is shifted right by one bit. Bit 0 is stored in the [carry flag](../flags#c-carry), and 0 is stored in bit 7.
* Opcode: `regi` `11001011` `ofs8` `00111110`
* Bytes: 4
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Reset
    * P/V: Detects parity
    * N: Reset
    * C: Data from bit 0 of the value pointed to by `regi` + `ofs8`
* Cycles: 4F + 1R + 1W + 1
{{< /expand >}}

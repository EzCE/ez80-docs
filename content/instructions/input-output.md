---
title: Input / Output
weight: -10
---

{{< toc >}}

{{< hint type=caution >}}
The instructions in this section are included for completeness, but are not usable in user privileged code. Attempting to use an `out` instruction will trigger a reset and `in` will return garbage.
{{< /hint >}}

## IN

{{< expand "in a, (imm8)" "..." >}}
Reads a byte from the port located at a 16-bit address formed by the value in `a` and `imm8`. The upper byte of the address is the value in `a`, and the lower byte is `imm8`. The byte read from the port is then stored in `a`.
* Opcode: `11011011` `imm8`
* Bytes: 2
* Flags:
    * None
* Cycles: 2F + 1R
{{< /expand >}}

{{< expand "in reg8, (bc)" "..." >}}
Reads a byte from the port located at the 16-bit address in `bc` to `reg8`.
* Opcode: `11101101` `01` `reg8` `000`
    | Register | Bit Field |
    |----------|-----------|
    | `a`      | `111`     |
    | `b`      | `000`     |
    | `c`      | `001`     |
    | `d`      | `010`     |
    | `e`      | `011`     |
    | `h`      | `100`     |
    | `l`      | `101`     |

* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Reset
    * P/V: Detects parity
    * N: Reset
* Cycles: 2F + 1R
{{< /expand >}}

{{< expand "in (bc)" "..." >}}
Reads a byte from the port located at 16-bit address `bc` and affects flags accordingly.
* Opcode: `11101101` `01110000`
* Bytes: 2
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Reset
    * P/V: Detects parity
    * N: Reset
* Cycles: 2F + 1R
{{< /expand >}}

## IN0

{{< expand "in0 (imm8)" "..." >}}
Reads a byte from port `imm8` and affects flags accordingly.
* Opcode: `11101101` `00110000` `imm8`
* Bytes: 3
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Reset
    * P/V: Detects parity
    * N: Reset
* Cycles: 3F + 1R
{{< /expand >}}

{{< expand "in0 reg8, (imm8)" "..." >}}
Reads a byte from port `imm8` and stores it into `reg8`.
* Opcode: `11101101` `00` `reg8` `000` `imm8`
    | Register | Bit Field |
    |----------|-----------|
    | `a`      | `111`     |
    | `b`      | `000`     |
    | `c`      | `001`     |
    | `d`      | `010`     |
    | `e`      | `011`     |
    | `h`      | `100`     |
    | `l`      | `101`     |
* Bytes: 3
* Flags:
    * S: Affected as [defined](../flags/#s-sign)
    * Z: Affected as [defined](../flags/#z-zero)
    * H: Reset
    * P/V: Detects parity
    * N: Reset
* Cycles: 3F + 1R
{{< /expand >}}

## IND

{{< expand "ind" "..." >}}
Reads a byte from the port located at the 16-bit address in `bc`, which is then stored at the address in `hl`. Both `b` and `hl` are decremented, and the Z flag is set if `b` is decremented to 0.
* Opcode: `11101101` `10101010`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + 1R + 1W + 1
{{< /expand >}}

## INDR

{{< expand "indr" "..." >}}
Reads a byte from the port located at the 16-bit address in `bc`, which is then stored at the address in `hl`. Both `b` and `hl` are decremented, and the Z flag is set if `b` is decremented to 0. This operation is repeated until `b` is equal to 0.
* Opcode: `11101101` `10111010`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + (1R + 1W + 1) * b
{{< /expand >}}

## INDRX

{{< expand "indrx" "..." >}}
Reads a byte from the port located at the 16-bit address in `de`, which is then stored at the address in `hl`. Both `bc` and `hl` are decremented, and the Z flag is set if `bc` is decremented to 0. This operation is repeated until `bc` is equal to 0.
* Opcode: `11101101` `11001010`
* Bytes: 2
* Flags:
    * Z: Set if `bc` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + (1R + 1W + 1) * bc
{{< /expand >}}

## IND2

{{< expand "ind2" "..." >}}
Reads a byte from the port located at the 16-bit address in `bc`, which is then stored at the address in `hl`. Both `b`, `c`, and `hl` are decremented, and the Z flag is set if `b` is decremented to 0.
* Opcode: `11101101` `10001100`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + 1R + 1W + 1
{{< /expand >}}

## IND2R

{{< expand "ind2r" "..." >}}
Reads a byte from the port located at the 16-bit address in `de`, which is then stored at the address in `hl`. Both `bc`, `de`, and `hl` are decremented, and the Z flag is set if `bc` is decremented to 0. This operation is repeated until `bc` is equal to 0.
* Opcode: `11101101` `10011100`
* Bytes: 2
* Flags:
    * Z: Set if `bc` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + (1R + 1W + 1) * bc
{{< /expand >}}

## INDM

{{< expand "indm" "..." >}}
Reads a byte from port `c`, which is then stored at the address in `hl`. Both `b`, `c`, and `hl` are decremented, and the Z flag is set if `b` is decremented to 0.
* Opcode: `11101101` `10001010`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + 1R + 1W + 1
{{< /expand >}}

## INDMR

{{< expand "indmr" "..." >}}
Reads a byte from port `c`, which is then stored at the address in `hl`. Both `b`, `c`, and `hl` are decremented, and the Z flag is set if `b` is decremented to 0. This operation is repeated until `b` is equal to 0.
* Opcode: `11101101` `10011010`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + (1R + 1W + 1) * b
{{< /expand >}}

## INI

{{< expand "ini" "..." >}}
Reads a byte from the port located at the 16-bit address in `bc`, which is then stored at the address in `hl`. Then, `b` is decremented and `hl` is incremented by 1, and the Z flag is set if `b` is decremented to 0.
* Opcode: `11101101` `10100010`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + 1R + 1W + 1
{{< /expand >}}

## INIR

{{< expand "inir" "..." >}}
Reads a byte from the port located at the 16-bit address in `bc`, which is then stored at the address in `hl`. Then, `b` is decremented and `hl` is incremented by 1, and the Z flag is set if `b` is decremented to 0. This operation is repeated until `b` is equal to 0.
* Opcode: `11101101` `10110010`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + (1R + 1W + 1) * b
{{< /expand >}}

## INIRX

{{< expand "inirx" "..." >}}
Reads a byte from the port located at the 16-bit address in `de`, which is then stored at the address in `hl`. Then, `bc` is decremented and `hl` is incremented by 1, and the Z flag is set if `bc` is decremented to 0. This operation is repeated until `bc` is equal to 0.
* Opcode: `11101101` `11000010`
* Bytes: 2
* Flags:
    * Z: Set if `bc` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + (1R + 1W + 1) * bc
{{< /expand >}}

## INI2

{{< expand "ini2" "..." >}}
Reads a byte from the port located at the 16-bit address in `bc`, which is then stored at the address in `hl`. Then, `b` is decremented and `c` and `hl` are both incremented by 1, and the Z flag is set if `b` is decremented to 0.
* Opcode: `11101101` `10000100`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + 1R + 1W + 1
{{< /expand >}}

## INI2R

{{< expand "ini2r" "..." >}}
Reads a byte from the port located at the 16-bit address in `de`, which is then stored at the address in `hl`. Then, `bc` is decremented and `de` and `hl` are both incremented by 1, and the Z flag is set if `bc` is decremented to 0. This operation is repeated until `bc` is equal to 0.
* Opcode: `11101101` `10010100`
* Bytes: 2
* Flags:
    * Z: Set if `bc` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + (1R + 1W + 1) * bc
{{< /expand >}}

## INIM

{{< expand "inim" "..." >}}
Reads a byte from port `c`, which is then stored at the address in `hl`. Then, `b` is decremented and `c` and `hl` are both incremented by 1, and the Z flag is set if `b` is decremented to 0.
* Opcode: `11101101` `10000010`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + 1R + 1W + 1
{{< /expand >}}

## INIMR

{{< expand "inimr" "..." >}}
Reads a byte from port `c`, which is then stored at the address in `hl`. Then, `b` is decremented and `c` and `hl` are both incremented by 1, and the Z flag is set if `b` is decremented to 0. This operation is repeated until `b` is equal to 0.
* Opcode: `11101101` `10010010`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + (1R + 1W + 1) * b
{{< /expand >}}

## OTDM

{{< expand "otdm" "..." >}}
Outputs the value pointed to by `hl` to port `c`. Both `b`, `c`, and `hl` are decremented, and the Z flag is set if `b` is decremented to 0.
* Opcode: `11101101` `10001011`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + 1R + 1W + 1
{{< /expand >}}

## OTDMR

{{< expand "otdmr" "..." >}}
Outputs the value pointed to by `hl` to port `c`. Both `b`, `c`, and `hl` are decremented, and the Z flag is set if `b` is decremented to 0. This operation is repeated until `b` is equal to 0.
* Opcode: `11101101` `10011011`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + (1R + 1W + 1) * b
{{< /expand >}}


## OTDRX

{{< expand "otdrx" "..." >}}
Outputs the value pointed to by `hl` to the port located at the 16-bit address in `de`. Both `bc` and `hl` are decremented, and the Z flag is set if `bc` is decremented to 0. This operation is repeated until `bc` is equal to 0.
* Opcode: `11101101` `11001011`
* Bytes: 2
* Flags:
    * Z: Set if `bc` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + (1R + 1W + 1) * bc
{{< /expand >}}

## OTIM

{{< expand "otim" "..." >}}
Outputs the value pointed to by `hl` to port `c`. Then, `b` is decremented and `c` and `hl` are both incremented by 1, and the Z flag is set if `b` is decremented to 0.
* Opcode: `11101101` `10000011`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + 1R + 1W + 1
{{< /expand >}}

## OTIMR

{{< expand "otimr" "..." >}}
Outputs the value pointed to by `hl` to port `c`. Then, `b` is decremented and `c` and `hl` are both incremented by 1, and the Z flag is set if `b` is decremented to 0. This operation is repeated until `b` is equal to 0.
* Opcode: `11101101` `10010011`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + (1R + 1W + 1) * b
{{< /expand >}}

## OTIRX

{{< expand "otirx" "..." >}}
Outputs the value pointed to by `hl` to the port located at the 16-bit address in `de`. Then, `bc` is decremented and `hl` is incremented by 1, and the Z flag is set if `bc` is decremented to 0. This operation is repeated until `bc` is equal to 0.
* Opcode: `11101101` `11000011`
* Bytes: 2
* Flags:
    * Z: Set if `bc` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + (1R + 1W + 1) * bc
{{< /expand >}}

## OUT

{{< expand "out (imm8), a" "..." >}}
Outputs the value in `a` to the port located at a 16-bit address formed by the value in `a` and `imm8`. The upper byte of the address is the value in `a`, and the lower byte is `imm8`.
* Opcode: `11010011` `imm8`
* Bytes: 2
* Flags:
    * None
* Cycles: 2F + 1W
{{< /expand >}}

{{< expand "out (bc), reg8" "..." >}}
Outputs the byte in `reg8` to the port located at the 16-bit address in `bc`.
* Opcode: `11101101` `01` `reg8` `001`
    | Register | Bit Field |
    |----------|-----------|
    | `a`      | `111`     |
    | `b`      | `000`     |
    | `c`      | `001`     |
    | `d`      | `010`     |
    | `e`      | `011`     |
    | `h`      | `100`     |
    | `l`      | `101`     |

* Bytes: 2
* Flags:
    * None
* Cycles: 2F + 1R
{{< /expand >}}

## OUT0

{{< expand "out0 (imm8), reg8" "..." >}}
Outputs the value in `reg8` to port `imm8`.
* Opcode: `11101101` `00` `reg8` `001` `imm8`
    | Register | Bit Field |
    |----------|-----------|
    | `a`      | `111`     |
    | `b`      | `000`     |
    | `c`      | `001`     |
    | `d`      | `010`     |
    | `e`      | `011`     |
    | `h`      | `100`     |
    | `l`      | `101`     |
* Bytes: 3
* Flags:
    * None
* Cycles: 3F + 1W
{{< /expand >}}

## OUTD

{{< expand "outd" "..." >}}
Outputs the value pointed to by `hl` to the port located at the 16-bit address in `bc`. Both `b` and `hl` are decremented, and the Z flag is set if `b` is decremented to 0.
* Opcode: `11101101` `10101011`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + 1R + 1W + 1
{{< /expand >}}

## OTDR

{{< expand "otdr" "..." >}}
Outputs the value pointed to by `hl` to the port located at the 16-bit address in `bc`. Both `b` and `hl` are decremented, and the Z flag is set if `b` is decremented to 0. This operation is repeated until `b` is equal to 0.
* Opcode: `11101101` `10111011`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + (1R + 1W + 1) * b
{{< /expand >}}

## OUTD2

{{< expand "outd2" "..." >}}
Outputs the value pointed to by `hl` to the port located at the 16-bit address in `bc`. Both `b`, `c`, and `hl` are decremented, and the Z flag is set if `b` is decremented to 0.
* Opcode: `11101101` `10101100`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + 1R + 1W + 1
{{< /expand >}}

## OTD2R

{{< expand "otd2r" "..." >}}
Outputs the value pointed to by `hl` to the port located at the 16-bit address in `de`. Both `bc`, `de`, and `hl` are decremented, and the Z flag is set if `bc` is decremented to 0. This operation is repeated until `bc` is equal to 0.
* Opcode: `11101101` `10111100`
* Bytes: 2
* Flags:
    * Z: Set if `bc` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + (1R + 1W + 1) * bc
{{< /expand >}}

## OUTI

{{< expand "outi" "..." >}}
Outputs the value pointed to by `hl` to the port located at the 16-bit address in `bc`. Then, `b` is decremented and `hl` is incremented by 1, and the Z flag is set if `b` is decremented to 0.
* Opcode: `11101101` `10100011`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + 1R + 1W + 1
{{< /expand >}}

## OTIR

{{< expand "otir" "..." >}}
Outputs the value pointed to by `hl` to the port located at the 16-bit address in `bc`. Then, `b` is decremented and `hl` is incremented by 1, and the Z flag is set if `b` is decremented to 0. This operation is repeated until `b` is equal to 0.
* Opcode: `11101101` `10110011`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + (1R + 1W + 1) * b
{{< /expand >}}

## OUTI2

{{< expand "outi2" "..." >}}
Outputs the value pointed to by `hl` to the port located at the 16-bit address in `bc`. Then, `b` is decremented and `c` and `hl` are both incremented by 1, and the Z flag is set if `b` is decremented to 0.
* Opcode: `11101101` `10100100`
* Bytes: 2
* Flags:
    * Z: Set if `b` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + 1R + 1W + 1
{{< /expand >}}

## OTI2R

{{< expand "oti2r" "..." >}}
Outputs the value pointed to by `hl` to the port located at the 16-bit address in `de`. Then, `bc` is decremented and `de` and `hl` are both incremented by 1, and the Z flag is set if `bc` is decremented to 0. This operation is repeated until `bc` is equal to 0.
* Opcode: `11101101` `10110100`
* Bytes: 2
* Flags:
    * Z: Set if `bc` is decremented to 0, reset otherwise
    * N: Set if msb of data is 1, reset otherwise
* Cycles: 2F + (1R + 1W + 1) * bc
{{< /expand >}}

## TSTIO

{{< expand "tstio imm8" "..." >}}
Reads a byte from port `c`. Then, a bitwise AND operation is performed on the byte read with `imm8`, and flags are affected accordingly.
* Opcode: `11101101` `01110100` `imm8`
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

---
title: Processor Control
weight: -10
---

{{< toc >}}

## CCF

{{< expand "ccf" "..." >}}
Inverts the carry flag.
* Opcode: `00111111`
* Bytes: 1
* Flags:
    * H: Previous carry is copied
    * N: Reset
    * C: Inverted
* Cycles: 1F
{{< /expand >}}

## DI

{{< expand "di" "..." >}}
Resets the interrupt flags IEF1 and IEF2, disabling maskable interrupts.
* Opcode: `11110011`
* Bytes: 1
* Flags:
    * None
* Cycles: 1F
{{< /expand >}}

## EI

{{< expand "ei" "..." >}}
Sets the interrupt flags IEF1 and IEF2, enabling maskable interrupts.
* Opcode: `11111011`
* Bytes: 1
* Flags:
    * None
* Cycles: 1F
{{< /expand >}}

## HALT

{{< expand "halt" "..." >}}
Suspends CPU operation until an interrupt or reset occurs.
* Opcode: `01110110`
* Bytes: 1
* Flags:
    * None
* Cycles: 1F
{{< /expand >}}

## IM

{{< expand "im mode" "..." >}}
Sets the interrupt mode to either 0, 1, or 2. The different modes are described by this table:
| Mode | Behavior                                                                                                                                                                                                                                                                                                   |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0    | The interrupting device inserts an instruction on the data bus during an interrupt acknowledge cycle.                                                                                                                                                                                                      |
| 1    | The CPU responds to an interrupt by executing a restart to location $000038.                                                                                                                                                                                                                              |
| 2    | The interrupting device places the low-order address of the interrupt vector on the data bus during an interrupt acknowledge cycle. The `i` register provides the high-order byte of the interrupt vector table address. The 16-bit value formed is the starting address of the interrupt service routine. |
* Opcode: `11101101` `010` `mode` `110`
    | Mode | Bit Field |
    |------|-----------|
    | 0    | 00        |
    | 1    | 10        |
    | 2    | 11        |
* Bytes: 1
* Flags:
    * None
* Cycles: 1F
{{< /expand >}}

## NOP

{{< expand "nop" "..." >}}
No operation is perfomed.
* Opcode: `00000000`
* Bytes: 1
* Flags:
    * None
* Cycles: 1F
{{< /expand >}}

## RSMIX

{{< expand "rsmix" "..." >}}
Resets the mixed memory mode flag.
* Opcode: `11101101` `01111110`
* Bytes: 2
* Flags:
    * None
* Cycles: 2F
{{< /expand >}}

## SCF

{{< expand "scf" "..." >}}
Sets the carry flag.
* Opcode: `00111111`
* Bytes: 1
* Flags:
    * H: Reset
    * N: Reset
    * C: Set
* Cycles: 1F
{{< /expand >}}

## SLP

{{< expand "slp" "..." >}}
Suspends CPU operation until an interrupt or reset occurs.
* Opcode: `11101101` `01110110`
* Bytes: 2
* Flags:
    * None
* Cycles: 2F
{{< /expand >}}

## STMIX

{{< expand "stmix" "..." >}}
Sets the mixed memory mode flag.
* Opcode: `11101101` `01111101`
* Bytes: 2
* Flags:
    * None
* Cycles: 2F
{{< /expand >}}

## CALL

{{< expand "call cc, imm24" "..." >}}
If the condition `cc` is true, this operation pushes a return address (the address of the instruction immediately after this instruction) to the stack, then loads `pc` with `imm24` and resumes execution at that address.
* Opcode: `11` `cc` `100` `imm24`
    | Condition | Bit Field |
    |-----------|-----------|
    | NZ        | 000       |
    | Z         | 001       |
    | NC        | 010       |
    | C         | 011       |
    | PO        | 100       |
    | PE        | 101       |
    | P         | 110       |
    | M         | 111       |
* Bytes: 4
* Flags:
    * None
* Cycles:
    * If `cc` is true: 4F + 3W
    * If `cc` is false: 4F
{{< /expand >}}

{{< expand "call imm24" "..." >}}
This operation pushes a return address (the address of the instruction immediately after this instruction) to the stack, then loads `pc` with `imm24` and resumes execution at that address.
* Opcode: `11001101` `imm24`
* Bytes: 4
* Flags:
    * None
* Cycles: 4F + 3W
{{< /expand >}}

## DJNZ

{{< expand "djnz ofs8" "..." >}}
Decrements `b`, then checks if the resulting value in `b` is 0. If it is not, the signed value `ofs8` is added to `pc`.
* Opcode: `00010000` `ofs8`
* Bytes: 2
* Flags:
    * None
* Cycles:
    * If `b` is not decremented to 0: 3F + 1
    * If `b` is decremented to 0: 2F
{{< /expand >}}

## JP

{{< expand "jp (hl)" "..." >}}
Loads `pc` with the address stored in `hl`.
* Opcode: `11101001`
* Bytes: 1
* Flags:
    * None
* Cycles: 3F
{{< /expand >}}

{{< expand "jp cc, imm24" "..." >}}
If the condition `cc` is true, `pc` is loaded with the address stored in `hl`.
* Opcode: `11` `cc` `010` `imm24`
    | Condition | Bit Field |
    |-----------|-----------|
    | NZ        | 000       |
    | Z         | 001       |
    | NC        | 010       |
    | C         | 011       |
    | PO        | 100       |
    | PE        | 101       |
    | P         | 110       |
    | M         | 111       |
* Bytes: 4
* Flags:
    * None
* Cycles:
    * If `cc` is true: 4F + 1
    * If `cc` is false: 4F
{{< /expand >}}

{{< expand "jp imm24" "..." >}}
Loads `pc` with the address `imm24`.
* Opcode: `11000011` `imm24`
* Bytes: 4
* Flags:
    * None
* Cycles: 4F + 1
{{< /expand >}}

{{< expand "jp (regi)" "..." >}}
Loads `pc` with the address stored in `regi`.
* Opcode: `regi` `11101001`
    | Index | Bit Field  |
    |-------|------------|
    | `ix`  | `11011101` |
    | `iy`  | `11111101` |
* Bytes: 2
* Flags:
    * None
* Cycles: 4F
{{< /expand >}}

## JR

{{< expand "jr ofs8" "..." >}}
The signed value `ofs8` is added to `pc`.
* Opcode: `00011000` `ofs8`
* Bytes: 2
* Flags:
    * None
* Cycles: 3F
{{< /expand >}}

{{< expand "jr cc, ofs8" "..." >}}
If the condition `cc` is true, the signed value `ofs8` is added to `pc`.
* Opcode: `001` `cc` `000`
    | Condition | Bit Field |
    |-----------|-----------|
    | NZ        | 00        |
    | Z         | 01        |
    | NC        | 10        |
    | C         | 11        |
* Bytes: 2
* Flags:
    * None
* Cycles:
    * If `cc` is true: 3F + 1
    * If `cc` is false: 2F
{{< /expand >}}

## RET

{{< expand "ret cc" "..." >}}
If the condition `cc` is true, the top stack value is popped off into `pc`.
* Opcode: `11` `cc` `000`
    | Condition | Bit Field |
    |-----------|-----------|
    | NZ        | 000       |
    | Z         | 001       |
    | NC        | 010       |
    | C         | 011       |
    | PO        | 100       |
    | PE        | 101       |
    | P         | 110       |
    | M         | 111       |
* Bytes: 1
* Flags:
    * None
* Cycles:
    * If `cc` is true: 2F + 3R + 2
    * If `cc` is false: 1F + 1
{{< /expand >}}

{{< expand "ret" "..." >}}
The top stack value is popped off into `pc`.
* Opcode: `11001001`
* Bytes: 1
* Flags:
    * None
* Cycles: 2F + 3R + 1
{{< /expand >}}

## RETI

{{< expand "reti" "..." >}}
Used at the end of a maskable interrupt service routine to return to the point which caused the interrupt to trigger. Before calling this instruction, it is recommended to also enable interrupts with [`ei`](#ei) to allow recognition of interrupts after completion of the current interrupt service routine. The top stack entry is popped from the stack into `pc`.
* Opcode: `11101101` `01001101`
* Bytes: 2
* Flags:
    * None
* Cycles: 3F + 3R + 1
{{< /expand >}}

## RETN

{{< expand "retn" "..." >}}
Used at the end of a nonmaskable interrupt service routine to return to the point which caused the interrupt to trigger. The return address is popped from the stack into `pc`, and the state of IEF2 is copied back into IEF1. As a result, maskable interrupts will be immediately enabled after calling this instruction if they were enabled prior to when the current interrupt occured.
* Opcode: `11101101` `01000101`
* Bytes: 2
* Flags:
    * None
* Cycles: 3F + 3R + 1
{{< /expand >}}

## RST

{{< expand "rst imm8" "..." >}}
This instruction functions similar to the [`call`](#call) instruction. However `imm8` is limited to 8 specific values: $00, $08, $10, $18, $20, $28, $30, and $38. The address of the instruction following the current `rst` instruction is pushed to the stack, and then `pc` is loaded with `imm8`.
{{< hint type=warning >}}
Using this instruction on the CE will most likely cause a crash to occur, regardless of the restart address.
{{< /hint >}}
* Opcode: `11` `imm8` `111`
    | Restart Address | Bit Field |
    |-----------------|-----------|
    | $00             | 000       |
    | $08             | 001       |
    | $10             | 010       |
    | $18             | 011       |
    | $20             | 100       |
    | $28             | 101       |
    | $30             | 110       |
    | $38             | 111       |
* Bytes: 1
* Flags:
    * None
* Cycles: 2F + 3W + 1
{{< /expand >}}

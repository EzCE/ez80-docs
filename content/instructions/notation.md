---
title: Notation
weight: -20
---

{{< toc >}}

The instruction documentation includes shorthand abbreviation for frequently used terms. A table containing the notations and their definitions is below:

| Notation      | Definition                                                                                                                                                                   |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| (imm24)       | The value pointed to by a 24-bit address. The size of the value depends on the instruction.                                                                                  |
| (reg24)       | The value pointed to by the address in a 24-bit register. The size of the value depends on the instruction.                                                                  |
| (regi + ofs8) | The value pointed to by an address formed by the sum of the 24-bit value of an index register plus an 8-bit signed offset. The size of the value depends on the instruction. |
| cc            | Condition code C, NC, Z, NZ, P, M, PO, or PE - tests of single bits in Flags register.                                                                                       |
| cc'           | Condition code C, NC, Z, or NZ - tests of single bits in Flags register.                                                                                                     |
| h / l         | High or low byte of a register pair, respectively.                                                                                                                           |
| imm24         | 24-bit immediate data value.                                                                                                                                                 |
| imm16         | 16-bit immediate data value.                                                                                                                                                 |
| imm8          | 8-bit immediate data value.                                                                                                                                                  |
| imm3          | 3-bit immediate data value.                                                                                                                                                  |
| ofs8          | 8-bit immediate data value serving as an offset.                                                                                                                             |
| reg24         | 24-bit register pair.                                                                                                                                                        |
| reg16         | 16-bit register pair.                                                                                                                                                        |
| reg8          | 8-bit register.                                                                                                                                                              |
| reg8i         | 8-bit high or low byte of an index register.                                                                                                                                 |
| regi          | Index register pair `ix` or `iy`                                                                                                                                             |
| regir         | Interrupt vector register `i` or refresh counter regiser `r`.                                                                                                                |

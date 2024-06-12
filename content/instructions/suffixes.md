---
title: Suffixes
weight: -20
---

{{< toc >}}

## Overview
Many instructions have optional suffixes which can be added for switching between memory modes. The four suffixes available are **.SIS**, **.SIL**, **.LIS**, and **.LIL**. These suffixes can be used when an exception to the default memory mode is needed for a certain instruction or a section of instructions.

These four suffixes are made up of two parts, the first being either **.S** or **.L** and the second being either **.IS** or **.IL**. The **.S** and **.L** portion (**S**hort and **L**ong) indicate whether the the operation and internal registers use 16-bits or 24-bits, respectively. They also indicate whether the MBASE is used for addresses, with **.S** using it and **.L** not.

The **.IS** or **.IL** portion (**I**nstruction Stream **S**hort and **I**nstruction Stream **L**ong) affect the CPU's control block, indicating whether a multibyte immediate data or address value fetched during instruction execution is 2 or 3 bytes long. For example, an `ld.lil hl, imm24` requires 3 bytes of data (imm24) to be loaded while an `ld.sis hl, imm16` instruction requires only 2 bytes of data (imm16) to be loaded.

If only a partial suffix is supplied, such as `ld.s` or `ld.il`, the assembler determines the other part of the suffix based on the default memory mode which is determined by the ADL mode bit. For more detail, see the table below:

| Partial Suffix | ADL Bit | Full Suffix |
|----------------|---------|-------------|
| .S             | 0       | .SIS        |
| .S             | 1       | .SIL        |
| .L             | 0       | .LIS        |
| .L             | 1       | .LIL        |
| .IS            | 0       | .SIS        |
| .IS            | 1       | .LIS        |
| .IL            | 0       | .SIL        |
| .IL            | 1       | .LIL        |

## Single-Instruction Suffix Application
The CPU can perform a single instruction's operation in a specified memory mode and will then switch back to the prior mode afterwards. This applies to all instructions using suffixes other than [`call`](../processor-control/#call), [`jp`](../processor-control/#jp), [`ret`](../processor-control/#ret), [`reti`](../processor-control/#reti), [`retn`](../processor-control/#retn), and [`rst`](../processor-control/#rst).

## Persistent Suffix Application
To make a persistent change in memory mode, a control transfer instruction ([`call`](../processor-control/#call), [`jp`](../processor-control/#jp), [`ret`](../processor-control/#ret), [`reti`](../processor-control/#reti), [`retn`](../processor-control/#retn), and [`rst`](../processor-control/#rst)) with a suffix must be used. It is also possible to achieve this with an interrupt or trap operation, though user-written code does not really have control over this. After the memory mode has been changed by one of these instructions, it will remain changed until the same method is used to change it back. For example, calling or jumping with the `.lis` suffix will keep the changed memory mode active, but returning with `.lil` will force it back.

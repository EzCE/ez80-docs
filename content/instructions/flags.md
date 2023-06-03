---
title: Flags
weight: -20
---

{{< toc >}}

## Introduction

This page contains information on the flags available on the TI-84 Plus CE, and is based on the lesson "Day 4: Flags" from [*Learn TI-83 Plus Assembly In 28 Days*](https://taricorp.gitlab.io/83pa28d/index.html). The flags are stored in the F register, with each bit representing a certain flag. When a flag is set, the bit is equal to 1, and when a flag is reset, the bit is equal to 0. Below is a map with each bit and the flag it represents:

| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|
| s | z | - | h | - |p/v| n | c |

As you can see, the 3rd and 5th bits are not used as flags. Here's what the rest of the flags do:

## S (Sign)

This flag is set if the result of an operation is a negative number, and reset if the result is a positive number. Note that some instructions do not modify the sign flag, while others do, so keep that in mind.

## Z (Zero)

If the last instruction caused a register to equal zero, this flag is set. Otherwise, the flag is reset. In some instructions, such as `cp`, this flag is set when the things being compared are identical, and reset if they are not. When checking a bit, this flag will reflect the status of the bit being checked, with the flag being set if the bit is 0 and reset if the bit is 1.

## H (Half-Carry)

This flag functions nearly identically to `c`, though the carry is instead detected in the least-significant nibble. It is almost never used.

## P / V (Parity / Overflow)

This flag checks both parity and overflow (as the name implies). An overflow occurs when a register has a value exceeding the signed 8-bit range, which will cause this to be set. For the parity, the flag will be set when the number of 1s in the accumulator is even, and reset when it is odd. Whether the flag reflects parity or overflow will depend on the instruction being used.

## N (Add / Subtract)

This flag is reset if the last instruction used was an addition instruction, and set if the last instruction was a subtraction instruction. However, it is almost never used like `h`.

## C (Carry)

This flag is similar to `p/v`, with the difference being that `p/v` detects signed overflows, while `c` detects unsigned overflows. If the result of an addition was too large to fit in an 8-bit or 16-bit register, this flag is set. It is also set if the result of a subtraction was negative.

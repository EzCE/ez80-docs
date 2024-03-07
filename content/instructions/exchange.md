---
title: Exchange
weight: -10
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

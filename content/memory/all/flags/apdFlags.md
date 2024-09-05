---
title: apdFlags
geekdocHidden: true
params:
    address: $D00088 (ti.flags + $08)
    name: apdFlags
---

Automatic power-down flags.

### Address: $D00088 (ti.flags + $08)

### Size: 1 byte

#### Bit 2 - apdAble:
Set if APD is enabled.

#### Bit 3 - apdRunning:
Set if the APD clock is running.

#### Bit 4 - apdWarmStart:
Set if the calculator is turning on from APD or a power failure.

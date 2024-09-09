---
title: groupFlags
geekdocHidden: true
params:
    address: $D000A6 (ti.flags + $26)
    name: groupFlags
---

Flags used temporarily in Arc_Unarc.

### Address: $D000A6 (ti.flags + $26)

### Size: 1 byte

#### Bit 1 - inGroup:
Set when in group context.

#### Bit 2 - noCompletionByte:
Set to not write $FC when calling Arc_Unarc and leave as $FE.

#### Bit 3 - noDataWrite:
Set to not write data or size bytes when calling Arc_Unarc.

#### Bit 5 - writeSizeBytesOnly:
Set to only write size bytes when calling Arc_Unarc.

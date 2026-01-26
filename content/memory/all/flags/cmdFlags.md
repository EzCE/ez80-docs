---
title: cmdFlags
geekdocHidden: true
params:
    address: $D0008C (ti.flags + $0C)
    name: cmdFlags
---

### Address: $D0008C (ti.flags + $0C)

Command editor flags.

### Size: 1 byte

#### Bit 5 - cmdVirgin:
Set if nothing has been typed in the CMD buffer.

#### Bit 6 - cmdExec:
Set if a command needs to be executed.

---
title: flags
geekdocHidden: true
params:
    address: $D00080
    name: flags
---

This area holds system flags, and consists of 128 bytes before `$D00080` and 127 bytes after. Because of this, the area technically spans from `$D00000` - `D000FF`, but it is equated to `$D00080` so that flags can be accessed at both positive and negative offsets.

### Address: $D00080

### Size: 256 bytes

A list of known system flag locations is below:

{{% list-by-address "memory/all/flags" %}}

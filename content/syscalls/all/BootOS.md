---
title: BootOS
geekdocHidden: true
params:
    address: $020108
    category: System
    name: BootOS
---

### Address: $020108

As the name suggests, this call boots the OS.

{{< hint type=caution >}}
If this routine is called, it will not return.
{{< /hint >}}

### Inputs:
* None.

### Outputs:
* Boots the OS.

### Destroys:
* All RAM is reset.

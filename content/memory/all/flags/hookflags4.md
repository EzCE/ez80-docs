---
title: hookflags4
geekdocHidden: true
params:
    address: $D000B6 (ti.flags + $36)
    name: hookflags4
---

### Address: $D000B6 (ti.flags + $36)

### Size: 1 byte

### Bit 0 - traceHookActive:
Set if a [trace hook](../../../../other/hooks/Trace) is active, reset otherwise.

### Bit 1 - parserHookActive:
Set if a [parser hook](../../../../other/hooks/Parser) is active, reset otherwise.

### Bit 2 - appChangeHookActive:
Set if an [app change hook](../../../../other/hooks/AppChange) is active, reset otherwise.

### Bit 3 - catalog1HookActive:
Set if a [catalog 1 hook](../../../../other/hooks/Catalog1) is active, reset otherwise.

### Bit 4 - helpHookActive:
Set if a [help hook](../../../../other/hooks/Help) is active, reset otherwise.

### Bit 5 - cxRedispHookActive:
Set if a [cxRedisp hook](../../../../other/hooks/cxRedisp) is active, reset otherwise.

### Bit 6 - menuHookActive:
Set if a [menu hook](../../../../other/hooks/Menu) is active, reset otherwise.

### Bit 7 - silentLinkHookActive:
Set if a [silent link hook](../../../../other/hooks/SilentLink) is active, reset otherwise.

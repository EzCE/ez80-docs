---
title: CallFontHook
geekdocHidden: true
params:
    address: $020130
    category: Hooks
    name: CallFontHook
---

Checks if a valid font hook is currently installed. If so, that hook is called, otherwise, this routine returns.

### Address: $020130

### Inputs:
* None.

### Outputs:
* Calls the currently installed font hook if it exists.

### Destroys:
* If no font hook exists, this call does not destory anything. Otherwise it follows the behavior of the currently installed font hook.

---
title: CallFontHook
geekdocHidden: true
params:
    address: $020130
    category: Hooks
    name: CallFontHook
---

### Address: $020130

Checks if a valid font hook is currently installed. If so, that hook is called, otherwise, this routine returns.

### Inputs:
* None.

### Outputs:
* Calls the currently installed font hook if it exists.

### Destroys:
* If no font hook exists, this call does not destory anything. Otherwise it follows the behavior of the currently installed font hook.

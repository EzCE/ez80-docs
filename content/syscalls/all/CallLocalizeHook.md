---
title: CallLocalizeHook
geekdocHidden: true
params:
    address: $020134
    category: Hooks
    name: CallLocalizeHook
---

Checks if a valid localization hook is currently installed. If so, that hook is called, otherwise, this routine returns.

### Address: $020134

### Inputs:
* None.

### Outputs:
* Calls the currently installed localization hook if it exists.

### Destroys:
* If no localization hook exists, this call does not destory anything. Otherwise it follows the behavior of the currently installed localization hook.

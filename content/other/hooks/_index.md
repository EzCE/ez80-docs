---
title: Hooks
weight: -20
---

{{< toc >}}

{{< hint type=important >}}
As of TI-OS version 5.8.3, TI-OS prevents hook pointer locations outside of apps and the OS itself. In order for your hooks to work on all OS versions, it is recommended to use an app to store your hook code. Provided that the pointer to the hook code is located in the correct area of memory, the hook installation / removal calls can be used from any context, including programs.
{{< /hint >}}

## Introduction
Hooks are a feature of TI-OS which allow user-created apps and programs to run code when certain events in TI-OS are triggered. TI-OS supports a number of different hooks, which are listed [below](#list-of-hooks).

Each hook type typically has a system call for both setting and clearing itself, along with a flag which is set when the a hook of that type is installed and a 3-byte section of RAM which holds a pointer to the hook's code if one is installed.

When working with a user-created hook, the code for the hook should be located in the **safest location** feasible. If a hook is stored in a place like RAM which is prone to frequent movement, it is likely to be quickly destroyed. Ideally, hooks are stored in an app (which is stored in a stable portion of flash memory), but for smaller projects this may seem like overkill. Another possible solution (on OS versions **Pre-5.8.3**) is to store it in an archived AppVar. A source code template for making a hook stored in an AppVar with an installer program can be found [here](https://github.com/EzCE/hook-template/).

## Working with hooks
In order for TI-OS to recognize a section of code as a valid hook, the first byte of it **must** be `$83`. This can be achieved as follows:
```
_hookStart:
    db $83
    ; main hook code
    ret
```

To set the hook as active, simply load `hl` with the address of the hook's data and call the set hook system call for the hook type of your choice. For example, the code to set an App Change hook would be:
```
ld hl, _hookStart
call ti.SetAppChangeHook
```

To clear the currently active hook of a certain type, TI-OS only requires you to call the clear hook system call for that hook type. Continuing with our previous example, clearing an App Change hook would look like this:
```
call ti.ClrAppChangeHook
```

To check if a hook is active, you can use the [bit instruction](../../instructions/bit-manipulation#bit) to check that hook's associated system flag. To check if an App Change hook is active, you would do this:
```
ld iy, ti.flags
bit ti.appChangeHookActive, (iy + hookflags4)
; Zero flag is reset (nz) if an App Change hook is active, and set (z) otherwise.
```

In some cases, you may want to know more than just whether a hook of a certain type is active, such as specfic details about the code of the hook currently active. You can achieve this by reading the hook's data pointer from its associated 3 bytes of RAM, and use this for whatever purposes you wish. For example, to check if the App Change hook currently active is our hook starting at `_hookStart`, we can read the pointer from memory and compare it with the address of `_hookStart` to check if they match:
```
ld hl, (ti.appChangeHookPtr)
ld de, _hookStart
or a, a
sbc hl, de
; Zero flag is reset if the pointers match
```

## Restoring and chaining hooks
In some cases, it will be necessary to take care of a previously installed hook before installing another hook of the same type. In this situation, you have three options: to clear the original hook completely, to save and restore the original hook at a future time, or to chain the original hook allowing both your hook and that hook to be used at the same time. The best option out of these three is different depending on the type of hook you're working with and how long you plan for it to be enabled; some hooks cooperate well with others in a chain and others do not.

Saving and restoring the original hook is simpler than chaining, and is especially useful in cases where a hook will only be installed for a brief period of time. Using this method, you can save the original hook, install your own hook, and then clear your hook and restore the original one later. To do this, start by loading the original hook's data pointer from RAM and saving it in a secure location before installing your own hook. This location will differ depending on your exact situation, but one possible location would be an AppVar. After clearing your hook, load the original hook's data pointer back from the secure location and install it again to restore it.

Chaining a hook begins with a similar process to saving and restoring, by saving the data pointer to the hook being chained with in a secure location such as an AppVar. However, in order to trigger the original hook when your hook is finished executing, you'll need to load the pointer for the original hook and then jump to it at the end of your hook's code. When doing this, it is important to keep a few things in mind: First, it is a good practice to check that the pointer is still pointing to a valid hook (check that the first byte is still `$83`). You'll also need to make sure to jump to the byte after the `$83` hook signifier, since the actual hook execution begins after it. Finally, you should ensure that the registers, stack, and any other special conditions are in the same state they were when your hook was entered. This is necessary as the hook you jump to will expect them to be set up as if it is being called from the OS.

## List of hooks

{{% list-by-name "other/hooks/" %}}

---
title: Testing Programs With CEmu
weight: -10
---

It's important to have a safe way to test your assembly programs before trying them out on physical hardware. This section covers how to use the [CEmu](https://github.com/CE-Programming/CEmu) emulator to test and debug your programs on Windows, macOS, or Linux.

{{< toc >}}

## Setup
First, make sure you've followed the steps to install CEmu and set up a ROM. If you haven't done this already, you can follow the instructions in the [Getting Started](../getting-started/#installing-cemu) section. Once you're all set up, locate the **.8xp** file that fasmg generated in your file manager and drag it over the emulator's screen. You should see two options: One to send the file to the Archive, and one to send it to RAM.

<p style="text-align: center;"><img src="../images/transfer-file-cemu.png" alt="Transferring a file to CEmu"></p>

Either RAM or Archive is fine, but sending to Archive will ensure the file is not lost and will not need to be re-sent in the event of a crash. Running the program is the same as on physical hardware, and you can either use the CEmu's keypad dock or your own keyboard to navigate through TI-OS.

## Debugging Programs
This section is simply a brief overview of some of CEmu's debugging features. For a more thorough explanation, check out CEmu's [official documentation](https://github.com/CE-Programming/CEmu/wiki).

One of the benefits of testing programs in an emulator like CEmu is the ability to step through and debug assembly, along with viewing the status of memory, flags, registers, and more at any time. To access CEmu's assembly debugger, the emulation must first be stopped. This can be done with the Debug Control dock, found under **Debug > Debug Control**. The Debug Control dock will also be necessary for other features of the assembly debugger, so it is recommended to have it easily accessible.

It is also possible to open the debugger with software commands that can be included in your assembly program. To do this, insert the following code in your assembly program at the point you wish to debug:

```
scf
sbc hl, hl
ld (hl), 2
```

There are a number of other software commands CEmu supports as well, which can be seen [here](https://github.com/CE-Programming/CEmu/wiki/Software-Commands).

With the disassembly view (**Debug > Disassembly**), you can see the currently executing instruction, and you can use the debug controls to step through one instruction at a time, step out of a call, and more. You can also right click an instruction in the assembly view to run until the emulator reaches it, or jump to a specific instruction by right clicking it and selecting "Set PC" to set the program counter. The **Goto** button allows you to view a disassembly at a specific address without jumping to it, and the small folder icon by **Equates** lets you load a file such as **ti84pceg.inc** and view the symbols associated with certain values.

<p style="text-align: center;"><img src="../images/disassembly-view.png" alt="Disassembly view"></p>

When stepping through an assembly program, it's also a good idea to keep an eye on the CPU registers, flags, and stack. You'll learn about these more in future tutorial sections, but for now you can view them using the CPU Status dock (**Debug > CPU Status**). When the debugger is open, you can select and modify the values of flags and registers. When closing and reopening the debugger, you may also notice that some values are highlighted in yellow. The yellow highlight indicates that the value has changed since the last time that the emulation was stopped, and can be useful for monitoring what is affected by certain instructions or calls.

<p style="text-align: center;"><img src="../images/cpu-status.png" alt="CPU Status dock"></p>

The last debugging dock this brief overview will cover is the Memory View (**Debug > Add memory view**). The Memory View is pretty self explanatory, and allows you to view the data in memory at any specific address, and has an interface similar to a hex editor. You can also modify the values in memory as well. To jump to an address in the Memory View, press the **Goto** button.

<p style="text-align: center;"><img src="../images/memory-view.png" alt="Memory View"></p>

While these are the only features covered in this section, CEmu also supports quite a number of other more specific debugging features, which you can learn about [here](https://github.com/CE-Programming/CEmu/wiki/Basic-Debugging-Features).

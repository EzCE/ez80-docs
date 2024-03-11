# Contributing

## Format

The format for system calls is as follows:

````Markdown
---
title: System call name
geekdocHidden: true
params:
    address: System call address
    category: System call category
    name: System call name
---

Overview of what the system call does / is used for

### Address: $000000

### Inputs:
* Input 1: Description
* Input 2: Description...

### Outputs:
* Output 1: Description
* Output 2: Description...

### Destroys:
* Destroy 1
* Destroy 2...

### Examples:                       <!-- If applicable -->
Description of example:

```asm
; example code goes here
; since it's an example, be sure to comment thoroughly
```
````

An alternative method is to use the command `hugo new "syscalls/all/<name>.md" --kind calls`

Each call should have its own file, named after the call. These files go in the **content/syscalls/all/** directory.

It is also recommended to take a look at some the already existing documentation to get a feel for how things should be formatted.

A list of system calls which are not yet documented in eZ80 docs can be found under **content/syscalls/to-do.txt**. If you add a call, make sure ot remove it from the text file as well!

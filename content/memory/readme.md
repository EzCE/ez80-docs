# Contributing

## Format

The format memory areas is as follows:

````Markdown
---
title: Memory area name
geekdocHidden: true
params:
    address: Memory address
    name: Memory area name
---

Overview of what the memory area does / is used for

### Address: $000000

### Size: Size of the area in bytes
````

An alternative method is to use the command `hugo new "memory/all/<name>.md" --kind memory`

Each area should have its own file, named after the area. These files go in the **content/memory/all/** directory.

It is also recommended to take a look at some the already existing documentation to get a feel for how things should be formatted.

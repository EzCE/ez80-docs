# Contributing

## Format

The format for instructions is as follows:

```Markdown
# Parent Instruction

{{< expand "variant 1" "..." >}}
Brief overview of what the variant does
* Opcode: `opcode`
* Bytes: Size of the opcode in bytes
* Flags: Flags affected and causes
* Cycles: Cycle count
{{< /expand >}}

{{< expand "variant 2" "..." >}}
...
```


Immediate values are represented by `imm` and the size. For example, `imm8` is an immediate 8-bit value.

Offset values are represented by `off` and the size. For example, `ofs8` is an 8-bit offset.

Registers can be named, or a wildcard can be used instead depending on the context. For example, `reg8` refers to any 8-bit register, `regi` refers to the index registers, and `regir` refers to the `i` and `r` registers.

For easier understanding, a letter is used to note the wildcard register's purpose. For example, `reg8D` refers to the destination, while `reg8S` refers to the source.

import sys
import re

MATCH_EQUATE = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:=\s*([0-9A-Fa-f]+)h\s*$")
FILE = "content/syscalls/to-do.txt"

with open(FILE, "r") as f:
    lines = f.readlines()

addresses = {}

for line in lines:
    m = MATCH_EQUATE.match(line)
    if m:
        name = m.group(1)
        addr = m.group(2).upper().rjust(6, "0")
        addresses[name] = f"$0{addr}" if len(addr) == 6 else f"${addr}"

name = sys.argv[1]

if input("Remove line from to-do.txt? (y/n): ").strip().lower() == 'y':
    linesnew = []
    for line in lines:
        m = MATCH_EQUATE.match(line)
        if m and m.group(1) == name:
            print("Removed")
            continue
        linesnew.append(line)

    with open(FILE, "w") as f:
        f.writelines(linesnew)

address = addresses[name]
category = sys.argv[2]

with open(f"content/syscalls/all/{name}.md", "w") as f:
    f.write(f"""---
title: {name}
geekdocHidden: true
params:
    address: ${address[2:8]}
    category: {category}
    name: {name}
---

### Address: ${address[2:8]}

Overview of what the system call does / is used for

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
""")

print(f"Created 'content/syscalls/all/{name}.md'")

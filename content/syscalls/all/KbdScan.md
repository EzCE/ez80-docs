---
title: KbdScan
geekdocHidden: true
params:
    address: $020148
    category: Keyboard
    name: KbdScan
---

Scans the keyboard for any key presses and updates the value at [`kbdScanCode`](../../../memory/all/kbdScanCode) accordingly.  A list of possible scan codes is below:

{{< expand "Scan Codes" "..." >}}
| Scan Code  | Scan Code (Hex) |
|------------|-----------------|
| skDown     | $01             |
| skLeft     | $02             |
| skRight    | $03             |
| skUp       | $04             |
| skEnter    | $09             |
| skAdd      | $0A             |
| skSub      | $0B             |
| skMul      | $0C             |
| skDiv      | $0D             |
| skPower    | $0E             |
| skClear    | $0F             |
| skChs      | $11             |
| sk3        | $12             |
| sk6        | $13             |
| sk9        | $14             |
| skRParen   | $15             |
| skTan      | $16             |
| skVars     | $17             |
| skDecPnt   | $19             |
| sk2        | $1A             |
| sk5        | $1B             |
| sk8        | $1C             |
| skLParen   | $1D             |
| skCos      | $1E             |
| skPrgm     | $1F             |
| skStat     | $20             |
| sk0        | $21             |
| sk1        | $22             |
| sk4        | $23             |
| sk7        | $24             |
| skComma    | $25             |
| skSin      | $26             |
| skMatrix   | $27             |
| skGraphvar | $28             |
| skStore    | $2A             |
| skLn       | $2B             |
| skLog      | $2C             |
| skSquare   | $2D             |
| skRecip    | $2E             |
| skMath     | $2F             |
| skAlpha    | $30             |
| skGraph    | $31             |
| skTrace    | $32             |
| skZoom     | $33             |
| skWindow   | $34             |
| skYequ     | $35             |
| sk2nd      | $36             |
| skMode     | $37             |
| skDel      | $38             |
{{< /expand >}}

### Address: $020148

### Inputs:
* None.

### Outputs:
* Value at [`kbdScanCode`](../../../memory/all/kbdScanCode) contains scan code.

### Destroys:
* `hl`, `bc`, `a`

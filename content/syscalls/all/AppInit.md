---
title: AppInit
geekdocHidden: true
params:
    address: $020190
    category: Context
    name: AppInit
---

This routine is used by applications to override the system vectors with the app's own vectors.

For more info on each vector, see:
- [Main](../../../memory/all/cxMain)
- [Partial PutAway](../../../memory/all/cxPPutAway)
- [PutAway](../../../memory/all/cxPutAway)
- [ReDisplay](../../../memory/all/cxReDisp)
- [Error EP](../../../memory/all/cxErrorEP)
- [Window Size Change](../../../memory/all/cxSizeWind)

### Address: $020190

### Inputs:
* `hl`: Pointer to vector table.

### Outputs:
* Sets vector table.

### Destroys:
* `af`, `bc`, `de`, `hl`.

### Examples:
This is the appropriate format expected for the vector table. You must define the pointers to these vectors yourself. If you are not using a vector, you can set the pointer to a dummy return label:

```asm
vectors:
dl cxMainPtr        ; Pointer to your routine to be used as the Main vector.
dl cxPPutAwayPtr    ; Pointer to your routine to be used as the Partial PutAway vector.
dl cxPutAwayPtr     ; Pointer to your routine to be used as the PutAway vector.
dl cxReDispPtr      ; Pointer to your routine to be used as the ReDisplay vector.
dl cxErrorEPPtr     ; Pointer to your routine to be used as the Error EP vector.
dl cxSizeWindPtr    ; Pointer to your routine to be used as the Window Size Change vector.
db appFlags         ; Value copied to `(iy + appFlags)`
```

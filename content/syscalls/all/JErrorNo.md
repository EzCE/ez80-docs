---
title: JErrorNo
geekdocHidden: true
params:
    address: $02012C
    category: System
    name: JErrorNo
---

This routine displays a system error or calls an error handler, based on the value at [`errNo`](../../../memory/all/errNo). To allow the "Goto" option for a system error, bit 7 of the error code should be set, and to prevent it, bit 7 should be reset.
A list of system error codes is below. These are taken from **ti84pceg.inc**, and you should note that some allow "Goto" by default while others do not. However, this behavior can be changed by modifying bit 7.

{{< expand "Error Codes" "..." >}}
| Error             | Default Code (Hex) |
|-------------------|--------------------|
| E_Mask (No error)	| $7F                |
| E_Overflow        | $81                |
| E_DivBy0          | $82                |
| E_SingularMat     | $83                |
| E_Domain          | $84                |
| E_Increment       | $85                |
| E_Break           | $86                |
| E_NonReal         | $87                |
| E_Syntax          | $88                |
| E_DataType        | $89                |
| E_Argument        | $8A                |
| E_DimMismatch     | $8B                |
| E_Dimension       | $8C                |
| E_Undefined       | $8D                |
| E_Memory          | $8E                |
| E_Invalid         | $8F                |
| E_IllegalNest     | $90                |
| E_Bound           | $91                |
| E_GraphRange      | $92                |
| E_Zoom            | $93                |
| E_Label           | $14                |
| E_Stat            | $15                |
| E_Solver          | $96                |
| E_Singularity     | $97                |
| E_SignChange      | $98                |
| E_Iterations      | $99                |
| E_BadGuess        | $9A                |
| E_StatPlo         | $1B                |
| E_TolTooSmall     | $9C                |
| E_Reserved        | $9D                |
| E_Mode            | $9E                |
| E_LnkErr          | $9F                |
| E_LnkMemErr       | $A0                |
| E_LnkTransErr     | $A1                |
| E_LnkDupErr       | $A2                |
| E_LnkMemFull      | $A3                |
| E_Unknown         | $A4                |
| E_Scale           | $A5                |
| E_IdNotFound      | $26                |
| E_NoMode          | $A7                |
| E_Validation      | $28                |
| E_Length          | $A9                |
| E_Application     | $AA                |
| E_AppErr1         | $AB                |
| E_AppErr2         | $AC                |
| E_ExpiredApp      | $2D                |
| E_BadAdd          | $2E                |
| E_Archived        | $AF                |
| E_Version         | $30                |
| E_ArchFull        | $31                |
| E_Variable        | $B2                |
| E_Duplicate       | $B3                |
| E_Date            | $B4                |
| E_UnknownCmd      | $B5                |
| E_OverLimit       | $36                |
| E_Disabled        | $37                |
| E_Xmit            | $38                |
| E_MemFull         | $39                |
{{< /expand >}}

{{< hint type=caution >}}
If this routine is called, it will not return.
{{< /hint >}}

### Address: $02012C

### Inputs:
* Value at [`errNo`](../../../memory/all/errNo) contains error code.
* Bit 7 of error code is set for "Goto" option, or reset if "Goto" is not allowed.

### Outputs:
* Displays system error or calls error handler.
* If a custom error handler is called, the error code will be in `a`.

### Destroys:
* This routine does not return.

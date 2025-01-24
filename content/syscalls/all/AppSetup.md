---
title: AppSetup
geekdocHidden: true
params:
    address: $021148
    category: Apps
    name: AppSetup
---

Cleans up flags and hooks before running a flash application. 

### Address: $021148

### Inputs:
* Set bit in [`hookflags2Override`](../../../memory/all/flags/hookflags2Override), [`hookflags3Override`](../../../memory/all/flags/hookflags3Override), or [`hookflags4Override`](../../../memory/all/flags/hookflags4Override) corresponding to a [`hookflags2`](../../../memory/all/flags/hookflags2), [`hookflags3`](../../../memory/all/flags/hookflags3), or [`hookflags4`](../../../memory/all/flags/hookflags4) hook to uninstall that hook.

### Outputs:
* Reset [`bufferOnly, (flags + plotFlag3)`](../../../memory/all/flags/plotFlag3#bit-0---bufferOnly).
* Reset [`appRunning, (flags + APIFlg)`](../../../memory/all/flags/APIFlg#bit-4---apprunning).
* Zeroes out [`textFlags`](../../../memory/all/flags/textFlags), [`apiFlg2`](../../../memory/all/flags/apiFlg2), [`apiFlg3`](../../../memory/all/flags/apiFlg3), [`apiFlg4`](../../../memory/all/flags/apiFlg4), [`hookflags2Override`](../../../memory/all/flags/hookflags2Override), [`hookflags3Override`](../../../memory/all/flags/hookflags3Override), and [`hookflags4Override`](../../../memory/all/flags/hookflags4Override).

### Destroys:
* `af`, `hl`

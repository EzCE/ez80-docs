---
title: Getting Started
weight: -20
---

This page will walk you through the basics of setting up an environment for writing assembly programs for the TI-84 Plus CE on the system of your choice.

{{< toc >}}

## Installing a compiler

To start writing and compiling programs, you'll need to have a way to compile them. If you've already installed and set up the [CE C Toolchain](https://ce-programming.github.io/toolchain/index.html), then you also already have a way to compile ez80 assembly. In that case, you're already ready for the [next step](#installing-cemu)! Otherwise, follow the instructions below.

1. Download the latest version of the flat assembler g (fasmg) from its website [here](https://flatassembler.net/download.php). It will probably be at the very bottom of the page.
2. Extract the downloaded zip and find the version for your OS. If you're confused, this handy chart will help you pick the one that's right for you:

| File Name              | Platform                                                             |
|------------------------|----------------------------------------------------------------------|
| fasmg.exe              | Windows                                                              |
| fasmg                  | Linux (32-Bit)                                                       |
| fasmg.x64              | Linux (64-Bit)                                                       |
| source/macos/fasmg     | macOS (32-Bit)                                                       |
| source/macos/x64/fasmg | macOS (64-Bit) (You almost certainly have this one if you use macOS) |

3. The next step will vary depending on your OS as well:

{{< tabs "installfasmg" >}}
{{< tab "Windows" >}}
1. Move `fasmg.exe` to a location with no spaces in the the file path. For example, `C:\ez80-fasmg`.
2. Add the directory containing fasmg to your PATH environment variable. To do this, first open the start menu and search for "Edit the system environment variables"
3. Click the "Environment Variables" button and find "PATH" in the lower (System Variables) section.
4. Click on "Edit" and then click "New". You should see a text box, where you should add the path to the directory containing fasmg. In our example, this is `C:\ez80-fasmg`.
5. Once you are done, exit the windows by pressing "OK", "OK", and "OK".
6. To confirm that this was done correctly, open a command prompt and type and run `fasmg`. You should see an output like this:
```Plain
C:\>fasmg
flat assembler  version g.jmhx
Usage: fasmg source [output]
Optional settings:
    -e limit    Set the maximum number of displayed errors (default 1)
    -p limit    Set the maximum allowed number of passes (default 100)
    -r limit    Set the maximum depth of the stack (default 10000)
    -v flag     Enable or disable showing all lines from the stack (default 0)
    -i command  Insert instruction at the beginning of source
    -n          Do not show logo nor summary
```
{{< /tab >}}

{{< tab "Linux" >}}
1. Move either `fasmg` or `fasmg.x64` to a file path without any spaces. For example, `/home/user/ez80-fasmg`.
2. Add the directory containing fasmg to your PATH environment variable. To do this first open a terminal.
3. In the terminal, we need to edit our rc file. In this example, we'll be assuming it is a bashrc, as this is one of the most common. To do this, run the following command, where `<path to fasmg>` is the path to the directory containing it. (In our example, `/home/user/ez80-fasmg`):
```Plain
echo "export PATH=/<path to fasmg>:$PATH" >> .bashrc
```
4. Confirm everything has worked correctly by closing your current terminal and opening a new one. In the new one, type and run `fasmg`. You should see an output like this:
```Plain
$ fasmg
flat assembler  version g.jmhx
Usage: fasmg source [output]
Optional settings:
    -e limit    Set the maximum number of displayed errors (default 1)
    -p limit    Set the maximum allowed number of passes (default 100)
    -r limit    Set the maximum depth of the stack (default 10000)
    -v flag     Enable or disable showing all lines from the stack (default 0)
    -i command  Insert instruction at the beginning of source
    -n          Do not show logo nor summary
```
{{< /tab >}}

{{< tab "macOS" >}}
1. Move `source/macos/fasmg` or `source/macos/x64/fasmg` to a file path without any spaces. For example, `/Users/<user>/ez80-fasmg`.
2. Add the directory containing fasmg to your PATH environment variable. To do this first open a terminal.
3. In the terminal, we need to edit our rc file. In this example, we'll be assuming it is a zshrc, as this is the default on macOS. To do this, run the following command, where `<path to fasmg>` is the path to the directory containing it. (In our example, `/Users/<user>/ez80-fasmg`):
```Plain
echo "export PATH=$PATH:/<path to fasmg>" >> .zshrc
```
4. Confirm everything has worked correctly by closing your current terminal and opening a new one. In the new one, type and run `fasmg`. You should see an output like this:
```Plain
$ fasmg
flat assembler  version g.jmhx
Usage: fasmg source [output]
Optional settings:
    -e limit    Set the maximum number of displayed errors (default 1)
    -p limit    Set the maximum allowed number of passes (default 100)
    -r limit    Set the maximum depth of the stack (default 10000)
    -v flag     Enable or disable showing all lines from the stack (default 0)
    -i command  Insert instruction at the beginning of source
    -n          Do not show logo nor summary
```
{{< /tab >}}
{{< /tabs >}}

## Installing CEmu

Now that we have a way to build our programs, we need a way to test them! While testing on a physical calculator is possible, even the best programmers always run the risk of accidentally causing a crash or damaging the calculator when things don't go as planned. Thankfully, there's a solution! Using an emulator called CEmu, you can test your programs on the computer, along with using some of CEmu's handy debugging features.

1. First, download the latest nightly build of CEmu for your operating system [here](https://github.com/CE-Programming/CEmu/releases/tag/nightly).
2. Open and run CEmu, and you should be greeted with a welcome menu. Click "Create a ROM image from your calculator" and follow the steps to generate a ROM. CEmu will automatically load this ROM in the future unless you delete it.
3. Congratulations! You have succesfully set up CEmu and are ready to begin writing [your first program!](../your-first-program)

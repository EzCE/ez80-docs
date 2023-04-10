---
title: Your First Program
weight: -20
---

Now that you're all ready to go, let's make a program!

{{< toc >}}

## Setting Up a Project 
One of the most important things when making a project is sticking to a consistent format and keeping your files organized. You'll need to have source code, include files, and ideally some documentation or readme for your project as well. Here's a sample format we recommend and will use for this example:

```Plain
project                         // The main folder for your project
├── include                     // A folder containing the include files
│   ├── commands.alm
│   ├── ez80.alm
│   ├── ez80.inc
│   ├── ti84pceg.inc
│   ├── tiformat.inc
├── src                         // A folder containing all your source code
│   ├── main.asm
└── readme                      // A file explaining what your program does and how to use it (optional)
```

We'll start by downloading the include files. These contain system calls and other equates you'll use in your programs. Make a folder called `include` in your project folder and download the five include files for fasmg made by [jacobly](https://github.com/jacobly0), which you can get in a zip [here](https://github.com/EzCE/ez80-docs/raw/main/assets/include.zip). Extract all five of these files into the folder you previously created called `include`.

## Writing the Program

Now, it's time to start writing the actual code. First, make a folder called `src`, which will contain your source code. Next, in the `src` directory, create a file called `main.asm` and open it in your favorite code editor. Let's begin by adding this at the beginning:

```Plain
include 'include/ez80.inc'
include 'include/tiformat.inc'
include 'include/ti84pceg.inc'
```

This makes so that equates and calls from the include files are recognized in your program. Next, add this line:

```Plain
format ti archived executable protected program 'HELLO'
```

This tells the compiler how to format the compiled program. You'll usually want to keep most of this the same, though you can change the name by replacing 'HELLO' with something else ('WORLD') for example if you'd like.

Now for the code:

```Plain
main:
    call ti.ClrLCDFull  ; Clear the screen
    call ti.HomeUp      ; Reset the column and row to 0, 0
    ld hl, text         ; Load hl with the pointer to the text
    call ti.PutS        ; Display the string pointed to by hl
    ret                 ; Exit

text:
    db "Hello, world!", 0   ; Store this string in memory for whatever we want
```

If you've been following along so far, your program should look something like this:

```Plain
include 'include/ez80.inc'
include 'include/tiformat.inc'
include 'include/ti84pceg.inc'

format ti archived executable protected program 'HELLO'

main:
    call ti.ClrLCDFull  ; Clear the screen
    call ti.HomeUp      ; Reset the column and row to 0, 0
    ld hl, text         ; Load hl with the pointer to the text
    call ti.PutS        ; Display the string pointed to by hl
    ret                 ; Exit

text:
    db "Hello, world!", 0   ; Store this string in memory for whatever we want
```

## Compiling

Now let's compile it. The basic syntax for the fasmg compiler is `fasmg <source file> <output file>`. Open a terminal in the main folder of your project and run this command:

```Plain
fasmg src/main.asm HELLO.8xp
```

You should hopefully see an output like this, along with a file called `HELLO.8xp` which was created in the project folder:

```Plain
flat assembler  version g.jmhx
3 passes, 0.1 seconds, 109 bytes.
```

If not, look back over your code and make sure it matches with the example. If so, try sending it to CEmu and testing it out! You can do this by opening CEmu and dragging the file onto the calculator.

## What Next?
Now that you've made your first assembly program, it's time to create your own. For starters, you can try messing around with the source code of this example! Try displaying a different message, or naming the program something different! Once you're ready, you can use the information on instructions and system calls to make your own programs.

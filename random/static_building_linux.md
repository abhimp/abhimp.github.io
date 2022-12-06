---
layout: blog
title: Static building and binary distribution in Linux
menutype: blog
menu_order: 10
plink: bitch_glibc
---

# Static binary distribution for Linux based OSes

Go language by default create static executable binary and it is pretty easy to distribute. The binary mostly runs on any Linux based operating system without any hiccup. The only problem with the binary is that it is very large.

However, it is not same for other language. For example, C/C++. To build C/C++ codebase, most of the cases it requires a lot of help from standard library as those libraries actually handle the interaction between kernel surface and user program. So, to build a static binary one need to put all the required library functions in the executable. It should should fairly easy, right? Infact, the `gcc` and `g++` tool have option `-static` to build a static binary. So, just pass the `-static` switch during the build, and the final executable will run anywhere.

Well, this is not so simple. Primary because most of the mainline Linux distribution use `glibc` as the C library, and **the `glibc` is a b@@@h**. Under no circumstances, `glibc` want you to build a static binary. Even if you create an executable with `-static`, the executable still load the `glibc` shared-object during runtime. If this is not good enough, `glibc` always checks the system library version and load them only if the system has a higher or equal version. `glibc` tried very hard to disable static binary distribution.

So, is there any option to distribute static binary? Fortunately, there are few.

### A. Static build with a very old `glibc`
This is probably the easiest option. Find a Linux based operating system with very old `glibc`, build there and distribute. Although this is quite a good option, it does not guarantee 100% compatibility. Also, older version might be vulnerable to different security issues. At the end, API may not match completely and can not take to the advantage of latest compiler version. I am not sure if any other issue exists with this technique.

### B. Mimic the older `glibc` version

### C. Use alternate library
As last two options are not very good and attractive, I tried to look for other method to make distributable static build. My primary goal is to find an alternative to `glibc`. There are several options to `glibc`. Among them, `ulibc` and `musl` is very prominent. 

After researching few blogs and articles, I decided to uses one of the alternate library. However, these are only alternative to `glibc`. To use build C++ code, I had to build the `stdlibc++` using these library as well. Although it is not difficult to build `stdlibc++` using `musl` or `ulibc`, it is too much work.

Fortunately, Alpine Linux is there to help. It is developed using `musl` and it provides complete C++ toolchain to build C++/C code. It also provide complete `gcc`/`g++` surface. So, I can pass `-static` switch to build distributable static binary.

---
layout: blog
title: C++, Computer network and Windows
menutype: blog
menu_order: 20
plink: port_to_windows
---

## Porting a C++ network program to windows

*This is a note only for my help. If you find any problem, you can inform me.*

Recently I am developing an application and, aim is to distribute the binary only.
The application is developed

I have developed an application which is highly dependent on the Linux system network system calls. 
I used `poll` for multiplexing and other code system calls including.
Although the initial version was written primarily for Linux, it was very close to POSIX.
So, It was very easy to port to MacOS. 
It was so easy, that I don't even remeber.

At this point I should tell that I was using `g++` in linux and `clang++` in MacOS for compiling and linking the code.

After porting to MacOS, it was to time to port to Windos system.
As soon as I started porting to windows, I realised how difficult it is.
Before starting starting to port, I thought I will port it gradually.
I mean, I will try to find some wrapper library first so that my linux code can compile and run the linux code as it is.
There are several ways to port a Linux C++ code to windows.
Some of them are easy but require additional help from other libraries.
So, it either impossible or difficult to make a distributable binary out it.

Anyway, my target was to use native API, so I that it run faster and I have full control over the system.

---
layout: system
title: BASH cheats
menutype: system
menu_order: 30
---

### Intro
Tricks in BASH


1. Get filename without extension

    ``$ echo ${filename%.*}``

2. Get extension only

    ``$ echo ${filename##*.}``

    **Does not works with tar.xz files

3. Quick directory tree

    ``$ find . -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'``

4. Sync system time with google.in

    ``$ sudo date -s "$(curl -sD - google.in | grep '^Date:' | cut -d' ' -f3-6)Z"``

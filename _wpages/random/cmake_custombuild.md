---
layout: blog
title: CMake and custom target
menutype: blog
menu_order: 20
plink: cmakeCustomTarget
---

# CMAKE

CMAKE is a versatile cross platform build system generator. For portable code, one simple `cmake` configuration can help coder to build on different platform using different compiler.

However, CMake employ a very complecated and extremely instrusive configuration. It is really hard to understand and configure it differently. However, once it is configured successfully, it can work like magic.

In this blog, I don't want to discuss anything related to basic cmake configuration. Rather, something different.

## Find Package
Cmake by default have lot of packages that can help resolve application dependency. This packages can be find via `find_package` function. This works like charm in while linking with `ssh` or `ssl`.

## Custom target
Cmake have ability
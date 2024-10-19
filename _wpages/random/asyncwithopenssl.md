---
layout: blog
title: Openssl and single threaded application
menutype: blog
menu_order: 20
plink: asyncOpenSSL
---

## OpenSSL

OpenSSL is one of the greatest opensource tool we have. It is used by many project as it is defacto tool for SSL based solutions.

The best thing about OpenSSL is that it is platform agonastic and ease of use. Writing portable code is so much easier with OpenSSL.

Also OpenSSL support different kind of IOs and very easy adapt a new one if it does exists already. It also support both blocking and non-blocking IO operation. The blocking IO operation is easy and simple. OpenSSL would wait until underlying operation ends. It works out of the box, easy and simple. However, it needs system threads to handle each side of a connection which could be wastfull. The non-blocking IO is little involving and have several caveates.

### OpenSSL with non-blocking IO
Non-blocking IO is a way to perform multiple 

---
layout: system
title: SSH tricks
menutype: system
menu_order: 10
---

### Intro
Tricks in SSH


1. Setup autologin to a remote host<br>
        ``$ if [ ! -f ~/.ssh/id_rsa.pub ]; then ssh-keygen -t rsa; fi; cat ~/.ssh/id_rsa.pub | ssh <ssh options> <user>@<host> 'if [[ ! -d .ssh ]]; then mkdir .ssh; fi;cat >> .ssh/authorized_keys'``

2. Login to `U1@H1:P1` via `U2@H2:P2`
    1. Old style, works only on linux with bsd style netcat <br>
        ``$ ssh -o ProxyCommand="ssh -p P2 U2@H2 nc -q0 %h %p" -p P1 U1@H1``
    2. New style, may require an updated version of SSH <br>
        ``$ ssh -J U2@H2:P2 -p P1 U1@H1`` <br>
        ``$ ssh -o ProxyJump U2@H2:P2 -p P1 U1@H1``<br>
        **Can add more jump by sperating using comman

3. Login to `U1@H1:P1` through `U2@H2:P2` transparently
    1. Need to add info to the ``~/.ssh/config``

        ```
        Host aRandomName2
            User U1
            Port P1
            Hostname H1

        Host aRandomName1
            User U1
            Port P1
            Hostname H1
            ProxyJump aRandomName2
        ```

        * `ssh` to `U1@H1:P1` <br>
            ``$ ssh aRandomName1 ``
        * To open `U1@H1:P1` from file browser, type
            ``sftp://aRandomName1``
            and enter



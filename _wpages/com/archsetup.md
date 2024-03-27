---
layout: system
title: ArchLinux
menutype: system
menu_order: 20
---

## Installation

### Prepare disk
Follow the exact commands provided at the archwiki [Installation guide](https://wiki.archlinux.org/index.php/installation_guide)

### Install require software

1. First need to install the required packages.
Here we assume that linux is mounted at the /mnt

    ``# pacstrap /mnt base base-devel linux linux-firmware vim man-pages networkmanager grub efibootmgr sbctl``


1. Follow arch guide to install and setup fstab and chroot to mnt

    ``# genfstab -U /mnt >> /mnt/etc/fstab``<br>
    ``# arch-chroot /mnt``

1. Install grub and config for uefi

    ``# grub-install --target=x86_64-efi --efi-directory=/boot/efi/ --bootloader-id="Red Hat Enterprise Linux" --recheck --debug``<br>
    ``# grub-mkconfig -o /boot/grub/grub.cfg`` <br>
    ``# systemctl enable netowrkmanager`` <br>
    ``# systemctl enable NetworkManager`` <br>
    ``# systemctl start NetworkManager`` <br>

1. Secure boot

    ``# grub-install --target=x86_64-efi --efi-directory=esp --bootloader-id=GRUB --modules="tpm"`` <br>
    Now follow (https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface/Secure_Boot#Implementing_Secure_Boot)

1. Add user and make it admin

    ``# useradd -m abhijit -s /bin/bash -c "Abhijit Mondal, email@gmail.com"`` <br>
    ``# passwd abhijit`` <br>
    ``# usermod -aG sudo abhijit`` <br>


## Installation on ACER S1002
### Booting iso

Find 32bit grub (`bootia32.efi`) somewhere and put inside `/EFI/Boot/` in the iso

1. Disable secure boot
1. Boot from the flush drive
1. In the grub shell type the followings:

    ``linux   (hd0)/arch/boot/x86_64/vmlinuz archisobasedir=arch archisolabel=ARCH_202003`` <br>
    ``initrd  (hd0)/arch/boot/intel_ucode.img`` <br>
    ``initrd  (hd0)/arch/boot/amd_ucode.img`` <br>
    ``initrd  (hd0)/arch/boot/x86_64/archiso.img`` <br>
    ``boot``

    Replace ARCH_202003 with iso label

## Configure git with gnome-keyring
1. Install ``libsecret``
2. Fire <br>
    ``$ git config --global credential.helper /usr/lib/git-core/git-credential-libsecret``

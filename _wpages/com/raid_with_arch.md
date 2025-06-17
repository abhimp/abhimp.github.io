---
layout: system
title: Setting up software raid in (arch)linux
menutype: system
menu_order: 60
---

I want to save my collection of data in raid of 4 hdd.


# Create RAID array

## Step 1:
First thing we need is `mdadm` and other disk related tools. However, `mdadm` is the raid controller. It can be installed via following command:

```
sudo pacman -Syu mdadm
```

## Step 2:
Once `mdadm` is installed, we can prepare the disk by wiping them.

```
for disk in /dev/sd{a,b,c,d}; do
  sudo wipefs -a "$disk"
  sudo dd if=/dev/zero of="$disk" bs=1M count=100
done
```

## Step 3:
Create GPT partition table on all the disks.
```
for disk in /dev/sd{a,b,c,d}; do
  sudo parted -s "$disk" mklabel gpt
  sudo parted -s "$disk" mkpart primary 0% 100%
done
```

## Step 4:
Mark partitions for RAID
```
for disk in /dev/sd{a,b,c,d}; do
  sudo parted "$disk" set 1 raid on
done
```

## Step 5:
Create the RAID10 Array
```
sudo mdadm --create --verbose /dev/md0 --level=10 --raid-devices=4 /dev/sd[b-e]1
```

## Step 6:
Save the raid configuration for portability. We can do this in any system and the raid array will work there.
```
sudo mdadm --detail --scan | sudo tee -a /etc/mdadm.conf
```

## Step 7:
Make the array detectable on other systems
```
sudo mdadm --assemble --scan
```

# Maintenance

## Remove the array safely

### Unmount the disk
```
sudo umount /dev/md0
```
or
```
udiskctl unmount -b /dev/md0
```

### Stop the array
```
sudo mdadm --stop /dev/md0
```

### Check status
```
cat /proc/mdstat
```

### Check details
```
sudo mdadm --detail /dev/md0
```
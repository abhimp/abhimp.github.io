---
layout: blog
title: Wifi Provisioning
menutype: blog
menu_order: 20
plink: wifi
---

# Wifi Provisioning

## Package Installation

```
sudo pacman -S bluez bluez-utils networkmanager
sudo pacman -S python python-dbus
```

```
sudo systemctl enable --now bluetooth
sudo systemctl enable --now NetworkManager
```

### Verify BLE support

```
bluetoothctl show
```

## Start provisioning service at boot

```
# /etc/systemd/system/wifi-provision.service
[Unit]
Description=BLE WiFi Provisioning
After=bluetooth.service NetworkManager.service

[Service]
ExecStart=/usr/bin/python /opt/wifi_ble_provision.py
Restart=always

[Install]
WantedBy=multi-user.target

```

### Enable it

```
sudo systemctl enable wifi-provision
```
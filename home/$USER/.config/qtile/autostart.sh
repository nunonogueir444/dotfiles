#!/bin/bash

# xorg-xrandr
xrandr --output DisplayPort-1 --mode 2560x1440 --rate 59.95 &

# picom
picom -b &

# numlockx
numlockx &

# nitrogen
nitrogen --restore &

# polkit-gnome
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

#dbus-update-activation-environment --all &

# easyeffects
easyeffects --gapplication-service &

# dropbox
dropbox &

# network-manager-applet
nm-applet &

# volumeicon
volumeicon &

# blueman
blueman-applet &

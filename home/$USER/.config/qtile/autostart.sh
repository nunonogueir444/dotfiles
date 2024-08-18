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

# trayer
#sleep 2 && trayer --edge top --align right --margin 400 --monitor 0 --widthtype request --heighttype pixel --height 30 --distancefrom top --distance 3 --iconspacing 10 &

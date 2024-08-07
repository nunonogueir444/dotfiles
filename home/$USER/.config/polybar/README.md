1- Copy the configuration example from /etc/polybar/config.ini to ~/.config/polybar/config.ini

2- Create an executable file containing the startup logic, for example $HOME/.config/polybar/launch.sh

bspwm <br/>
If using bspwm, add the following to bspwmrc: <br/>
$HOME/.config/polybar/launch.sh

i3 <br/>
If using i3, add the following to your i3 configuration: <br/>
exec_always --no-startup-id $HOME/.config/polybar/launch.sh

SOURCE: [ArchWiki](https://wiki.archlinux.org/title/Polybar)

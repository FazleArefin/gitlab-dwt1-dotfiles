#!/usr/bin/env bash 

COLORSCHEME=tomorrow-night

### AUTOSTART PROGRAMS ###

if systemd-detect-virt --quiet; then
    lxsession &
    sleep 1
    killall picom
    xrandr -s 1920x1080 &
else
    lxsession &
fi

nm-applet &
systemctl --user start mpd &
"$HOME"/.screenlayout/layout.sh &
sleep 1
conky -c "$HOME"/.config/conky/qtile/01/"$COLORSCHEME".conf || echo "Couldn't start conky."
sleep 1
yes | /usr/bin/emacs --daemon &

### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
xargs xwallpaper --stretch < ~/.cache/wall &
# 2. Uncomment to set a random wallpaper on login
# find /usr/share/backgrounds/dtos-backgrounds/ -type f | shuf -n 1 | xargs xwallpaper --stretch &
# 3. Uncomment to set wallpaper with nitrogen
# nitrogen --restore &

if  [ ! -d "$HOME"/.cache/betterlockscreen/ ]; then
    betterlockscreen -u /usr/share/backgrounds/dtos-backgrounds/0277.jpg & 
fi

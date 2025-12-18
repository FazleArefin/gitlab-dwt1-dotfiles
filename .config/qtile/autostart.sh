#!/usr/bin/env bash 

COLORSCHEME=doom-one

### AUTOSTART PROGRAMS ###
dunst -conf "$HOME"/.config/dunst/"$COLORSCHEME" &
nm-applet &
systemctl --user start mpd &
"$HOME"/.screenlayout/layout.sh &
picom --daemon &
sleep 1
conky -c "$HOME"/.config/conky/qtile/01/"$COLORSCHEME".conf || echo "Couldn't start conky."
sleep 1
yes | /usr/bin/emacs --daemon &
waypaper --restore &

if  [ ! -d "$HOME"/.cache/betterlockscreen/ ]; then
    betterlockscreen -u /usr/share/backgrounds/dtos-backgrounds/0277.jpg & 
fi

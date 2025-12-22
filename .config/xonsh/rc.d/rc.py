#  ____ _____
# |  _ \_   _|  Derek Taylor (DistroTube)
# | | | || |    http://www.youtube.com/c/DistroTube
# | |_| || |    http://www.gitlab.com/dwt1/
# |____/ |_|
#
# My xonsh config written in python as opposed to using the standard .xonshrc format.

from pathlib import Path
from xonsh.xontribs import xontribs_load

xenv = __xonsh__.env


### ADDING DIRS TO PATH ###
for d in ["~/.local/bin", "~/Applications"]:
    xenv["PATH"].append(Path(d).expanduser())


### XONSH THEME ###
xenv['XONSH_COLOR_STYLE'] = 'one-dark'

### STARSHIP PROMPT ###
xontribs_load(['prompt_starship'])

### RANDOM COLOR SCRIPT ###
__xonsh__.subproc_uncaptured(['colorscript', 'random'])

### SET EDITORS ###
xenv['EDITOR'] = "emacsclient -t -a ''"
xenv['VISUAL'] = "emacsclient -c -a emacs"

### SET FZF DEFAULTS
xenv['FZF_DEFAULT_OPTS'] = "--layout=reverse --exact --border=bold --border=rounded --margin=3%  --color=dark"

### SET MANPAGER ###
xenv['MANPAGER'] = 'nvim +Man!'
#xenv['MANPAGER'] = 'less'

### ALIASES ###
# Navigation
aliases['..'] = 'cd ..'
aliases['-'] = 'cd -'

for i in range(1, 10):
    aliases[','*i] = lambda: $[cd @("../" * len($__ALIAS_NAME))]

# Vim and Emacs
aliases |= {
    'vim': 'nvim',
    'emacs': "emacsclient -c -a 'emacs'",
    'em': '/usr/bin/emacs -nw',
    'rem': "killall emacs || echo 'Emacs server not running'; /usr/bin/emacs --daemon",
}

# Eza (ls replacement)
eza_base = 'eza --color=always --group-directories-first'
aliases['ls'] = f'{eza_base} -al'
aliases['la'] = f'{eza_base} -a'
aliases['ll'] = f'{eza_base} -l'
aliases['lt'] = f'{eza_base} -aT'
aliases['l.'] = 'eza -a | grep "^\\."'
aliases['l..'] = f'{eza_base} -al ../'
aliases['l...'] = f'{eza_base} -al ../../'
aliases['l....'] = f'{eza_base} -al ../../../'

# Pacman and Yay/Paru
aliases['pacsyu'] = 'sudo pacman -Syu'
aliases['pacsyyu'] = 'sudo pacman -Syyu'
aliases['parsua'] = 'paru -Sua --noconfirm'
aliases['parsyu'] = 'paru -Syu --noconfirm'
aliases['unlock'] = 'sudo rm /var/lib/pacman/db.lck'
aliases['orphan'] = 'sudo pacman -Rns $(pacman -Qtdq)'

# Reflector (Mirrors)
aliases['mirror'] = "sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist"
aliases['mirrord'] = "sudo reflector --latest 50 --number 20 --sort delay --save /etc/pacman.d/mirrorlist"
aliases['mirrors'] = "sudo reflector --latest 50 --number 20 --sort score --save /etc/pacman.d/mirrorlist"
aliases['mirrora'] = "sudo reflector --latest 50 --number 20 --sort age --save /etc/pacman.d/mirrorlist"

# System Tools
aliases['df'] = 'df -h'
aliases['free'] = 'free -m'
aliases['grep'] = 'grep --color=auto'
aliases['psa'] = "ps auxf"
aliases['psgrep'] = "ps aux | grep -v grep | grep -i -e VSZ -e"
aliases['psmem'] = 'ps auxf | sort -nr -k 4'
aliases['pscpu'] = 'ps auxf | sort -nr -k 3'
aliases['merge'] = 'xrdb -merge ~/.Xresources'
aliases['jctl'] = "journalctl -p 3 -xb"

# Git
aliases['addup'] = 'git add -u'
aliases['addall'] = 'git add .'
aliases['branch'] = 'git branch'
aliases['checkout'] = 'git checkout'
aliases['clone'] = 'git clone'
aliases['commit'] = 'git commit -m'
aliases['fetch'] = 'git fetch'
aliases['pull'] = 'git pull origin'
aliases['push'] = 'git push origin'
aliases['tag'] = 'git tag'
aliases['newtag'] = 'git tag -a'

# GPG
aliases['gpg-check'] = "gpg2 --keyserver-options auto-key-retrieve --verify"
aliases['gpg-retrieve'] = "gpg2 --keyserver-options auto-key-retrieve --receive-keys"

# Shell Switching (using $USER env variable from xonsh)
user = xenv.get('USER')
aliases['tobash'] = f"chsh {user} -s /bin/bash && echo 'Log out and log back in.'"
aliases['tozsh'] = f"chsh {user} -s /bin/zsh && echo 'Log out and log back in.'"
aliases['tofish'] = f"chsh {user} -s /bin/fish && echo 'Log out and log back in.'"

# TTY Fonts
aliases['bigfont'] = "setfont ter-132b"
aliases['regfont'] = "setfont default8x16"

# Misc
aliases['config'] = f"/usr/bin/git --git-dir={xenv.get('HOME')}/dotfiles --work-tree={xenv.get('HOME')}"
aliases['tb'] = "nc termbin.com 9999"
aliases['rr'] = 'curl -s -L https://raw.githubusercontent.com/keroserene/rickrollrc/master/roll.sh | bash'
aliases['mocp'] = "bash -c mocp"

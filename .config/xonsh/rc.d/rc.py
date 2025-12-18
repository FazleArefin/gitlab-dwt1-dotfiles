#  ____ _____
# |  _ \_   _|  Derek Taylor (DistroTube)
# | | | || |    http://www.youtube.com/c/DistroTube
# | |_| || |    http://www.gitlab.com/dwt1/
# |____/ |_|
#
# My xonsh config written in python as opposed to using the standard .xonshrc format.

from xonsh.xontribs import xontribs_load

### XONSH THEME ###
__xonsh__.env['XONSH_COLOR_STYLE'] = 'one-dark'

### STARSHIP PROMPT ###
xontribs_load(['prompt_starship'])

### RANDOM COLOR SCRIPT ###
__xonsh__.subproc_uncaptured(['colorscript', 'random'])

### SET EDITORS ###
__xonsh__.env['EDITOR'] = "emacsclient -t -a ''"
__xonsh__.env['VISUAL'] = "emacsclient -c -a emacs"

### SET FZF DEFAULTS
__xonsh__.env['FZF_DEFAULT_OPTS'] = "--layout=reverse --exact --border=bold --border=rounded --margin=3%  --color=dark"

### SET MANPAGER ###
__xonsh__.env['MANPAGER'] = 'nvim +Man!'
#__xonsh__.env['MANPAGER'] = 'less'

### ALIASES ###
# Navigation
__xonsh__.aliases['..'] = 'cd ..'
__xonsh__.aliases['...'] = 'cd ../..'
__xonsh__.aliases['.3'] = 'cd ../../..'
__xonsh__.aliases['.4'] = 'cd ../../../..'
__xonsh__.aliases['.5'] = 'cd ../../../../..'

# Vim and Emacs
__xonsh__.aliases['vim'] = 'nvim'
__xonsh__.aliases['emacs'] = "emacsclient -c -a 'emacs'"
__xonsh__.aliases['em'] = '/usr/bin/emacs -nw'
__xonsh__.aliases['rem'] = "killall emacs || echo 'Emacs server not running'; /usr/bin/emacs --daemon"

# Eza (ls replacement)
eza_base = 'eza --color=always --group-directories-first'
__xonsh__.aliases['ls'] = f'{eza_base} -al'
__xonsh__.aliases['la'] = f'{eza_base} -a'
__xonsh__.aliases['ll'] = f'{eza_base} -l'
__xonsh__.aliases['lt'] = f'{eza_base} -aT'
__xonsh__.aliases['l.'] = 'eza -a | grep "^\\."'
__xonsh__.aliases['l..'] = f'{eza_base} -al ../'
__xonsh__.aliases['l...'] = f'{eza_base} -al ../../'
__xonsh__.aliases['l....'] = f'{eza_base} -al ../../../'

# Pacman and Yay/Paru
__xonsh__.aliases['pacsyu'] = 'sudo pacman -Syu'
__xonsh__.aliases['pacsyyu'] = 'sudo pacman -Syyu'
__xonsh__.aliases['parsua'] = 'paru -Sua --noconfirm'
__xonsh__.aliases['parsyu'] = 'paru -Syu --noconfirm'
__xonsh__.aliases['unlock'] = 'sudo rm /var/lib/pacman/db.lck'
__xonsh__.aliases['orphan'] = 'sudo pacman -Rns $(pacman -Qtdq)'

# Reflector (Mirrors)
__xonsh__.aliases['mirror'] = "sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist"
__xonsh__.aliases['mirrord'] = "sudo reflector --latest 50 --number 20 --sort delay --save /etc/pacman.d/mirrorlist"
__xonsh__.aliases['mirrors'] = "sudo reflector --latest 50 --number 20 --sort score --save /etc/pacman.d/mirrorlist"
__xonsh__.aliases['mirrora'] = "sudo reflector --latest 50 --number 20 --sort age --save /etc/pacman.d/mirrorlist"

# System Tools
__xonsh__.aliases['df'] = 'df -h'
__xonsh__.aliases['free'] = 'free -m'
__xonsh__.aliases['grep'] = 'grep --color=auto'
__xonsh__.aliases['psa'] = "ps auxf"
__xonsh__.aliases['psgrep'] = "ps aux | grep -v grep | grep -i -e VSZ -e"
__xonsh__.aliases['psmem'] = 'ps auxf | sort -nr -k 4'
__xonsh__.aliases['pscpu'] = 'ps auxf | sort -nr -k 3'
__xonsh__.aliases['merge'] = 'xrdb -merge ~/.Xresources'
__xonsh__.aliases['jctl'] = "journalctl -p 3 -xb"

# Git
__xonsh__.aliases['addup'] = 'git add -u'
__xonsh__.aliases['addall'] = 'git add .'
__xonsh__.aliases['branch'] = 'git branch'
__xonsh__.aliases['checkout'] = 'git checkout'
__xonsh__.aliases['clone'] = 'git clone'
__xonsh__.aliases['commit'] = 'git commit -m'
__xonsh__.aliases['fetch'] = 'git fetch'
__xonsh__.aliases['pull'] = 'git pull origin'
__xonsh__.aliases['push'] = 'git push origin'
__xonsh__.aliases['tag'] = 'git tag'
__xonsh__.aliases['newtag'] = 'git tag -a'

# GPG
__xonsh__.aliases['gpg-check'] = "gpg2 --keyserver-options auto-key-retrieve --verify"
__xonsh__.aliases['gpg-retrieve'] = "gpg2 --keyserver-options auto-key-retrieve --receive-keys"

# Shell Switching (using $USER env variable from xonsh)
user = __xonsh__.env.get('USER')
__xonsh__.aliases['tobash'] = f"chsh {user} -s /bin/bash && echo 'Log out and log back in.'"
__xonsh__.aliases['tozsh'] = f"chsh {user} -s /bin/zsh && echo 'Log out and log back in.'"
__xonsh__.aliases['tofish'] = f"chsh {user} -s /bin/fish && echo 'Log out and log back in.'"

# TTY Fonts
__xonsh__.aliases['bigfont'] = "setfont ter-132b"
__xonsh__.aliases['regfont'] = "setfont default8x16"

# Misc
__xonsh__.aliases['config'] = f"/usr/bin/git --git-dir={__xonsh__.env.get('HOME')}/dotfiles --work-tree={__xonsh__.env.get('HOME')}"
__xonsh__.aliases['tb'] = "nc termbin.com 9999"
__xonsh__.aliases['rr'] = 'curl -s -L https://raw.githubusercontent.com/keroserene/rickrollrc/master/roll.sh | bash'
__xonsh__.aliases['mocp'] = "bash -c mocp"

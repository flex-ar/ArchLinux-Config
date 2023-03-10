# Qtile workspaces

from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import mod, keys

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons 1: 
# nf-fa-firefox, 
# nf-fae-python, 
# nf-dev-terminal, 
# nf-fa-code, 
# nf-oct-git_merge, 
# nf-linux-docker,
# nf-mdi-folder,
# nf-mdi-image,
# nf-mdi-layers

# Icons 2:
# nf-dev-terminal,
# nf-fa-chrome,
# nf-dev-javascript_badge,
# nf-mdi-nodejs,
# nf-mdi-react,
# nf-mdi-language_typescript,
# nf-linux-archlinux,
# nf-seti-haskell,
# nf-mdi-layers

# Icon: fa-circle-small
groups = [Group(name=name, label=label) for [name, label] in [
    ["1", "  "],
    ["2", "  "],
    ["3", "  "],
    ["4", "  "],
    ["5", "  "],
    ["6", "  "],
    ["7", "  "],
    ["8", "  "],
    ["9", "  "],
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

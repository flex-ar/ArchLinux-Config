# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy

mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    ([mod], "space", lazy.layout.next()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    # ([mod], "period", lazy.next_screen()),
    # ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    (["control"], "Menu", lazy.spawn("rofi -show drun")),

    # Window Nav
    ([mod], "Menu", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "b", lazy.spawn("google-chrome-stable")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Redshift
    ([], "Pause", lazy.spawn("redshift -O 2400")),
    ([mod], "Pause", lazy.spawn("redshift -x")),

    # Screenshot
    ([], "Print", lazy.spawn("scrot")),
    (["control"], "Print", lazy.spawn("maim -s captura.png")),

    # ------------ Hardware Configs ------------

    # Volume

    # US-2x2
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume 1 -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume 1 +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute 1 toggle"
    )),

    # Monitor audio
    (["control"], "F10", lazy.spawn(
        "pactl set-sink-volume 0 -5%"
    )),
    (["control"], "F11", lazy.spawn(
        "pactl set-sink-volume 0 +5%"
    )),
    (["control"], "F9", lazy.spawn(
        "pactl set-sink-mute 0 toggle"
    )),

    # Multimedia
    ([], "XF86AudioPlay", lazy.spawn(
        "playerctl play-pause"
    )),

    ([], "XF86AudioNext", lazy.spawn(
        "playerctl next"
    )),

    ([], "XF86AudioPrev", lazy.spawn(
        "playerctl previous"
    ))
]]

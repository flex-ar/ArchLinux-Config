from libqtile import widget
from .theme import colors

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)

def icon(fg='text', bg='dark', fontsize=17, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=5
    )

def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="\ue0ca",
        fontsize=27,
        padding=0
    )

def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='Fira Code',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]

primary_widgets = [
    *workspaces(),

    separator(),

    # 7
    powerline('dark', 'dark'),
    widget.Systray(background=colors['dark'], padding=5),

    # 6
    powerline('color6', 'dark'),
    icon(bg="color6", text='\uf019'), # Icon: fa-download
    widget.CheckUpdates(
        background=colors['color6'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        # distro='Arch_checkupdates',
        update_interval=1800,
        custom_command='checkupdates',
        padding=5
    ),

    # 5
    powerline('color5', 'color6'),
    icon(bg="color5", text='\uf028'), # Icon: fa-volume-high
    widget.PulseVolume(
        **base(bg='color5'),
        volume_app="pavucontrol",
        fmt='{}',
        padding=5
    ),

    # 4
    powerline('color4', 'color5'),
    icon(bg="color4", text='\uf538'), # Icon: fa-memory
    widget.Memory(**base(bg='color4'), fmt='{}', padding=5),

    # 3
    powerline('color3', 'color4'),
    icon(bg="color3", text='\uf012'), # Icon: fa-signal
    widget.Net(
        **base(bg='color3'),
        interface='enp4s0',
        format='{down} ↓↑ {up}',
        padding=5
    ),

    # 2
    powerline('color2', 'color3'),
    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),
    widget.CurrentLayout(**base(bg='color2'), padding=5),

    # 1
    powerline('color1', 'color2'),
    icon(bg="color1", text='\uf017'), # Icon: fa-clock
    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'Fira Code SemiBold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()

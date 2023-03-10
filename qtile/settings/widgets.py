from libqtile import widget
from .theme import colors

font = {
    'regular': 'Fira Code',
    'bold': 'Fira Code Bold',
}

fontsize = {
    'default': 16,
    'icon': 18,
    'powerline': 32,
}

padding = 8

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

def separator(width=5):
    return widget.Sep(**base(), linewidth=width)

def icon(bg='dark', fg='text', text='?', fontwidth='regular'):
    return widget.TextBox(
        **base(fg, bg),
        font=font[fontwidth],
        fontsize=fontsize['icon'],
        text=text,
        padding=padding
    )

def powerline(fg='light', bg='dark', mirrored=True):
    return widget.TextBox(
        **base(fg, bg),
        text='\ue0ca' if mirrored else '\ue0c8',
        fontsize=fontsize['powerline'],
        padding=0
    )

def divider():
    return [
        # separator(10),
        icon(
            fg='inactive',
            text='\ue411', # Icon: fa-grip-dots-vertical
            fontwidth='bold'
        ),
        # separator(0),
    ]

def layout():
    return [
        widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),
        powerline(fg='color1', bg='color6', mirrored=False),
    ]

def volume():
    return [
        icon(bg='color6', text='\uf028'), # Icon: fa-volume-high
        widget.PulseVolume(
            **base(bg='color6'),
            volume_app="pavucontrol",
            padding=padding
        ),
        powerline(fg='color6', bg='color5', mirrored=False),
    ]

def updates():
    return [
        icon(bg='color5', text='\uf019'), # Icon: fa-download
        widget.CheckUpdates(
            background=colors['color5'],
            colour_have_updates=colors['text'],
            colour_no_updates=colors['text'],
            no_update_string='0',
            display_format='{updates}',
            update_interval=3600,
            custom_command='checkupdates',
            padding=padding
        ),
        powerline(fg='color5', mirrored=False),
    ]

def workspaces(): 
    return [
        widget.GroupBox(
            **base(fg='light'),
            font=font['bold'],
            fontsize=fontsize['icon'],
            borderwidth=2,
            active=colors['active'],
            inactive=colors['inactive'],
            highlight_method='text',
            highlight_color=[colors['dark'], colors['dark']],
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
    ]

def ram():
    return [
        powerline(fg='color4'),
        icon(bg='color4', text='\uf538'), # Icon: fa-memory
        widget.Memory(
            **base(bg='color4'),
            format='{MemUsed:.0f}{mm}',
            padding=padding
        ),
    ]

def disk():
    return [
        powerline(fg='color3', bg='color4'),
        icon(bg='color3', text='\uf0a0'), # Icon: fa-hard-drive
        widget.DF(
            **base(bg='color3'),
            format='{f}GB',
            partition='/',
            visible_on_warn=False,
            padding=padding
        ),
    ]


def cpu():
    return [
        powerline(fg='color2', bg='color3'),
        icon(bg='color2', text='\uf2db'), # Icon: fa-microchip
        widget.CPU(
            **base(bg='color2'),
            format='{load_percent:.0f}%',
            padding=padding
        ),
    ]

def clock():
    return [
        powerline(fg='color1', bg='color2'),
        icon(bg='color1', text='\uf017'), # Icon: fa-clock
        widget.Clock(
            **base(bg='color1'),
            format='%H:%M - %A %d/%m/%Y '
        ),
    ]


primary_widgets = [
    *layout(),
    *volume(),
    *updates(),
    *divider(),
    *workspaces(),
    *divider(),

    widget.Spacer(background=colors['dark']),

    *ram(),
    *disk(),
    *cpu(),
    *clock(),
]

secondary_widgets = [
    *workspaces(),
    separator(),
    powerline('color1', 'dark'),
    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),
    widget.CurrentLayout(**base(bg='color1'), padding=padding),
    *clock(),
]

widget_defaults = {
    'font': font['regular'],
    'fontsize': fontsize['default'],
    'padding': 1,
}
extension_defaults = widget_defaults.copy()

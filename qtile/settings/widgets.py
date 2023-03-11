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

def base(fg='text', bg='bg'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

def separator(width=5):
    return widget.Sep(**base(), linewidth=width)

def icon(bg='bg', fg='text', text='?', fontwidth='regular'):
    return widget.TextBox(
        **base(fg, bg),
        font=font[fontwidth],
        fontsize=fontsize['icon'],
        text=text,
        padding=padding
    )

def powerline(fg='light', bg='bg', mirrored=True):
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
        widget.CurrentLayoutIcon(**base(bg='red'), scale=0.65),
        powerline(fg='red', bg='green', mirrored=False),
    ]

def disk():
    return [
        icon(bg='green', text='\uf0a0'), # Icon: fa-hard-drive
        widget.DF(
            **base(bg='green'),
            format='{f}GB',
            partition='/',
            visible_on_warn=False,
            padding=padding
        ),
        powerline(fg='green', bg='yellow', mirrored=False),
    ]

def volume():
    return [
        icon(bg='yellow', text='\uf028'), # Icon: fa-volume-high
        widget.PulseVolume(
            **base(bg='yellow'),
            volume_app="pavucontrol",
            padding=padding
        ),
        powerline(fg='yellow', bg='blue', mirrored=False),
    ]

def updates():
    return [
        icon(bg='blue', text='\uf019'), # Icon: fa-download
        widget.CheckUpdates(
            background=colors['blue'],
            colour_have_updates=colors['text'],
            colour_no_updates=colors['text'],
            no_update_string='0',
            display_format='{updates}',
            update_interval=3600,
            custom_command='checkupdates',
            padding=padding
        ),
        powerline(fg='blue', mirrored=False),
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
            highlight_color=[colors['bg'], colors['bg']],
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['bg'],
            other_screen_border=colors['bg'],
            disable_drag=True
        ),
    ]

def ram():
    return [
        powerline(fg='blue'),
        icon(bg='blue', text='\uf538'), # Icon: fa-memory
        widget.Memory(
            **base(bg='blue'),
            format='{MemUsed:.0f}{mm}',
            padding=padding
        ),
    ]

def cpu():
    return [
        powerline(fg='yellow', bg='blue'),
        icon(bg='yellow', text='\uf2db'), # Icon: fa-microchip
        widget.CPU(
            **base(bg='yellow'),
            format='{load_percent:.0f}%',
            padding=padding
        ),
    ]

def clock():
    return [
        powerline(fg='green', bg='yellow'),
        icon(bg='green', text='\uf017'), # Icon: fa-clock
        widget.Clock(
            **base(bg='green'),
            format='%H:%M'
        ),
    ]

def date():
    return [
        powerline(fg='red', bg='green'),
        widget.Clock(
            **base(bg='red'),
            format=' %A %d/%m/%Y '
        ),
    ]


primary_widgets = [
    *layout(),
    *disk(),
    *volume(),
    *updates(),

    widget.Spacer(),
    *divider(),
    *workspaces(),
    *divider(),
    widget.Spacer(),

    *ram(),
    *cpu(),
    *clock(),
    *date(),
]

secondary_widgets = [
    *workspaces(),
    separator(),
    powerline(fg='red', bg='bg'),
    widget.CurrentLayoutIcon(**base(bg='red'), scale=0.65),
    widget.CurrentLayout(**base(bg='red'), padding=padding),
    *clock(),
]

widget_defaults = {
    'font': font['regular'],
    'fontsize': fontsize['default'],
    'padding': 1,
}
extension_defaults = widget_defaults.copy()

################################################################################
################################ nunonogueir444 ################################
################################################################################

# mypy
# qtile check
# python -m py_compile ~/.config/qtile/config.py

from libqtile import bar, layout, qtile, widget, extension, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, EzKey
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import backlight
import os, subprocess

mod = "mod4"
alt = "mod1"

terminal = "kitty"

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # layout.Columns
    #Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    #Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    #Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    #Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    #Key([mod, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    #Key([mod, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    #Key([mod, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    #Key([mod, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),

    #Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    #Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    #Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    #Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    #Key([mod, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    #Key([mod, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
    #Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    #Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
    #Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

        # layout.plasma
        Key([mod, "shift"], "left", lazy.layout.move_left(), desc="Move window to the left"),
        Key([mod, "shift"], "right", lazy.layout.move_right(), desc="Move window to the right"),
        Key([mod, "shift"], "down", lazy.layout.move_down(), desc="Move window down"),
        Key([mod, "shift"], "up", lazy.layout.move_up(), desc="Move window up"),

        Key([mod, "control"], "left", lazy.layout.integrate_left(), desc="Grow window to the left"),
        Key([mod, "control"], "right", lazy.layout.integrate_right(), desc="Grow window to the right"),
        Key([mod, "control"], "down", lazy.layout.integrate_down(), desc="Grow window down"),
        Key([mod, "control"], "up", lazy.layout.integrate_up(), desc="Grow window up"),

        Key([mod, alt], "left", lazy.layout.grow_width(-30), desc="Grow window to the left"),
        Key([mod, alt], "right", lazy.layout.grow_width(30), desc="Grow window to the right"),
        Key([mod, alt], "down", lazy.layout.grow_height(-30), desc="Grow window down"),
        Key([mod, alt], "up", lazy.layout.grow_height(30), desc="Grow window up"),

        Key([mod], "n", lazy.layout.reset_size(), desc="Reset all window sizes"),

    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # dmenu
    Key([mod], "d", lazy.run_extension(extension.DmenuRun(
        dmenu_prompt=">",
        dmenu_font="FiraCode Nerd Font-12",
        background="#15181a",
        foreground="#00ff00",
        selected_background="#079822",
        selected_foreground="#fff",
        #dmenu_height=24,  # Only supported by some dmenu forks
    ))),

    Key([mod, "control"], "page_down", lazy.spawn("systemctl suspend")),
    Key([mod, "control"], "page_up", lazy.spawn("systemctl reboot")),
    Key([mod, "control"], "home", lazy.spawn("systemctl poweroff")),

    # rofi
    Key([mod], "Tab", lazy.spawn("rofi -modi drun -show drun -show-icons -dpi 192")),

    # brightness
    Key([mod, "control"], "1", lazy.spawn("brightness 10")),
    Key([mod, "control"], "2", lazy.spawn("brightness 20")),
    Key([mod, "control"], "3", lazy.spawn("brightness 30")),
    Key([mod, "control"], "4", lazy.spawn("brightness 40")),
    Key([mod, "control"], "5", lazy.spawn("brightness 50")),
    Key([mod, "control"], "6", lazy.spawn("brightness 60")),
    Key([mod, "control"], "7", lazy.spawn("brightness 70")),
    Key([mod, "control"], "8", lazy.spawn("brightness 80")),
    Key([mod, "control"], "9", lazy.spawn("brightness 90")),
    Key([mod, "control"], "0", lazy.spawn("brightness 100")),

    #Key([], "XF86MonBrightnessDown", lazy.spawn("dmenu_run")),
    #Key([], "XF86MonBrightnessUp", lazy.spawn("dmenu_run")),

    # alsa-utils
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 5%-"), desc="Lower Volume by 5%"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 5%+"), desc="Raise Volume by 5%"),
    Key([], "XF86AudioMute", lazy.spawn("amixer sset Master 1+ toggle"), desc="Mute/Unmute Volume"),

    # playerctl
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause player"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"),

    # qalculate-gtk
    Key([], "XF86Calculator", lazy.spawn("qalculate-gtk"), desc="Run calculator"),

    # flameshot
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="Run screenshot"),

]
# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

groups = [
    Group(name="1", label=" 󰍹 "),
    Group(name="2", label=" 󰍹 "),
    Group(name="3", label=" 󰍹 "),
    Group(name="4", label="  ", spawn="google-chrome-stable"   , matches=[Match(wm_instance_class="google-chrome")]),
    Group(name="5", label=" 󰨞 ", spawn="code"                   , matches=[Match(wm_instance_class="code")]),
    Group(name="6", label="  ", spawn="nemo"                   , matches=[Match(wm_instance_class="nemo")]),
    Group(name="7", label="  ", spawn="kitty"                  ),# matches=[Match(wm_instance_class="kitty")]),
    Group(name="8", label="  ", spawn="github-desktop"         , matches=[Match(wm_instance_class="github-desktop")]),
    Group(name="9", label="  ", spawn="vmware"                 , matches=[Match(wm_instance_class="vmware")]),
    Group(name="0", label=" 󰝚 ", spawn="youtube-music"          , matches=[Match(wm_instance_class="youtube-music")]),
]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),

            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),

            # Or, use below if you prefer not to switch to that group. mod + shift + group number = move focused window to group
            #Key(
            #    [mod, "shift"],
            #    i.name,
            #    lazy.window.togroup(i.name),
            #    desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    #layout.Bsp(),
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=5, margin=[10, 10, 10, 10]),
    #layout.Floating(),
    #layout.Matrix(),
    #layout.Max(),
    #layout.MonadTall(),
    #layout.MonadThreeCol(),
    #layout.MonadWide(),
    layout.Plasma(
        border_focus='#FF0000',
        border_focus_fixed='#00e8dc',
        border_normal='#333333',
        border_normal_fixed='#333333',
        border_width=2,
        border_width_single=0,
        fair=False,
        margin=10,
        name='gore'
        ),
    #layout.RatioTile(),
    #layout.ScreenSplit(),
    #layout.Slice(),
    #layout.Spiral(),
    #layout.Stack(num_stacks=2),
    #layout.Tile(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

widget_defaults = dict(
    font="FiraCode Nerd Font",
    fontsize=20,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.WindowName(),
                widget.Spacer(length=bar.STRETCH),
                widget.Prompt(),
                widget.GroupBox(
                    active='FF0000',
                    inactive='AAAAAA',
                    screen_border='#00FF00',
                    this_screen_border='AA0000',
                    this_current_screen_border='FF0000',
                    other_screen_border='005500',
                    other_current_screen_border='005500',
                    padding_x = 10,
                    padding_y = 3,
                    ),
                widget.CurrentLayout(),
                widget.Spacer(length = bar.STRETCH),
                widget.Sep(padding=20),
                widget.Mpris2(
                    foreground='ff0000',
                    display_metadata=["xesam:title", "xesam:artist"],
                    scroll=True,
                    scroll_fixed_width=True,
                    scroll_step=3,
                    width=600,
                    poll_interval=1,
                ),
                widget.Sep(padding=20),
                widget.OpenWeather(
                    location='Clones',
                    format='{location_city} {icon} {temp}°{units_temperature}'
                ),
                widget.Sep(padding=20),
                widget.Systray(icon_size=24, padding=10),
                widget.Sep(padding=20),
                #widget.Volume(emoji = True, emoji_list = ['🔇', '🔈', '🔉', '🔊']),
                #widget.Volume(),
                #widget.Sep(padding=20),
                widget.Clock(format="%a %d-%m-%Y %H:%M:%S"),
            ],
            36,
            background="#333333",
            border_width=0,
            border_color="#ff0000",
            opacity=1,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        #x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="qalculate-gtk"),
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 42

wmname = "gore"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

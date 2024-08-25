/* See LICENSE file for copyright and license details. */

/* appearance */
static const unsigned int borderpx  = 2;        /* border pixel of windows */
static const unsigned int gappx     = 10;        /* gaps between windows */
static const unsigned int snap      = 32;       /* snap pixel */
static const unsigned int systraypinning = 0;   /* 0: sloppy systray follows selected monitor, >0: pin systray to monitor X */
static const unsigned int systrayonleft = 0;    /* 0: systray in the right corner, >0: systray on left of status text */
static const unsigned int systrayspacing = 2;   /* systray spacing */
static const int systraypinningfailfirst = 1;   /* 1: if pinning fails, display systray on the first monitor, False: display systray on the last monitor*/
static const int showsystray        = 1;        /* 0 means no systray */
static const int showbar            = 1;        /* 0 means no bar */
static const int topbar             = 1;        /* 0 means bottom bar */
static const char *fonts[]          = { "FiraCode Nerd Font:size=12" };
static const char dmenufont[]       = "FiraCode Nerd Font:size=12";
static const char col_gray1[]       = "#222222";
static const char col_gray2[]       = "#444444";
static const char col_gray3[]       = "#bbbbbb";
static const char col_gray4[]       = "#eeeeee";
static const char col_cyan[]        = "#005577";
static const char *colors[][3]      = {
	/*               fg         bg         border   */
	[SchemeNorm] = { col_gray3, col_gray1, col_gray2 },
	[SchemeSel]  = { col_gray4, col_cyan,  col_cyan  },
};

static const char *const autostart[] = {
	"xrandr", "--output", "DisplayPort-1", "--mode", "2560x1440", "--rate", "59.95", NULL,
	"nitrogen", "--restore", NULL,
	"volumeicon", NULL,
	"nm-applet", NULL,
	"numlockx", NULL,
	"dropbox", NULL,
	"slstatus", NULL,
	"blueman-applet", NULL,
	"/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1", NULL,
	"easyeffects", "--gapplication-service", NULL,
	"picom", "-b", NULL,
	NULL /* terminate */
};

/* tagging */
static const char *tags[] = { "1", "2", "3", "4", "5", "6", "7", "8", "9" };

static const Rule rules[] = {
	/* xprop(1):
	 *	WM_CLASS(STRING) = instance, class
	 *	WM_NAME(STRING) = title
	 */
	/* class      instance    title       tags mask     isfloating   monitor */
	{ "Gimp",     NULL,       NULL,       0,            1,           -1 },
	{ "Qalculate",NULL,       NULL,       0,            1,           -1 },
	{ "Firefox",  NULL,       NULL,       1 << 8,       0,           -1 },
};

/* layout(s) */
static const float mfact     = 0.55; /* factor of master area size [0.05..0.95] */
static const int nmaster     = 1;    /* number of clients in master area */
static const int resizehints = 1;    /* 1 means respect size hints in tiled resizals */
static const int lockfullscreen = 1; /* 1 will force focus on the fullscreen window */

static const Layout layouts[] = {
	/* symbol     arrange function */
	{ "[]=",      tile },    /* first entry is default */
	{ "><>",      NULL },    /* no layout function means floating behavior */
	{ "[M]",      monocle },
};

/* key definitions */
//#define MODKEY Mod1Mask //alt key
#define MODKEY Mod4Mask //win key
#define TAGKEYS(KEY,TAG) \
	{ MODKEY,                       KEY,      view,           {.ui = 1 << TAG} }, \
	{ MODKEY|ControlMask,           KEY,      toggleview,     {.ui = 1 << TAG} }, \
	{ MODKEY|ShiftMask,             KEY,      tag,            {.ui = 1 << TAG} }, \
	{ MODKEY|ControlMask|ShiftMask, KEY,      toggletag,      {.ui = 1 << TAG} },

/* helper for spawning shell commands in the pre dwm-5.0 fashion */
#define SHCMD(cmd) { .v = (const char*[]){ "/bin/sh", "-c", cmd, NULL } }

/* commands */
static char dmenumon[2] = "0"; /* component of dmenucmd, manipulated in spawn() */
static const char *dmenucmd[] = { "dmenu_run", "-m", dmenumon, "-fn", dmenufont, "-nb", col_gray1, "-nf", col_gray3, "-sb", col_cyan, "-sf", col_gray4, NULL };
static const char *termcmd[]  = { "alacritty", NULL };

static const char *brightness10[]  = { "brightness", "10", NULL };
static const char *brightness20[]  = { "brightness", "20", NULL };
static const char *brightness30[]  = { "brightness", "30", NULL };
static const char *brightness40[]  = { "brightness", "40", NULL };
static const char *brightness50[]  = { "brightness", "50", NULL };
static const char *brightness60[]  = { "brightness", "60", NULL };
static const char *brightness70[]  = { "brightness", "70", NULL };
static const char *brightness80[]  = { "brightness", "80", NULL };
static const char *brightness90[]  = { "brightness", "90", NULL };
static const char *brightness100[] = { "brightness", "100", NULL };

static const char *suspend[]  	   = { "systemctl", "suspend", NULL };
static const char *reboot[]  	   = { "systemctl", "reboot", NULL };
static const char *poweroff[]      = { "systemctl", "poweroff", NULL };

#include <X11/XF86keysym.h>
static const char *lowerVolume[]   = { "amixer", "sset", "Master", "5%-", NULL };
static const char *raiseVolume[]   = { "amixer", "sset", "Master", "5%+", NULL };
static const char *muteToggle[]    = { "amixer", "sset", "Master", "1+", "toggle", NULL };
static const char *audioPlay[]     = { "playerctl", "play-pause", NULL };
static const char *audioNext[]     = { "playerctl", "next", NULL };
static const char *audioPrev[]     = { "playerctl", "previous", NULL };

static const char *calc[]     	   = { "qalculate-gtk", NULL };
static const char *screenshot[]    = { "flameshot", "gui", NULL };

static const Key keys[] = {
	/* modifier                     key        function        argument */
	{ MODKEY,                       XK_p,      spawn,          {.v = dmenucmd } },
	{ MODKEY|ShiftMask,             XK_Return, spawn,          {.v = termcmd } },
	{ MODKEY,                       XK_b,      togglebar,      {0} },
	{ MODKEY,                       XK_j,      focusstack,     {.i = +1 } },
	{ MODKEY,                       XK_k,      focusstack,     {.i = -1 } },
	{ MODKEY,                       XK_i,      incnmaster,     {.i = +1 } },
	{ MODKEY,                       XK_d,      incnmaster,     {.i = -1 } },
	{ MODKEY,                       XK_h,      setmfact,       {.f = -0.05} },
	{ MODKEY,                       XK_l,      setmfact,       {.f = +0.05} },
	{ MODKEY,                       XK_Return, zoom,           {0} },
	{ MODKEY,                       XK_Tab,    view,           {0} },
	{ MODKEY|ShiftMask,             XK_c,      killclient,     {0} },
	{ MODKEY,                       XK_t,      setlayout,      {.v = &layouts[0]} },
	{ MODKEY,                       XK_f,      setlayout,      {.v = &layouts[1]} },
	{ MODKEY,                       XK_m,      setlayout,      {.v = &layouts[2]} },
	{ MODKEY,                       XK_space,  setlayout,      {0} },
	{ MODKEY|ShiftMask,             XK_space,  togglefloating, {0} },
	{ MODKEY,                       XK_0,      view,           {.ui = ~0 } },
	{ MODKEY|ShiftMask,             XK_0,      tag,            {.ui = ~0 } },
	{ MODKEY,                       XK_comma,  focusmon,       {.i = -1 } },
	{ MODKEY,                       XK_period, focusmon,       {.i = +1 } },
	{ MODKEY|ShiftMask,             XK_comma,  tagmon,         {.i = -1 } },
	{ MODKEY|ShiftMask,             XK_period, tagmon,         {.i = +1 } },
	{ MODKEY,                       XK_minus,  setgaps,        {.i = -1 } },
	{ MODKEY,                       XK_equal,  setgaps,        {.i = +1 } },
	{ MODKEY|ShiftMask,             XK_equal,  setgaps,        {.i = 0  } },

	TAGKEYS(                        XK_1,                      0)
	TAGKEYS(                        XK_2,                      1)
	TAGKEYS(                        XK_3,                      2)
	TAGKEYS(                        XK_4,                      3)
	TAGKEYS(                        XK_5,                      4)
	TAGKEYS(                        XK_6,                      5)
	TAGKEYS(                        XK_7,                      6)
	TAGKEYS(                        XK_8,                      7)
	TAGKEYS(                        XK_9,                      8)

	{ MODKEY|ShiftMask,             XK_q,      quit,           {0} },
	{ MODKEY|Mod1Mask,		        XK_1,      spawn,          {.v = brightness10} },
	{ MODKEY|Mod1Mask,		        XK_2,      spawn,          {.v = brightness20} },
	{ MODKEY|Mod1Mask,		        XK_3,      spawn,          {.v = brightness30} },
	{ MODKEY|Mod1Mask,		        XK_4,      spawn,          {.v = brightness40} },
	{ MODKEY|Mod1Mask,		        XK_5,      spawn,          {.v = brightness50} },
	{ MODKEY|Mod1Mask,		        XK_6,      spawn,          {.v = brightness60} },
	{ MODKEY|Mod1Mask,		        XK_7,      spawn,          {.v = brightness70} },
	{ MODKEY|Mod1Mask,		        XK_8,      spawn,          {.v = brightness80} },
	{ MODKEY|Mod1Mask,		        XK_9,      spawn,          {.v = brightness90} },
	{ MODKEY|Mod1Mask,		        XK_0,      spawn,          {.v = brightness100} },
	{ MODKEY|Mod1Mask,		 	 XK_Page_Down, spawn,     	   {.v = suspend} },
	{ MODKEY|Mod1Mask,		     XK_Page_Up,   spawn,   	   {.v = reboot} },
	{ MODKEY|Mod1Mask,		     XK_Home,  	   spawn,	       {.v = poweroff} },

	{ MODKEY|ShiftMask,             XK_q,      quit,           {0} },

	{ 0,		      XF86XK_AudioLowerVolume, spawn,     	   {.v = lowerVolume} },
	{ 0,		      XF86XK_AudioRaiseVolume, spawn,     	   {.v = raiseVolume} },
	{ 0,		      XF86XK_AudioMute,        spawn,     	   {.v = muteToggle} },
	{ 0,		      XF86XK_AudioPlay, 	   spawn,     	   {.v = audioPlay} },
	{ 0,		      XF86XK_AudioNext, 	   spawn,     	   {.v = audioNext} },
	{ 0,		      XF86XK_AudioPrev,        spawn,     	   {.v = audioPrev} },

	{ 0,		      XF86XK_Calculator, 	   spawn,     	   {.v = calc} },
	{ MODKEY|ShiftMask,		      XK_s,        spawn,     	   {.v = screenshot} },
};

/* button definitions */
/* click can be ClkTagBar, ClkLtSymbol, ClkStatusText, ClkWinTitle, ClkClientWin, or ClkRootWin */
static const Button buttons[] = {
	/* click                event mask      button          function        argument */
	{ ClkLtSymbol,          0,              Button1,        setlayout,      {0} },
	{ ClkLtSymbol,          0,              Button3,        setlayout,      {.v = &layouts[2]} },
	{ ClkWinTitle,          0,              Button2,        zoom,           {0} },
	{ ClkStatusText,        0,              Button2,        spawn,          {.v = termcmd } },
	{ ClkClientWin,         MODKEY,         Button1,        movemouse,      {0} },
	{ ClkClientWin,         MODKEY,         Button2,        togglefloating, {0} },
	{ ClkClientWin,         MODKEY,         Button3,        resizemouse,    {0} },
	{ ClkTagBar,            0,              Button1,        view,           {0} },
	{ ClkTagBar,            0,              Button3,        toggleview,     {0} },
	{ ClkTagBar,            MODKEY,         Button1,        tag,            {0} },
	{ ClkTagBar,            MODKEY,         Button3,        toggletag,      {0} },
};


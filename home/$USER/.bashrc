#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

powerline-daemon -q
POWERLINE_BASH_CONTINUATION=1
POWERLINE_BASH_SELECT=1
. /usr/share/powerline/bindings/bash/powerline.sh

# environment variables
export EDITOR=vim
export TERM=kitty
export BROWSER=google-chrome-stable

alias c='clear'
alias ff='fastfetch'
alias rr='source ranger'
# open files on click and lsd alias
alias ls="lsd --hyperlink=auto --color=auto "$@""

fastfetch

# complete command names and file names
complete -cf sudo

# Syntax highlighting and autosuggestions
source /usr/share/blesh/ble.sh

#"command not found" hook that will automatically search the official repositories
source /usr/share/doc/pkgfile/command-not-found.bash

# Auto "cd" when entering just a path
shopt -s autocd

# Line wrap on window resize
shopt -s checkwinsize



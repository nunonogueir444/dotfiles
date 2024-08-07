if status is-interactive
    # Commands to run in interactive sessions can go here
neofetch
end

starship init fish | source
starship preset gruvbox-rainbow -o ~/.config/starship.toml

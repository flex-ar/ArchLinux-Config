if status is-interactive
    # Commands to run in interactive sessions can go here
end

# Aliases

alias ls "exa --icons -h -F"
alias la "exa --icons -l -a -h -F"
alias cat "bat -p"
alias vim "nvim"

starship init fish | source

set -q GHCUP_INSTALL_BASE_PREFIX[1]; or set GHCUP_INSTALL_BASE_PREFIX $HOME ; set -gx PATH $HOME/.cabal/bin $PATH /home/flex/.ghcup/bin # ghcup-env

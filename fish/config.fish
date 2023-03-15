if status is-interactive
    # Commands to run in interactive sessions can go here
  starship init fish | source
end

# Aliases
alias ls "exa --icons -h -F"
alias la "exa --icons -l -a -h -F"
alias cat "bat -p"
alias vim "nvim"
alias hora "tty-clock -f %d/%m/%y -c"


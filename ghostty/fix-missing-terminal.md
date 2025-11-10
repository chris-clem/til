# Fix missing terminal error message

https://ghostty.org/docs/help/terminfo

## Copy Ghostty terminfo to remote server
```
infocmp -x xterm-ghostty | ssh YOUR-SERVER -- tic -x -
```

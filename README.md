# lookup.py
Makes saving little snippets accessible through a keyboard shortcut.

![screenshot](http://i.imgur.com/1N2dR4m.png)

## Dependencies:
- `python-keybinder`
- `python-gtk2`

## Usage:

The program runs in the background. By pressing `Ctrl+I` a text field appears.
Input a short snippet of information and press `Ctrl+Enter` to save it. 
Input a string to search previously saved snippets. Press `ESC` or `Ctrl+I` again to make the window disappear.

## Things to improve:
- Make the entries deletable
- Validate the input so it can't interfere with the highlighting later (uses markdown)
- make the search more google-like, instead of a straight substring search

# Sublime syntax + color theme for Mathematica / Wolfram Language

## Features

* Nice colors
* Modern symbols and syntax (Associations <| |>, /* etc)
* Jump-to-definition for := definitions
* Cmd+click does go-to-definition on symbol under cursor

## Instructions

In the unlikely event that you haven't already, start by installing Package Control. Then use it to install Colorsublime, which we'll use later to switch to Brainon, the custom theme that goes with the syntax definition.

No idea how you're *supposed* to share Sublime text packages, and I don't have time to find out, but colleagues want to use this, so here's how to do it on OS X assuming this repo is at "~/git/WLSublime", haven't actually tested this from-scratch though. If you already have a "Colorsublime - Themes" subfolder, then soft link in the "Brainon" subfolder of this repo into "Colorsublime - Themes". 

```
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
ln -s ~/git/WLSublime/Colorsublime\ -\ Themes Colorsublime\ -\ Themes 
ln -s ~/git/WLSublime/ClickExpand ClickExpand
ln -s ~/git/WLSublime/Mathematica.tmbundle Mathematica.tmbundle
```

On Windows 10 you just have to copy the corresponding folders into `C:/Users/yourname/AppData/Roaming/Sublime Text 3/Packages`. Windows seems to hide AppData by default but you can copy it into the location bar in Explorer just fine.

Make sure to switch to use the Brainon color theme, it goes with the syntax. Do this via Preferences > Color Scheme > Colorsublime Themes > Brainon.

To associate all future .m (or .wl) files with the syntax, open a .m file and at the bottom right of the window, click Objective C (or whatever it is) to get a popup, select `Open all with current extension as ... > Mathematica`.

For click-to-expand, you hold down control, and each successive click will move out one level in the AST. Its starts to break down when it hits the file-level, .tm syntaxer does shallow parsing and can't solve this problem properly.

The Mathematica.tmbundle thing is originally due to Shad Sharma, I've removed some stuff I didn't use that took up space in the repo and modified it a bit to add new symbols, nice Jump To Definition support for := definitions, coloring that attempts to symbols used as functions from symbols on their own, "production-dangerous" symbols like Throw and Print and Echo are bright red, $globals are colored differently, other shit like that.

Here's my sublime preferences, FWIW (the word_seperators is actually important for Mathematica, though that should probably be in a syntax-specific config file):

```
{
    "auto_complete": false,
    "auto_match_enabled": false,
    "bold_folder_labels": true,
    "caret_style": "wide",
    "color_scheme": "Packages/Colorsublime - Themes/Brainon.tmTheme",
    "detect_indentation": false,
    "draw_white_space": "all",
    "fade_fold_buttons": false,
    "font_size": 13,
    "highlight_line": true,
    "line_padding_bottom": 0,
    "line_padding_top": 0,
    "tab_size": 4,
    "theme": "Soda Dark 3.sublime-theme",
    "translate_tabs_to_spaces": false,
    "word_separators": "./\\()\"'-:,.;<>~!@#%^&*|+=[]{}`~?"
}
```

If you want to modify the syntax yourself, I recommend modifying the JSON version and then rebuilding the other with the Sublime Text tool that does this, can't remember what its called.

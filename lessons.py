NAMES = [
    "LEVEL 0 - INTRO",
    "LEVEL 1 - INTRO",
    "LEVEL 2 - BEGINNER",
    "LEVEL 3 - BEGINNER",
    "LEVEL 4 - NORMAL",
    "LEVEL 5 - NORMAL",
    "LEVEL 7 - INTERMEDIATE",
    "LEVEL 8 - INTERMEDIATE",
    "LEVEL 8 - EXPERT",
    "LEVEL 9 - EXPERT",
    "LEVEL 10 - ARE U A GENIUS?"
]

LESSONS = [
    {
        "Move cursor left": ["h"],
        "Move cursor right": ["l"],
        "Move cursor down": ["j"],
        "Move cursor up": ["k"],
        "Close file": [":q"],
        "Close file, don't save changes": [":q!"],
        "Save changes to file": [":w"],
        "Save changes and close file": [":wq", ":x", "ZZ"],
        "Delete character at cursor": ["x"],
        "Insert at cursor": ["i"],
        "Insert at beginning of line": ["I"],
        "Append at cursor": ["a"],
        "Append at end of line": ["A"],
        "Exit insert mode": ["ESC"]
    },
    {
        "Delete word": ["dw"],
        "Delete to end of line": ["d$", "D"],
        "Next word": ["w"],
        "Go to end of text on current line": ["$"],
        "Go to beginning of text on current line": ["^"],
        "Go to beginning of current line": ["0"],
        "Go two word forward": ["2w"],
        "Go to end of third word ahead": ["3e"],
        "Delete two words": ["d2w"],
        "Delete entire line": ["dd"],
        "Delete two lines": ["2dd"],
        "Undo last change": ["u"],
        "Undo changes on entire line": ["U"],
        "Redo changes": ["CTRL_R"]
    },
    {
        "Paste after cursor": ["p"],
        "Paste before cursor": ["P"],
        "Replace character under cursor": ["r"],
        "Change word": ["cw"],
        "Change to end of line": ["c$", "C"],
        "Change two words": ["c2w"]
    },
    {
        "Go to line 50": ["50G"],
        "Go to last line in file": ["G"],
        "Go to first line in file": ["gg"],
        "Search for \"vim\"": ["/vim"],
        "Go to next search result": ["n"],
        "Go to previous search result": ["N"],
        "Search backwards for \"editor\"": ["?editor"],
        "Jump to previous location (jump back)": ["CTRL_O"],
        "Jump to next location (jump foward)": ["CTRL_I"],
        "Go to matching parentheses or brackets": ["%"],
        "Replace bad with good in CURRENT LINE": [":%s/bad/good"],
        "Replace hi with bye in entire file": [":%s/hi/bye/g"],
        "Replace x with y in entire file, prompt for changes": ["%s/x/y/gc"]
    },
    {
        "Run shell command ls": [":!ls"],
        "Open visual mode": ["v"],
        "Visual selected world": ["vw"],
        "Visual select word, then delete word": ["vwd", "vwx"],
        "Save current file as \"play.rb\"": [":w play.rb"],
        "Read in file \"hat.rb\"": [":r hat.rb"]
    }
]

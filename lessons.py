NAMES = [
    "LEVEL 0",
    "LEVEL 1",
    "LEVEL 2",
    "LEVEL 3",
    "LEVEL 4",
    "LEVEL 5",
    "LEVEL 7",
    "LEVEL 8",
    "LEVEL 8",
    "LEVEL 9",
    "LEVEL 10"
]

LESSONS = [
    {
        "Move cursor left": [["H"]],
        "Move cursor right": [["L"]],
        "Move cursor down": [["J"]],
        "Move cursor up": [["K"]],
        "Close file": [["COLON", "Q"]],
        "Close file, don't save changes": [["COLON", "Q", "EXCLAMATION"]],
        "Save changes to file": [["COLON", "W"]],
        "Save changes and close file": [["COLON", "W", "Q"], ["COLON", "X"], ["SHIFT_Z", "SHIFT_Z"]],
        "Delete character at cursor": [["X"]],
        "Insert at cursor": [["I"]],
        "Insert at beginning of line": [["SHIFT_I"]],
        "Append at cursor": [["A"]],
        "Append at end of line": [["SHIFT_A"]],
        "Exit insert mode": [["ESC"]]
    },
    {
        "Delete word": [["D", "W"]],
        "Delete to end of line": [["D", "DOLLAR"], ["SHIFT_D"]],
        "Next word": [["W"]],
        "Go to end of text on current line": [["DOLLAR"]],
        "Go to beginning of text on current line": [["CARET"]],
        "Go to beginning of current line": [["N0"]],
        "Go two word forward": [["N2", "W"]],
        "Go to end of third word ahead": [["N3", "E"]],
        "Delete two words": [["D", "N2", "W"]],
        "Delete entire line": [["D", "D"]],
        "Delete two lines": [["N2", "D", "D"]],
        "Undo last change": [["U"]],
        "Undo changes on entire line": [["SHIFT_U"]],
        "Redo changes": [["CTRL_R"]]
    },
    {
        "Paste after cursor": [["P"]],
        "Paste before cursor": [["SHIFT_P"]],
        "Replace character under cursor": [["R"]],
        "Change word": [["C", "W"]],
        "Change to end of line": [["C", "$"], ["SHIFT_C"]],
        "Change two words": [["C", "N2", "W"]]
    }
]

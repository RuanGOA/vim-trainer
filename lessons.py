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
    }
]

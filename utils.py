from os import system as sys, name as nm



def up_next(level):
    print(level.name)
    for text, lesson_list in level.lessons.items():
        print("    " + text, end=": ")
        for i in range(len(lesson_list)):
            if(i > 0):
                print(" or ", end="")
            print("\u001b[46m " + lesson_to_string(lesson_list[i]) + " \u001b[0m", end="")
        print()
    print()


def lesson_to_string(lesson):
    result = ""
    for item in lesson:
        if ("CTRL_" in item):
            result += "ctrl+"
            result += item[-1].lower()
        else:
            result += item
        """
        if (item == "COLON"):
            result += ":"
        elif (item == "ESC"):
            result += "escape"
        elif (item == "EXCLAMATION"):
            result += "!"
        elif ("SHIFT" in item):
            result += item[-1].upper()
        elif ("CTRL" in item):
            cache = item[5:]
            result += "ctrl+"
            if(cache == "LEFT BRACKET"):
                result += "["
            else:
                result += item[-1].lower()
        elif (item == "DOLLAR"):
            result += "$"
        elif (item == "CARET"):
            result += "^"
        elif (item[0] == "N" and item[1].isnumeric()):
            result += item[1]
        else:
            result += item.lower()
        """
    return result


def verify(answer, right_answers):
    for el in right_answers:
        stri = lesson_to_string(el)
        if answer == stri:
            return True
    return False


def clear():
    if nm == 'nt':
        sys('cls')
    else:
        sys('clear')


def verify_event_key_down(answers):
    res = False
    for ans in answers:
        if ('CTRL_' in ans[0] or ans[0] == 'ESC'):
            res = True
    return res


def verify_key_down(key, right_answers):
    result = False
    for answer in right_answers:
        if key == answer[0]:
            result = True
    return result


def create_title(text, color="\u001b[46m", size=45):
    sides_spaces = int((size - len(text))/2)*' '
    return color + sides_spaces + text + sides_spaces + "\u001b[0m"


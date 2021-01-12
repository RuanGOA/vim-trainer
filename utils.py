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
            elif(cache == "R"):
                result += "r"
        else:
            result += item.lower()
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


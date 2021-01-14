from os import system as sys, name as nm


def up_next(level):
    print(level.name)
    for text, lesson_list in level.lessons.items():
        print("    " + text, end=": ")
        for i, answer in enumerate(lesson_list):
            if i > 0:
                print(" or ", end="")
            print("\u001b[46m " + lesson_to_string(answer) + " \u001b[0m", end="")
        print()
    print()


def lesson_to_string(lesson):
    result = ""
    for item in lesson:
        if "CTRL_" in item:
            result += "ctrl+"
            result += item[-1].lower()
        else:
            result += item
    return result


def verify(user_answer, right_answers):
    for answer in right_answers:
        stri = lesson_to_string(answer)
        if user_answer == stri:
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
        if ('CTRL_' in ans or ans == 'ESC'):
            res = True
    return res


def verify_key_down(key, right_answers):
    result = False
    for answer in right_answers:
        if key == answer:
            result = True
    return result


def create_title(text, color="\u001b[46m", size=45):
    sides_spaces = int((size - len(text))/2)*' '
    return color + sides_spaces + text + sides_spaces + "\u001b[0m"


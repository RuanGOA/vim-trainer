import time

from getkey import getkey, keys
from simple_term_menu import TerminalMenu

from utils import (
    up_next,
    verify,
    clear,
    verify_event_key_down,
    verify_key_down,
    create_title
)
from lessons import NAMES, LESSONS
from level import level


MAIN_MENU_TITLE = "                  VIM TRAINER                 \n\n" + "What's your Vim skill level right now?\n"
MAIN_MENU_ITEMS = ["I'm a beginner", "I'm experienced, but I want to learn more", "I'm tired, I'm going out"]
MAIN_MENU_CURSOR = "> "
MAIN_MENU_CURSOR_STYLE = ("fg_red", "bold")
MAIN_MENU_STYLE = ("bg_cyan", "fg_gray")
MAIN_MENU_EXIT = False


def start_beginner():
    for i in range(0, 10):
        level_i = level(NAMES[i], LESSONS[i])
        start_level(level_i)


def start_level(level):
    up_next(level)
    input("-> PRESS ENTER TO START THIS LEVEL <-")
    clear()

    for i in range(4):
        lesson = level.get_lesson()
        show_lesson(lesson)

    print(f"\n-> YOU COMPLETED {level.name} <-\n")


def show_lesson(lesson):
    flag = False
    first_lesson = True
    lesson_title = f" >>  {lesson[0]}" if (len(lesson[0])%2==0) else f" >> {lesson[0]}"
    while not flag:
        clear()
        print(create_title(lesson_title))

        if(not first_lesson):
            print(create_title("WRONG", "\u001b[41m"))
            print(create_title("TRY AGAIN", "\u001b[41m"))
        else:
            first_lesson = False
            print("\n")

        if(verify_event_key_down(lesson[1])):
            answer = getkey()
            answer = str(keys.name(answer))
            flag = verify_key_down(answer, lesson[1])
        else:
            answer = input("\u001b[31m" + "> " + "\u001b[0m")
            flag = verify(answer, lesson[1])

    clear()
    print(create_title(lesson_title))
    print(create_title("RIGHT", "\u001b[42m"))
    input(create_title("PRESS ENTER TO CONTINUE", "\u001b[42m"))
    clear()


if(__name__ == '__main__'):
    main_menu = TerminalMenu(menu_entries=MAIN_MENU_ITEMS,
                         title=MAIN_MENU_TITLE,
                         menu_cursor=MAIN_MENU_CURSOR,
                         menu_cursor_style=MAIN_MENU_CURSOR_STYLE,
                         menu_highlight_style=MAIN_MENU_STYLE,
                         cycle_cursor=True,
                         clear_screen=True)

    while not MAIN_MENU_EXIT:
        menu_var = main_menu.show()
        if menu_var == 0:
            start_beginner()
        elif menu_var == 1:
            print("This feature has not yet been implemented :(")
            input("PRESS ENTER TO EXIT")
        else:
            MAIN_MENU_EXIT = True


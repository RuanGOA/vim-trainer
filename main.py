from simple_term_menu import TerminalMenu
import time
from utils import up_next, verify, clear
from levels import NAMES, LESSONS
from level import level


MAIN_MENU_TITLE = "                  VIM TRAINER                 \n\n" + "What's your Vim skill level right now?"
MAIN_MENU_ITEMS = ["I'm a beginner", "I'm experienced, but I want to learn more", "I'm tired, I'm going out"]
MAIN_MENU_CURSOR = "> "
MAIN_MENU_CURSOR_STYLE = ("fg_red", "bold")
MAIN_MENU_STYLE = ("bg_cyan", "fg_gray")
MAIN_MENU_EXIT = False


def start_beginner():
    for i in range(0, 11):
        level_i = level(NAMES[i], LESSONS[i])
        start_level(level_i)


def start_level(level):
    up_next(level)
    input("-> PRESS ENTER TO START THIS LEVEL")
    clear()

    for i in range(4):
        lesson = level.get_lesson()
        create_lesson(lesson)

    print(f"YOU COMPLETED {level.name}")


def create_lesson(lesson):
    flag = False
    while not flag:
        clear()
        print("    " + "\u001b[46m    " + lesson[0] + "    \u001b[0m")
        answer = input("\u001b[31m" + "> " + "\u001b[0m")
        flag = verify(answer, lesson[1])
        if(flag):
            print("\u001b[42m" + (20*" ") + "RIGHT" + (20*" "))
        else:
            print("\u001b[41m" + (20*" ") + "WRONG" + (20*" "))
        input((11*" ") + "PRESS ENTER TO CONTINUE" + (11*" ") + "\u001b[0m")
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
            print("b")
            time.sleep(5)
        else:
            MAIN_MENU_EXIT = True


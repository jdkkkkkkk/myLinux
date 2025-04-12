#online_setup.py

import curses
from globl import *


def draw_menu(stdscr):
    """绘制菜单界面"""
    stdscr.clear()
    curses.curs_set(0)  # 隐藏光标

    stdscr.addstr(1, 10, "SETUP(ONLINE)", curses.A_BOLD)

    for idx, item in enumerate(menu_items):
        if idx == current_item:
            stdscr.addstr(3 + idx, 5, f"> {item}: {online_settings[item]} <", curses.A_REVERSE)
        else:
            stdscr.addstr(3 + idx, 5, f"{item}: {online_settings[item]}")

    stdscr.addstr(7, 5, "↑/↓ choose, ←/→ change, Q/q exit", curses.A_DIM)
    stdscr.refresh()

def main(stdscr):
    global current_item

    curses.cbreak()
    stdscr.keypad(True)

    while True:
        draw_menu(stdscr)
        key = stdscr.getch()

        if key == curses.KEY_UP and current_item > 0:
            current_item -= 1
        elif key == curses.KEY_DOWN and current_item < len(menu_items) - 1:
            current_item += 1
        elif key == curses.KEY_LEFT or key == curses.KEY_RIGHT:
            item = menu_items[current_item]

            if item == "model":
                step = 1 if key == curses.KEY_RIGHT else -1
                selected_index[item] = (selected_index[item] + step) % len(online_model_options)
                online_settings[item] = online_model_options[selected_index[item]]
            elif item == "simplify":
                step = 1 if key == curses.KEY_RIGHT else -1
                selected_index[item] = (selected_index[item] + step) % len(simplify_options)
                online_settings[item] = simplify_options[selected_index[item]]
                #settings[item] = "false" if settings[item] == "true" else "true"

        elif key in [ord('q'), ord('Q')]:  # 按 Q 退出
            break

curses.wrapper(main)


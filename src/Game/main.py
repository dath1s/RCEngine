from lib.RCEngine.BasicClasses.Entity import Entity
from lib.RCEngine.BasicClasses.EntityList import EntityList
from lib.RCEngine.BasicClasses.Game import Game
from lib.RCEngine.BasicClasses.Ray import Ray
import curses



if __name__ == '__main__':
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(1)

    stdscr.addstr(0, 10, "Hit 'esc' to quit")
    stdscr.refresh()

    key = ''
    while key != ord('esc'):
        key = stdscr.getch()
        stdscr.addch(20, 25, key)
        stdscr.refresh()
        if key == curses.KEY_UP:
            stdscr.addstr(2, 20, "Up")
        elif key == curses.KEY_DOWN:
            stdscr.addstr(3, 20, "Down")

    curses.endwin()
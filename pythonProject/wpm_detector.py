import curses
from curses import wrapper

def main(stdscr): #standard output screen
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW) # (id number,foreground color,background color)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)

    stdscr.clear()
    stdscr.addstr(0,0,"hello world !" , curses.color_pair(1))
    stdscr.refresh() # refreshes cmd
    stdscr.getkey() # fetches the string 'hello world ! '


wrapper(main)    

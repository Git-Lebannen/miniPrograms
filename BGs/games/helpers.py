from textwrap import dedent
from time import sleep
import os
import keyboard

# set up ANSI sequences
class colors:
    defwhite = "\033[37m"
    resc = "\033[0m"
    bold = "\033[1m"
    red = "\033[31m" # errors
    p1 = "\033[35m" # Player One, purple
    p2 = "\033[32m" # Player Two, green
    high = "\033[36m" # highlight, cyan
    blue = "\033[34m"
    yellow = "\033{33m"
    
# selector function for the menues
def select(list): 

    sleep(0.2)
    selected = 0
    selecting = True
    
    while selecting:
        clear()

        if selected > len(list) - 1:
            selected = int(len(list) - 1)
        
        elif selected < 0:
            selected = 0

        selections = []
        for i in range(len(list)):
            selections.append("[ ] ")

            if i == selected:
                selections[i] = f"[{colors.high}x{colors.resc}] "

            print(dedent(("""\
                """ + selections[i] + list[i] + """""")))

        print(f"\nUse the {colors.high}arrow keys{colors.resc} to navigate and use {colors.high}<ENTER>{colors.resc} to select.")
        
        # have keyboard listen to inputs
        if keyboard.is_pressed("up") or keyboard.is_pressed("left"):
            selected -= 1
            sleep(0.1)
            continue

        elif keyboard.is_pressed("down") or keyboard.is_pressed("right"):
            selected += 1
            sleep(0.1)
            continue

        elif keyboard.read_key() == "enter":
            return list[selected].lower()

# function to clear console
clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")

# function to print quit game screens
def quitGame(bool, moveCount):
   
    clear()
    match [bool, moveCount]:
        case [True, 0]:
            print(f"{colors.p1}Player One{colors.resc} quit before even getting started.")
        case [False, 0]:
            print(f"{colors.p2}Player Two{colors.resc} quit before even getting started.")
        case [True, 1]:
            print(f"{colors.p1}Player One{colors.resc} quit after {colors.high}1{colors.resc} move.")
        case [False, 1]:
            print(f"{colors.p2}Player Two{colors.resc} quit after {colors.high}1{colors.resc} move.")
        case [True, _]:
            print(f"{colors.p1}Player One{colors.resc} quit the game after {colors.high}" + str(moveCount) + f"{colors.resc} moves.")
        case [False, _]:
            print(f"{colors.p2}Player Two{colors.resc} quit the game after {colors.high}" + str(moveCount) + f"{colors.resc} moves.")

# function to run at end of game
def gameEnd():
    while True:
        endInput = input(f"Enter {colors.high}<A>{colors.resc} to play again, {colors.high}<P>{colors.resc} to play something else or {colors.high}<Q>{colors.resc} to quit playing: ").lower()
        if endInput == "again" or "a":
            return 2
        elif endInput == "quit" or "q":
            return 1    
        elif endInput == "play" or "p":
            return 3 


### A collection of board games ###

# import libraries
import games as g, games.helpers as h, signal, os

# stop Keyboard interrupt path displaying
signal.signal(signal.SIGINT, lambda x, y: os._exit(0))

# set default color to white, Player One is magenta, Player Two is x, Errors are red, highlight is green
os.system("color 07")

# lists selection lists
games = ["TTT", "Mancala"]
actions = ["play", "login", "register"]


def main():

    input(f"{h.colors.bold}Welcome to the Board (bored) Games! {h.colors.resc}")
    h.clear()

    # select play/register/login
    action = h.select(actions)

    match action:
        case "play":

            # select a game to play, games can return 1 (quit), 2 (play again) or 3 (play something else)
            game = getattr(g, h.select(games))
            h.clear()

            match game():
                case 1:
                    print("quit")
                case 2:     
                    print("again")
                case 3:
                    print("something else")

        case "login":
            print("lsfjla")
        case "register":
            print("adfadfasf")

if __name__ == "__main__":
    h.clear()
    main()

import re, games.helpers as h
from textwrap import dedent

def ttt():
	### A simple game of Tic-Tac-Toe (also known as noughts and crosses) ###

	# clear current fieldStatus
    
    # define and set global game vars
    ttt = False
    player = True
    moveCount = 1
    messageCode = 0
    lastMove = "_"
    fieldStatus = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    wPh = re.compile(r"([\w ]{3})*(xxx|ooo)([\w ]{3})*")
    wPv = re.compile(r"[\w ]*(x[\w ]{2}x[\w ]{2}x[\w ]*|o[\w ]{2}o[\w ]{2}o[\w ]*)")
    wPd1 = re.compile(r"(x[\w ]{3}x[\w ]{3}x|o[\w ]{3}o[\w ]{3}o)")
    wPd2 = re.compile(r"([\w ]{2}x[\w ]x[\w ]x[\w ]{2}|[\ w]{2}o[\w ]o[\w ]o[\w ]{2})")

    # set and print rules text
    rules = f"""\
		===================================== *** {h.colors.bold}Tic-Tac-Toe, rules and controls{h.colors.resc} *** =====================================

		- The playing field starts off empty
		- Each turn the current player chooses a field and marks it with their symbol (either x or o)
		- The goal is to have three of your own symbols in a straight line, diagonally, vertically or horizontally
		- The game ends when one player satisfies the winning condition

			+---+---+---+
			|   |   | {h.colors.p2}o{h.colors.resc} | <- A field {h.colors.p2}player two{h.colors.resc} has marked
			+---+---+---+
			|   |   |   |
			+---+---+---+
			|   |   | {h.colors.p1}x{h.colors.resc} | <- A field {h.colors.p1}player one{h.colors.resc} has marked
			+---+---+---+

		- The controls let you select a field during your turn by matching each field with a number, starting in the top left:

			+---+---+---+
			|{h.colors.high}<1>{h.colors.resc}|{h.colors.high}<2>{h.colors.resc}|{h.colors.high}<3>{h.colors.resc}| 
			+---+---+---+
			|{h.colors.high}<4>{h.colors.resc}|{h.colors.high}<5>{h.colors.resc}|{h.colors.high}<6>{h.colors.resc}|
			+---+---+---+
			|{h.colors.high}<7>{h.colors.resc}|{h.colors.high}<8>{h.colors.resc}|{h.colors.high}<9>{h.colors.resc}|    
			+---+---+---+

		- To reread the rules during play, input {h.colors.high}<R>{h.colors.resc} at the prompt

		===================================================================================================================
		"""
    print(dedent(rules))

	# check for keypress to start
    while True:
        startInput = input(f"Enter {h.colors.high}<S>{h.colors.resc} to begin the game or {h.colors.high}<Q>{h.colors.resc} to quit: ").lower()
        if startInput == "start" or startInput == "s":
            break
        elif startInput == "q" or startInput == "quit":
            return 1
        
    ttt = True
    h.clear()
    
	# running game code
    while ttt:

		# print the current status or error message
        match [player, messageCode]:
            case [True, 0]:
                message = f"{h.colors.p1}Player One{h.colors.resc}'s turn..."
            case [False, 0]:
                message = f"{h.colors.p2}Player Two{h.colors.resc}'s turn..."
            case [True, -1]:
                message = f"You must {h.colors.red}choose an empty field{h.colors.resc}, {h.colors.p1}Player One{h.colors.resc}"
            case [False, -1]:
                message = f"You must {h.colors.red}choose an empty field{h.colors.resc}, {h.colors.p2}Player Two{h.colors.resc}"
            case [True, -2]:
                message = f"{h.colors.red}Invalid Input{h.colors.resc}. Try again, {h.colors.p1}Player One{h.colors.resc}"
            case [False, -2]:
                message = f"{h.colors.red}Invalid Input{h.colors.resc}. Try again, {h.colors.p2}Player Two{h.colors.resc}"
        messageCode = 0
        print()
        if lastMove == "_":
            print(f"{h.colors.high}First move{h.colors.resc}.")
        else:
            print(f"Move Nr. {h.colors.high}" + str(moveCount) + f"{h.colors.resc}, last move: {h.colors.high}" + lastMove + f"{h.colors.resc}")
        print(message)

		# print playing field and input prompt
        field = """
				+---+---+---+
				| """ + fieldStatus[0] + """ | """ + fieldStatus[1] + """ | """ + fieldStatus[2] + """ | 
				+---+---+---+
				| """ + fieldStatus[3] + """ | """ + fieldStatus[4] + """ | """ + fieldStatus[5] + """ |
				+---+---+---+
				| """ + fieldStatus[6] + """ | """ + fieldStatus[7] + """ | """ + fieldStatus[8] + """ | 
				+---+---+---+
				"""

        print(dedent(field))
		
        userInput = input(f"Enter a {h.colors.high}number{h.colors.resc} to choose a field or press {h.colors.high}<Q>{h.colors.resc} to quit the game: ").lower()

		# clear terminal window
        h.clear()

		# check user's input
        match userInput:
            case "quit" | "q":
                ttt = False
                h.quitGame(player, moveCount)
                return 1
            case "rules" | "r":
                print(dedent(rules))
                while True:
                    continueInput = input(f"Enter {h.colors.high}<C>{h.colors.resc} to resume the game or {h.colors.high}<Q>{h.colors.resc}: ").lower()
                    if continueInput == "continue" or continueInput == "c":
                        break
                    elif continueInput == "quit" or continueInput == "q":
                        h.quitGame(player, moveCount)
                        return 1
                continue

        match [player, userInput]:
            case [True, "1"]:
                chosenField = 0
            case [True, "2"]:
                chosenField = 1
            case [True, "3"]:
                chosenField = 2
            case [True, "4"]:
                chosenField = 3
            case [True, "5"]:
                chosenField = 4
            case [True, "6"]:
                chosenField = 5
            case [True, "7"]:
                chosenField = 6
            case [True, "8"]:
                chosenField = 7
            case [True, "9"]:
                chosenField = 8

            case [False, "1"]:
                chosenField = 0
            case [False, "2"]:
                chosenField = 1
            case [False, "3"]:
                chosenField = 2
            case [False, "4"]:
                chosenField = 3
            case [False, "5"]:
                chosenField = 4
            case [False, "6"]:
                chosenField = 5
            case [False, "7"]:
                chosenField = 6
            case [False, "8"]:
                chosenField = 7
            case [False, "9"]:
                chosenField = 8

            case _:
                messageCode = -2
                continue 
		
        if fieldStatus[chosenField] != " ":
            messageCode = -1
            continue

        elif player:
            fieldStatus[chosenField] = "x"
        else:
            fieldStatus[chosenField] = "o"

        lastMove = f"{h.colors.high}<" + userInput + f">{h.colors.resc}" 

		# check winning conditions
        fieldString = "".join([item for item in fieldStatus])
        
        if wPh.match(fieldString) or wPv.match(fieldString) or wPd1.match(fieldString) or wPd2.match(fieldString):
            moveCount = str(moveCount)
            print(f"{h.colors.bold}The game is over!{h.colors.resc}")
            if player:
                print(f"{h.colors.p1}Player One{h.colors.resc} has won in {h.colors.high}" + moveCount + f"{h.colors.resc} moves.")
            elif not(player):
                print(f"{h.colors.p2}Player Two{h.colors.resc} has won in {h.colors.high}" + moveCount + f"{h.colors.resc} moves.")
            
            field = """
				+---+---+---+
				| """ + fieldStatus[0] + """ | """ + fieldStatus[1] + """ | """ + fieldStatus[2] + """ | 
				+---+---+---+
				| """ + fieldStatus[3] + """ | """ + fieldStatus[4] + """ | """ + fieldStatus[5] + """ |
				+---+---+---+
				| """ + fieldStatus[6] + """ | """ + fieldStatus[7] + """ | """ + fieldStatus[8] + """ | 
				+---+---+---+
				"""

            print(dedent(field))
            ttt = False
            return h.gameEnd()
			
        elif moveCount == 9:
            print(f"{h.colors.bold}The game ended in a draw.{h.colors.resc}")

            field = """
				+---+---+---+
				| """ + fieldStatus[0] + """ | """ + fieldStatus[1] + """ | """ + fieldStatus[2] + """ | 
				+---+---+---+
				| """ + fieldStatus[3] + """ | """ + fieldStatus[4] + """ | """ + fieldStatus[5] + """ |
				+---+---+---+
				| """ + fieldStatus[6] + """ | """ + fieldStatus[7] + """ | """ + fieldStatus[8] + """ | 
				+---+---+---+
				"""

            print(dedent(field))
            ttt = False
            return h.gameEnd()

        else:    
            moveCount += 1
            player = not(player)

		

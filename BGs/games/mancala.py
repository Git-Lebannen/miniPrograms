import games.helpers as h
from textwrap import dedent

def mancala():
    ### A Mancala command line game, credits to https://www.youtube.com/channel/UCthQFmHq8BrXpw-ISqeDxkg (Hands on Math) ###

    # clear current display
    
    # define and set global game vars
    Mancala = False
    player = True
    moveCount = 1
    messageCode = 0
    fieldAmount = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
    lastMove = "_"
    
    h.clear()

    # set and print rules text
    rules = f"""
            ===================================== *** {h.colors.bold}Mancala, rules and controls{h.colors.resc} *** ========================================

            - Each player has six fields and one mancala, 
              each of the six fields start of with 4 pieces (represented as numbers) and the mancala starts empty

                                        {h.colors.p2}P l a y e r  T w o{h.colors.resc} ' s  f i e l d s 
                                            \u2304    \u2304    \u2304    \u2304    \u2304    \u2304    
                                           {h.colors.high}<F>  <E>  <D>  <C>  <B>  <A>{h.colors.resc}
                                    +----+----+----+----+----+----+----+----+
                                    |    |  4 |  4 |  4 |  4 |  4 |  4 |    |
            {h.colors.p2}Player Two{h.colors.resc}'s mancala -> |  {h.colors.p2}0{h.colors.resc} |----+----+----+----+----+----|  {h.colors.p1}0{h.colors.resc} | <- {h.colors.p1}Player One{h.colors.resc}'s mancala
                                    |    |  4 |  4 |  4 |  4 |  4 |  4 |    |
                                    +----+----+----+----+----+----+----+----+
                                           {h.colors.high}<A>  <B>  <C>  <D>  <E>  <F>{h.colors.resc}
                                            ^    ^    ^    ^    ^    ^
                                        {h.colors.p1}P l a y e r  O n e{h.colors.resc} ' s  f i e l d s

            - Each turn the current player chooses a field
            - The pieces are distributed one by one counter-clockwise
            - Choosing an empty (0) field is not allowed
            - Goal is to end up with the most pieces in your own mancala
    
            - If, on your turn, your last piece is distributed to your own mancala, you get to go again
            - Distributing your last piece to an empty (0) field 
              moves that piece and any pieces across from that piece (the opponents fields!) to your own mancala straight away
            - You cannot distribute pieces to your opponent's mancala, the distribution will simply skip that field

            - The game ends when one player doesn't have any pieces in any of their fields
            - When the game ends, the pieces are tallied by adding all pieces on the players sides to their mancala, 
              meaning the player with none on their side usually looses 

            - To choose a field, simply input the letter marking the field you want to choose
            - To reread the rules during play, input '{h.colors.high}rules{h.colors.resc}' at the prompt

            ====================================================================================================================
            """
    print(dedent(rules))

    # check for keypress to start
    while True:
        startInput = input(f"Enter '{h.colors.high}start{h.colors.resc}' to begin the game: ").lower()
        if startInput == "start" or startInput == "s":
            break
        
    mancala = True
    h.clear()

    # runnning game code
    while mancala:

        # print the current status or error message
        match [player, messageCode]:
            case [True, 0]:
                message = f"{h.colors.p1}Player One{h.colors.resc}'s turn..."
            case [False, 0]:
                message = f"{h.colors.p2}Player Two{h.colors.resc}'s turn..."
            case [True, 1]:
                message = f"Still {h.colors.p1}Player One{h.colors.resc}'s turn..."
            case [False, 1]:
                message = f"Still {h.colors.p2}Player Two{h.colors.resc}'s turn..."
            case [True, -1]:
                message = f"You must {h.colors.red}choose a non empty field{h.colors.resc}, {h.colors.p1}Player One{h.colors.resc}"
            case [False, -1]:
                message = f"You must {h.colors.red}choose a non empty field{h.colors.resc}, {h.colors.p2}Player Two{h.colors.resc}"
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
        print()

        # convert fieldAmount elements to strings for displaying
        i = 0
        for element in fieldAmount:
            fieldAmount[i] = int(fieldAmount[i])
            if int(fieldAmount[i]) < 10:
                fieldAmount[i] = " " + str(fieldAmount[i])
            else:
                fieldAmount[i] = str(fieldAmount[i])
            i += 1

        # print playing field and input prompt
        field = """\
            +----+----+----+----+----+----+----+----+
            |    | """+ fieldAmount[12] +""" | """+ fieldAmount[11] +""" | """+ fieldAmount[10] +""" | """+ fieldAmount[9] +""" | """+ fieldAmount[8] +""" | """+ fieldAmount[7] + f""" |    |
            | {h.colors.p2}"""+ fieldAmount[13] + f"""{h.colors.resc} |----+----+----+----+----+----| {h.colors.p1}"""+ fieldAmount[6] + f"""{h.colors.resc} |
            |    | """+ fieldAmount[0] +""" | """+ fieldAmount[1] +""" | """+ fieldAmount[2] +""" | """+ fieldAmount[3] +""" | """+ fieldAmount[4] +""" | """+ fieldAmount[5] +""" |    |
            +----+----+----+----+----+----+----+----+"""

        if player:
            print()
            print(dedent(field))
            print(f"       {h.colors.high}<A>  <B>  <C>  <D>  <E>  <F>{h.colors.resc}")
        
        if not player:
            print(f"       {h.colors.high}<F>  <E>  <D>  <C>  <B>  <A>{h.colors.resc}")
            print(dedent(field))
            print()

        print()
        userInput = input(f"Enter a {h.colors.high}letter{h.colors.resc} to choose a field or press {h.colors.high}<Q>{h.colors.resc} to quit the game: ").lower()

        # clear the terminal window
        h.clear()

        # check user's input
        match userInput:
            case "quit" | "q":
                mancala = False
                h.quitGame(player, moveCount)
            case "rules" | "r":
                print(dedent(rules))
                continue

        match [player, userInput]:
            case [True, "a"]:
                chosenField = 0
            case [True, "b"]:
                chosenField = 1
            case [True, "c"]:
                chosenField = 2
            case [True, "d"]:
                chosenField = 3
            case [True, "e"]:
                chosenField = 4
            case [True, "f"]:
                chosenField = 5

            case [False, "a"]:
                chosenField = 7
            case [False, "b"]:
                chosenField = 8
            case [False, "c"]:
                chosenField = 9
            case [False, "d"]:
                chosenField = 10
            case [False, "e"]:
                chosenField = 11
            case [False, "f"]:
                chosenField = 12

            case _:
                messageCode = -2
                continue

        lastMove = "<" + userInput.upper() + ">"

        # set the giveawayPile and check if the chosenField is empty
        giveawayPile = int(fieldAmount[chosenField])
        if giveawayPile == 0:
            messageCode = -1
            continue
    
        # distribute the pieces from the chosenField and check for a last piece in the current player's mancala
        fieldAmount[chosenField] = 0
        recipient = chosenField + 1

        while(giveawayPile > 0):

            # check for pieces going into the opposite player's mancala
            if player and recipient == 13:
                recipient = 0
            elif not(player) and recipient == 6:
                recipient = 7

            # reset the recipient to 0 to manage correct looping of pieces
            if recipient > 13:
                recipient = 0

            # add a piece to the current field and -- the giveawayPile
            fieldAmount[recipient] = int(fieldAmount[recipient]) + 1
            giveawayPile -= 1 

            # log the last recipient 
            if int(giveawayPile) == 0:
                lastRecipient = recipient

            else:
                recipient += 1

        # gamerules for bonus turn and stealing
        if player and int(lastRecipient) == 6:
            player = True
            messageCode = 1
            continue
        elif player and int(fieldAmount[lastRecipient]) == 1 and lastRecipient < 6:
            fieldAmount[6] = int(fieldAmount[6]) + int(fieldAmount[12 - lastRecipient]) + 1
            fieldAmount[lastRecipient] = 0
            fieldAmount[12 - lastRecipient] = 0
            player = not(player)

        elif not(player) and int(lastRecipient) == 13:
            player = False
            messageCode = 1
            continue
        elif not(player) and int(fieldAmount[lastRecipient]) == 1 and lastRecipient > 6:
            fieldAmount[13] = int(fieldAmount[13]) + int(fieldAmount[12 - lastRecipient]) + 1
            fieldAmount[lastRecipient] = 0
            fieldAmount[12 - lastRecipient] = 0
            player = not(player)

        else:
            player = not(player)

        # ++ moveCount check game end condition
        sideOne = 0
        sideTwo = 0
        for j in range(6):
            sideOne += int(fieldAmount[j])
            sideTwo += int(fieldAmount[j + 7])

        # set up won table and check winner
        if sideOne == 0 or sideTwo == 0:
        
            fieldAmount[6] = int(fieldAmount[6]) + sideOne
            fieldAmount[13] = int(fieldAmount[13]) + sideTwo
            for k in range(6):
                fieldAmount[k] = 0
                fieldAmount[k + 7] = 0

            moveCount = str(moveCount)
            print(f"{h.colors.bold}The game is over!{h.colors.resc}")
            if int(fieldAmount[13]) < int(fieldAmount[6]):
                print(f"{h.colors.p1}Player One{h.colors.resc} has won in {h.colors.high}" + moveCount + f" {h.colors.resc}moves.")
            elif int(fieldAmount[13]) > int(fieldAmount[6]):
                print(f"{h.colors.p2}Player Two{h.colors.resc} has won in {h.colors.high}" + moveCount + f" {h.colors.resc}moves.")
            else:
                print(f"It ended in a {h.colors.bold}draw{h.colors.resc} after {h.colors.high}" + moveCount + f" {h.colors.resc}moves.")

            # convert fieldAmount elements to strings for displaying
            i = 0
            for element in fieldAmount:
                fieldAmount[i] = int(fieldAmount[i])
                if int(fieldAmount[i]) < 10:
                    fieldAmount[i] = " " + str(fieldAmount[i])
                else:
                    fieldAmount[i] = str(fieldAmount[i])
                i += 1

            # print won playing field
            print()
            field = """\
                    +----+----+----+----+----+----+----+----+
                    |    | """+ fieldAmount[12] +""" | """+ fieldAmount[11] +""" | """+ fieldAmount[10] +""" | """+ fieldAmount[9] +""" | """+ fieldAmount[8] +""" | """+ fieldAmount[7] + f""" |    |
                    | {h.colors.p2}"""+ fieldAmount[13] + f"""{h.colors.resc} |----+----+----+----+----+----| {h.colors.p1}"""+ fieldAmount[6] + f"""{h.colors.resc} |
                    |    | """+ fieldAmount[0] +""" | """+ fieldAmount[1] +""" | """+ fieldAmount[2] +""" | """+ fieldAmount[3] +""" | """+ fieldAmount[4] +""" | """+ fieldAmount[5] +""" |    |
                    +----+----+----+----+----+----+----+----+"""
            print(dedent(field))
            # print(dedent("""\
            # +----+----+----+----+----+----+----+----+
            # |    | """+ fieldAmount[12] +""" | """+ fieldAmount[11] +""" | """+ fieldAmount[10] +""" | """+ fieldAmount[9] +""" | """+ fieldAmount[8] +""" | """+ fieldAmount[7] +""" |    |
            # | """+ fieldAmount[13] +""" |----+----+----+----+----+----| """+ fieldAmount[6] +""" |
            # |    | """+ fieldAmount[0] +""" | """+ fieldAmount[1] +""" | """+ fieldAmount[2] +""" | """+ fieldAmount[3] +""" | """+ fieldAmount[4] +""" | """+ fieldAmount[5] +""" |    |
            # +----+----+----+----+----+----+----+----+"""))
            print()

            mancala = False
        
        else:
            moveCount += 1

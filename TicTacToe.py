# TicTacToe.py Gergely Sajdik 301142046

import os
import random
import copy
import time

#Decides the players symbol and who goes first. Also initializes the blank board.
def initializeGame():
    print()
    print("Would you like to be \"x\" or \"o\"?")
    playerLetterSet = False
    global playerLetter 
    playerLetter = input().upper()
    if isLetterValid(playerLetter):
        playerLetterSet = True
    else:
        while (playerLetterSet == False):
            print()
            print("Please enter a valid choice. Would you like to be \"x\" or \"o\"?")
            playerLetter = input().upper()            
            if isLetterValid(playerLetter):
                playerLetterSet = True                

    print()
    print("Do you want to go first? (yes/no)")
    playerTurnSet = False
    playerTurn = input().lower()
    if isTurnValid(playerTurn):
        playerTurnSet = True
    else:
        while (playerTurnSet == False):
            print()
            print("Please enter a valid choice. Would you like to go first? (yes/no)")
            playerTurn = input().lower()
            if isTurnValid(playerTurn):
                playerTurnSet = True
    global board 
    board = [" "," "," "," "," "," "," "," "," "]


#Checks whether the player input is a valid symbol and sets the computer to the opposite symbol.
def isLetterValid(theInput):
    global botLetter
    if theInput == "X":
        botLetter = "O"
        return True
    elif theInput == "O": 
        botLetter = "X"
        return True
    else:
        return False


#checks whether the player input yes or no for going first in the game.
def isTurnValid(theInput):
    global playerStart
    if theInput.startswith("y"):
        playerStart = True
        return True
    elif theInput.startswith("n"):
        playerStart = False
        return True
    else:
        return False
        

#Neatly displays the current standing of the tic tac toe board.
def displayBoard(theBoard):
    print()
    print("     |  " + "   |   ")
    print("  " + theBoard[6] + "  |  " + theBoard[7] + "  |  " + theBoard[8] + " ")
    print("     |  " + "   |   ")
    print("-----------------")
    print("     |  " + "   |   ")
    print("  " + theBoard[3] + "  |  " + theBoard[4] + "  |  " + theBoard[5] + " ")
    print("     |  " + "   |   ")
    print("-----------------")
    print("     |  " + "   |   ")
    print("  " + theBoard[0] + "  |  " + theBoard[1] + "  |  " + theBoard[2] + " ")
    print("     |  " + "   |   ")
    print()


#Runs the game until a winner is found and restarts the game if player chooses to play again.
def playGame():
    isFirstTurn = True
    isGameOver = False
    turnIndicator = "None"
    displayBoard(board)
    if isFirstTurn == True:
        if playerStart == True:
            playerMove()
            turnIndicator = "bot"
            isFirstTurn = False
        else:
            botMove()
            turnIndicator = "player"
            isFirstTurn = False

    while (isGameOver == False and isFirstTurn == False):
        displayBoard(board)
        if turnIndicator == "player":
            isGameOver = playerMove()
            turnIndicator = "bot"
        else:
            isGameOver = botMove()
            turnIndicator = "player"

    print("Would you like to play again? (yes/no)")
    gameChoice = input().lower()
    if gameChoice.startswith("y"):
        os.system('clear')
        initializeGame()
        playGame()
    else:
        print()
        print("Thanks for playing!")


#Checks whether the player input a valid value (1-9) and if that the board is vacant for that spot.
def isValidMove(spot,theBoard):
    validValues = [1,2,3,4,5,6,7,8,9]
    if spot.isdigit() == True:
        if int(spot) in validValues:
            if theBoard[int(spot)-1] == " ":
                return True
            else:
                print()
                print("That spot is already taken, pick an empty spot!")
                return False
        else:
            print()
            print("That choice is not valid!.")
            return False
    else:
        print()
        print("That choice is not valid!.")
        return False


#Checks if the move chosen by the bot is valid (no need for messages or checking if the value isn't between 1-9).
def isValidBotMove(spot,theBoard):
    if theBoard[spot] == " ":
        return True
    else:
        return False


#Checks if the game has been won or a draw.
def gameStanding(L,B):
    if (B[6] == L and B[7] == L and B[8] == L or B[3] == L and B[4] == L and B[5] == L or
B[0] == L and B[1] == L and B[2] == L or B[6] == L and B[3] == L and B[0] == L or B[7] == L and
B[4] == L and B[1] == L or B[8] == L and B[5] == L and B[2] == L or B[6] == L and B[4] == L and B[2] == L or B[8] == L and B[4] == L and B[0] == L):
        return "win"
    elif isBoardFull(B) == True:
        return "draw"  
    

#Checks if the board is full (which would result in a draw if not a win/loss).
def isBoardFull(theBoard):
    emptySpaceCounter = 0
    for i in range(len(theBoard)):
        if theBoard[i] == " ":
            emptySpaceCounter+=1
    if emptySpaceCounter == 0:
        return True
    else:
        return False


#Updates the board with the players move. Displays a message if a win or draw occurs.
def playerMove():
    global turnIndicator
    global isGameOver
    print("Please pick a spot to place your \"{}\" (1-9). Table uses number pad layout.".format(playerLetter))
    move = input()
    if isValidMove(move,board) == True:
        board[int(move)-1] = playerLetter
        if gameStanding(playerLetter,board) == "win":
            displayBoard(board)
            print()
            print("Congratulations, you've won!")
            print()
            return True
        elif gameStanding(playerLetter,board) == "draw":
            displayBoard(board)
            print()
            print("The game is a draw.")
            print()
            return True
    else:
        playerMove()
    return False
    

#Updates the board with the bots move. Calls the MTC random playout method and displays a message if game is over. Makes the bot pause for 1-3 seconds to increase the realism feeling of the game instead of having the bot make the move instantly.
def botMove():
    print("The almighty computer is making its move...")
    time.sleep(random.randint(1,3))
    testBoard = board.copy()
    numberOfPlayouts = 30000
    MTCplayout(testBoard, numberOfPlayouts)
    if gameStanding(botLetter,board) == "win":
        displayBoard(board)
        print("Sorry but you lost!")
        return True
    elif gameStanding(botLetter,board) == "draw":
        displayBoard(board)
        print("The game is a draw.")
        print()
        return True
    return False


#Performs the amount of random playouts defined in botMove() and chooses the best move using the win/draw/loss results.
def MTCplayout(testBoard, numberOfPlayouts):
    #testBoard[3] = "X"
    #board[4] = "X"
    global winCounter 
    winCounter = [0,0,0,0,0,0,0,0,0]
    global drawCounter 
    drawCounter = [0,0,0,0,0,0,0,0,0]
    global lossCounter
    lossCounter = [0,0,0,0,0,0,0,0,0]
    if botLetter == "X":
        bot2Letter = "O"
    else:
        bot2Letter = "X"
    global firstMoveValue
    global useBot2Letter 
    useBot2Letter = False
    firstMove = True

    for i in range(numberOfPlayouts):
        botVSBoard = testBoard.copy()
        areBotsFinished = False
        while (areBotsFinished == False):
            if useBot2Letter == False:
                areBotsFinished = botVSbotMove(botLetter, botVSBoard, firstMove)
                useBot2Letter = True
            else:
                areBotsFinished = botVSbotMove(bot2Letter, botVSBoard, firstMove)
                useBot2Letter = False

    maxDrawValue = 0
    maxAdjustedWinLossValue = 0
    topWinLossSpotValue = 0
    topDrawSpotValue = 0

    for i in range(len(winCounter)):
        if winCounter[i] + lossCounter[i] > maxAdjustedWinLossValue:
            topWinLossSpotValue = i
            maxAdjustedWinLossValue = winCounter[i] + lossCounter[i]
    maxDrawValue = max(drawCounter)
    topDrawSpotValue = drawCounter.index(maxDrawValue)

    if maxAdjustedWinLossValue == 0:
        debuggingMove = random.randint(0,8)
        while (isValidBotMove(debuggingMove, testBoard) == False):
           debuggingMove = random.randint(0,8)
        bestSpot = debuggingMove
        board[debuggingMove] = botLetter
    elif maxDrawValue == 0 or max(winCounter) > (0.25*numberOfPlayouts):
            bestWinningMoveValue = max(winCounter)
            bestWinningMoveSpot = winCounter.index(bestWinningMoveValue)
            board[bestWinningMoveSpot] = botLetter
            bestSpot = bestWinningMoveSpot
    elif max(lossCounter) > (0.25*numberOfPlayouts):
            bestContinueMoveValue = max(lossCounter)
            bestContinueMoveSpot = lossCounter.index(bestContinueMoveValue)
            board[bestContinueMoveSpot] = botLetter
            bestSpot = bestContinueMoveSpot 
    elif maxAdjustedWinLossValue/maxDrawValue < 12.5:
        board[topWinLossSpotValue] = botLetter
        bestSpot = topWinLossSpotValue
    else:
        length = len(winCounter)
        sortedWinCounter = winCounter[:]
        sortedLossCounter = lossCounter[:]
        sortedWinCounter.sort()
        sortedLossCounter.sort()
        secondHighestWin = sortedWinCounter[length-2]
        secondHighestLoss = sortedLossCounter[length-2]
        secondHighestWinSpot = winCounter.index(secondHighestWin)
        secondHighestLossSpot = lossCounter.index(secondHighestLoss)

        if winCounter[topDrawSpotValue] == max(winCounter) or lossCounter[topDrawSpotValue] == max(lossCounter) or winCounter[topDrawSpotValue] == winCounter[secondHighestWinSpot] or lossCounter[topDrawSpotValue] == lossCounter[secondHighestLossSpot]:
            length = len(winCounter)
            tempCounter = drawCounter
            tempCounter.sort()
            secondHighest = tempCounter[length-2]
            editedSpotValue = drawCounter.index(secondHighest)
            board[editedSpotValue] = botLetter
            bestSpot = editedSpotValue
        else:
            topDrawSpotValue = drawCounter.index(maxDrawValue)
            board[topDrawSpotValue] = botLetter
            bestSpot = topDrawSpotValue


#Picks a random spot for the bot to play. Keeps track of the very first move made to later update the result of that moves random playout. Updates the win/draw/loss counters as needed when the bots finish their playout.
def botVSbotMove(letterToCheck, theBoard, firstMove):
    botMove = random.randint(0,8)       
    while (isValidBotMove(botMove,theBoard) == False):
        botMove = random.randint(0,8)

    if firstMove == True:
        firstMoveValue = botMove
        firstMove = False

    theBoard[botMove] = letterToCheck

    if gameStanding(letterToCheck,theBoard) == "win":
        if letterToCheck == botLetter:
            winCounter[firstMoveValue]+=1
        else:
            lossCounter[firstMoveValue]+=1
        return True
    elif gameStanding(letterToCheck,theBoard) == "draw":
            drawCounter[firstMoveValue]+=1
            return True
    else:
        return False


#Run the game--------------------------------------------------------------------------------------

print()
print("Welcome to Tic Tac Toe - can you beat the almighty computer?")
initializeGame()
playGame()

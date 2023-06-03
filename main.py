import random

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

currentPlayer = "X"
winner = None
running = True

# Prints the board nice

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8] + " | ")

# Takes input

def playerInp(board):
    inp = int(input("Enter a space (1 - 9) "))

    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = currentPlayer

    else:
        print("Oops an error occured!")

# Checks horizontal lanes to see if someone won

def checkHorizontal(board):
    global winner

    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True

    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True

    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

    else:
        pass

# Checks vertical lanes to see if someone won

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True

    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True

    elif board[0] == board[3] == board[6] and board[2] != "-":
        winner = board[0]
        return True

    else:
        pass

# Checks diagonal lanes to see if someone won

def checkDiagonal(board):
    global winner

    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True

    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

# Checks tie

def checkTie(board):
    global running
    
    if "-" not in board:
        printBoard(board)
        print("It is a Tie!")
        running = False

# Switches turns

def TurnSwitch():
    global currentPlayer

    if currentPlayer == "X":
        currentPlayer = "O"

    else:
        currentPlayer = "X"

# Checks wins

def checkWin():
    global gameRunning

    if checkHorizontal(board)(board):
        printBoard(board)
        print(f"The winner is {winner}!"/n)
        gameRunning = False

    elif checkVertical(board)(board):
        printBoard(board)
        print(f"The winner is {winner}!"/n)
        gameRunning = False

    elif checkDiagonal(board)(board):
        printBoard(board)
        print(f"The winner is {winner}!"/n)
        gameRunning = False

# Just a stoopid computer that makes turns

def stoopidAI(board):

    while currentPlayer == "O":
        position = random.randint(0, 8)

        if board[position] == "-":
            board[position] = "O"
            TurnSwitch()

# Gameloop

while running:
    printBoard(board)
    playerInp(board)
    checkWin()
    checkTie(board)
    TurnSwitch()
    stoopidAI(board)
    checkWin()
    checkTie(board)
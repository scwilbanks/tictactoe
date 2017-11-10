"""
Simple Tic Tac Toe game in Python

"""


def newgame():

    """
    Returns empty playing field.

    """

    return [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def getmoves(game):

    """
    Returns all possible moves.

    """

    moves = set()
    for i in range(9):
        if game[i] == ' ':
            moves.add(i)
    return moves


def move(game, turn):

    """
    Takes returns new game field based on player input for turn.
    If turn is True then it is X's turn.

    """

    moves = getmoves(game)
    if turn:
        print("X's turn")
    elif not turn:
        print("O's turn")
    place = int(input(">>>"))
    while place not in moves:
        place = int(input("Try again >>>"))
    if turn:
        game[place] = "X"
    else:
        game[place] = "O"
    return game


def showgame(game):

    """
    Print game field to output.

    """

    print("-------")
    for i in [0, 3, 6]:
        print("|"+game[0+i]+"|"+game[1+i]+"|"+game[2+i]+"|")
        print("-------")


def end(game):

    """
    Checks if game is ended due to a win or a tie.

    """

    wins = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]]
    for first, second, third in wins:
        if game[first] == "X" and game[second] == "X" and game[third] == "X":
            return "X wins!"
        elif game[first] == "O" and game[second] == "O" and game[third] == "O":
            return "O wins!"
    if ' ' not in game:
        return "Tie"


def main():

    """
    Main game loop.

    """

    game = newgame()
    turn = True
    while True:
        showgame(game)
        game = move(game, turn)
        ended = end(game)
        if ended:
            showgame(game)
            print(ended)
            break
        else:
            turn = not turn


main()

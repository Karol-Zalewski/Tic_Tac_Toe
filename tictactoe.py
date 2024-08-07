"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0

    for row in range (len(board)):
        for col in range (len(board[row])):
            if board[row][col] == X:
                countX += 1
            elif board[row][col] == O:
                countO += 1
    if countX > countO:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    PosibleMoves = set ()
    for row in range (len(board)):
        for col in range (len(board[row])):
            if board[row][col] == EMPTY:
                PosibleMoves.add ((row, col))
    return PosibleMoves
                


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions (board):
        raise Exception ('Not valid move')
    
    row, col = action
    board_copy = copy.deepcopy(board)
    board_copy[row,col] = player (board)
    return board_copy

def check_row (board, player):
    symbols = 0
    for row in range (len(board)):
        for col in range (len(board)):
            if board[row][col] == player:
                symbols += 1
                if symbols == 3:
                    return True
            symbols = 0
    return False

def check_col (board, player):
    symbols = 0
    for col in range (len(board)):
        for row in range (len(board)):
            if board[row][col] == player:
                symbols += 1
                if symbols == 3:
                    return True
            symbols = 0
    return False

def check_dia (board, player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    else:
        return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_row (board, X) or check_col (board, X) or check_dia (board, X):
        return X
    if check_row (board, O) or check_col (board, O) or check_dia (board, O):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner (board) != None or actions(board) == set():
        return True
    else:
        return False
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner (board) == X:
        return 1
    if winner (board) == O:
        return -1
    else:
        return 0

def max_value (board):
    v = -math.inf
    if terminal (board):
        return utility (board)
    for action in actions (board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value (board):
    v = math.inf
    if terminal (board):
        return utility (board)
    for action in actions (board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal (board):
        return None
    elif player (board) == X:
        plays = []
        for action in actions (board):
            plays.append (min_value(result(board, action), action))
        return sorted (plays, key = lambda x: x[0], reverse = True)[0][1]
    
    elif player (board) == O:
        plays = []
        for action in actions (board):
            plays.append (max_value(result(board, action), action))
        return sorted (plays, key = lambda x: x[0])[0][1]


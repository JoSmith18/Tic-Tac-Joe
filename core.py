from flask import Markup


def clear_board(board, color):
    for n in range(len(board) - 1):
        board[n][1] = Markup('style="background-color:' + color +
                             ';" disabled')


def is_winner(board):
    for x in range(0, 9, 3):
        row = board[x][0] + board[x + 1][0] + board[x + 2][0]
        if row.count('J') == 3 or row.count('S') == 3:
            clear_board(board, 'green')
            return True

    for x in range(3):
        row = board[x][0] + board[x + 3][0] + board[x + 6][0]
        if row.count('J') == 3 or row.count('S') == 3:
            clear_board(board, 'green')
            return True

    row = board[0][0] + board[4][0] + board[8][0]
    if row.count('J') == 3 or row.count('S') == 3:
        clear_board(board, 'green')
        return True

    row = board[2][0] + board[4][0] + board[6][0]
    if row.count('J') == 3 or row.count('S') == 3:
        clear_board(board, 'green')
        return True

    if len(''.join(map(lambda l: l[0], board[:-1]))) > 8:
        clear_board(board, 'red')
        return True
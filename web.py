from flask import Flask, request, render_template, Markup
from core import *

app = Flask(__name__)

board = [['', ''] for _ in range(9)]
board.append(True)


@app.route('/')
def root():
    return render_template('root.html', board=board)

    # spot = int(request.args.get('spot', 1))


@app.route('/<int:n>')
def set_box(n):
    ch = 'J'
    if board[-1]:
        ch = 'S'
    board[n][0] = ch
    board[n][1] = 'disabled'
    board[-1] = not board[-1]
    is_winner(board)
    return render_template('root.html', board=board)


@app.route('/r')
def reset():
    for n in range(len(board) - 1):
        board[n] = ['', '']
    return render_template('root.html', board=board)
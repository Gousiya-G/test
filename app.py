from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

xState = [0] * 9
zState = [0] * 9
turn = 1

def sum(a, b, c):
    return a + b + c

def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            return "X"
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            return "O"
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    global turn, xState, zState

    position = int(request.form['position'])

    if xState[position] == 0 and zState[position] == 0:  # Ensure the cell is not already occupied
        if turn == 1:
            xState[position] = 1
        else:
            zState[position] = 1

        winner = checkWin(xState, zState)
        turn = 1 - turn

        return jsonify({
            'xState': xState,
            'zState': zState,
            'turn': turn,
            'winner': winner
        })
    else:
        return jsonify({
            'xState': xState,
            'zState': zState,
            'turn': turn,
            'winner': None
        })

@app.route('/reset', methods=['POST'])
def reset():
    global xState, zState, turn
    xState = [0] * 9
    zState = [0] * 9
    turn = 1
    return jsonify({
        'xState': xState,
        'zState': zState
    })



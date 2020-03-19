from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit, send

from random import randint

suits = {
    0: 'Pik',
    1: 'Karo',
    2: 'Kier',
    3: 'Trefl'
}

cards = {
    0: 'Ass',
    1: '2',
    2: '3',
    3: '4',
    4: '5',
    5: '6',
    6: '7',
    7: '8',
    8: '9',
    9: '10',
    10: 'Dupek',
    11: 'Królowa',
    12: 'Król'
}

# initialize Flask
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    """Serve the index HTML"""
    return render_template('index.html')

@socketio.on('create')
def on_create():
    """Create a game lobby"""
    room = 1
    join_room(room)
    emit('join_room', {'room': room})

@socketio.on('draw_card')
def on_draw_card():
    card = draw_card()
    socketio.emit('newcard', {'card': card})


def draw_card():
    x = randint(0,3) #random integer 0 to 3 to pick suit
    y = randint(0,12) #random integer 0 to 12 to pick card
    return f"{cards[y]} {suits[x]}"

if __name__ == '__main__':
    socketio.run(app, debug=True)

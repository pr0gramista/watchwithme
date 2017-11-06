import random
import string
import time

from flask import Flask, url_for, render_template, make_response, redirect
from flask_socketio import SocketIO, join_room
from room import Room
from video import VideoState

app = Flask(__name__)
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

rooms = []


def get_room_with_id(id):
    try:
        return [room for room in rooms if room.id == id][0]
    except Exception:
        return None


@socketio.on('join')
def handle_join(room_id):
    room = get_room_with_id(room_id)
    if room is not None:
        join_room(room_id)


@socketio.on('pause')
def handle_pause(room_id, t):
    print('Pause: {}'.format(t))
    room = get_room_with_id(room_id)
    if room is not None:
        room.pause(t)
        socketio.emit('pause', t, room=room_id, include_self=False)


@socketio.on('play')
def handle_play_at(room_id, t):
    print('Play: {}'.format(t))
    room = get_room_with_id(room_id)
    if room is not None:
        room.play(t)
        socketio.emit('play', t, room=room_id, include_self=False)


def get_unique(length):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length))


def get_unique_room_id():
    i = get_unique(16)
    while i in rooms:
        i = get_unique(16)
    return i


@app.route('/')
def index():
    # Create new room
    room_id = get_unique_room_id()
    new_room = Room(room_id)
    rooms.append(new_room)

    response = make_response(redirect(url_for('single_room', room_id=new_room.id)))
    return response


@app.route('/room/<room_id>')
def single_room(room_id):
    room = get_room_with_id(room_id)
    if room is not None:
        play = room.video_state.value
        if room.video_state == VideoState.PLAYING:
            t = room.video_time + time.time() - room.video_timestamp
        else:
            t = room.video_time
        return render_template('room.html',
                               room_id=room_id,
                               play=play,
                               time=t,
                               room=room)
    else:
        return make_response(redirect(url_for('index')))

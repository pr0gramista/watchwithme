from flask import Flask, url_for, render_template, request, make_response, redirect
from flask_socketio import SocketIO, join_room, leave_room
import random
import string
import sys
import time
import re
app = Flask(__name__)
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

rooms = {}

video_patterns = [
    re.compile(r'(?:.*)v=([^\?&]*)'),
    re.compile(r'(?:.*)youtu.be/([^\?&]*)'),
]


def get_video_id(url):
    for video_pattern in video_patterns:
        match = video_pattern.match(url)
        if match:
            return match.group(1)
    return None


def get_unique(length):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length))


@socketio.on('join')
def handle_join(room):
    if room in rooms:
        print("User joined %s" % room)
        join_room(room)


@socketio.on('pauseAt')
def handle_pause_at(room, t):
    print('Pause: ' + str(t))
    rooms[room]['video_time'] = t
    rooms[room]['last_update'] = time.time()
    rooms[room]['video_state'] = 'pause'
    socketio.emit('pause', t, room=room, include_self=False)


@socketio.on('chat')
def handle_pause_at(room, name, message):
    socketio.emit('chat', "%s: %s" % (name, message), room=room)


@socketio.on('playAt')
def handle_play_at(room, t):
    print('Play: ' + str(t))
    rooms[room]['video_time'] = t
    rooms[room]['last_update'] = time.time()
    rooms[room]['video_state'] = 'play'
    socketio.emit('play', t, room=room, include_self=False)


@socketio.on('setVideo')
def handle_set_video(room, name, url):
    print('Set video: ' + str(url))

    video_id = get_video_id(url)
    if video_id:
        rooms[room]['video_id'] = video_id
        socketio.emit('changeVideo', video_id, room=room)
    else:
        print("Bad url!")


def get_unique_room_id():
    i = get_unique(16)
    while i in rooms:
        i = get_unique(16)
    return i


@app.route('/')
def index():
    # Get user cookie or create it
    secret = request.cookies.get('wwm-secret')
    if secret is None:
        secret = get_unique(128)

    # Create new room
    room_id = get_unique_room_id()
    room = {
        'owner': secret,
        'video_id': 'feA64wXhbjo',
        'video_state': 'pause',
        'video_set_permission': 'all',
        'video_time': 0,
        'last_update': time.time()
    }
    rooms[room_id] = room

    response = make_response(redirect(url_for('single_room', room_id=room_id)))
    response.set_cookie('wwm-secret', secret)
    return response


@app.route('/room/<room_id>')
def single_room(room_id):
    if rooms[room_id]['video_state'] == 'play':
        t = rooms[room_id]['video_time'] + time.time() - rooms[room_id]['last_update']
        play = 1
    else:
        t = rooms[room_id]['video_time']
        play = 0

    return render_template('room.html',
                           room_id=room_id,
                           play=play,
                           time=t,
                           room=rooms[room_id])

from flask import Flask, url_for, render_template, request, make_response, redirect
from flask_socketio import SocketIO, join_room, leave_room
import random, string, sys, time
app = Flask(__name__)
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

rooms = {}

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


@socketio.on('playAt')
def handle_play_at(room, t):
    print('Play: ' + str(t))
    rooms[room]['video_time'] = t
    rooms[room]['last_update'] = time.time()
    rooms[room]['video_state'] = 'play'
    socketio.emit('play', t, room=room, include_self=False)


def get_unique_room_id():
    i = get_unique(16)
    while i in rooms:
        i = get_unique(16)
    return i

@app.route('/')
def index():
    # Get user cookie or create it
    username = request.cookies.get('wwm-user')
    if username is None:
        username = get_unique(128)

    # Create new room
    room_id = get_unique_room_id()
    room = {
        'owner': username,
        'video_id': 'feA64wXhbjo',
        'video_state': 'pause',
        'video_set_permission': 'all',
        'video_time': 0,
        'last_update': time.time()
    }
    rooms[room_id] = room

    response = make_response(redirect(url_for('single_room', room_id=room_id)))
    response.set_cookie('wwm-user', username)
    return response


@app.route('/room/<room_id>')
def single_room(room_id):
    if rooms[room_id]['video_state'] == 'play':
        t = rooms[room_id]['video_time'] + time.time() - rooms[room_id]['last_update']
    else:
        t = rooms[room_id]['video_time']

    return render_template('room.html',
        room_id=room_id,
        time=t,
        room=rooms[room_id])

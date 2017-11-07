import random
import string
import time

import config
import youtube
from flask import Flask, url_for, render_template, make_response, redirect, abort
from flask_socketio import SocketIO, join_room
from room import Room
from video import VideoState

app = Flask(__name__)
socketio = SocketIO(app)
yt = youtube.YouTube(config.API)

if __name__ == '__main__':
    socketio.run(app)

rooms = []


def get_room_with_id(id):
    r = [room for room in rooms if room.id == id]
    if len(r) > 0:
        return r[0]
    else:
        return None


@socketio.on('add')
def handle_add(room_id, url):
    room = get_room_with_id(room_id)
    if room is None:
        return abort(404)

    playlist_id = yt.get_playlist_id_from_url(url)
    if playlist_id is None:
        video_id = yt.get_video_id_from_url(url)
        if video_id is None:
            print('No video found')
        else:
            room.add_video(yt.get_video(video_id))
    else:
        room.import_yt_playlist(yt.get_playlist(playlist_id))


@socketio.on('join')
def handle_join(room_id):
    room = get_room_with_id(room_id)
    if room is None:
        return abort(404)

    join_room(room_id)


@socketio.on('pause')
def handle_pause(room_id, t):
    print('Pause: {}'.format(t))
    room = get_room_with_id(room_id)
    if room is None:
        return abort(404)

    room.pause(t)
    socketio.emit('pause', t, room=room_id, include_self=False)


@socketio.on('play')
def handle_play_at(room_id, t):
    print('Play: {}'.format(t))
    room = get_room_with_id(room_id)
    if room is None:
        return abort(404)

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

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


@socketio.on('add_playlist')
def handle_add_playlist(room_id, playlist_url):
    print(playlist_url)
    room = get_room_with_id(room_id)
    if room is None:
        return abort(404)

    playlist_id = yt.get_playlist_id_from_url(playlist_url)
    room.import_yt_playlist(playlist_id)


@socketio.on('remove_playlist')
def handle_add_playlist(room_id, playlist_id):
    room = get_room_with_id(room_id)
    if room is None:
        return abort(404)

    room.remove_playlist(playlist_id)


@socketio.on('live_change_video')
def handle_live_change(room_id, video_url):
    room = get_room_with_id(room_id)
    if room is None:
        return abort(404)

    video_id = yt.get_video_id_from_url(video_url)
    room.change_live_video(video_id)


@socketio.on('send_message')
def handle_send_message(room_id, message):
    room = get_room_with_id(room_id)
    if room is None:
        return abort(404)

    room.send_message(message)


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
        play = room.live_video_state.value
        if room.live_video_state == VideoState.PLAYING:
            t = room.live_video_time + time.time() - room.live_video_timestamp
        else:
            t = room.live_video_time
        return render_template('room.html',
                               room_id=room_id,
                               play=play,
                               time=t,
                               room=room)
    else:
        return make_response(redirect(url_for('index')))

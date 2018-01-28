import random
import string
import time

from flask import Flask, url_for, render_template, make_response, redirect, abort
from flask_socketio import SocketIO, join_room

from watchwithme.models.room import Room
from . import youtube as yt

app = Flask(__name__)
socket_io = SocketIO(app)

if __name__ == '__main__':
    socket_io.run(app)

rooms = []


def get_room_with_id(id):
    r = [room for room in rooms if room.id == id]
    if len(r) > 0:
        return r[0]
    else:
        return None


@socket_io.on('playlist_change_video')
def handle_change_video_on_playlist(room_id, video_id):
    room = get_room_with_id(room_id)
    if room is None:
        return abort(404)

    playlist = room.current_playlist
    if playlist.set_current_video(video_id):
        socket_io.emit('playlist_video_changed', playlist.current_video.for_socketio(), room=room_id)


@socket_io.on('playlist_next_video')
def handle_get_next_video_on_playlist(room_id, current_video_id):
    room = get_room_with_id(room_id)
    if room is None:
        return abort(404)

    playlist = room.current_playlist
    next_video = playlist.next_video()
    if next_video is not None:
        socket_io.emit('playlist_video_changed', next_video.for_socketio(), room=room_id)


@socket_io.on('change_playlist')
def handle_change_playlist(room_id, playlist_id):
    room = get_room_with_id(room_id)
    if room is None:
        return abort(404)

    matched_playlists = [playlist for playlist in room.playlists if playlist.id == playlist_id]
    if len(matched_playlists) >= 1:
        room.current_playlist = matched_playlists[0]
        socket_io.emit('playlist_changed', playlist_id, room=room_id)
        socket_io.emit('playlist_video_changed', matched_playlists[0].current_video.for_socketio(), room=room_id)
    elif playlist_id == "live":
        room.current_playlist = None
        socket_io.emit('playlist_changed', playlist_id, room=room_id)
        socket_io.emit('live_video_changed', room.live.video.for_socketio(), room=room_id)


@socket_io.on('add_playlist')
def handle_add_playlist(room_id, playlist_url):
    """Handles adding playlist to the room"""
    room = get_room_with_id(room_id)
    if room is None:
        return abort(404)

    playlist_id = yt.get_playlist_id_from_url(playlist_url)
    new_playlist = room.import_yt_playlist(playlist_id)
    socket_io.emit('playlist_added', new_playlist.for_socketio(), room=room_id)


@socket_io.on('remove_playlist')
def handle_add_playlist(room_id, playlist_id):
    """Handles removing playlist from the room"""
    room = get_room_with_id(room_id)
    if room is None:
        return abort(404)

    if room.remove_playlist(playlist_id):
        socket_io.emit('playlist_removed', playlist_id, room=room_id)


@socket_io.on('live_change_video')
def handle_live_video_change(room_id, video_url):
    """Handles changing current live video"""
    room = get_room_with_id(room_id)
    if room is None:
        return abort(404)

    video_id = yt.get_video_id_from_url(video_url)
    video = yt.get_video(video_id)
    room.live.set_video(video)
    socket_io.emit('live_video_changed', video.for_socketio(), room=room_id)


@socket_io.on('send_message')
def handle_send_message(room_id, message):
    """Handles sending chat message"""
    room = get_room_with_id(room_id)
    if room is None:
        return abort(404)

    socket_io.emit('message_sent', message, room=room_id)


@socket_io.on('join')
def handle_join(room_id):
    """Handles joining a room"""
    room = get_room_with_id(room_id)
    if room is None:
        return abort(404)

    join_room(room_id)
    for playlist in room.playlists:
        socket_io.emit('playlist_added', playlist.for_socketio(), room=room_id)
    socket_io.emit('live_video_changed', room.live.video.for_socketio(), room=room_id)


@socket_io.on('pause')
def handle_pause(room_id, t):
    """Handles pausing player"""
    print('Pause: {}'.format(t))
    room = get_room_with_id(room_id)
    if room is None:
        return abort(404)

    room.pause(t)
    socket_io.emit('pause', t, room=room_id, include_self=False)


@socket_io.on('play')
def handle_play_at(room_id, t):
    """Handles playing/resuming player"""
    print('Play: {}'.format(t))
    room = get_room_with_id(room_id)
    if room is None:
        return abort(404)

    room.play(t)
    socket_io.emit('play', t, room=room_id, include_self=False)


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
        play = 1 if room.is_video_playing else 0
        if room.is_video_playing:
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

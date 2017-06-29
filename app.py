from flask import Flask, url_for, render_template, request, make_response, redirect
import random, string, sys
app = Flask(__name__)


rooms = {}

def get_unique(length):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length))


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
        'video_set_permission': 'all'
    }
    rooms[room_id] = room

    response = make_response(redirect(url_for('single_room', room_id=room_id)))
    response.set_cookie('wwm-user', username)
    return response


@app.route('/room/<room_id>')
def single_room(room_id):
    return render_template('room.html',
        room_id=room_id,
        room={'video_id': rooms[room_id]['video_id']})

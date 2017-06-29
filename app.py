from flask import Flask, url_for, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/room')
def rooms():
    return 'Rooms'


@app.route('/room/<room_id>')
def single_room(room_id):
    return render_template('room.html', room_id=room_id)

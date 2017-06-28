from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/room')
def rooms():
    return 'Roooms'

@app.route('/room/<room_id>')
def single_room(room_id):
    return 'This is room %s' % room_id

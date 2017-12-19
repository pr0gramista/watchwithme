// Dirty

let sock;
let room_id;

export default class socket {
    static init(_room_id, _socketio) {
        sock = _socketio;
        room_id = _room_id;
    }

    static join() {
        sock.emit('join', room_id);
    }

    static pause(time) {
        sock.emit('pause', room_id, time);
    }

    static play(time) {
        sock.emit('play', room_id, time);
    }

    static send_chat_message(message) {
        sock.emit('send_message', room_id, message);
    }

    static get io() {
        return sock;
    }
}
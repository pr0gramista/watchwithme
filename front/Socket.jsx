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

    static send_chat_message(message) {
        sock.emit('send_message', room_id, message);
        console.log("Message sent")
    }

    static get io() {
        return sock;
    }
}
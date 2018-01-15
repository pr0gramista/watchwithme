// Dirty

let sock;
let room_id;
let nickname;

export default class socket {
    static init(_room_id, _socketio) {
        sock = _socketio;
        room_id = _room_id;
    }

    static setNickname(_nickname) {
        nickname = _nickname;
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
        sock.emit('send_message', room_id, nickname + ": " + message);
    }

    static add_playlist(url) {
        sock.emit('add_playlist', room_id, url);
    }

    static change_playlist(playlistId) {
        sock.emit('change_playlist', room_id, playlistId)
    }

    static get io() {
        return sock;
    }
}
import {addPlaylist, addToHistory, receiveMessage, setCurrentPlaylist, setCurrentVideo} from "./store/actions.jsx";

let sock;
let room_id;
let store;

export default class socket {
    static init(_room_id, _socketio, _store) {
        sock = _socketio;
        room_id = _room_id;
        store = _store;

        socket.io.on('message_sent', function (message) {
            store.dispatch(receiveMessage(message));
        });
        socket.io.on('playlist_added', function (playlist) {
            store.dispatch(addPlaylist(playlist));
        });
        socket.io.on('playlist_changed', function (playlistId) {
            let playlist;
            if (playlistId === "live")
                playlist = "live";
            else
                playlist = store.getState().playlists.find(function (playlist) {
                    return playlist.id === playlistId;
                });

            if (playlist !== undefined)
                store.dispatch(setCurrentPlaylist(playlist));
            else
                console.error("Playlist changed, but it doesn't exist locally.")
        });
        socket.io.on('live_video_changed', function (video) {
            let currentVideo = store.getState().currentVideo;
            if (currentVideo !== null && currentVideo.id !== video.id) {
                store.dispatch(addToHistory(store.getState().currentVideo));
            }
            store.dispatch(setCurrentVideo(video));
        });
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

    static sendChatMessage(message) {
        sock.emit('send_message', room_id, store.getState().nickname + ": " + message);
    }

    static addPlaylist(url) {
        sock.emit('add_playlist', room_id, url);
    }

    static changePlaylist(playlistId) {
        sock.emit('change_playlist', room_id, playlistId);
    }

    static setLiveVideo(videoUrl) {
        sock.emit('live_change_video', room_id, videoUrl);
    }

    static changePlaylistVideo(videoId) {
        sock.emit('playlist_change_video', room_id, videoId);
    }

    static getNextVideoIfPossible(videoId) {
        if (store.getState().currentPlaylist !== "live") {
            sock.emit('playlist_next_video', room_id, videoId);
        }
    }

    static get io() {
        return sock;
    }
}
import random
import string

from . import app
from .playlist import Playlist
from .live import Live


class Room:
    def __init__(self, unique_id):
        self.id = unique_id

        self.current_playlist = None
        self.playlists = []

        self.live = Live(self.id)

    def play(self, t):
        if self.current_playlist is not None:
            self.current_playlist.play()
        else:
            self.live.play(t)

    def pause(self, t):
        if self.current_playlist is not None:
            self.current_playlist.pause()
        else:
            self.live.pause(t)

    @property
    def video(self):
        if self.current_playlist is not None:
            pass  # TODO: Get current video form playlist
        else:
            return self.live.video
        
    @property
    def video_state(self):
        if self.current_playlist is not None:
            pass  # TODO: Get current video state form playlist
        else:
            return self.live.video_state

    @property
    def video_time(self):
        if self.current_playlist is not None:
            pass  # TODO: Get current video time form playlist
        else:
            return self.live.video_time

    @property
    def video_timestamp(self):
        if self.current_playlist is not None:
            pass  # TODO: Get current video timestamp form playlist
        else:
            return self.live.video_timestamp

    def send_message(self, message):
        app.socketio.emit('message_sent', message, room=self.id)

    def remove_playlist(self, playlist_id):
        updated_playlists = [playlist for playlist in self.playlists if playlist.id != playlist_id]
        if len(updated_playlists) < len(self.playlists):
            self.playlists = updated_playlists
            app.socketio.emit('playlist_removed', playlist_id, room=self.id)

    def import_yt_playlist(self, playlist_id):
        new_playlist = Playlist(playlist_id)
        self.playlists.append(new_playlist)
        app.socketio.emit('playlist_added', new_playlist.__dict__, room=self.id)

    @staticmethod
    def __get_unique():
        return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(16))

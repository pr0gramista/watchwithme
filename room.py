import random
import string
import time

import app
from playlist import Playlist
from video import VideoState


class Room():
    def __init__(self, unique_id):
        self.id = unique_id
        self.playlists = []
        self.live_video = 'feA64wXhbjo'
        self.live_video_time = 0
        self.live_video_timestamp = time.time()
        self.live_video_state = VideoState.PAUSED

    def play(self, t):
        self.live_video_time = t
        self.live_video_timestamp = time.time()
        self.live_video_state = VideoState.PLAYING

    def pause(self, t):
        self.live_video_time = t
        self.live_video_timestamp = time.time()
        self.live_video_state = VideoState.PAUSED

    def change_live_video(self, video_id):
        self.live_video = video_id
        self.live_video_time = 0
        self.live_video_timestamp = time.time()
        self.live_video_state = VideoState.PLAYING
        app.socketio.emit('live_video_changed', video_id)

    def remove_playlist(self, playlist_id):
        updated_playlists = [playlist for playlist in self.playlists if playlist.id != playlist_id]
        if len(updated_playlists) < len(self.playlists):
            self.playlists = updated_playlists
            app.socketio.emit('playlist_removed', playlist_id, room=self.id)

    def import_yt_playlist(self, playlist_id):
        new_playlist = Playlist(playlist_id)
        self.playlists.append(new_playlist)
        app.socketio.emit('playlist_added', new_playlist.__dict__, room=self.id)

    def __get_unique(self):
        return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(16))

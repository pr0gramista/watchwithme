import random
import string
import time

import app
from video import VideoState


class Room():
    def __init__(self, unique_id):
        self.id = unique_id
        self.playlist = []
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

    def create_playlist(self):
        pass

    def remove_playlist(self):
        pass

    def import_yt_playlist(self, playlist):
        data = [{'id': l['snippet']['resourceId']['videoId'],
                 'title': l['snippet']['title'],
                 'thumbnail': l['snippet']['thumbnails']['high']['url']
                 } for l in playlist['items'] if l['snippet']['title'] != 'Deleted video']
        self.playlist.extend(data)
        app.socketio.emit('video_added', data, room=self.id)

    def __get_unique(self):
        return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(16))

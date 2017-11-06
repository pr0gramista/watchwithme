import random
import string
import time

import app
from video import VideoState


class Room():
    def __init__(self, unique_id):
        self.id = unique_id
        self.playlist = []
        self.video_now = 'feA64wXhbjo'
        self.video_time = 0
        self.video_timestamp = time.time()
        self.video_state = VideoState.PAUSED

    def play(self, t):
        self.video_time = t
        self.video_timestamp = time.time()
        self.video_state = VideoState.PLAYING

    def pause(self, t):
        self.video_time = t
        self.video_timestamp = time.time()
        self.video_state = VideoState.PAUSED

    def change_video(self):
        pass

    def add_video(self, video):
        data = {
            'id': video['items'][0]['id'],
            'title': video['items'][0]['snippet']['title'],
            'thumbnail': video['items'][0]['snippet']['thumbnails']['high']['url']
        }
        self.playlist.append(data)
        app.socketio.emit('video_added', [data], room=self.id)

    def remove_video(self):
        pass

    def change_playlist(self):
        pass

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

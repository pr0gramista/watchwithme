import time

from . import app
from .video import VideoState

class Live():
    def __init__(self, room_id):
        self.room_id = room_id
        self.queue = []
        self.video = 'feA64wXhbjo'
        self.video_time = 0
        self.video_timestamp = time.time()
        self.video_state = VideoState.PAUSED

    def add_video(self, video_id):
        self.queue.append(app.yt.get_video)

    def remove_video(self, video_id):
        updated_queue = [video for video in self.queue if video.id != video_id]
        if len(updated_queue) < len(self.queue):
            self.queue = updated_queue
            app.socketio.emit('live_feed_video_removed', video_id, room=self.room_id)

    def set_video(self, video_id):
        self.video = video_id
        self.video_time = 0
        self.video_timestamp = time.time()
        self.video_state = VideoState.PLAYING
        app.socketio.emit('live_video_changed', video_id, room=self.room_id)

    def play(self, t):
        self.video_time = t
        self.video_timestamp = time.time()
        self.video_state = VideoState.PLAYING

    def pause(self, t):
        self.video_time = t
        self.video_timestamp = time.time()
        self.video_state = VideoState.PAUSED

    def get_current_video_info(self):
        return
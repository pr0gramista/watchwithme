import time

from watchwithme.app import yt
from watchwithme.video_state import VideoState


class Live:
    def __init__(self, room_id):
        self.room_id = room_id
        self.history = []
        self.video = 'feA64wXhbjo'
        self.video_time = 0
        self.video_timestamp = time.time()
        self.video_state = VideoState.PAUSED

    def add_video_to_history(self, video_id):
        self.history.append(yt.get_video(video_id))

    def remove_video_from_history(self, video_id):
        """"Removes video from the queue, returns None if video wasn't found"""
        updated_history = [video for video in self.history if video.id != video_id]
        if len(updated_history) < len(self.history):
            self.history = updated_history
            return video_id
        return None

    def set_video(self, video_id):
        """Sets video for live feed"""
        self.video = video_id
        self.video_time = 0
        self.video_timestamp = time.time()
        self.video_state = VideoState.PLAYING

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

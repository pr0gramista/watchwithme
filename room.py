import random
import string
import time

from video import VideoState


class Room():
    def __init__(self, unique_id):
        self.id = unique_id
        self.playlist = []
        self.video_now = 'feA64wXhbjo'
        self.video_time = 0
        self.video_timestamp = time.time()
        self.video_state = VideoState.PAUSED

    def play(self):
        pass

    def stop(self):
        pass

    def seek(self):
        pass

    def change_video(self):
        pass

    def add_video(self):
        pass

    def remove_video(self):
        pass

    def change_playlist(self):
        pass

    def create_playlist(self):
        pass

    def remove_playlist(self):
        pass

    def import_yt_playlist(self):
        pass

    def __get_unique(self):
        return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(16))

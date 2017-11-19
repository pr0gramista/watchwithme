import time

from . import app
from .video import VideoState


class Playlist:
    def __init__(self, playlist_id):
        self.id = playlist_id
        vars().update(app.yt.get_playlist_info(playlist_id))
        self.videos = app.yt.get_playlist_items(playlist_id)

        self.video_time = 0
        self.video_timestamp = time.time()
        self.video_state = VideoState.PAUSED

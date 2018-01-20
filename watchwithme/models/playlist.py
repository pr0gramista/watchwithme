import time

import watchwithme.youtube as yt
from watchwithme.video_state import VideoState


class Playlist:
    def __init__(self, playlist_id):
        self.id = playlist_id
        self.__dict__.update(yt.get_playlist_info(playlist_id))
        self.videos = yt.get_playlist_items(playlist_id)

        self.video_time = 0
        self.video_timestamp = time.time()
        self.video_state = VideoState.PAUSED

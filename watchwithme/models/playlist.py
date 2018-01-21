import time

import watchwithme.youtube as yt


class Playlist:
    """Playlist is a list of videos with variables needed for synchronous playback"""
    def __init__(self, playlist_id):
        self.id = playlist_id
        self.__dict__.update(yt.get_playlist_info(playlist_id))
        self.videos = yt.get_playlist_items(playlist_id)

        self.video_time = 0
        self.video_timestamp = time.time()
        self.is_video_playing = False
        self.current_index = 0

    @property
    def current_video(self):
        return self.videos[self.current_index]

    def for_socketio(self):
        videos_for_socketio = [video.for_socketio() for video in self.videos]
        playlist_for_socketio = self.__dict__
        playlist_for_socketio['videos'] = videos_for_socketio
        return playlist_for_socketio

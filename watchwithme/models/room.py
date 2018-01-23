import random
import string

from watchwithme.models.playlist import Playlist
from .live import Live


class Room:
    def __init__(self, unique_id):
        self.id = unique_id

        self.current_playlist = None
        self.playlists = []

        self.live = Live(self.id)

    def play(self, t):
        if self.current_playlist is not None:
            self.current_playlist.play(t)
        else:
            self.live.play(t)

    def pause(self, t):
        if self.current_playlist is not None:
            self.current_playlist.pause(t)
        else:
            self.live.pause(t)

    @property
    def video(self):
        if self.current_playlist is not None:
            return self.current_playlist.current_video
        else:
            return self.live.video
        
    @property
    def is_video_playing(self):
        if self.current_playlist is not None:
            return self.current_playlist.is_video_playing
        else:
            return self.live.is_video_playing

    @property
    def video_time(self):
        if self.current_playlist is not None:
            return self.current_playlist.video_time
        else:
            return self.live.video_time

    @property
    def video_timestamp(self):
        if self.current_playlist is not None:
            return self.current_playlist.video_timestamp
        else:
            return self.live.video_timestamp

    def remove_playlist(self, playlist_id):
        """Removes playlist with given id.

        :param playlist_id: id of playlist
        :return: True is playlist was removed, False if no playlist was removed
        """
        updated_playlists = [playlist for playlist in self.playlists if playlist.id != playlist_id]
        if len(updated_playlists) < len(self.playlists):
            self.playlists = updated_playlists
            return True
        return False

    def import_yt_playlist(self, playlist_id):
        """Imports playlist.

        :param playlist_id: id of playlist
        :return: newly added playlist
        """
        new_playlist = Playlist(playlist_id)
        self.playlists.append(new_playlist)
        return new_playlist

    @staticmethod
    def __get_unique():
        return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(16))

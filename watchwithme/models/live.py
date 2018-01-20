import time

import watchwithme.youtube as yt

LIMIT_HISTORY = 20


class Live:
    """Live is used to watch single videos without need to add them to a playlist
    Note that this class doesn't send any responses, but may use YouTube API.
    """
    def __init__(self, room_id):
        self.room_id = room_id
        self.history = []
        self.video = 'feA64wXhbjo'
        self.video_time = 0
        self.video_timestamp = time.time()
        self.is_video_playing = False

    def add_video_to_history(self, video_id):
        """Adds video to a history. If history is too long it will be shrank"""
        # TODO: implement real get_video
        self.history.append(yt.get_raw_video(video_id))

        # Shrink history
        # TODO: need testing
        while len(self.history) > LIMIT_HISTORY:
            self.history.pop(0)

    def remove_video_from_history(self, video_id):
        """"Removes video from the history, returns None if video wasn't found"""
        updated_history = [video for video in self.history if video.id != video_id]
        if len(updated_history) < len(self.history):
            self.history = updated_history
            return video_id
        return None

    def set_video(self, video_id):
        """Sets video for live feed, it will add existing video to history"""
        self.add_video_to_history(self.video)

        self.video = video_id
        self.video_time = 0
        self.video_timestamp = time.time()
        self.is_video_playing = True

    def play(self, t):
        self.video_time = t
        self.video_timestamp = time.time()
        self.is_video_playing = True

    def pause(self, t):
        self.video_time = t
        self.video_timestamp = time.time()
        self.is_video_playing = False

    def get_current_video_info(self):
        return

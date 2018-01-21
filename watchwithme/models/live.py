import time

from watchwithme.models.video import Video

LIMIT_HISTORY = 20


class Live:
    """Live is used to watch single videos without need to add them to a playlist
    Note that this class doesn't send any responses, but may use YouTube API.
    """
    def __init__(self, room_id):
        self.room_id = room_id
        self.history = []
        self.video = Video.from_items('feA64wXhbjo', 'Bag Raiders - Shooting Stars',
                                      'https://i.ytimg.com/vi/feA64wXhbjo/hqdefault.jpg')
        self.video_time = 0
        self.video_timestamp = time.time()
        self.is_video_playing = False

    def add_video_to_history(self, video):
        """Adds video to a history. If history is too long it will be shrank"""
        self.history.append(video)

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

    def set_video(self, video):
        """Sets video for live feed, it will add existing video to history"""
        self.add_video_to_history(self.video)

        self.video = video
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

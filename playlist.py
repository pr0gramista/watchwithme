import time

import app
from video import VideoState


class Playlist():
    def __init__(self, playlist_id):
        playlist_info = app.yt.get_playlist_info(playlist_id)
        playlist_items = app.yt.get_playlist_items(playlist_id)
        items = playlist_items['items']

        # Get all pages
        while 'nextPageToken' in playlist_items:
            playlist_items = app.yt.get_playlist_items(playlist_id, page_token=playlist_items['nextPageToken'])
            items += playlist_items['items']

        self.title = playlist_info['items'][0]['snippet']['title']
        self.videos = [{
            'id': item['snippet']['resourceId']['videoId'],
            'title': item['snippet']['title'],
            'thumbnail': item['snippet']['thumbnails']['high']['url']
        } for item in items if item['snippet']['title'] != 'Deleted video']
        self.id = playlist_id
        self.description = playlist_info['items'][0]['snippet']['description']
        self.channel_id = playlist_info['items'][0]['snippet']['channelId']
        self.channel_title = playlist_info['items'][0]['snippet']['channelTitle']

        self.current_video = 0
        self.current_video_time = 0
        self.current_video_timestamp = time.time()
        self.current_video_state = VideoState.PLAYING

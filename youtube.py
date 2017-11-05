import json
from urllib.parse import urlencode
from urllib.request import urlopen


class YouTube():
    def __init__(self, key):
        self.key = key


    def get_playlist(self, playlist_id):
        base = 'https://www.googleapis.com/youtube/v3/playlistItems?'
        params = urlencode({
            'key': self.key,
            'part': 'snippet',
            'maxResults': 50,
            'playlistId': playlist_id
        })
        response = urlopen(base + params).read()
        return json.loads(response, encoding='utf8')


    def get_video(self, video_id):
        base = 'https://www.googleapis.com/youtube/v3/videos?'
        params = urlencode({
            'key': self.key,
            'part': 'snippet',
            'id': video_id
        })
        response = urlopen(base + params).read()
        return json.loads(response, encoding='utf8')
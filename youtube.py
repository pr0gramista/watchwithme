import json
import re
from urllib.parse import urlencode
from urllib.request import urlopen


class YouTube():
    def __init__(self, key):
        self.key = key
        self.__video_patterns = [
            re.compile(r'(?:.*)v=([^\?&]*)'),
            re.compile(r'(?:.*)youtu.be/([^\?&]*)'),
        ]

        self.__playlist_patterns = [
            re.compile(r'(?:.*)list=([^\?&]*)')
        ]


    def get_playlist_id_from_url(self, url):
        for video_pattern in self.__playlist_patterns:
            match = video_pattern.match(url)
            if match:
                return match.group(1)
        return None


    def get_video_id_from_url(self, url):
        for video_pattern in self.__video_patterns:
            match = video_pattern.match(url)
            if match:
                return match.group(1)
        return None

    def get_playlist_items(self, playlist_id, page_token=""):
        base = 'https://www.googleapis.com/youtube/v3/playlistItems?'
        params = urlencode({
            'key': self.key,
            'part': 'snippet',
            'maxResults': 50,
            'playlistId': playlist_id,
            'pageToken': page_token
        })
        response = urlopen(base + params).read()
        return json.loads(response, encoding='utf8')

    def get_playlist_info(self, playlist_id):
        base = 'https://www.googleapis.com/youtube/v3/playlists?'
        params = urlencode({
            'key': self.key,
            'part': 'snippet',
            'id': playlist_id
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
import json
import re
from urllib.parse import urlencode
from urllib.request import urlopen


class YouTube:
    def __init__(self, key):
        self.key = key
        self.__video_patterns = [
            re.compile(r'(?:.*)v=([^?&]*)'),
            re.compile(r'(?:.*)youtu.be/([^?&]*)'),
        ]

        self.__playlist_patterns = [
            re.compile(r'(?:.*)list=([^?&]*)')
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

    def get_playlist_items(self, playlist_id):
        """Get all playlist videos in processed format.
        Videos are dictionaries with keys: id, title, thumbnail

        :param playlist_id: id of playlist
        :return: list of videos in specified format
        """
        playlist_items = self.get_raw_playlist_items(playlist_id)
        items = playlist_items['items']

        # Get all pages
        while 'nextPageToken' in playlist_items:
            playlist_items = self.get_raw_playlist_items(playlist_id, page_token=playlist_items[
                'nextPageToken'])
            items += playlist_items['items']

        return [{
            'id': item['snippet']['resourceId']['videoId'],
            'title': item['snippet']['title'],
            'thumbnail': item['snippet']['thumbnails']['high']['url']
        } for item in items if item['snippet']['title'] != 'Deleted video']

    def get_playlist_info(self, playlist_id):
        """Get playlist info in processed format.

        :param playlist_id: id of playlist
        :return: dictionary with keys: title, description, channelId, channelTitle
        """
        playlist_info = self.get_raw_playlist_info(playlist_id)
        return {
            'title': playlist_info['items'][0]['snippet']['title'],
            'description': playlist_info['items'][0]['snippet']['description'],
            'channelId': playlist_info['items'][0]['snippet']['channelId'],
            'channelTitle': playlist_info['items'][0]['snippet']['channelTitle'],
        }

    def get_raw_playlist_items(self, playlist_id, page_token=""):
        """Get JSON response from YouTube Data API v3 of playlist items

        :param playlist_id: id of playlist
        :param page_token: page token for retrieving next/prev page of vidoes
        :return: json response
        """
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

    def get_raw_playlist_info(self, playlist_id):
        """Get JSON response from YouTube Data API v3 of playlist info

        :param playlist_id: id of playlist
        :return json response
        """
        base = 'https://www.googleapis.com/youtube/v3/playlists?'
        params = urlencode({
            'key': self.key,
            'part': 'snippet',
            'id': playlist_id
        })
        response = urlopen(base + params).read()
        return json.loads(response, encoding='utf8')

    def get_raw_video(self, video_id):
        base = 'https://www.googleapis.com/youtube/v3/videos?'
        params = urlencode({
            'key': self.key,
            'part': 'snippet',
            'id': video_id
        })
        response = urlopen(base + params).read()
        return json.loads(response, encoding='utf8')
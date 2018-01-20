import json
import re
from urllib.parse import urlencode
from urllib.request import urlopen

from . import config

KEY = config.API

VIDEO_PATTERNS = [
    re.compile(r'(?:.*)v=([^?&]*)'),
    re.compile(r'(?:.*)youtu.be/([^?&]*)'),
]
PLAYLIST_PATTERNS = [
    re.compile(r'(?:.*)list=([^?&]*)')
]


def get_playlist_id_from_url(url):
    for video_pattern in PLAYLIST_PATTERNS:
        match = video_pattern.match(url)
        if match:
            return match.group(1)
    return None


def get_video_id_from_url(url):
    for video_pattern in VIDEO_PATTERNS:
        match = video_pattern.match(url)
        if match:
            return match.group(1)
    return None


def get_playlist_items(playlist_id):
    """Get all playlist videos in processed format.
    Videos are dictionaries with keys: id, title, thumbnail
    :param playlist_id: id of playlist
    :return: list of videos in specified format
    """
    playlist_items = get_raw_playlist_items(playlist_id)
    items = playlist_items['items']
    # Get all pages
    while 'nextPageToken' in playlist_items:
        playlist_items = get_raw_playlist_items(playlist_id, page_token=playlist_items[
            'nextPageToken'])
        items += playlist_items['items']
    return [{
        'id': item['snippet']['resourceId']['videoId'],
        'title': item['snippet']['title'],
        'thumbnail': item['snippet']['thumbnails']['high']['url']
    } for item in items if item['snippet']['title'] != 'Deleted video']


def get_playlist_info(playlist_id):
    """Get playlist info in processed format.
    :param playlist_id: id of playlist
    :return: dictionary with keys: title, description, channelId, channelTitle
    """
    playlist_info = get_raw_playlist_info(playlist_id)
    return {
        'title': playlist_info['items'][0]['snippet']['title'],
        'description': playlist_info['items'][0]['snippet']['description'],
        'channelId': playlist_info['items'][0]['snippet']['channelId'],
        'channelTitle': playlist_info['items'][0]['snippet']['channelTitle'],
    }


def get_raw_playlist_items(playlist_id, page_token=""):
    """Get JSON response from YouTube Data API v3 of playlist items
    :param playlist_id: id of playlist
    :param page_token: page token for retrieving next/prev page of videos
    :return: json response
    """
    base = 'https://www.googleapis.com/youtube/v3/playlistItems?'
    params = urlencode({
        'key': KEY,
        'part': 'snippet',
        'maxResults': 50,
        'playlistId': playlist_id,
        'pageToken': page_token
    })
    response = urlopen(base + params).read()
    return json.loads(response, encoding='utf8')


def get_raw_playlist_info(playlist_id):
    """Get JSON response from YouTube Data API v3 of playlist info
    :param playlist_id: id of playlist
    :return json response
    """
    base = 'https://www.googleapis.com/youtube/v3/playlists?'
    params = urlencode({
        'key': KEY,
        'part': 'snippet',
        'id': playlist_id
    })
    response = urlopen(base + params).read()
    return json.loads(response, encoding='utf8')


def get_raw_video(video_id):
    base = 'https://www.googleapis.com/youtube/v3/videos?'
    params = urlencode({
        'key': KEY,
        'part': 'snippet',
        'id': video_id
    })
    response = urlopen(base + params).read()
    return json.loads(response, encoding='utf8')

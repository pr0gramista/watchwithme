from watchwithme import app
from watchwithme.models import room

r = room.Room('this2is6unique')


def test_is_playlist_added():
    def mock_get_playlist_info(playlist_id):
        return {
            'title': 'This is sample playlist',
            'description': 'You shoudn\'t read this...',
            'channelId': 'noThis66notachanlle',
            'channelTitle': 'NoNoChananel',
        }

    def mock_get_playlist_items(playlist_id, page_token=""):
        return [
            {
                'id': 'y6120QOlsfU',
                'title': 'Darude - Sandstorm',
                'thumbnail': 'https://i.ytimg.com/vi/y6120QOlsfU/hqdefault.jpg'
            },
            {
                'id': 'Be0OAjuk_1k',
                'title': 'Scatman John - Scatman (Extended Mix) 1995',
                'thumbnail': 'https://i.ytimg.com/vi/Be0OAjuk_1k/hqdefault.jpg'
            }]

    app.yt.get_playlist_items = mock_get_playlist_items
    app.yt.get_playlist_info = mock_get_playlist_info
    r.import_yt_playlist('PL3hSzXlZKYpM8XhxS0v7v4SB2aWLeCcUj')
    assert len(r.playlists) == 1


def test_is_playlist_removed():
    r.remove_playlist('PL3hSzXlZKYpM8XhxS0v7v4SB2aWLeCcUj')
    assert len(r.playlists) == 0


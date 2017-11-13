import app
import room
import test_data

r = room.Room('this2is6unique')


def test_is_playlist_added():
    def mock_get_playlist_info(playlist_id):
        return test_data.playlist_info

    def mock_get_playlist_items(playlist_id):
        return test_data.playlist_items

    app.yt.get_playlist_items = mock_get_playlist_items
    app.yt.get_playlist_info = mock_get_playlist_info
    r.import_yt_playlist('PL3hSzXlZKYpM8XhxS0v7v4SB2aWLeCcUj')
    assert len(r.playlists) == 1


def test_is_playlist_removed():
    r.remove_playlist('PL3hSzXlZKYpM8XhxS0v7v4SB2aWLeCcUj')
    assert len(r.playlists) == 0


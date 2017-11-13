import app
import room

r = room.Room('this2is6unique')


def test_is_playlist_added():
    r.import_yt_playlist('PL3hSzXlZKYpM8XhxS0v7v4SB2aWLeCcUj')
    assert len(r.playlists) == 1


def test_is_playlist_removed():
    r.remove_playlist('PL3hSzXlZKYpM8XhxS0v7v4SB2aWLeCcUj')
    assert len(r.playlists) == 0

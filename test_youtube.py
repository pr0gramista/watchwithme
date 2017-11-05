import youtube
import config

yt = youtube.YouTube(config.API)

def test_get_video_id_from_url():
    assert 'u0pmV7GoTjc' == yt.get_video_id_from_url(
               'https://www.youtube.com/watch?v=u0pmV7GoTjc&index=1&list=PLFBGoru86zY8ILLlLL17Ftj2fzqueUrF0')

    assert '1seENWiVxx8' == yt.get_video_id_from_url('https://www.youtube.com/watch?v=1seENWiVxx8')
    assert 'Gd1dM5VcC14' == yt.get_video_id_from_url('https://youtu.be/Gd1dM5VcC14')


def test_get_playlist_id_from_url():
    assert 'PLC90FB71F6ECE17F3' == yt.get_playlist_id_from_url(
        'https://www.youtube.com/playlist?list=PLC90FB71F6ECE17F3')
    assert 'PL_uBB7xUdveWcaG15Mm6p5HKv0at2PFVu' == yt.get_playlist_id_from_url(
        'https://www.youtube.com/watch?v=VqB1uoDTdKM&index=1&list=PL_uBB7xUdveWcaG15Mm6p5HKv0at2PFVu')
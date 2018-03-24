from django.db import models


class Room(models.Model):
    id = models.SlugField(max_length=12, primary_key=True, unique=True, verbose_name="ID")

    def __str__(self):
        return self.id


class Playlist(models.Model):
    pid = models.SlugField(max_length=64, verbose_name="ID")
    title = models.TextField(verbose_name="Title")
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({})'.format(self.title, self.pid)


class Video(models.Model):
    vid = models.SlugField(max_length=11, db_index=True, verbose_name="ID")
    title = models.TextField(verbose_name="Title")
    thumbnail = models.URLField(verbose_name="Thumbnail url")
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({})'.format(self.title, self.vid)

    def get_video_url(self):
        return 'https://www.youtube.com/watch?v={}'.format(self.id)

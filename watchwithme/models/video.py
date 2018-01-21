class Video:
    @classmethod
    def from_api_item(cls, api_item):
        video = cls()

        video.id = api_item['id']
        video.title = api_item['snippet']['title']
        video.thumbnail = api_item['snippet']['thumbnails']['high']['url']
        return video

    @classmethod
    def from_items(cls, id, title, thumbnail):
        video = cls()
        video.id = id
        video.title = title
        video.thumbnail = thumbnail
        return video

    @classmethod
    def from_dict(cls, dict):
        video = cls()
        video.id = dict['id']
        video.title = dict['title']
        video.thumbnail = dict['thumbnail']
        return video

    def for_socketio(self):
        return self.__dict__

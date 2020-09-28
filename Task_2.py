
class Track:

    def __init__(self, track_name, track_duration):
        self.track_name = track_name
        self.track_duration = int(track_duration)  # in minutes

    def __gt__(self, other):
        if not isinstance(other, Track):
            print('один из объектов не класса Track')
            return
        return self.track_duration > other.track_duration

    def __str__(self):
        return f'\t{self.track_name} - {self.track_duration}'


class Album:
    album_name = 'Default'
    album_author = 'Default'
    track_list = []

    def __str__(self):
        return f'Album: {self.album_name} by {self.album_author}\n' + self.get_tracks()

    def get_tracks(self):
        lists = ''
        for track in self.track_list:
            if isinstance(track, Track):
                lists = lists + str(track) + '\n'
            else:
                return 'Unknown track format'
        return lists

    def add_track(self, new_track):
        # Не смотря на отсутствие конструктора класса, в отличие от примера, приведенного на уроке,
        # код работает, и не преобразует атрибут класса Album track_list в новый список(?)
        self.track_list.append(new_track)

    def get_duration(self):
        duration = 0
        for track in self.track_list:
            duration += track.track_duration
        return duration


album_1 = Album()
album_1.album_name = 'Sonata #14'
album_1.album_author = 'Beethoven'
album_1.track_list = [Track('part_1', 4),
                      Track('part_2', 5),
                      Track('part_3', 3)]

album_2 = Album()
album_2.album_name = 'Abbey Road'
album_2.album_author = 'The Beatles'
album_2.track_list = [Track('Come together', 2),
                      Track('Here Comes the Sun', 4),
                      Track('Because', 3)]


albums_collection = [album_1, album_2]


def all_albums_duration(albums_list):
    for album in albums_list:
        print(f'Альбом {album.album_name} длится: {album.get_duration()}')


# album_1.add_track(Track('new', 5))
# all_albums_duration(albums_collection)

track1 = Track('Bohemian rhapsody', 6)
track2 = Track('The show must go on', 4)
print(track2)
print(album_1)

print(track2 > track1)



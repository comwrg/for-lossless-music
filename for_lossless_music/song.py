from prettytable import PrettyTable

class Song:
    def __init__(self, name, singers, album, tags=[]):
        self.name = name
        self.singers = singers
        self.album = album
        self.tags = tags


def print_table(songs):
    """Print song table
    :param songs: list<Song>
    """

    t = PrettyTable(['ID', '歌名', '歌手', '专辑', '标签'])
    for i, s in enumerate(songs):
        t.add_row([i+1, s.name, ','.join(s.singers), s.album, ','.join(s.tags)])

    print(t)



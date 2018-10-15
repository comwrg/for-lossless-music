from prettytable import PrettyTable

class Song:
    def __init__(self, name, singers, album, interval, tags, source, token):
        self.name = name
        self.singers = singers
        self.album = album
        self.interval = interval
        self.tags = tags
        self.source = source
        self.token = token


def songs2table(songs):
    """return table what can print
    :param songs: list<Song>
    """

    t = PrettyTable(['ID', '歌名', '歌手', '专辑', '长度', '标签'])
    for i, s in enumerate(songs):
        t.add_row([i+1, s.name, ','.join(s.singers), s.album, s.interval, ','.join(s.tags)])

    return t



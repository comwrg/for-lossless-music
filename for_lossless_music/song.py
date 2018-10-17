from prettytable import PrettyTable

class Song:
    def __init__(self, id, name, singers, album, interval, tags, source, token):
        self.id = id
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
    for s in songs:
        t.add_row([s.id, s.name, ','.join(s.singers), s.album, s.interval, ','.join(s.tags)])

    return t

class FoundSong:
    def __init__(self, origin_name, origin_singer, song=None, status='ERROR'):
        self.origin_name = origin_name
        self.origin_singer = origin_singer
        self.song = song
        self.status = status

def foundsong2table(foundsongs, idx=None):
    t = PrettyTable(['ID', '歌名', '歌手', '专辑', '长度', '标签', '状态'])
    for i, e in enumerate(foundsongs):
        if e.song:
            t.add_row([idx if idx else i+1, e.origin_name, e.origin_singer, e.song.album, e.song.interval, ','.join(e.song.tags), e.status])
        else:
            t.add_row([idx if idx else i+1, e.origin_name, e.origin_singer, ' - ', ' - ', ' - ', e.status])
    return t

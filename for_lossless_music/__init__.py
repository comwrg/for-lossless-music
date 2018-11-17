
from .moresound import Moresound, Source, str2source
from .song import songs2table, FoundSong, foundsong2table
from .download import download
from .qqmusic import QQMusic
from .song import Song
from .quality import *

__version__ = '0.1.1'


def search(keyword, source: Source, page=1, num=20):
    if source == Source.QQ:
        return QQMusic.search(keyword, page, num)
    else:
        return Moresound.search(keyword, source, page, num)


def get_download_urls(song: Song):
    if song.source == Source.QQ:
        return QQMusic.get_download_urls(song)
    else:
        return Moresound.get_download_urls(song)

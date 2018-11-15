from enum import Enum

class Source(Enum):
    QQ   = 'qq'
    KUWO = 'kw'

def str2source(s):
    if isinstance(s, Source):
        return s
    for e in Source:
        if e.value == s:
            return e
    return None
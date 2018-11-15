def find_best_quality(songs):
    ranks = ['FLAC', 'APE', '320MP3', '192AAC', '192OGG', '128MP3', '96AAC', '48AAC', '24AAC']
    for r in ranks:
        if r in songs:
            return r
    return None


def get_suffix_by_quality(quality):
    return {
        'FLAC'  : 'flac',
        'APE'   : 'ape',
        '320MP3': 'mp3',
        '128MP3': 'mp3',
    }[quality]

import requests
from .progressbar import SimpleProgressBar


def download(url, dst):
    r = requests.get(
        url,
        stream=True,
    )
    bar = SimpleProgressBar(int(r.headers['Content-Length']))
    with open(dst, 'wb') as f:
        CHUNK_SIZE = 256 * 1024
        for chunk in r.iter_content(chunk_size=CHUNK_SIZE):
            if not chunk:
                break
            f.write(chunk)
            bar.update_received(CHUNK_SIZE)

    bar.done()

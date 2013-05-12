import time
import urllib

from django.core.cache import cache
from django.http import HttpResponse

from torrent_stream import settings


def torrent_stream_js(request, torrent_content_hash):
    attempts = range(60)
    for attempt in attempts:
        content_id = cache.get(
            settings.TORRENT_STREAM_CACHE_PREFIX + torrent_content_hash)
        if content_id:
            url = 'http://torrentstream.net/p/{0}'.format(content_id)
            return HttpResponse(urllib.urlopen(url).read(), content_type='text/javascript')
        else:
            time.sleep(1)

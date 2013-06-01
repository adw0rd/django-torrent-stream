import urllib

from django.core.cache import cache
from django.http import HttpResponse, Http404

from torrent_stream import settings
from torrent_stream.helpers import get_content_id
from torrent_stream.exceptions import FailedResponse, ServerFault


def torrent_stream_js(request, torrent_content_hash):
    cache_key = settings.TORRENT_STREAM_CACHE_PREFIX + torrent_content_hash
    torrent_stream = cache.get(cache_key)
    if not torrent_stream:
        raise Http404

    content_id = torrent_stream.get('content_id', None)
    if not content_id:
        torrent_content = torrent_stream.get('content', None)
        if torrent_content:
            try:
                torrent_stream['content_id'] = get_content_id(torrent_content)
                cache.set(cache_key, torrent_stream)
            except (FailedResponse, ServerFault):
                pass
    url = 'http://torrentstream.net/p/{0}'.format(torrent_stream['content_id'])
    return HttpResponse(urllib.urlopen(url).read(), content_type='text/javascript')

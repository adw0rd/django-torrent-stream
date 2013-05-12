import threading

from django.core.cache import cache

from settings import (
    TORRENT_STREAM_AFFILIATE_KEY, TORRENT_STREAM_ZONE_ID, TORRENT_STREAM_CACHE_PREFIX)
from api import TorrentStreamAPI
from exceptions import FailedResponse, ServerFault


def get_content_id(torrent_data, content_name="", duration=""):
    """Return content id by torrent data
    @param string torrent_data - Content of torrent file
    @param string content_name - Name of video, example "My video" (optional)
    @param integer duration - Duration of video in seconds (optional)
    @return integer
    """
    api = TorrentStreamAPI(
        TORRENT_STREAM_AFFILIATE_KEY,
        TORRENT_STREAM_ZONE_ID)
    content_id = api.get_content_id(
        torrent_data, content_name, duration)
    return content_id


def deffered_get_content_id(torrent_data, torrent_content_hash):
    # if cache.has_key(TORRENT_STREAM_CACHE_PREFIX + torrent_content_hash):
    #     return True
    def runner(torrent_data, torrent_content_hash):
        try:
            content_id = get_content_id(torrent_data)
            cache.set(TORRENT_STREAM_CACHE_PREFIX + torrent_content_hash, content_id)
        except (FailedResponse, ServerFault):
            return None
    thread = threading.Thread(target=runner, args=[torrent_data, torrent_content_hash])
    thread.daemon = True
    thread.start()
    return True

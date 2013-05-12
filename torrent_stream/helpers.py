from settings import (
    TORRENT_STREAM_AFFILIATE_KEY, TORRENT_STREAM_ZONE_ID)
from api import TorrentStreamAPI


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

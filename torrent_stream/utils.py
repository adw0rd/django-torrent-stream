from helpers import get_content_id
from exceptions import ServerFault


def receive_content_id(torrent_file):
    """content_id extractor
    """
    content = ""
    if hasattr(torrent_file, 'read'):
        content = torrent_file.read()
    try:
        return get_content_id(content)
    except ServerFault:
        return None

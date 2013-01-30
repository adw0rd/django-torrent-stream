from django import template

from ..helpers import get_content_id
from ..settings import TORRENT_STREAM_PLAYER
from ..exceptions import FailedResponse, ServerFault

register = template.Library()


def receive_content_id(torrent_file):
    """content_id extractor
    """
    content = ""
    if hasattr(torrent_file, 'read'):
        content = torrent_file.read()
    try:
        return get_content_id(content)
    except (FailedResponse, ServerFault):
        return None


def torrent_stream_player(torrent_file):
    """Common context for player/button templates
    """
    return {
        'content_id': receive_content_id(torrent_file),
        'TORRENT_STREAM_PLAYER': TORRENT_STREAM_PLAYER,
    }


def torrent_stream_button(*args):
    return torrent_stream_player(*args)

register.inclusion_tag('torrent_stream/player.html')(torrent_stream_player)
register.inclusion_tag('torrent_stream/button.html')(torrent_stream_button)

import hashlib

from django import template

from ..helpers import deffered_get_content_id
from ..settings import TORRENT_STREAM_PLAYER

register = template.Library()


def torrent_stream_player(torrent_file):
    """Common context for player/button templates
    """
    if hasattr(torrent_file, 'read'):
        content = torrent_file.read()
        torrent_content_hash = hashlib.md5(content).hexdigest()
        deffered_get_content_id(content, torrent_content_hash)
    return {
        'torrent_content_hash': torrent_content_hash,
        'TORRENT_STREAM_PLAYER': TORRENT_STREAM_PLAYER,
    }


def torrent_stream_button(*args):
    return torrent_stream_player(*args)

register.inclusion_tag('torrent_stream/player.html')(torrent_stream_player)
register.inclusion_tag('torrent_stream/button.html')(torrent_stream_button)

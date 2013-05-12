import hashlib

from django import template
from django.core.cache import cache

from ..settings import TORRENT_STREAM_PLAYER, TORRENT_STREAM_CACHE_PREFIX

register = template.Library()


def torrent_stream_player(torrent_file):
    """Common context for player/button templates
    """
    torrent_content_hash = ''
    if hasattr(torrent_file, 'read'):
        torrent_content = torrent_file.read()
        torrent_content_hash = hashlib.md5(torrent_content).hexdigest()
        cache.set(
            TORRENT_STREAM_CACHE_PREFIX + torrent_content_hash,
            {'content': torrent_content})
    return {
        'torrent_content_hash': torrent_content_hash,
        'TORRENT_STREAM_PLAYER': TORRENT_STREAM_PLAYER,
    }


def torrent_stream_button(*args):
    return torrent_stream_player(*args)


register.inclusion_tag('torrent_stream/player.html')(torrent_stream_player)
register.inclusion_tag('torrent_stream/button.html')(torrent_stream_button)

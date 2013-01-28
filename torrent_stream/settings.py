from django.conf import settings

TORRENT_STREAM_PLAYER = {
    'width': '650px',
    'height': '342px',
}

if hasattr(settings, 'TORRENT_STREAM_PLAYER'):
    TORRENT_STREAM_PLAYER.update(settings.TORRENT_STREAM_PLAYER)

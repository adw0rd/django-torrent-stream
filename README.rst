django-torrent-stream
=====================

Wraps the Torrent Stream http://torrentstream.org/

Installation
-------------

Application is still in alpha, so you can install so::

    pip install -e git://github.com/adw0rd/django-torrent-stream.git#egg=torrent_stream


Add to ``settings.py``::

    TORRENT_STREAM_AFFILIATE_KEY = "<HASH>"
    TORRENT_STREAM_ZONE_ID = <DIGIT>

These ``KEY`` and ``ID`` you can get on a page http://acestream.net/affiliate/

Usage
---------

For example, you have a model Torrent::

    class Torrent(models.Model):
        name = models.CharField(max_length=300, blank=True)
        content = models.FileField(upload_to="torrents/torrents", blank=True)

Then you can get the ``CONTENT_ID`` like this::

    from app.models import Torrent
    from torrent_stream.helpers import get_content_id

    torrent_obj = Torrent.objects.get(pk=42)

    # Enough to transmit the content of the torrent file
    content_id = get_content_id(torrent_obj.content.read())

    # Or you can also pass the name of the torrent, and the duration to display the data in the player
    content_id = get_content_id(torrent_obj.content.read(), torrent_obj.name, duration_in_seconds)

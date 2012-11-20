django-torrent-stream
=====================

Wraps the Torrent Stream http://torrentstream.org/

Installation
-------------
::

    pip install -e git://github.com/adw0rd/django-torrent-stream.git#egg=torrent_stream

Usage
---------

For example, you have a model Torrent::

    class Torrent(models.Model):
        name = models.CharField(max_length=300, blank=True)
        content = models.FileField(upload_to="torrents/torrents", blank=True)

Then you can get the ``CONTENT_ID`` like this::

    from app.models import Torrent
    from torrent_stream import get_content_id

    torrent_obj = Torrent.objects.get(pk=42)

    # Enough to transmit the content of the torrent file
    content_id = get_content_id(torrent_obj.content.read())

    # You can also pass the name of the torrent, and the duration to display the data in the player
    content_id = get_content_id(torrent_obj.content.read(), torrent_obj.name, duration_on_seconds)

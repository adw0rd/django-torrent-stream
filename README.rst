django-torrent-stream
=====================

Wraps the Torrent Stream http://torrentstream.org/

Installation
-------------

Install a stable version::

    pip install django-torrent-stream

Or install an alpha version::

    pip install -e git://github.com/adw0rd/django-torrent-stream.git#egg=torrent_stream


Add to ``settings.py``::

    TORRENT_STREAM_AFFILIATE_KEY = "<HASH>"
    TORRENT_STREAM_ZONE_ID = <DIGIT>
    
    # You can specify size of player
    TORRENT_STREAM_PLAYER = {
        'width': '650px',
        'height': '342px',
    }

These ``KEY`` and ``ID`` you can get on a page http://acestream.net/affiliate/

Usage
---------

For example, you have a model Torrent::

    class Torrent(models.Model):
        name = models.CharField(max_length=300, blank=True)
        content = models.FileField(upload_to="torrents/torrents", blank=True)


You can display the button, when clicked, will be available to the player::

    {% torrent_stream_button torrent.filename %}

Or you can display a player at once::

    {% torrent_stream_player torrent.filename %}

How to get CONTENT_ID
------------------------

Sometimes you need to get ``CONTENT_ID``, you can do so::

    from app.models import Torrent
    from torrent_stream.helpers import get_content_id

    torrent_obj = Torrent.objects.get(pk=42)

    # Enough to transmit the content of the torrent file
    content_id = get_content_id(torrent_obj.content.read())

    # Or you can also pass the name of the torrent, and the duration to display the data in the player
    content_id = get_content_id(torrent_obj.content.read(), torrent_obj.name, duration_in_seconds)

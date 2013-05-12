from django.conf.urls import patterns, url


urlpatterns = patterns(
    'torrent_stream.views',
    url(r'^js/(\w{32})/$', 'torrent_stream_js', name='torrent_stream_js'),
)

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'torrent_stream.views',
    url(r'^assets/(\w{32}).js$', 'torrent_stream_js', name='torrent_stream_js'),
)

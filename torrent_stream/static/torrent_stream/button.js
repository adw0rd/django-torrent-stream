var torrent_stream_video_box_id = "torrent_stream_video_box";
if (!document.getElementById(torrent_stream_video_box_id)) {
    // Once create a video-box for output online video
    var el = document.createElement('div');
    el.id = torrent_stream_video_box_id;
    var browser_size = get_browser_size();
    var box_top = (browser_size['h'] / 2) - (torrent_stream['box_height'] / 2);
    var box_left = (browser_size['w'] / 2) - (torrent_stream['box_width'] / 2);
    el.style.cssText = 'position:fixed;top:'+box_top+'px;left:'+box_left+'px;width:'+torrent_stream['box_width']+'px;height:'+torrent_stream['box_height']+'px';
    document.body.appendChild(el);
}

document.getElementById("torrent_stream_button_" + torrent_stream['content_id']).onclick = function(){
    // Click to "Watch online" and setup video-player to video-box
    var script = document.createElement('script');
    script.src = "http://torrentstream.net/p/" + torrent_stream['content_id'];
    document.documentElement.appendChild(script);
    script.onload = function() {
        tsplayer(
            torrent_stream_video_box_id,
            {width: torrent_stream['box_width'], height: torrent_stream['box_height']}
        );
    };
    return false;
};

function get_browser_size () {
    var browserWidth, browserHeight;
    if (typeof(window.innerWidth) == 'number') {
        // Non-IE
        browserWidth = window.innerWidth;
        browserHeight = window.innerHeight;
    } else if (document.documentElement && (document.documentElement.clientWidth || document.documentElement.clientHeight)) {
        // IE 6+ in 'standards compliant mode'
        browserWidth = document.documentElement.clientWidth;
        browserHeight = document.documentElement.clientHeight;
    }
    return {'w': parseInt(browserWidth), 'h': parseInt(browserHeight)}
}

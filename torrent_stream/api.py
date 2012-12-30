import base64
import os.path
import requests

from lxml import etree
from django.template import Context, Template

import default_settings
import exceptions


class TorrentStreamAPI(object):
    _content_id = None

    def __init__(self, affiliate_key, zone_id, xml_api_url=None):
        """
        @param string affiliate_key -
        @param integer zone_id -
        @see http://acestream.net/affiliate/index.php
        """
        self.affiliate_key = affiliate_key
        self.zone_id = zone_id
        self.xml_api_url = xml_api_url or default_settings.XML_API_URL

    def send_request(self, template_name, params):
        """Send XML request
        @param string template_name - Path to xml-template
        @param dict params - Context for xml-template
        @return string - Response in XML
        """
        xml_template = open(os.path.join(os.path.dirname(__file__), template_name)).read()
        xml_content = Template(xml_template).render(Context(params))
        response = requests.post(self.xml_api_url, xml_content)
        return response.content

    def get_content_id(self, torrent_data, content_name=None, duration=None):
        """
        @param string torrent_data - Content of torrent file
        @param string content_name - Name of video, example "My home video" (optional)
        @param integer duration - Duration of video in seconds (optional)
        """
        self.torrent_data = base64.encodestring(torrent_data)
        self.content_name = content_name
        self.duration = duration

        if not self._content_id:
            # Request for getting Content ID
            try:
                xml_result = self.send_request("templates/request.xml", params=vars(self))
            except (Exception, ), e:
                raise exceptions.ServerFault(e.message)
            tree = etree.HTML(xml_result)
            statuses = tree.xpath('//response/status')
            if statuses:
                status = statuses[0]
                if status.text == 'accepted':
                    self._content_id = tree.xpath('//response/id/text()')[0]
                else:
                    error = "TorrentStream Error: {0} (Errcode: {1})".format(status.attrib.get('error'), status.attrib.get('errorcode'))
                    raise exceptions.FailedResponse(error)
        return self._content_id

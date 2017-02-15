import config as cfg
import json

from .base import BaseProvider
from http.client import HTTPSConnection


class GoogleProvider(BaseProvider):
    """ Provider to short given link. """

    config = cfg.get('providers.google')
    headers = {'Content-Type': 'application/json'}

    def __init__(self):
        self.connection = HTTPSConnection(self.config['api_host'])
        self.api_url = '{path}?key={key}'.format(
            path=self.config['api_path'],
            key=self.config['api_key']
        )

    def short(self, url):
        """ Make short url from long with goo.gl API. """
        data = json.dumps({'longUrl': url})
        response = self.make_request(data)

        return json.loads(response)['id']

    def make_request(self, data):
        connection = self.connection

        connection.request('POST', self.api_url, data, self.headers)
        response = connection.getresponse()

        return response.read().decode()

import re
import validators

from pyquery import PyQuery
from urllib.error import URLError


class LinkUtils:
    """ Module with helpful utils to manipulate with URL's. """

    @staticmethod
    def detect_media_type(url):
        """ Check if given URL is image or regular page.
        Return None if url is invalid.
        """

        if not validators.url(url):
            return None

        IMAGE_REGEX = re.compile('\.(png|gif|jpg|jpeg)$', re.IGNORECASE)

        if IMAGE_REGEX.search(url):
            return 'image'
        else:
            return 'page'

    @staticmethod
    def fetch_info(url):
        """ Fetch title and description from given URL.
        Return None if URL is invalid.
        """
        try:
            pq = PyQuery(url=url)

            # Get url title
            title = pq('meta[property="og:title"]').attr('content')
            if title is None:
                title = pq('title').text()

            # Get url description
            description = pq('meta[property="og:description"]').attr('content')
            if description is None:
                description = pq('meta[name="description"]').attr('content')

            return (title, description)
        except (URLError, ValueError):
            return None

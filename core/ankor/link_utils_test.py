from .link_utils import LinkUtils


class TestLinkUtils:
    """ Test LinkUtils module. """

    INVALID_URL = 'invalid_url'
    IMAGE_URL = 'http://example.org/logo.png'
    PAGE_URL = 'http://example.org'

    def test_detect_media_type(self):
        """ Test if invalid URL will return None.
        Image URL will return 'image'.
        Page URL will return 'page'.
        """
        assert LinkUtils.detect_media_type(self.INVALID_URL) is None
        assert LinkUtils.detect_media_type(self.IMAGE_URL) is 'image'
        assert LinkUtils.detect_media_type(self.PAGE_URL) is 'page'

    def test_fetch_info(self):
        """ Test if invalid URL will return None.
        Page URL will return ('Example Domain', None).
        """
        assert LinkUtils.fetch_info(self.INVALID_URL) is None
        assert LinkUtils.fetch_info(self.PAGE_URL) == {
            'title': 'Example Domain',
            'description': None,
        }

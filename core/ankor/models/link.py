from .base import BaseModel
from ..link_utils import LinkUtils


class Link(BaseModel):
    """ Link model. """

    """ DB fields for link:
    id -- integer primary key autoincrement
    url -- string(255)
    title -- string(100)
    description -- string(255)
    media_type -- string(20), values: page/image
    short_url -- string(30)
    created_at -- timestamp
    updated_at -- timestamp
    """
    def __init__(self, **kwargs):
        """ Create new link and assign default values. """
        super().__init__(**kwargs)

        # Detect url media type
        self.media_type = LinkUtils.detect_media_type(kwargs['url'])

        # Fetch information about link from url if it is page
        if self.media_type == 'page':
            link_info = LinkUtils.fetch_info(kwargs['url'])

            self.title = link_info['title']
            self.description = link_info['description']

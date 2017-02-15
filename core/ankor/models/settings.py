from .base import BaseModel


class Settings(BaseModel):
    """ Representation of user settings for Ankor app. """

    """ DB fields for settings:
    id -- integer primary key autoincrement
    listen_clipboard -- NUMERIC(1) NOT NULL DEFAULT 1,
    start_at_login -- NUMERIC(1) NOT NULL DEFAULT 0,
    short_all_links -- NUMERIC(1) NOT NULL DEFAULT 0,
    api_provider -- TEXT(20) NOT NULL DEFAULT 'google'
    """

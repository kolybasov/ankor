from importlib import import_module
from inflection import camelize


class Shortener:
    """ Factory for available shorteners api. """

    def __init__(self, url, provider='google'):
        self.full_url = url
        self.short_url = None

        provider_name = camelize('{}_provider'.format(provider))
        providers_module = import_module('ankor.providers')
        provider_class = getattr(providers_module, provider_name)

        self.provider = provider_class()

    def short(self):
        """ Short full url and asign it to short url property. """
        if self.short_url is None:
            short_url = self.provider.short(self.full_url)
            self.short_url = short_url

        return self.short_url

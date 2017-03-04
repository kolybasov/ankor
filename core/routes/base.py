from flask import request
from abc import ABC


class BaseRoute(ABC):
    def __init__(self, env):
        self.env = env

    def call(self, *args, **kwargs):
        handler = self.__handler__(request.method)

        if type(handler) is dict:
            method = 'index' if len(kwargs) == 0 else 'show'
            print(method)
            handler = handler[method]

        return handler(*args, **kwargs)

    def __handler__(self, method):
        if getattr(self, '__handlers_cache__', None) is None:
            setattr(self, '__handlers_cache__', {
                'GET': {
                    'index': getattr(self, 'index', None),
                    'show': getattr(self, 'show', None)
                },
                'POST': getattr(self, 'create', None),
                'PUT': getattr(self, 'update', None),
                'DELETE': getattr(self, 'destroy', None)
            })

        return self.__handlers_cache__[method]

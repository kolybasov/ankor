from .settings import Settings
from .link import Link

models = [
    Settings,
    Link,
]


def setup(db):
    for model in models:
        model.__setup__(db)


__all__ = ['setup'] + [model.__name__ for model in models]

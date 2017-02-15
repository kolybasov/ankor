from .base import BaseProvider
from pytest import raises


class TestBaseProvider:
    def test_short(self):
        with raises(TypeError):
            BaseProvider()

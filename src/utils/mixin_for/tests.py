import unittest

from .base import mixin_for


class MixinForTest(unittest.TestCase):
    def test_return_object(self) -> None:
        print('hi')
        self.assertEqual(mixin_for(1), 1)

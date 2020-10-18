import unittest

from model.input_modify import get_isbn


class TestDummy(unittest.TestCase):
    def test_setting_environment(self):
        self.assertEqual(1, 1, 'environment not set up')

    def test_get_isbn(self):
        title = 'The Fellowship of the Ring'
        output = get_isbn(title)

        self.assertEqual('0345339703', output)

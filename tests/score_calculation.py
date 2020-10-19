import unittest
import pandas as pd

from model.score_calculation import same_author_score


class TestDummy(unittest.TestCase):
    def test_setting_environment(self):
        self.assertEqual(1, 1, 'environment not set up')

    def test_same_author_score(self):
        author = 'J.R.R.Tolkien'
        book = pd.DataFrame({"author": 'J.R.R.Tolkien'}, index=[1])
        output = same_author_score(book, author)

        self.assertEqual(1, output, 'author score not correct')

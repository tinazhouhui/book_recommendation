import unittest
import pandas as pd

from model.score_calculation import same_author_score, similar_title_score, same_language_score


class TestDummy(unittest.TestCase):
    def test_setting_environment(self):
        self.assertEqual(1, 1, 'environment not set up')

    def test_same_author_score(self):
        author = 'J.R.R.Tolkien'
        book = pd.DataFrame({"author": 'J.R.R.Tolkien'}, index=[1])
        output = same_author_score(book, author)

        self.assertEqual(1, output, 'author score not correct')

    def test_similar_title_score(self):
        title = 'Lord of the Rings, Part 1'
        book = pd.DataFrame({"title": 'Lord of the Rings, Part 2'}, index=[1])
        output = similar_title_score(book, title)

        self.assertEqual(0.96, output, 'title score not correct')

    def test_same_language_score(self):
        isbn = '6543413545'
        book = pd.DataFrame({"ISBN": '6533471097'}, index=[1])
        output = same_language_score(book, isbn)

        self.assertEqual(1, output, 'language score not correct')

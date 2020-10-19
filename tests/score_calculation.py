import unittest
import pandas as pd

from model.score_calculation import same_author_score, similar_title_score, same_language_score, \
    similar_rating_score


class TestDummy(unittest.TestCase):
    def test_setting_environment(self):
        self.assertEqual(1, 1, 'environment not set up')

    def test_same_author_score(self):
        author = 'J.R.R.Tolkien'
        author_to_score = 'J.R.R.Tolkien'
        output = same_author_score(author_to_score, author)

        self.assertEqual(1, output, 'author score not correct')

    def test_similar_title_score(self):
        title = 'Lord of the Rings, Part 1'
        title_to_score = 'Lord of the Rings, Part 2'
        output = similar_title_score(title_to_score, title)

        self.assertEqual(0.96, output, 'title score not correct')

    def test_same_language_score(self):
        isbn = '6543413545'
        isbn_to_score = '6533471097'
        output = same_language_score(isbn_to_score, isbn)

        self.assertEqual(1, output, 'language score not correct')

    def test_similar_rating_score(self):
        rating_to_score = 3.4
        rating = 3.4
        output = similar_rating_score(rating_to_score, rating)

        self.assertEqual(1, output, 'similar rating not correct')

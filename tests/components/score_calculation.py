import unittest

from app.model.entities.book import Book

input_book = Book(
    isbn='6543413545',
    title='Lord of the Rings, Part 1',
    author='J. R. R.Tolkien',
    rating_average=3.4,
    rating_count=68,
)

book_to_compare = Book(
    isbn='6533471097',
    title='Lord of the Rings',
    author='J.R.R.Tolkien',
    rating_average=3.4,
    rating_count=95,
    popularity_relative=0.698468463,
    st_dev=2.871345,
    input_book=input_book,

)

class TestScoreCalculation(unittest.TestCase):
    def test_same_author_score(self):
        self.assertEqual(1, book_to_compare.same_author_score, 'author score not correct')

    def test_similar_title_score(self):
        self.assertEqual(0.8095, book_to_compare.similar_title_score, 'title score not correct')

    def test_same_language_score(self):
        self.assertEqual(1, book_to_compare.same_lang_score, 'language score not correct')

    def test_similar_rating_score(self):
        self.assertEqual(1, book_to_compare.rating_relative_score, 'similar rating not correct')

    def test_relative_popularity_score(self):
        self.assertEqual(0.6985, book_to_compare.popularity_relative_score, 'relative popularity not correct')

    def test_st_dev_score(self):
        self.assertEqual(0.8405, book_to_compare.st_dev_score, 'stdev not correct')

    def test_final_score(self):
        self.assertEqual(0.7277750000000001, book_to_compare.final_score, 'final score not correct')
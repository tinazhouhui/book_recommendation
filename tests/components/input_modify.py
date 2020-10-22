import unittest


# books_popularity = pd.read_csv("../../data/input/books_popularity.csv", encoding='utf-8')
# books = pd.read_csv("../../data/input/books.csv", encoding='utf-8')


class TestDummy(unittest.TestCase):

    def test_setting_environment(self):
        self.assertEqual(1, 1, 'environment not set up')

    # def test_get_book_info(self):
    #     title = 'The Fellowship of the Ring'
    #     output = get_book_info(books_popularity, title)
    #
    #     self.assertEqual('0345339703', output.ISBN)

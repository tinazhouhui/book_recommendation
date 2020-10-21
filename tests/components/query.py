import unittest

from app.components.query import main_query


class TestDummy(unittest.TestCase):
    def test_setting_environment(self):
        self.assertEqual(1, 1, 'environment not set up')

    def test_main_query(self):
        actual = main_query('0345339703')
        expected = "select final_index.*, similar.relative_popularity from final_index left join (select isbn, count*average/ (select max(relative_popularity) from (select isbn, count*average as relative_popularity from (select isbn, count(isbn) as count, avg(ratings) as average from ratings_cleaned where user_id in (select user_id from ratings_cleaned where isbn = '0345339703' and ratings > 8) group by isbn))) as relative_popularity from (select isbn, count(isbn) as count, avg(ratings) as average from ratings_cleaned where user_id in (select user_id from ratings_cleaned where isbn = '0345339703' and ratings > 8) group by isbn)) as similar on final_index.isbn = similar.isbn order by similar.relative_popularity desc;"

        self.assertEqual(actual, expected, 'query not correct')

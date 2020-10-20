import pandas as pd
import sys

from model.input_modify import convert_to_utf, get_book_info
from model.score_calculation import same_language_score, same_author_score, similar_rating_score, \
    similar_title_score
# path_book_popularity = './input/books.csv'
# convert_to_utf(path_book_popularity)


# read csv and transfer to pandas dataframe
books = pd.read_csv("input/books.csv", encoding='utf-8')
books_popularity = pd.read_csv("input/books_popularity.csv", encoding='utf-8')

# get book title from argument
book_title = str(sys.argv[1])
book = get_book_info(books_popularity, book_title)


def add_score(row):

    outcome = {
        'title': row.title,
        'lang_score': same_language_score(str(row.ISBN), book.ISBN),
        'author_score': same_author_score(str(row.author), book.author),
        'title_score': similar_title_score(str(row.title), book.title),
    }

    return pd.Series(outcome)


result = books.apply(add_score, axis=1)

print(result)


# TODO: Left join??
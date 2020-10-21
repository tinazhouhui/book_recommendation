import pandas as pd
import sys

from components.database import Database
from app.model.input_modify import get_book_info
from app.model.score_calculation import same_language_score, same_author_score, similar_title_score
from sqlalchemy.ext.declarative import declarative_base

# convert csv to correct encoding
# path_book_popularity = './input/books.csv'
# convert_to_utf(path_book_popularity)


engine = Database.get_engine()
Base = declarative_base()



# read csv and transfer to pandas dataframe
books = pd.read_csv("data/input/books.csv", encoding='utf-8')
books_popularity = pd.read_csv("data/input/books_popularity.csv", encoding='utf-8')

# get book title from argument
book_title = str(sys.argv[1])
book = get_book_info(books_popularity, book_title)
print(book)


def add_score(row):

    outcome = {
        'title': row.title,
        'lang_score': same_language_score(str(row.ISBN), book.ISBN),
        'author_score': same_author_score(str(row.author), book.author),
        'title_score': similar_title_score(str(row.title), book.title),  # TODO: dalsi funkce
    }

    return pd.Series(outcome)


result = books.apply(add_score, axis=1)

print(result)

# TODO: SQL Alchemy rozchodit
# TODO: vytvorit master tabulku left join books a index - fill blanks with none
# TODO: Execute spravne select - nechceme publisher, pouze ty sloupecky co chceme
# TODO: covnert sql answer to pandas dataframe
# TODO: zbyle dve funkce dopocitat - standard deviation a ostatnim se take libilo

import pandas as pd

from model.input_modify import convert_to_utf

path_book_popularity = './input/books_popularity.csv'
convert_to_utf(path_book_popularity)

books_popularity = pd.read_csv("input/books_popularity.csv", encoding='utf-8')

print(books_popularity.columns)

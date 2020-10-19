import pandas as pd


def convert_to_utf(path):
    data = pd.read_csv(path, encoding='latin-1')
    data.to_csv(path, encoding='utf-8', index=False)


def get_book_info(books: object, book_title: str) -> object:
    """Takes the exact name of the book title and gives back the most popular ISBN"""

    books_with_same_title = books[books['title'].str.contains(book_title)]
    sorted_by_popularity = books_with_same_title.sort_values(by=['popularity'], ascending=False)

    return sorted_by_popularity.iloc[0]

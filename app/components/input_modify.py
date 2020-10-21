import pandas as pd

#
# def get_book_info(books: pd.DataFrame, book_title: str) -> pd.DataFrame:
#     """Takes the exact name of the book title and gives back the most popular ISBN"""
#
#     books_with_same_title = books[books['title'].str.contains(book_title)]
#     sorted_by_popularity = books_with_same_title.sort_values(by=['popularity'], ascending=False)
#
#     return sorted_by_popularity.iloc[0]

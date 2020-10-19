"""
All functions necessary to calculate the score of individual books.
"""
from difflib import SequenceMatcher


def same_author_score(book: object, author: str) -> float:
    """
    Scores the authors based on how similar they are
    :param book: dataframe containing the book info
    :param author: the author from input book
    :return: float between 0 and 1 establishing how similar the two are
    """
    author_to_score = book.author.iloc[0]

    # doc: https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher
    similarity = SequenceMatcher(lambda x: x == " ", author_to_score, author)

    return similarity.quick_ratio()


def similar_title_score(book: object, title: str) -> float:
    """
    Scores the titles based on how similar they are
    :param book: dataframe containing the book info
    :param title: the title from input book
    :return: float between 0 and 1 establishing how similar the two are
    """
    title_to_score = book.title.iloc[0]

    similarity = SequenceMatcher(lambda x: x == " ", title_to_score, title)
    return similarity.quick_ratio()

import pandas as pd
from difflib import SequenceMatcher


def same_author_score(book: object, author: str):
    author_to_score = book.author.iloc[0]

    # doc: https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher
    output = SequenceMatcher(lambda x: x == " ", author_to_score, author)

    return output.quick_ratio()

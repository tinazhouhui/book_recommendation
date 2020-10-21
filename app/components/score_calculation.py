"""
All functions necessary to calculate the score of individual books.
"""
from difflib import SequenceMatcher


def same_author_score(author_to_score: str, author: str) -> float:

    """
    Scores the authors based on how similar they are
    :param author_to_score: author from dataframe that we compare input to
    :param author: the author from input book
    :return: float between 0 and 1 establishing how similar the two are
    """
    # doc: https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher
    similarity = SequenceMatcher(lambda x: x == " ", author_to_score, author)

    return similarity.quick_ratio()


def similar_title_score(title_to_score: str, title: str) -> float:

    """
    Scores the titles based on how similar they are
    :param title_to_score: title from dataframe that we compare input to
    :param title: the title from input book
    :return: float between 0 and 1 establishing how similar the two are
    """

    similarity = SequenceMatcher(lambda x: x == " ", title_to_score, title)
    return similarity.quick_ratio()


def define_region(isbn: str) -> str:
    """
    Function to parse isbn and extract the region from it
    :param isbn: book isbn
    :return: region in number format
    """
    if isbn[0] in ['0', '1', '2', '4', '5', '7']:
        return isbn[0]
    elif isbn[0] == '6':
        if 60 <= int(isbn[0:2]) < 65:
            return isbn[0:3]
        elif int(isbn[0:2]) == 65:
            return isbn[0:2]
        else:
            return '6'
    elif isbn[0] in ['8', '9']:
        if 80 <= int(isbn[0:2]) <= 94:
            return isbn[0:2]
        elif 95 <= int(isbn[0:2]) <= 98:
            return isbn[0:3]
        else:
            if 990 <= int(isbn[0:3]) <= 998:
                return isbn[0:4]
            else:
                return isbn[0:4]
    else:
        return '99999'


def same_language_score(isbn_to_score: str, isbn: str) -> float:
    """
    Scores each book based on language/region of the book
    :param isbn_to_score: isbn from dataframe that we compare input to
    :param isbn: the isbn from input book
    :return: float between 0 and 1 establishing how similar the two are
    """

    region_to_score = define_region(isbn_to_score)
    region = define_region(isbn)

    if len(region_to_score) == len(region):
        if region_to_score == region:
            output = 1
        elif region_to_score == '0' and region == '1':
            output = 1
        elif region_to_score == '1' and region == '0':
            output = 1
        else:
            output = 0
    else:
        output = 0

    return output


def similar_rating_score(rating_to_score: float, rating: float) -> float:
    """
    Measures distance of ratings from input book rating and represents a score
    :param rating_to_score: rating from dataframe that we compare input to
    :param rating: the rating from input book
    :return: float between 0 and 1 establishing how similar the two are
    """
    distance = abs(rating_to_score - rating)

    return 1 - (distance / 10)


def relative_popularity_score(popularity_score: float):

    if popularity_score:
        return popularity_score
    else:
        return 0


def st_dev_score(avg_sq: float):
    return 1 - avg_sq/18  # 18 is max possible st deviation^2, reverse cause the higher the worse


def compute_score(row, book):

    same_lang = same_language_score(row[0], book[0])
    same_author = same_author_score(row[2], book[2])
    similar_title = similar_title_score(row[1], book[1])
    rating_relative = similar_rating_score(row[4], book[4])
    popularity_overall = float(row[6]) / 10
    popularity_relative = relative_popularity_score(row[8])
    st_dev = st_dev_score(row[7])

    final_score = same_lang + same_author + similar_title + rating_relative + popularity_overall + popularity_relative + st_dev

    outcome = (row[0], row[1], same_lang, same_author, similar_title, rating_relative, popularity_overall, popularity_relative, st_dev, final_score)

    return outcome

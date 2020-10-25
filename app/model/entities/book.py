from difflib import SequenceMatcher

from sqlalchemy import Column, Integer, String, Float

from app.model.entities.base import Base


class Book(Base):
    """
    definition of columns in books table.
    """
    __tablename__ = 'book'
    isbn = Column(String, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    st_dev = Column(Float, nullable=True)
    rating_average = Column(Float, nullable=True)
    rating_count = Column(Integer, nullable=True)
    popularity_overall = Column(Float, nullable=True)
    popularity_relative = Column(Float, nullable=True)
    same_lang_score = Column(Float, nullable=True)
    same_author_score = Column(Float, nullable=True)
    similar_title_score = Column(Float, nullable=True)
    rating_relative_score = Column(Float, nullable=True)
    popularity_overall_score = Column(Float, nullable=True)
    popularity_relative_score = Column(Float, nullable=True)
    st_dev_score = Column(Float, nullable=True)
    final_score = Column(Float, nullable=True)

    def __init__(self, isbn: str, title: str, author: str, st_dev: float = 0,
                 rating_average: float = 0, rating_count: int = 0, popularity_overall: float = 0,
                 popularity_relative: float = 0, input_book=None):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.st_dev = st_dev
        self.rating_average = rating_average
        self.rating_count = rating_count
        self.popularity_overall = popularity_overall
        self.popularity_relative = popularity_relative
        if input_book:
            self.same_author_score = self.compute_same_author_score(input_book.author)
            self.similar_title_score = self.compute_similar_title_score(input_book.title)
            self.same_lang_score = self.compute_same_language_score(input_book.isbn)
            self.rating_relative_score = self.compute_similar_rating_score(
                input_book.rating_average)
            self.popularity_overall_score = round(float(popularity_overall) / 10, 4)
            self.popularity_relative_score = self.compute_relative_popularity_score()
            self.st_dev_score = self.compute_st_dev_score()
            self.final_score = self.compute_final_score()

    def compute_same_author_score(self, author: str) -> float:
        """
        Scores the authors based on how similar they are
        :param author: the author from input book
        :return: float between 0 and 1 establishing how similar the two are
        """
        # doc: https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher
        similarity = SequenceMatcher(lambda x: x == " ", self.author, author).quick_ratio()
        if similarity >= 0.9:
            return 1
        else:
            return 0

    def compute_similar_title_score(self, input_title: str) -> float:
        """
        Scores the titles based on how similar they are
        :param input_title: the title from input book
        :return: float between 0 and 1 establishing how similar the two are
        """

        similarity = SequenceMatcher(lambda x: x == " ", self.title, input_title).quick_ratio()

        if similarity >= 0.9:
            return -10  # take out identical books

        return round(similarity, 4)

    def define_region(self, isbn: str) -> str:
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

    def compute_same_language_score(self, input_isbn: str) -> float:
        """
        Scores each book based on language/region of the book
        :param input_isbn: the isbn from input book
        :return: float between 0 and 1 establishing how similar the two are
        """

        region_to_score = self.define_region(self.isbn)
        region = self.define_region(input_isbn)

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

    def compute_similar_rating_score(self, input_rating: float) -> float:
        """
        Measures distance of ratings from input book rating and represents a score
        :param input_rating: the rating from input book
        :return: float between 0 and 1 establishing how similar the two are
        """
        distance = abs(self.rating_average - input_rating)

        return round(1 - (distance / 10), 4)

    def compute_relative_popularity_score(self):
        """
        Popularity score of books of other readers who also liked the input book
        :return: float or 0 if the book was not rated by others
        """

        if self.popularity_relative:
            return round(self.popularity_relative, 4)
        else:
            return 0

    def compute_st_dev_score(self):
        """
        Scores how controversial the ratings are
        :return: float normalised to be between 0 and 1. Also reversed.
        """
        return 1 - self.st_dev / 18  # 18 is max possible st deviation^2, reverse cause the higher the worse

    def compute_final_score(self) -> float:
        """
        Final score computation of comparing book and based on input book
        :return: final score
        """

        same_lang_weight = 0.05
        same_author_weight = 0.2
        similar_title_weight = 0.15
        rating_relative_weight = 0.4
        popularity_overall_weight = 0.1
        popularity_relative_weight = 0.05
        st_dev_weight = 0.05

        final_score = sum(
            [
                self.same_lang_score * same_lang_weight,
                self.same_author_score * same_author_weight,
                self.similar_title_score * similar_title_weight,
                self.rating_relative_score * rating_relative_weight,
                self.popularity_overall_score * popularity_overall_weight,
                self.popularity_relative_score * popularity_relative_weight,
                self.st_dev_score * st_dev_weight,
            ])

        return final_score

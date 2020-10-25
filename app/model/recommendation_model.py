from app.components.query import main_query, get_book_info_query
from app.model.base import BaseModel
from app.model.entities.book import Book


def view_final_recommendation_list(recommendation_list: list):
    final_view = []

    for book in recommendation_list:
        book = {
            'isbn': book.isbn,
            'title': book.title,
            'same_lang': book.same_lang_score,
            'same_author': book.same_author_score,
            'similar_title': book.similar_title_score,
            'rating_relative': book.rating_relative_score,
            'popularity_overall': book.popularity_overall_score,
            'popularity_relative': book.popularity_relative_score,
            'st_dev': book.st_dev_score,
            'final_score': book.final_score,
        }

        final_view.append(book)

    return final_view


class RecommendationModel(BaseModel):

    def get_final_index(self, isbn: str, input_book: Book):
        query = main_query()
        output = self.db_session.execute(query, {"isbn": isbn})
        books_to_rank = output.fetchall()
        self.db_session.close()

        book_entities = []

        # f.ISBN, f.title, f.author, f.language, f.average, f.count, f.popularity, f.avg_sq, similar.relative_popularity

        for book in books_to_rank:
            book = Book(
                isbn=book[0],
                title=book[1],
                author=book[2],
                rating_average=book[3],
                rating_count=book[4],
                popularity_overall=book[5],
                st_dev=book[6],
                popularity_relative=book[7],
                input_book=input_book,
            )

            book_entities.append(book)

        recommendation_list_sorted_all = sorted(book_entities,
                                                key=lambda book_entity: book_entity.final_score,
                                                reverse=True)

        return recommendation_list_sorted_all[:11]

    def get_input_book_info(self, title: str):
        query = get_book_info_query()
        output = self.db_session.execute(query, {"title": '%' + title + '%'})
        result = output.fetchone()
        self.db_session.close()

        # f.ISBN, f.title, f.author, f.average, f.count

        book = Book(
            isbn=result[0],
            title=result[1],
            author=result[2],
            rating_average=result[3],
            rating_count=result[4],
        )

        return book

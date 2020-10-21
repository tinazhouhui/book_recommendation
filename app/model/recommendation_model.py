from app.components.query import main_query, get_book_info_query
from app.components.score_calculation import same_language_score, same_author_score, \
    similar_title_score, similar_rating_score, relative_popularity_score, st_dev_score
from app.model.base import BaseModel
import pandas as pd


class RecommendationModel(BaseModel):

    def get_final_index(self, isbn: str):
        query = main_query(isbn) # todo fix injection
        output = self.db_session.execute(query)
        result = output.fetchall()
        self.db_session.close()

        return result

    def get_input_book_info(self, title: str):
        query = get_book_info_query(title)
        output = self.db_session.execute(query)
        result = output.fetchone()
        self.db_session.close()

        return result

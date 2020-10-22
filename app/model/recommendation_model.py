from app.components.query import main_query, get_book_info_query
from app.model.base import BaseModel


class RecommendationModel(BaseModel):

    def get_final_index(self, isbn: str):
        query = main_query()
        output = self.db_session.execute(query, {"isbn": isbn})
        result = output.fetchall()
        self.db_session.close()

        return result

    def get_input_book_info(self, title: str):
        query = get_book_info_query()
        output = self.db_session.execute(query, {"title": '%' + title + '%'})
        result = output.fetchone()
        self.db_session.close()

        return result

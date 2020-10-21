from app.components.query import main_query
from app.components.score_calculation import same_language_score, same_author_score, \
    similar_title_score
from app.model.base import BaseModel
import pandas as pd


class RecommendationModel(BaseModel):

    def check_sql_connection(self):
        """
        passes raw query straight to database to check
        """
        output = self.db_session.execute('SELECT 1+1')
        result = output.fetchone()[0]
        self.db_session.close()
        print('output')
        print(output)
        return result


    def get_final_index(self, isbn):
        query = main_query(isbn) # todo fix injection
        print(query)
        output = self.db_session.execute(query)
        result = output.fetchall()
        self.db_session.close()

        return result

    def add_score(self, row, book):
        outcome = {
            'title': row.title,
            'lang_score': same_language_score(str(row.ISBN), book.ISBN),
            'author_score': same_author_score(str(row.author), book.author),
            'title_score': similar_title_score(str(row.title), book.title),  # TODO: dalsi funkce
        }

        return pd.Series(outcome)
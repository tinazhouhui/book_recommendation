from app.components.score_calculation import same_language_score, same_author_score, \
    similar_title_score
from app.model.base import BaseModel
import pandas as pd


class RecommendationModel(BaseModel):
    def add_score(self, row, book):
        outcome = {
            'title': row.title,
            'lang_score': same_language_score(str(row.ISBN), book.ISBN),
            'author_score': same_author_score(str(row.author), book.author),
            'title_score': similar_title_score(str(row.title), book.title),  # TODO: dalsi funkce
        }

        return pd.Series(outcome)
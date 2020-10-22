from app.components.score_calculation import compute_score
from app.controller.base import BaseController
from flask import make_response, jsonify, request


class RecommendationController(BaseController):
    def get(self):

        title = request.args.get('title')

        if not title:
            return make_response(jsonify({"message": "No title provided"}), 400)
        input_book_info = self.model.get_input_book_info(title)

        isbn = input_book_info[0]  # '0345339703'

        final_scores = []

        rows_to_compare = self.model.get_final_index(isbn)
        for row in rows_to_compare:

            computed_score = compute_score(row, input_book_info)
            row_score = {
                'isbn': computed_score[0],
                'title': computed_score[1],
                'same_lang': computed_score[2],
                'same_author': computed_score[3],
                'similar_title': computed_score[4],
                'rating_relative': computed_score[5],
                'popularity_overall': computed_score[6],
                'popularity_relative': computed_score[7],
                'st_dev': computed_score[8],
                'final_score': computed_score[9],
            }

            final_scores.append(row_score)

        final_recommendation_list = sorted(final_scores, key=lambda i: i['final_score'], reverse=True)

        return make_response(jsonify(final_recommendation_list[1:11]), 200)

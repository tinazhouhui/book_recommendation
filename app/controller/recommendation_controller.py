from app.components.score_calculation import compute_score
from app.controller.base import BaseController
from flask import make_response, jsonify, request


class RecommendationController(BaseController):
    def get(self):

        title = request.args.get('title')
        input_book_info = self.model.get_input_book_info(title)

        isbn = input_book_info[0]  # '0345339703'

        row_to_compare = self.model.get_final_index(isbn)
        final = compute_score(row_to_compare, input_book_info)

        print(final)

        return make_response('book recommendation link', 200)

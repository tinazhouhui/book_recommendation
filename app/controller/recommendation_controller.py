from app.controller.base import BaseController
from flask import make_response, jsonify, request

from app.model.recommendation_model import view_final_recommendation_list


class RecommendationController(BaseController):
    def get(self):

        title = request.args.get('title')

        if not title:
            return make_response(jsonify({"message": "No title provided"}), 400)

        input_book = self.model.get_input_book_info(title)

        if not input_book:
            return make_response(jsonify({"message": "Title does not exist in database"}), 400)

        isbn = input_book.isbn  # '0345339703'

        recommendation_list = self.model.get_final_index(isbn, input_book)
        final_view = view_final_recommendation_list(recommendation_list)

        return make_response(jsonify(final_view), 200)

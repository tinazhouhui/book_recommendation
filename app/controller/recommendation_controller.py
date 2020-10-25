from app.controller.base import BaseController
from flask import make_response, jsonify, request
from time import perf_counter

from app.model.recommendation_model import view_final_recommendation_list


class RecommendationController(BaseController):
    def get(self):
        start = perf_counter()

        title = request.args.get('title')
        time_title = perf_counter() - start

        if not title:
            return make_response(jsonify({"message": "No title provided"}), 400)

        input_book = self.model.get_input_book_info(title)

        if not input_book:
            return make_response(jsonify({"message": "Title does not exist in database"}), 400)

        isbn = input_book.isbn  # '0345339703'
        time_input = perf_counter() - start - time_title

        recommendation_list = self.model.get_final_index(isbn, input_book)
        time_list = perf_counter() - start - time_input

        final_view = view_final_recommendation_list(recommendation_list)
        time_view = perf_counter() - start - time_list

        performance = {
            '1 to get title': time_title,
            '2 to get input': time_input,
            '3 to get list': time_list,
            '4 to get view': time_view,
        }

        return make_response(jsonify(performance, final_view), 200)

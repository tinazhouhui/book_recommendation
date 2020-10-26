from app.controller.base import BaseController
from flask import make_response, jsonify, request
from time import perf_counter

from app.model.recommendation_model import view_final_recommendation_list


class RecommendationController(BaseController):
    """
    Controller, GET method, orchestrating data input/output.
    Performance timing.
    """
    def get(self):
        start = perf_counter()

        # Receive input title
        title = request.args.get('title')
        time_title = perf_counter() - start

        # Validation
        if not title:
            return make_response(jsonify({"message": "No title provided"}), 400)

        input_book = self.model.get_input_book_info(title)

        if not input_book:
            return make_response(jsonify({"message": "Title does not exist in database"}), 400)

        time_input = perf_counter() - start - time_title

        # Get recommendation list
        recommendation_list = self.model.get_final_index(input_book)
        time_list = perf_counter() - start - time_input

        # Convert list to nice view
        final_view = view_final_recommendation_list(recommendation_list)
        time_view = perf_counter() - start - time_list

        # Performance indicators
        performance = {
            '1 to get title': time_title,
            '2 to get input': time_input,
            '3 to get list': time_list,
            '4 to get view': time_view,
        }

        return make_response(jsonify(performance, final_view), 200)

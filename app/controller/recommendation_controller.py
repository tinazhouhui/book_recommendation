from app.controller.base import BaseController
from flask import make_response, jsonify, request


class RecommendationController(BaseController):
    def get(self):

        title = request.args.get('title')

        if not title:
            return make_response(jsonify({"message": "No title provided"}), 400)

        input_book = self.model.get_input_book_info(title)

        if not input_book:
            return make_response(jsonify({"message": "Title does not exist in database"}), 400)

        isbn = input_book.isbn  # '0345339703'

        final_scores = []

        rows_to_compare = self.model.get_final_index(isbn, input_book)
        for row in rows_to_compare:
            row_score = {
                'isbn': row.isbn,
                'title': row.title,
                'same_lang': row.same_lang_score,
                'same_author': row.same_author_score,
                'similar_title': row.similar_title_score,
                'rating_relative': row.rating_relative_score,
                'popularity_overall': row.popularity_overall_score,
                'popularity_relative': row.popularity_relative_score,
                'st_dev': row.st_dev_score,
                'final_score': row.final_score,
            }

            final_scores.append(row_score)

        final_recommendation_list = sorted(final_scores, key=lambda i: i['final_score'], reverse=True)

        return make_response(jsonify(final_recommendation_list[0:10]), 200)

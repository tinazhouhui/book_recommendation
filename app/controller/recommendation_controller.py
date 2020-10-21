from app.controller.base import BaseController
from flask import make_response, jsonify


class RecommendationController(BaseController):
    def get(self):
        isbn = '0345339703'
        output = self.model.get_final_index(isbn)
        print(output)

        return make_response('book recommendation link', 200)

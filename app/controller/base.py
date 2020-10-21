"""
The purpose of base controller is that all other controllers can inherit from. This is
good if we want to pass certain data to all the controllers.
Also apply MethodView of flask to allow for easier routing - passing function to add rule.
"""
from flask import request, make_response
from flask.views import MethodView

from app.model import recommendation_model


class BaseController(MethodView):
    """
    The purpose of base controller is that all other controllers can inherit from. This is
    good if we want to pass certain data to all the controllers.
    Also apply MethodView of flask to allow for easier routing - passing function to add rule.
    """

    def __init__(self, model: recommendation_model):
        self.model = model

    def get(self):
        """
        making sure that any controller has at least some return
        """
        return "implement me!"

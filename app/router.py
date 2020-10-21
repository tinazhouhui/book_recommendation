from sqlalchemy.orm import sessionmaker

from app.components.database import Database
from app.controller.recommendation_controller import RecommendationController
from app.model.recommendation_model import RecommendationModel


class Router:
    def __init__(self, app):
        engine = Database().get_engine()
        Session = sessionmaker(bind=engine)
        session = Session()

        recommendation_model = RecommendationModel(session)

        app.add_url_rule(
            "/",
            view_func=RecommendationController.as_view(
                'recommendation',
                model=recommendation_model,
            ),
        )

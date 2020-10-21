"""
Base model, as model is the only way to connect to the database, we are passing in the db session.
"""


class BaseModel:
    """
    Base model, provides methods across all models.
    """
    def __init__(self, db_session):
        """
        constructor, passing in the db session in router as dependency.
        """
        self.db_session = db_session

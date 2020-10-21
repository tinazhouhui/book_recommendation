from sqlalchemy import create_engine


class Database:
    def __init__(self):
        self.engine = create_engine('sqlite:///database/books.db', echo=True)

    def get_engine(self):
        return self.engine

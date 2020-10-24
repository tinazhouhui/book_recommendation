from sqlalchemy import Column, Integer, String, Float

from app.model.entities.base import Base


class Book(Base):
    """
    definition of columns in books table.
    """
    __tablename__ = 'book'
    isbn = Column(String, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    language = Column(String, nullable=False)
    st_dev = Column(Float, nullable=True)
    rating_average = Column(Float, nullable=True)
    rating_count = Column(Integer, nullable=True)
    popularity_overall = Column(Float, nullable=True)
    popularity_relative = Column(Float, nullable=True)


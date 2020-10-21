from sqlalchemy import Column, Integer, String, Float, ForeignKey

from app.model.entities.base import Base


class Ratings(Base):
    """
    definition of columns in ratings table.
    """
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    isbn = Column(String, ForeignKey('isbn'), nullable=False, name='isbn')
    rating = Column(Float, nullable=False)
    rating_count = Column(Integer, nullable=True)
    popularity_overall = Column(Float, nullable=True)



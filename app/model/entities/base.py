"""
Base controller for tables, passing in declarative base to allow table creation with sqlalchemy.
"""

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

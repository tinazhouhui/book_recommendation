"""
starting the app, passing app to router to create routes.
"""

from flask import Flask
from app.router import Router

app = Flask(__name__)

Router(app)


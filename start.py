"""
starting the app, passing app to router to create routes.
"""

from flask import Flask
from app.router import Router

app = Flask(__name__)

Router(app)

if __name__ == "__main__":
    app.run(debug=True, threaded=False, processes=1)


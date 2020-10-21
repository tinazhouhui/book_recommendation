"""
starting the app, passing app to router to create routes.
"""

from flask import Flask
from app.router import Router

app = Flask(__name__)

Router(app)

# TODO: SQL Alchemy rozchodit
# TODO: vytvorit master tabulku left join books a index - fill blanks with none
# TODO: Execute spravne select - nechceme publisher, pouze ty sloupecky co chceme
# TODO: covnert sql answer to pandas dataframe
# TODO: zbyle dve funkce dopocitat - standard deviation a ostatnim se take libilo

from flask import Flask
from gallery.config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

import gallery.models
import gallery.views

db.create_all()

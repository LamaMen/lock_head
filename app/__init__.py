import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.logger.setLevel(logging.INFO)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

from views import views
from views import devices_views
from views import admin_views

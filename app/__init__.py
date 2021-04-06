from flask import Flask

app = Flask(__name__)

from app.views import views
from app.views import debug_views
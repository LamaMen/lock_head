from flask import Flask

app = Flask(__name__)

from views import views
# from views import debug_views
from views import devices_views
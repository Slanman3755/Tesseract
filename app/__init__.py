from flask import Flask
from flask_sitemap import Sitemap

# Initialize the app
app = Flask(__name__, static_folder='static', static_url_path='', instance_relative_config=True)
ext = Sitemap(app=app)

# Load the views
from app import views

# Load the config file
app.config.from_object('config')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_wtf import CSRFProtect
from .config import Config
 
app = Flask(__name__)
 
app.config.from_object(Config)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lab5_user:Password123@localhost:5432/lab5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
# Points to an 'uploads' folder sitting outside the app package,
# i.e. at the project root level (alongside the app/ directory)
app.config['UPLOAD_FOLDER'] = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'uploads'
)
 
# Ensures the uploads folder exists on startup
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
 
csrf = CSRFProtect(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
 
from app import views
 
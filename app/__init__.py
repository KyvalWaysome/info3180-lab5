from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_wtf import CSRFProtect
from .config import Config

app = Flask(__name__)
print(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:lab5@localhost/lab5'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Creates an 'uploads' folder in the same directory as your app
#app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')

# Ensures the uploads folder exists
#if not os.path.exists(app.config['UPLOAD_FOLDER']):
    #os.makedirs(app.config['UPLOAD_FOLDER'])

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config.from_object(Config)
csrf = CSRFProtect(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views


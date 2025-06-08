from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from flask_pymongo import PyMongo

db = SQLAlchemy()
mongo = PyMongo()
login_manager = LoginManager()
cors = CORS()

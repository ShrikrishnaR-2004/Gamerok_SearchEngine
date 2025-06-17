from flask_login import LoginManager, login_manager
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


migrate = Migrate()
db = SQLAlchemy()
mongo = PyMongo()
login_manager = LoginManager()
cors = CORS()

from flask import Flask
from app.config import Config
from app.extensions import db, mongo, login_manager, cors

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mongo.init_app(app)
    login_manager.init_app(app)
    cors.init_app(app)

    login_manager.login_view = 'auth.login'

    from app.auth.routes import auth_bp
    from app.main.routes import main_bp
    from app.user.routes import user_bp
    from app.search.text import search_bp
    from app.auth.google_auth import google_bp, handle_google_login

    app.register_blueprint(google_bp, url_prefix="/auth/google")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(search_bp, url_prefix="/search")

    return app

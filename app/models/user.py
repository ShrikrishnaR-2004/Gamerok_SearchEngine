from app.extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.extensions import db

favorites_table = db.Table(
    'favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('game_id', db.Integer, db.ForeignKey('game.id'), primary_key=True)
)

class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    # Optional additional fields
    search_history = db.Column(db.PickleType, default=[])  # Stores list of past queries

    # Relationship to favorite games
    favorites = db.relationship(
        'Game',
        secondary=favorites_table,
        backref=db.backref('liked_by', lazy='dynamic'),
        lazy='dynamic'
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def add_to_history(self, query):
        if self.search_history is None:
            self.search_history = []
        self.search_history.append(query)
        db.session.commit()

    def __repr__(self):
        return f'<User {self.username}>'

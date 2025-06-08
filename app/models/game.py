from app.extensions import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    genre = db.Column(db.String(100))
    platform = db.Column(db.String(100))
    release_date = db.Column(db.String(50))
    rawg_id = db.Column(db.String(100))  # For syncing with RAWG API
    thumbnail_url = db.Column(db.String(300))
    trailer_url = db.Column(db.String(300))

    reviews = db.relationship('Review', backref='game', lazy=True)

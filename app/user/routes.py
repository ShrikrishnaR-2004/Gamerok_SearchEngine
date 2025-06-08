from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.user import user_bp
from app.extensions import db
from app.models.game import Game
from app.models.user import User

@user_bp.route("/profile")
@login_required
def profile():
    favorites = current_user.favorites
    history = current_user.search_history or []
    return render_template("profile.html", user=current_user, favorites=favorites, history=history)

@user_bp.route("/favorite/<int:game_id>")
@login_required
def add_favorite(game_id):
    game = Game.query.get(game_id)
    if game and game not in current_user.favorites:
        current_user.favorites.append(game)
        db.session.commit()
        flash("Added to favorites.")
    return redirect(url_for("main.dashboard"))

@user_bp.route("/unfavorite/<int:game_id>")
@login_required
def remove_favorite(game_id):
    game = Game.query.get(game_id)
    if game and game in current_user.favorites:
        current_user.favorites.remove(game)
        db.session.commit()
        flash("Removed from favorites.")
    return redirect(url_for("user.profile"))

from flask import redirect, url_for, flash
from flask_dance.contrib.google import make_google_blueprint, google
from flask_login import login_user
from app.models.user import User
from app.extensions import db

import os

# Create Google OAuth blueprint
google_bp = make_google_blueprint(
    client_id=os.getenv("GOOGLE_OAUTH_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_OAUTH_CLIENT_SECRET"),
    scope=["profile", "email"],
    redirect_url="/auth/google/authorized"
)

def handle_google_login():
    if not google.authorized:
        return redirect(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    if not resp.ok:
        flash("Failed to fetch user info from Google.", "danger")
        return redirect(url_for("main.index"))

    user_info = resp.json()
    email = user_info["email"]
    username = user_info.get("name", email.split("@")[0])

    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(username=username, email=email)
        user.set_password("google")  # Placeholder; not used for Google accounts
        db.session.add(user)
        db.session.commit()

    login_user(user)
    flash("Logged in successfully with Google!", "success")
    return redirect(url_for("main.dashboard"))

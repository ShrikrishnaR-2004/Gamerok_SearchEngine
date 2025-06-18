from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app.main import main_bp

@main_bp.route("/")
def index():
    return render_template("index.html")
#
@main_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

@main_bp.route("/contact")
def contact():
    return render_template("contact.html")

@main_bp.route("/about")
def about():
    return render_template("about.html")

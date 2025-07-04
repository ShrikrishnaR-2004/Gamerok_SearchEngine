from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from app.auth.forms import LoginForm, RegisterForm
from app.extensions import db
from app.auth import auth_bp

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("main.dashboard"))
        flash("Invalid credentials", "danger")
    return render_template("login.html", form=form)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created!", "success")
        return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)

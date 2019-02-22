from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import AuthForm
from application.submissions.models import Submission

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))    

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index")) 

@app.route("/auth/new/")
def auth_form():
    return render_template("auth/new.html", form = AuthForm())


@app.route("/auth/", methods=["POST"])
def auth_create():
    form = AuthForm(request.form)


    if not form.validate():
        return render_template("auth/new.html", form = form)

    user = User.query.filter_by(username=form.username.data).first()
    if user is None:
        a = User(form.name.data, form.username.data, form.password.data)
  
        db.session().add(a)
        db.session().commit()
  
        return redirect(url_for("auth_login"))
    return render_template("auth/new.html", form = form,
                           errore = "Username " + user.username + " already in use")


@app.route("/auth/view/<account_id>", methods=["GET"])
def auth_view(account_id):
        header = 'Levels by '
        header += User.query.filter_by(id = account_id).first().username
        return render_template("submissions/list.html", submissions = Submission.query.filter_by(account_id = account_id), header = header)
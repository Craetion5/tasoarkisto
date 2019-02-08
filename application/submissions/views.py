from application import app, db
from flask import redirect, render_template, request, url_for
from application.submissions.models import Submission
from application.submissions.forms import SubmissionForm
from application.auth.models import User
from flask_login import login_required, current_user

@app.route("/submissions", methods=["GET"])
def submissions_index():
    return render_template("submissions/list.html", submissions = Submission.query.all())

@app.route("/submissions/new/")
@login_required
def submissions_form():
    return render_template("submissions/new.html", form = SubmissionForm())

@app.route("/submissions/", methods=["POST"])
@login_required
def submissions_create():

    form = SubmissionForm(request.form)

    if not form.validate():
        return render_template("submissions/new.html", form = form)

    t = Submission(form.name.data)
    t.code = form.code.data
    t.description = form.description.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()

    #t = Submission(request.form.get("name"))

    #db.session().add(t)
    #db.session().commit()
  
    return redirect(url_for("submissions_index"))

@app.route("/submissions/level", methods=["GET"])
def submissions_view():
    return render_template("submissions/level.html", submission = Submission.query.first())
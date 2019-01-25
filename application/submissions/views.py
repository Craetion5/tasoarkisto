from application import app, db
from flask import redirect, render_template, request, url_for
from application.submissions.models import Submission

@app.route("/submissions", methods=["GET"])
def submissions_index():
    return render_template("submissions/list.html", submissions = Submission.query.all())

@app.route("/submissions/new/")
def submissions_form():
    return render_template("submissions/new.html")

@app.route("/submissions/", methods=["POST"])
def submissions_create():
    t = Submission(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("submissions_index"))

from flask import render_template
from application import app
from application.submissions.models import Submission
from application.auth.models import User

@app.route("/")
def index():
    return render_template("index.html", lvls = Submission.count_submissions(), usrs = User.count_users())

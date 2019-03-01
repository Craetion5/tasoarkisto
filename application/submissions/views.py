from application import app, db
from flask import redirect, render_template, request, url_for
from application.submissions.models import Submission
from application.comments.models import Comment
from application.submissions.forms import SubmissionForm
from application.comments.forms import CommentForm
from application.auth.models import User
from flask_login import login_required, current_user

# listing all level submissions
@app.route("/submissions", methods=["GET"])
def submissions_index():
    return render_template("submissions/list.html", submissions = Submission.query.all(), header = 'Level submissions')

# listing level submissions featured by forum admins
@app.route("/submissions/featured", methods=["GET"])
def submissions_featured():
    return render_template("submissions/list.html", submissions = Submission.query.filter_by(featured=True), header = 'Featured levels')

# template for creating a submission
@app.route("/submissions/new/")
@login_required
def submissions_form():
    return render_template("submissions/new.html", form = SubmissionForm())

# functionality for creating a submission
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
  
    return redirect(url_for("submissions_index"))

# viewing information of a single level submission
@app.route("/submissions/level/<submission_id>", methods=["GET"])
def submissions_view(submission_id):
    s = Submission.query.get(submission_id)
    u = User.query.get(s.account_id)
    form = CommentForm(request.form)

    canDelete = False
    if current_user.is_authenticated:
        if s.account_id == current_user.id or current_user.admin == True:
            canDelete = True

    hasComments = True
    if Comment.query.filter_by(submission_id=submission_id).first() is None:
        hasComments = False

    canFeature = False
    if current_user.is_authenticated:
        if current_user.admin == True:
            canFeature = True

    featureText = 'Feature '
    featured = False
    if s.featured == True:
        featureText = 'Unfeature '
        featured = True

    return render_template("submissions/level.html", submission = s, account = u, form=form, comments2 = Comment.get_comments(subid = submission_id), canDelete = canDelete, hasComments = hasComments, canFeature = canFeature, featureText = featureText, featured = featured)

# deleting a level submission
@app.route("/submissions/level/<submission_id>", methods=["POST"])
@login_required
def submissions_delete(submission_id):
    lvl = Submission.query.get(submission_id)

    if lvl.account_id == current_user.id or current_user.admin == True:
        db.session.delete(lvl)
        db.session.commit()
        return redirect(url_for('index'))

# setting a level to featured/unfeatured
@app.route("/submissions/feature/<submission_id>", methods=["POST"])
@login_required
def submissions_feature(submission_id):
    if current_user.admin == True:
        s = Submission.query.get(submission_id)
        if s.featured == True:
            s.featured = False
        else:
            s.featured = True
        db.session().commit()
  
    return redirect(url_for('submissions_view', submission_id=submission_id))
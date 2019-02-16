from flask import render_template, request, redirect, url_for
from application import app, db
from application.comments.forms import CommentForm
from application.submissions.models import Submission
from application.auth.models import User
from application.comments.models import Comment
from flask_login import login_required, current_user

@app.route("/comment/<submission_id>", methods=["POST"])
@login_required
def comments_create(submission_id):
    form = CommentForm(request.form)
    if form.validate():
        comment = Comment(form.text.data)
        comment.account_id = current_user.id
        comment.submission_id = submission_id
        db.session().add(comment)
        db.session().commit()
        return redirect(url_for('submissions_view', submission_id=submission_id))
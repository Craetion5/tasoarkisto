from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CommentForm(FlaskForm):
    text = StringField("Leave a comment: ", [validators.Length(min=1)])

 
    class Meta:
        csrf = False

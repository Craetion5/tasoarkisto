from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators

class CommentForm(FlaskForm):
    text = TextAreaField("", [validators.Length(min=1)])

 
    class Meta:
        csrf = False

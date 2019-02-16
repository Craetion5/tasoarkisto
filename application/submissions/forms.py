from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class SubmissionForm(FlaskForm):
    name = StringField("Name: ", [validators.Length(min=1)])
    code = StringField("Code: ", [validators.Length(min=10)])
    description = TextAreaField("Description: ")
 
    class Meta:
        csrf = False

from flask_wtf import FlaskForm
from wtforms import StringField, validators

class SubmissionForm(FlaskForm):
    name = StringField("Name: ", [validators.Length(min=1)])
    code = StringField("Code: ", [validators.Length(min=42)])

 
    class Meta:
        csrf = False

from application import db
from application.models import Base

class Submission(Base):

    name = db.Column(db.String(144), nullable=False)
    code = db.Column(db.String(1440), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name
        self.code = "code..?"

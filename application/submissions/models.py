from application import db
from application.models import Base
from sqlalchemy.sql import text

class Submission(Base):

    name = db.Column(db.String(144), nullable=False)
    code = db.Column(db.String(1440), nullable=False)
    description = db.Column(db.String(1440), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    comments = db.relationship("Comment", backref='submission', lazy=True)

    def __init__(self, name):
        self.name = name
        self.code = "code..?"

    @staticmethod
    def count_submissions():
        stmt = text("SELECT COUNT(Submission.id) FROM Submission")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row[0])

        return response[0]

    @staticmethod
    def find_submission():
        stmt = text("SELECT * FROM Submission WHERE id = 1")
        res = db.engine.execute(stmt)
        return res;
        #response = []
        #for row in res:
        #    response.append(row[0])

        #return response[0]
from application import db
from application.models import Base
from sqlalchemy.sql import text

class Comment(Base):
    __tablename__ = "comment"
    text = db.Column(db.String(1440), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                            nullable=False)
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'),
                            nullable=False)

    def __init__(self, text):
        self.text = text
  
    def get_id(self):
        return self.id

    @staticmethod
    def get_comments(subid):
        stmt = text("select comment.text, account.username, account.id from comment left join account on account.id = comment.account_id where (comment.submission_id = :subid)").params(subid=subid)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"text":row[0], "account":row[1], "account_id":row[2]})
        return response

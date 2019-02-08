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
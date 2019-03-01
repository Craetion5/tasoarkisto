from application import db
from application.models import Base
from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean(), nullable=False)

    submissions = db.relationship("Submission", backref='account', lazy=True)
    comments = db.relationship("Comment", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.admin = False
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def count_users():
        stmt = text("SELECT COUNT(Account.id) FROM Account")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row[0])


        return response[0]

    @staticmethod
    def list_users():
        stmt = text("select account.username, count (submission.id), account.id from account left join submission on submission.account_id = account.id group by account.id having count(submission.id) != 0 order by 0 - count(submission.id)")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"username":row[0], "levels":row[1], "id":row[2]})
        return response

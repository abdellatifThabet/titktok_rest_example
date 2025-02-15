from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True,comment="user unique identifier")
    username = db.Column(db.String())


    def __init__(self, username):
        self.username = username
            
    def __repr__(self):
        return f"<User {self.username}>"
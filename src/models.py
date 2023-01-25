from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize_all(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

    def serialize_each(self):
         return {
            "id": self.id,
            "properties":{
                "name": self.name,
                "gender": self.gender
            }
            # do not serialize the password, its a security breach
        }
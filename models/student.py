from models.dbfile import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    gender = db.Column(db.String(10))

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

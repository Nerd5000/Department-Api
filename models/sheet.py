from models.dbfile import db


class Sheets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dname = db.Column(db.String(), unique=True)
    date = db.Column(db.String())
    todo = db.Column(db.String())

    def __init__(self, dname, date, todo):
        self.dname = dname
        self.date = date
        self.todo = todo

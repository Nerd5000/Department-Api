from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app=Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)

# Student Class/Model
class Student(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), unique=True)
  gender = db.Column(db.String(10))
  
  def __init__(self, name, gender):
    self.name = name
    self.gender = gender
    
# ======================================================
class Sheets(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  dname = db.Column(db.String(), unique=True)
  date = db.Column(db.String())
  todo = db.Column(db.String())
  
  def __init__(self, dname, date,todo):
    self.dname = dname
    self.date = date
    self.todo = todo

# ===================================================
import student
# ===================================================
import sheets
# ===================================================
import time-table
# ===================================================

if __name__ == "__main__":
    app.run(debug=True)



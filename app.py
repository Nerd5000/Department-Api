from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy 
import os


app=Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
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

@app.route('/students',methods=['GET'])
def students():
    students = Student.query.all()
    if len(students) > 0:
        studentList = []
        for student in students:
            studentList.append({'name': student.name, 'gender': student.gender,'id':student.id})
        return jsonify(studentList)
    else:
        return 'their\'s no Students'
# ===================================================

@app.route('/update_student/<int:id>',methods=['POST'])
def updateStudent(id):
    student = Student.query.get_or_404(id)

    student.name = request.json['name']
    student.gender = request.json['gender']

    try:
        db.session.commit()
        return 'Updated'
    except:
        return 'There was an issue updating Student'
# ===================================================
@app.route('/delete_student/<int:id>')
def deleteStudent(id):
    studentToDelete = Student.query.get_or_404(id)

    try:
        db.session.delete(studentToDelete)
        db.session.commit()
        return 'Deleted'
    except:
        return 'There was a problem deleting that Student'


# ===================================================

@app.route('/student',methods=['POST'])
def createStudent():
    jsonData = request.json
    try:
        student = Student(jsonData['name'],jsonData['gender'])
        db.session.add(student)
        db.session.commit()
        return 'created'
    except:
        return 'Error Has Occurd Check your json'
# ===================================================

@app.route('/sheets',methods=['GET'])
def getSheets():
    sheets = Sheets.query.all()
    if len(sheets) > 0:
        sheetsList = []
        for sheet in sheets:
            sheetsList.append({'dname': sheet.dname, 'date': sheet.date,'id':sheet.id,'todo':sheet.todo})
        return jsonify(sheetsList)
    else:
        return 'their\'s no sheets'


# ===================================================

@app.route('/update_sheet/<int:id>',methods=['POST'])
def updateSheet(id):
    sheet = Sheets.query.get_or_404(id)

    sheet.dname = request.json['dname']
    sheet.date = request.json['date']
    sheet.todo = request.json['todo']

    try:
        db.session.commit()
        return 'Updated'
    except:
        return 'There was an issue updating Sheet'
# ===================================================

@app.route('/delete_sheet/<int:id>')
def deleteSheet(id):
    sheetToDelete = Sheets.query.get_or_404(id)

    try:
        db.session.delete(sheetToDelete)
        db.session.commit()
        return 'Deleted'
    except:
        return 'There was a problem deleting that Student'

# ===================================================
@app.route('/sheets',methods=['POST'])
def createSheet():
    jsonData = request.json
    try:
        sheet = Sheets(jsonData['dname'],jsonData['date'],jsonData['todo'])
        db.session.add(sheet)
        db.session.commit()
        return 'created'
    except:
        return 'Error Has Occurd Check your json'
# ===================================================


if __name__ == "__main__":
    app.run(debug=True)



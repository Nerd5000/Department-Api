from models.dbfile import db
from models.sheet import Sheets
from flask import jsonify, request, Blueprint

sheets = Blueprint('sheets', __name__)


@sheets.route('/', methods=['GET'])
def getSheets():
    sheets = Sheets.query.all()
    if len(sheets) > 0:
        sheetsList = []
        for sheet in sheets:
            sheetsList.append(
                {'dname': sheet.dname, 'date': sheet.date, 'id': sheet.id, 'todo': sheet.todo})
        return jsonify(sheetsList)
    else:
        return 'their\'s no sheets'


# ===================================================
@sheets.route('/', methods=['POST'])
def createSheet():
    jsonData = request.json
    try:
        sheet = Sheets(jsonData['dname'], jsonData['date'], jsonData['todo'])
        db.session.add(sheet)
        db.session.commit()
        return 'created'
    except:
        return 'Error Has Occurd Check your json'


# ===================================================

@sheets.route('/update/<int:id>', methods=['POST'])
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


@sheets.route('/delete/<int:id>')
def deleteSheet(id):
    sheetToDelete = Sheets.query.get_or_404(id)

    try:
        db.session.delete(sheetToDelete)
        db.session.commit()
        return 'Deleted'
    except:
        return 'There was a problem deleting that Student'

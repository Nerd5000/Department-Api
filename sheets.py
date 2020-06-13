from __main__ import app, db, Sheets
from flask import Flask, jsonify, request


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
@app.route('/sheet',methods=['POST'])
def createSheet():
    jsonData = request.json
    try:
        sheet = Sheets(jsonData['dname'],jsonData['date'],jsonData['todo'])
        db.session.add(sheet)
        db.session.commit()
        return 'created'
    except:
        return 'Error Has Occurd Check your json'

from flask import Flask
from routes.students import students
from routes.sheets import sheets
from models.dbfile import db

app = Flask(__name__)
app.register_blueprint(students, url_prefix='/students')
app.register_blueprint(sheets, url_prefix='/sheets')

# Database

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# un comment below to create the database
# @app.route('/')
# def index():
#     from models.student import Student
#     from models.sheet import Sheets
#     db.create_all()
#     return 'Database Created'


if __name__ == "__main__":
    app.run(debug=True)

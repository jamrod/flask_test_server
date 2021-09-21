from flask import Flask, render_template, url_for, json, request
from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
import os


data_url = os.path.join('./static/', 'volunteers.json')

app = Flask(__name__)
CORS(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)

# class Volunteer(db.model):
#     id = db.column(db.Integer, primary_key=True)
#     isActive = db.Column(db.Boolean)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/volunteers', methods=['GET'])
def volunteers():
    with open(data_url) as file:
            data = json.load(file)
    if request.method == 'GET':
        return json.dumps(data)
    if request.method == 'POST':
        pass




if __name__ == "__main__":
    app.run(debug=True)
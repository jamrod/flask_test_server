from flask import Flask, render_template, url_for, json, request
from flask_cors import CORS
import os
from uuid import uuid4



data_url = os.path.join('./static/', 'volunteers.json')

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/volunteers', methods=['GET', 'POST', 'DELETE', 'PUT'])
def volunteers():
    with open(data_url) as file:
            data = json.load(file)

    if request.method == 'GET':
        return json.dumps(data)

    if request.method == 'POST':
        new_item = json.loads(request.json)
        new_item["id"] = uuid4()
        data.append(new_item)
        with open(data_url, 'w') as write_file:
            json.dump(data, write_file)
        return json.dumps(new_item)

    if request.method == 'DELETE':
        id = json.loads(request.json)['id']
        item_to_delete = None
        for i, item in enumerate(data):
            if item['id'] == id:
                item_to_delete = i
                break
        deleted = data.pop(item_to_delete)
        with open(data_url, 'w') as write_file:
            json.dump(data, write_file)
        return deleted

    if request.method == 'PUT':
        changes = json.loads(request.json)
        print(changes)
        id = changes['id']
        item_to_change = None
        for i, item in enumerate(data):
            if item['id'] == id:
                item_to_change = i
                break
        data[item_to_change] = changes
        with open(data_url, 'w') as write_file:
            json.dump(data, write_file)
        return changes

if __name__ == "__main__":
    app.run(debug=True)
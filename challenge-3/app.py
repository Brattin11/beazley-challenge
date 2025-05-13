from flask import Flask, request 
import json

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    with open('database.json', 'r') as database:
        data = json.load(database)
        return data
    

@app.route('/api/data/create', methods=['POST'])
def create_data():
    with open('database.json', 'r+') as database:
        data = json.load(database)
        body = request.get_json()
        data.append(body)
        database.seek(0)
        json.dump(data, database)
        return data

@app.route('/api/data/delete/<string:key>', methods=['DELETE'])
def delete_data(key):
    with open('database.json', 'r+') as database:
        data = json.load(database)

        for item in data:
            data_key = list(item.keys())[0]
            if data_key == key:
                data.remove(item)
        
        database.seek(0)
        json.dump(data, database)
        database.truncate()
        return data

@app.route('/api/data/update/<string:key>', methods=['PUT'])
def update_data(key):
    with open('database.json', 'r+') as database:
        data = json.load(database)
        body = request.get_json()
        for item in data:
            data_key = list(item.keys())[0]
            if data_key == key:
                item.update(body)
        
        database.seek(0)
        json.dump(data, database)
        database.truncate()
        return data




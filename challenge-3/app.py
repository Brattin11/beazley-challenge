from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        with open('database.json', 'r') as database:
            data = json.load(database)
            return data
    except:
        return jsonify({'message': 'Unable to process request'}), 503
    

@app.route('/api/data/create', methods=['POST'])
def create_data():
    try:
        with open('database.json', 'r+') as database:
            data = json.load(database)
            body = request.get_json()

            if body in data:
                return jsonify({'message': 'Item already exists.'}), 422

            data.append(body)
            database.seek(0)
            json.dump(data, database)
            return jsonify({'message': 'Success!'}), 201
    except:
        return jsonify({'message': 'Unable to process request'}), 503

@app.route('/api/data/delete/<string:key>', methods=['DELETE'])
def delete_data(key):
    try:
        with open('database.json', 'r+') as database:
            data = json.load(database)

            # verify item in database
            hasItem = False

            for item in data:
                data_key = list(item.keys())[0]
                if data_key == key:
                    hasItem = True
                    data.remove(item)
            
            if not hasItem:
                return jsonify({'message': 'Not found.'}), 401
            
            database.seek(0)
            json.dump(data, database)
            database.truncate()
            return jsonify({'message': 'Success!'}), 201
    except:
        return jsonify({'message': 'Unable to process request'}), 503

@app.route('/api/data/update/<string:key>', methods=['PUT'])
def update_data(key):
    try:
        with open('database.json', 'r+') as database:
            data = json.load(database)
            body = request.get_json()

            if not body in data:
                return jsonify({'message': 'Not found.'}), 401

            for item in data:
                data_key = list(item.keys())[0]
                if data_key == key:
                    item.update(body)
            
            database.seek(0)
            json.dump(data, database)
            database.truncate()
            return jsonify({'message': 'Success!'}), 201
    except:
        return jsonify({'message': 'Unable to process request'}), 503




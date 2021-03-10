from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'verbs'
app.config['MONGO_URI'] = 'mongodb+srv://cesar:darktower@cluster0.u0gom.mongodb.net/verbs'

mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/verb', methods=['POST'])
def add_verb():
    verbs_item = mongo.db.verbs

    category = request.json['category']
    infinitif = request.json['infinitif']
    indicative_present = request.json['indicative_present']
    
    item = {
        'category': category,
        'infinitif': infinitif,
        'indicative_present': indicative_present
    }
    
    verbs_id = verbs_item.insert(item)

    new_verb_item = verbs_item.find_one({'_id': verbs_id})   

    output = {'infinitif': new_verb_item['infinitif']}

    return jsonify(output)               
    
@app.route('/verb', methods=['GET'])
def get_verbs():
    
    result = 'hola'
    return jsonify(result)

@app.route('/verb/<id>', methods=['GET'])
def get_verb(id):
    verb = 'hola'
    return verb_schema.jsonify(verb)


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
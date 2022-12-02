import json
from flask import Flask, jsonify, request
app = Flask(__name__)

students = [
    {'adi': 'ramazan', 'soyadi': 'kilicaslan'}
]


@app.route('/students')
def get_students():
    return jsonify(students)


@app.route('/students', methods=['POST'])
def add_student():
    students.append(request.get_json())
    return '', 204


@app.route('/students', methods=['DELETE'])
def delete_student():
    students.remove(request.get_json())
    return '', 204


@app.route('/students', methods=['PUT'])
def update_student():
    name = request.args.get('name')
    for i in range(len(students)):
        student = students[i]
        if student['adi'] == name:
            students[i] = request.get_json()
    return '', 204


app.run()

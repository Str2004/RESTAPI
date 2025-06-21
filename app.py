from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb+srv://abhilashdalai2004:Abhi123@cluster0.13er5yi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["taskmanager"]
tasks = db["tasks"]

@app.route('/')
def home():
    return "Task Manager API is running!"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    all_tasks = []
    for task in tasks.find():
        task['_id'] = str(task['_id'])
        all_tasks.append(task)
    return jsonify(all_tasks), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = {
        "title": data.get("title"),
        "description": data.get("description", ""),
        "completed": False
    }
    result = tasks.insert_one(task)
    return jsonify({"_id": str(result.inserted_id)}), 201

@app.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    result = tasks.update_one(
        {"_id": ObjectId(id)},
        {"$set": {
            "title": data.get("title"),
            "description": data.get("description"),
            "completed": data.get("completed", False)
        }}
    )
    if result.matched_count:
        return jsonify({"message": "Task updated"}), 200
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    result = tasks.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return jsonify({"message": "Task deleted"}), 200
    return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
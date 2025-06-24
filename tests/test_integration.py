import mongomock
from bson import ObjectId

mock_client = mongomock.MongoClient()
db = mock_client["taskmanager"]
tasks = db["tasks"]

def test_insert_and_retrieve_task():
    task = {"title": "Test Task", "description": "Test Description", "completed": False}
    result = tasks.insert_one(task)
    inserted = tasks.find_one({"_id": result.inserted_id})
    assert inserted["title"] == "Test Task"

def test_update_task():
    task = {"title": "To Update", "description": "", "completed": False}
    task_id = tasks.insert_one(task).inserted_id
    tasks.update_one({"_id": task_id}, {"$set": {"completed": True}})
    updated = tasks.find_one({"_id": task_id})
    assert updated["completed"] is True

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app, tasks
from flask import json

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def clear_db():
    tasks.delete_many({})

def test_home(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Task Manager API is running!" in res.data

def test_create_task(client):
    res = client.post("/tasks", json={
        "title": "Test Task",
        "description": "Testing task creation"
    })
    assert res.status_code == 201
    data = res.get_json()
    assert "_id" in data

def test_get_tasks(client):
    tasks.insert_one({
        "title": "Sample Task",
        "description": "From test",
        "completed": False
    })
    res = client.get("/tasks")
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert "title" in data[0]

def test_update_task(client):
    res = client.post("/tasks", json={
        "title": "Update Me",
        "description": "before"
    })
    task_id = res.get_json()["_id"]

    res = client.put(f"/tasks/{task_id}", json={
        "title": "Updated",
        "description": "after",
        "completed": True
    })
    assert res.status_code == 200
    assert res.get_json()["message"] == "Task updated"

def test_delete_task(client):
    res = client.post("/tasks", json={
        "title": "Delete Me",
        "description": "bye"
    })
    task_id = res.get_json()["_id"]

    res = client.delete(f"/tasks/{task_id}")
    assert res.status_code == 200
    assert res.get_json()["message"] == "Task deleted"

def test_update_nonexistent_task(client):
    fake_id = "64d0c2efab12345678901234"
    res = client.put(f"/tasks/{fake_id}", json={
        "title": "Ghost",
        "description": "Nothing"
    })
    assert res.status_code == 404

def test_delete_nonexistent_task(client):
    fake_id = "64d0c2efab12345678901234"
    res = client.delete(f"/tasks/{fake_id}")
    assert res.status_code == 404
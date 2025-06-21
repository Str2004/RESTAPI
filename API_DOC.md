# 📘 Task Manager API Documentation

This document describes the available API endpoints in your Flask + MongoDB task manager project.

---

## 🔹 Base URL

```
http://localhost:5000
```

---

## 🔸 Endpoints

### 1. `GET /tasks`
Retrieve all tasks.

#### ✅ Example Response
```json
[
  {
    "_id": "60e8a1234abcd",
    "title": "Do homework",
    "description": "Complete math exercises",
    "completed": false
  }
]
```

---

### 2. `POST /tasks`
Create a new task.

#### 📤 Request Body
```json
{
  "title": "New Task",
  "description": "Optional description"
}
```

#### ✅ Example Response
```json
{
  "_id": "60e8a1234abcd"
}
```

---

### 3. `PUT /tasks/<id>`
Update an existing task by ID.

#### 📤 Request Body
```json
{
  "title": "Updated Task",
  "description": "New description",
  "completed": true
}
```

---

### 4. `DELETE /tasks/<id>`
Deletes a task by ID.

#### ✅ Example Response
```json
{
  "message": "Task deleted"
}
```
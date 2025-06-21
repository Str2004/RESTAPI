# 🧠 Task Manager API (Flask + MongoDB)

This is a simple REST API for managing tasks, built using Flask and MongoDB. It supports full CRUD operations and can be used with a frontend or Postman.

---

## 🚀 API Endpoints

| Method | Endpoint           | Description             |
|--------|--------------------|-------------------------|
| GET    | `/tasks`           | Get all tasks           |
| POST   | `/tasks`           | Create a new task       |
| PUT    | `/tasks/<id>`      | Update an existing task |
| DELETE | `/tasks/<id>`      | Delete a task           |

---

## 🛠 How to Run (Server)

### 1. Install dependencies:
```
pip install -r requirements.txt
```

### 2. Update MongoDB URI in `app.py`:
Replace:
```
<username>, <password>
```
with your MongoDB Atlas credentials.

### 3. Run the app:
```
python app.py
```

---

## 🧪 Sample curl Commands

### Create a Task
```
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d "{"title": "Test Task", "description": "Do something"}"
```

### Get All Tasks
```
curl http://localhost:5000/tasks
```

### Update a Task
```
curl -X PUT http://localhost:5000/tasks/<id> -H "Content-Type: application/json" -d "{"title": "Updated", "completed": true}"
```

### Delete a Task
```
curl -X DELETE http://localhost:5000/tasks/<id>
```

---

## 📦 Project Structure

```
task_manager_api_flask/
├── app.py
├── requirements.txt
└── README.md
```


---

## 🌐 Frontend

A simple HTML frontend is provided in `templates/index.html`.

### ▶ How to use it:
1. Make sure your Flask app is running
2. Open `templates/index.html` in your browser
3. Use the form to create, update, and delete tasks

---

## 📤 GitHub Submission Instructions

1. Create a GitHub repository (e.g., `task-manager-api`)
2. Push this full folder:
   ```
   git init
   git add .
   git commit -m "Initial commit - Flask Task Manager API"
   git branch -M main
   git remote add origin https://github.com/yourusername/task-manager-api.git
   git push -u origin main
   ```

---

## 🧾 Included Docs

- `README.md` (this file)
- `API_DOC.md` (endpoint-level documentation)
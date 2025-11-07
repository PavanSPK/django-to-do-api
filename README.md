# 📝 Django REST API - To-Do App

A simple **To-Do API** built with **Django** and **Django REST Framework (DRF)**.  
It lets users **Create, Read, Update, and Delete (CRUD)** tasks and manage them through the **Django Admin panel**.

----------------------------------------------------

## 🚀 Features
- Add, view, edit, and delete tasks  
- RESTful API using Django REST Framework  
- Django Admin to manage tasks visually  
- SQLite database (default)

----------------------------------------------------

## ⚙️ Setup Instructions

1️⃣ **Clone the repository**
```bash
git clone https://github.com/PavanSPK/django-to-do-api.git
cd django-to-do-api
```

2️⃣ **Create and activate virtual environment**
```bash
python -m venv env
source env\Scripts\activate  # Windows
```

3️⃣ **Install dependencies**
```bash
pip install django djangorestframework
```

4️⃣ **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5️⃣ **Create superuser**
```bash
python manage.py createsuperuser
```
👉 Set your username, email, and password for admin login.

6️⃣ **Run the server**
```bash
python manage.py runserver
```
Visit the app at:  
🔗 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

------------------------------------------------------

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| **GET** | `/api/tasks/` | Get all tasks |
| **POST** | `/api/tasks/` | Create new task |
| **GET** | `/api/tasks/<id>/` | Get task by ID |
| **PUT** | `/api/tasks/<id>/` | Update task |
| **DELETE** | `/api/tasks/<id>/` | Delete task |

-------------------------------------------------------

## 🔑 Django Admin Access

- Go to: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  
- Login with your superuser credentials  
- Manage your **Task** entries (add, edit, delete) directly from the admin panel

------------------------------------------------------

## 🧠 Tech Used
- **Python 3.14.0**
- **Django**
- **Django REST Framework**
- **SQLite3**

-----------------------------------

## 👤 Author
**Sandu Pavan Kumar**  
GitHub: [@PavanSPK](https://github.com/PavanSPK)

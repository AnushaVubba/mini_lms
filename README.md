# Mini Learning Management System (LMS)

A role-based Learning Management System built using Django REST Framework and JWT Authentication.  
The platform allows instructors to create courses and assignments, and students to submit solutions and receive grades.

---

## Features

- JWT Authentication (Secure Login)
- Custom User Roles (Student & Instructor)
- Course Creation and Listing
- Assignment Creation
- Student Assignment Submission
- Instructor Grading & Feedback
- Student Dashboard (View Grades)
- Role-Based API Permissions
- Secure Data Access (students cannot view others' submissions)
- Simple Frontend using HTML, CSS, JavaScript

---

## Tech Stack

### Backend
- Python
- Django
- Django REST Framework
- SimpleJWT Authentication

### Frontend
- HTML
- CSS
- JavaScript (Fetch API)

### Database
- SQLite

---

## Project Structure

```
mini_lms/
│
├── backend/              # Django Backend
│   ├── backend/          # Settings
│   ├── accounts/         # Authentication & roles
│   ├── courses/          # Courses & assignments
│   └── manage.py
│
├── frontend/             # Simple UI
│   ├── index.html
│   ├── courses.html
│   ├── assignments.html
│   ├── script.js
│   └── style.css
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation & Setup

### 1. Clone Repository
```
git clone <your-repository-link>
cd mini_lms
```

### 2. Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Run Backend Server
```
cd backend
python manage.py migrate
python manage.py runserver
```

### 5. Run Frontend Server
Open a new terminal:

```
cd frontend
python -m http.server 5500
```

Open browser:
```
http://127.0.0.1:5500
```

---

## User Roles

| Role | Permissions |
|-----|------|
| Instructor | Create courses, assignments, grade submissions |
| Student | Submit assignments, view grades |

---

## API Endpoints

| Endpoint | Description |
|--------|------|
| `/api/token/` | Login |
| `/api/accounts/register/` | Register user |
| `/api/courses/` | List/Create courses |
| `/api/courses/assignments/` | View assignments |
| `/api/courses/submissions/` | Submit assignment |
| `/api/courses/my-submissions/` | View grades |

---

## Learning Outcomes

- Custom Django User Model
- JWT Authentication
- Role-Based Authorization
- Object-Level Permissions
- Relational Database Design
- REST API Development
- Frontend-Backend Integration

---

## Author
**Nova Gupta**

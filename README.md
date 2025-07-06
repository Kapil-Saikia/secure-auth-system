# 🔐 Secure Authentication System

A Flask-based backend system that provides secure user **registration**, **login**, and **JWT-based session management**. Built with **Flask**, **PostgreSQL**, **bcrypt**, and **JWT**.

---

## 🚀 Features

- ✅ Secure user registration (password hashing with bcrypt)
- ✅ User login with JWT token generation
- ✅ Token-based session validation for protected routes
- ✅ PostgreSQL database integration with SQLAlchemy ORM
- ✅ `.env` for managing secrets securely

---

## 🛠️ Tech Stack

- **Backend**: Python (Flask)
- **Database**: PostgreSQL
- **Authentication**: JWT (PyJWT), bcrypt
- **Environment Config**: python-dotenv
- **ORM**: SQLAlchemy

---

## 📁 Project Structure
secure-auth-system/
│
├── app.py # Main Flask application
├── config.py # Configuration from .env
├── .env # Secret keys (not pushed to GitHub)
├── requirements.txt # Python dependencies
└── README.md # Project description
---
## ▶️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/Kapil-Saikia/secure-auth-system.git
cd secure-auth-system

# 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate    # For Windows users

# 3. Install all dependencies
pip install -r requirements.txt

# 4. Create a `.env` file in the root directory and add:
# (Replace with your actual DB password if needed)
# SECRET_KEY=this_should_be_secret
# JWT_SECRET_KEY=this_is_my_jwt_secret
# DATABASE_URL=postgresql://postgres:yourpassword@localhost/secure_auth_db

# 5. Make sure PostgreSQL is running and database is created

# 6. Start the Flask application
python app.py

# App will run locally at: http://127.0.0.1:5000
```

📌 Author
Kapil Saikia
B.Tech CSE Final Year Student

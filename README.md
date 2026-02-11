# 🔐 Secure Auth App (Flask)

## 📌 Project Overview
This project is a secure web application developed to demonstrate
authentication, authorization, and common web security protections.

## 🛠️ Technologies Used
- Python (Flask)
- SQLite
- HTML, CSS
- bcrypt

## 🔑 Security Features Implemented
- Password hashing using bcrypt
- Role-based access control (Admin/User)
- Secure session handling
- SQL Injection prevention
- XSS protection
- Input validation & sanitization

## 🔁 Application Flow
1. User signs up with strong password
2. Password is hashed and stored
3. User logs in
4. Session is created securely
5. Role-based access is applied
6. Logout clears session

## 📸 Screenshots
![Login] (Screenshots/login.png)
![Signup] (Screenshots/SignUp.png)
![User Dashboard] (Screenshots/U_db.png)
![Admin Panel] (Screenshots/A_db.png)
![Database] (Screenshots/database.png)
![Password Hash] (Screenshots/hash.png)
![Access Denied] (Screenshots/access.png)
![Weak Password] (Screenshots/weak.png)

## Detailed Security architecture is documented in SECURITY_DESIGN.md

## 🚀 How to Run the Project
```bash
pip install -r requirements.txt
python app.py
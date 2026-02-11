# 🔐 Secure Auth App (Flask)

## 📌 Project Overview
        This project is a secure web-based authentication system developed using Flask.It demonstrates industry-standard security practices including authentication, authorization, password  hashing, secure session handling, and protected database operations.
        This project was built during the Cryptonic Area Virtual Internship Program.
During this internship, I learned how to design and implement secure login systems, apply role-based access control, handle sessions securely, and structure a professional GitHub project suitable for real-world applications.

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

## Detailed Security architecture is documented in SECURITY_DESIGN.md

## 📂 File & Folder Structure

secure-auth-app/
        |___app.py
        |___database.db
        |___requirement.txt
        |___README.md
        |___SECURITY_DESIGN.md
        |
        |_templates/
        |     |__login.html
        |     |__signup.html
        |     |__dashboard.html
        |     |__admin.html
        |
        |_static/
        |   |__style.css
        |
        |_Screenshots/
        |     |__login.png
        |     |__signup.png
        |     |__user_db.png
        |     |__admin_db.png
        |     |__access_denied.png
        |     |__weak_pass.png
        |     |__hash.png
        |     |__server_runing.png   

## 🚀 How to Run the Project
```bash
pip install -r requirements.txt
python app.py

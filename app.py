from flask import Flask, render_template, request, redirect, session
from flask_bcrypt import Bcrypt
import sqlite3
import re
import os
from datetime import timedelta

app = Flask(__name__)
# 🔐 SECRET KEY
app.secret_key = os.urandom(32)

# 🔐 SESSION SECURITY
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=False,
    SESSION_COOKIE_SAMESITE="Lax"
)

# ⏱️ SESSION EXPIRY
app.permanent_session_lifetime = timedelta(minutes=15)

bcrypt = Bcrypt(app)

# ---------------- DATABASE ----------------
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# ---------------- HOME ----------------
@app.route("/")
def home():
    return redirect("/login")

# ---------------- SIGNUP ----------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # Password policy
        if (len(password) < 6 or
            not re.search("[A-Z]", password) or
            not re.search("[0-9]", password) or
            not re.search("[@#$%^+=!;?]", password)):
            return "Weak Password!"

        hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")

        try:
            conn = get_db()
            conn.execute(
                "INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)",
                (username, email, hashed_pw, "user")
            )
            conn.commit()
            conn.close()
        except:
            return "Email already exists"

        return redirect("/login")

    return render_template("signup.html")

# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()
       #ROLE BASED                
        if user and bcrypt.check_password_hash(user["password"], password):
            session.clear()  # old session clear

            session.permanent = True  # expiry apply
            session["user_id"] = user["id"]
            session["role"] = user["role"]

            if user["role"] == "admin":
                return redirect("/admin")
            else:
                return redirect("/dashboard")
        else:
            return "Invalid Email or Password"

    return render_template("login.html")

# ---------------  ADMIN ROUTE -----------------

@app.route("/admin")
def admin():
    if "user_id" not in session: # login check
        return redirect("/login")

    if session.get("role") != "admin": # role check
        return " User not Access This Page, only Admin can!! ", 403

    conn = get_db()
    users = conn.execute(
        "SELECT username, email, role FROM users WHERE role = 'user'"
    ).fetchall()

    return render_template("admin.html", users=users)

# ---------------- USER DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
      # 🔐 LOGIN CHECK
    if "user_id" not in session:
        return redirect("/login")
      # 🔐 ROLE CHECK
    if session.get("role") != "user":
        return "❌ Access Denied", 403

    conn = get_db()
    user = conn.execute(
        "SELECT username, email, role FROM users WHERE id = ?",
        (session["user_id"],)
    ).fetchone()

    return render_template("dashboard.html", user=user)

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)

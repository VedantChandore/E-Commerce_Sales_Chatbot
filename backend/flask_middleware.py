import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import requests
from flask_cors import CORS
import requests
import bcrypt
import jwt

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
SECRET_KEY = "salesbot123"

RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"

def db_connect():
    conn = sqlite3.connect("/Users/vedant/Desktop/ecommerce_salesbot/backend/inventory.db")
    print(conn)
    return conn

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not (name and email and password):
        return jsonify({"message": "All fields are required"}), 400

    # Hash password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    conn = db_connect()
    cursor = conn.cursor()

    try:
        # Check if email already exists in the database
        cursor.execute("SELECT * FROM customers WHERE email = ?", (email,))
        user = cursor.fetchone()
        if user:
            return jsonify({"message": "Email already exists"}), 400
        
        # Insert new user record into the database
        cursor.execute("INSERT INTO customers (name, email, password) VALUES (?, ?, ?)", (name, email, hashed_password))
        conn.commit()
        return jsonify({"message": "User registered successfully"}), 201

    except Exception as e:
        return jsonify({"message": str(e)}), 500
    finally:
        conn.close()

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()

    if not user or not bcrypt.checkpw(password.encode("utf-8"), user[3].encode("utf-8")):
        return jsonify({"message": "Invalid email or password"}), 401

    token = jwt.encode({"email": email}, SECRET_KEY, algorithm="HS256")
    return jsonify({"token": token}), 200


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = requests.post(RASA_SERVER_URL, json={"sender": "user", "message": user_message})
        response_data = response.json()

        bot_messages = [msg["text"] for msg in response_data if "text" in msg]
        return jsonify({"messages": bot_messages})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5001, debug=True)

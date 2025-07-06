from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import os
from functools import wraps
from dotenv import load_dotenv

# Load .env environment variables
load_dotenv()

# Initialize app and config
app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = app.config['JWT_SECRET_KEY']  # Loaded from .env

db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# ---------------------------
# Register Route
# ---------------------------
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    print("Received data in /register:", data)  # 🔍 DEBUG

    if not data or not all(k in data for k in ('username', 'email', 'password')):
        return jsonify({'error': 'Missing data'}), 400

    if User.query.filter((User.username == data['username']) | (User.email == data['email'])).first():
        return jsonify({'error': 'User already exists'}), 409

    hashed_pw = generate_password_hash(data['password'])
    user = User(username=data['username'], email=data['email'], password=hashed_pw)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

# ---------------------------
# Login Route
# ---------------------------
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print("Received data in /login:", data)  # 🔍 DEBUG

    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Missing email or password'}), 400

    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'error': 'Invalid credentials'}), 401

    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'token': token})

# ---------------------------
# JWT Token Required Decorator
# ---------------------------
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({'error': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.get(data['user_id'])
        except:
            return jsonify({'error': 'Token is invalid or expired!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

# ---------------------------
# Protected Route
# ---------------------------
@app.route('/dashboard', methods=['GET'])
@token_required
def dashboard(current_user):
    return jsonify({
        'message': f'Welcome, {current_user.username}!',
        'email': current_user.email
    })

# ---------------------------
# Root Test Route
# ---------------------------
@app.route('/', methods=['GET'])
def home():
    return "Flask app is running!", 200

# ---------------------------
# Run App
# ---------------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

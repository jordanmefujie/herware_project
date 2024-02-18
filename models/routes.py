#!/usr/bin/python3

from flask import jsonify, request
from app import app
from authentication import register_user, authenticate_user, create_token, get_current_user
from health import save_health_data, get_health_data
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from database import initialize_db
from models import User


app = Flask(__name__)
CORS(app)

# Configuration for JWT
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

# Initialize database
initialize_db(app)

# User registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400
    if User.objects(email=email):
        return jsonify({'message': 'User already exists'}), 400
    register_user(email, password)
    return jsonify({'message': 'User registered successfully'}), 201

# User login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400
    user = authenticate_user(email, password)
    if not user:
        return jsonify({'message': 'Invalid email or password'}), 401
    access_token = create_token(user)
    return jsonify({'access_token': access_token}), 200

# Profile management
@app.route('/profile', methods=['GET', 'PUT'])
@jwt_required()
def profile():
    user = get_current_user()
    if request.method == 'GET':
        return jsonify({'email': user.email}), 200
    elif request.method == 'PUT':
        data = request.json
        new_email = data.get('email')
        if new_email:
            user.email = new_email
            user.save()
            return jsonify({'message': 'Profile updated successfully'}), 200
        else:
            return jsonify({'message': 'No changes detected'}), 400

# Health data tracking
@app.route('/health', methods=['POST', 'GET'])
@jwt_required()
def health():
    if request.method == 'POST':
        data = request.json
        save_health_data(data)
        return jsonify({'message': 'Health data saved successfully'}), 201
    elif request.method == 'GET':
        health_data = get_health_data()
        return jsonify(health_data), 200

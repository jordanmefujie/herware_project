#!/usr/bin/python3

from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from models import User

jwt = JWTManager()

# User registration
def register_user(email, password):
    hashed_password = generate_password_hash(password)
    user = User(email=email, password=hashed_password)
    user.save()

# User login
def authenticate_user(email, password):
    user = User.objects(email=email).first()
    if user and check_password_hash(user.password, password):
        return user
    return None

# Create access token for user
def create_token(user):
    access_token = create_access_token(identity=str(user.id))
    return access_token

# Get current user from JWT token
def get_current_user():
    user_id = get_jwt_identity()
    user = User.objects(id=user_id).first()
    return user

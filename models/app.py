#!/usr/bin/python3

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager


app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(debug=True)

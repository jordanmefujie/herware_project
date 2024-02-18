#!/usr/bin/python3

from database import db

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)

class HealthData(db.Document):
    user_id = db.ReferenceField(User)
    cycle_start_date = db.DateTimeField()
    cycle_end_date = db.DateTimeField()
    # Add other fields as needed

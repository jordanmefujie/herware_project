#!/usr/bin/python3

# backend/utils.py

def validate_email(email):
    """
    Validate email format.
    """
    # You can implement your own email validation logic here
    if '@' in email and '.' in email:
        return True
    return False

def validate_password(password):
    """
    Validate password strength.
    """
    # You can implement your own password validation logic here
    if len(password) >= 6:
        return True
    return False

def validate_health_data(data):
    """
    Validate health data input.
    """
    # You can implement your own validation logic for health data here
    required_fields = ['cycle_start_date', 'cycle_end_date']
    for field in required_fields:
        if field not in data:
            return False
    return True

def handle_error(message, status_code):
    """
    Helper function to format error response.
    """
    response = {
        'error': message,
        'status_code': status_code
    }
    return response, status_code

#!/usr/bin/python3

from flask import Flask, request, jsonify
import logging
from .routers import device_router, data_router

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Register the device router
app.register_blueprint(device_router.bp)

# Register the data router
app.register_blueprint(data_router.bp)

# Error handling middleware


def handle_error(e):
    logger.error(str(e), exc_info=True)
    return jsonify(error='An internal error occurred'), 500
# Request data validation middleware


def validate_request_data(f):
    @functools.wraps(f)
def decorated_function(*args, **kwargs):
    try:
        request_data = request.get_json()
        if not request_data:
            raise ValueError('No JSON object provided in the request')
        return f(*args, **kwargs)
    except ValueError as ve:
        return jsonify(error='Invalid request data: {}'.format(str(ve))), 400


return decorated_function

# Apply request data validation middleware to all routes
for route in app.url_map.iter_rules():
    app.route(route.rule, **route.endpoint_arguments) =
    validate_request_data(app.view_functions[route.endpoint])

app.config[' Flask_restful_errorhandler'] = handle_error

if __name__ == '__main__':
    app.run(debug=True)

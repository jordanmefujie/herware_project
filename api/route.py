from flask import Flask
from device import DeviceManager
from user import UserManager

app = Flask(__name__)


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_manager = UserManager(data['username'])
    return user_manager.create(data)


@app.route('/devices', methods=['POST'])
def create_device():
    data = request.get_json()
    device_manager = DeviceManager(
        data['device_id'],
        data['name'],
        data['user_id'])
    return device_manager.create()


@app.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user_manager = UserManager(user_id)
    return user_manager.read(user_id)


@app.route('/devices/<string:device_id>', methods=['GET'])
def get_device(device_id):
    device_manager = DeviceManager(device_id)
    return device_manager.read(device_id)


@app.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user_manager = UserManager(user_id)
    return user_manager.update(user_id, data)


@app.route('/devices/<string:device_id>', methods=['PUT'])
def update_device(device_id):
    data = request.get_json()
    device_manager = DeviceManager(device_id)
    return device_manager.update(device_id, data)


@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_manager = UserManager(user_id)
    return user_manager.delete(user_id)


@app.route('/devices/<string:device_id>', methods=['DELETE'])
def delete_device(device_id):
    device_manager = DeviceManager(device_id)
    return device_manager.delete(device_id)

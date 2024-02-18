from flask import Flask, request, jsonify
from models import db, Device

app = Flask(__name__)


class DeviceManager:
    def __init__(self, db_storage):
        self.db_storage = db_storage

    @app.route('/create_device', methods=['POST'])
    def create_device(self):
        data = request.get_json()
        if 'device_id' in data and 'name' in data:
            device = Device(
                device_id=data['device_id'],
                name=data['name'],
                user_id=self.db_storage.get_from_db('user_id'))
            self.db_storage.create_device(device)
            return jsonify({'message': 'Device created successfully'})
        else:
            return jsonify(
                {'message': 'Invalid data provided.
                 Required: device_id and name'})

    @app.route('/get_device', methods=['GET'])
    def get_device(self):
        device_id = request.args.get('device_id')
        if device_id:
            device = self.db_storage.get_device(device_id)
            if device:
                return jsonify({'device_id': device.device_id,
                               'name': device.name, 'user_id': device.user_id})
            else:
                return jsonify({'message': 'Device not found'})
        else:
            return jsonify({'message': 'Device ID not provided'})

    @app.route('/update_device', methods=['POST'])
    def update_device(self):
        data = request.get_json()
        if 'device_id' in data and 'name' in data:
            device = self.db_storage.get_device(data['device_id'])
            if device:
                device.name = data['name']
                self.db_storage.update_device(device)
                return jsonify({'message': 'Device updated successfully'})
            else:
                return jsonify({'message': 'Device not found'})
        else:
            return jsonify(
                {'message': 'Invalid data provided.
                 Required: device_id and name'})

    @app.route('/delete_device', methods=['POST'])
    def delete_device(self):
        data = request.get_json()
        if 'device_id' in data:
            device = self.db_storage.get_device(data['device_id'])
            if device:
                self.db_storage.delete_device(device)
                return jsonify({'message': 'Device deleted successfully'})
            else:
                return jsonify({'message': 'Device not found'})
        else:
            return jsonify({'message': 'Device ID not provided'})

# Define db_storage methods as needed


if __name__ == '__main__':
    app.run(debug=True)

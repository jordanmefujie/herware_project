from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
models = [
    {"id": 1, "name": "Model 1", "description": "Description for Model 1"},
    {"id": 2, "name": "Model 2", "description": "Description for Model 2"},
]


@app.route('/models', methods=['GET'])
def get_models():
    return jsonify(models)


@app.route('/models/<int:model_id>', methods=['GET'])
def get_model(model_id):
    model = next((model for model in models if model['id'] == model_id), None)
    if model:
        return jsonify(model)
    return jsonify({"message": "Model not found"}), 404


@app.route('/models', methods=['POST'])
def create_model():
    data = request.get_json()
    new_model = {
        "id": len(models) + 1,
        "name": data["name"],
        "description": data["description"]}
    models.append(new_model)
    return jsonify(new_model), 201

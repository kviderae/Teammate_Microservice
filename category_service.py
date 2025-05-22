from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Simulated in-memory database
default_categories = [
    {"id": str(uuid.uuid4()), "name": "Food", "type": "default"},
    {"id": str(uuid.uuid4()), "name": "Transportation", "type": "default"},
    {"id": str(uuid.uuid4()), "name": "Entertainment", "type": "default"}
]

custom_categories = {}  # key: user_id, value: list of categories

@app.route("/categories", methods=["GET"])
def get_categories():
    user_id = request.args.get("userId")
    if not user_id:
        return jsonify({"error": "Missing userId"}), 400
    user_categories = custom_categories.get(user_id, [])
    return jsonify(default_categories + user_categories)

@app.route("/categories", methods=["POST"])
def add_category():
    data = request.get_json()
    user_id = data.get("userId")
    name = data.get("categoryName")
    if not user_id or not name:
        return jsonify({"error": "Missing userId or categoryName"}), 400
    category = {
        "id": str(uuid.uuid4()),
        "name": name,
        "type": "custom"
    }
    custom_categories.setdefault(user_id, []).append(category)
    return jsonify(category), 201

@app.route("/categories/<category_id>", methods=["DELETE"])
def delete_category(category_id):
    user_id = request.args.get("userId")
    if not user_id:
        return jsonify({"error": "Missing userId"}), 400
    user_cats = custom_categories.get(user_id, [])
    for cat in user_cats:
        if cat["id"] == category_id:
            user_cats.remove(cat)
            return jsonify({"message": "Category deleted"}), 200
    return jsonify({"error": "Category not found"}), 404

if __name__ == "__main__":
    app.run(port=5001)

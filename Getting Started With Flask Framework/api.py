### Put and Delete-HTTP Verbs
### Working With API's--Json

from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial Data in my to-do list
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route('/')
def home():
    return "Welcome To The Sample To-Do List App"

# Get: Retrieve all the items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Get: Retrieve a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

# Post: Create a new task
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not request.is_json:
        return jsonify({"error": "Invalid Content-Type. Must be application/json"}), 400

    if not request.json.get('name'):
        return jsonify({"error": "Name is required"}), 400

    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json.get("description", "")  # Default empty description
    }
    items.append(new_item)
    return jsonify(new_item), 201

# Put: Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404

    if not request.json or not request.is_json:
        return jsonify({"error": "Invalid Content-Type. Must be application/json"}), 400

    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# DELETE: Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404

    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)

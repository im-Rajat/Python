from flask import Flask, jsonify, request, send_from_directory

# --- Create the Flask app ---
app = Flask(__name__)
app.config['JSON_SORT_VALUES'] = False

# --- This is our "database" ---
guests = [
    { "id": 1, "name": "Rajat" },
    { "id": 2, "name": "Kunal" }
]

names = [
    { "name": "Rajat", "dob": 26, "city": "New Delhi" },
    { "name": "Tanisha", "dob": 18, "city": "Ghaziabad" },
    { "name" : "Kunal"}
]

# --- Serve the index.html file ---
# This route will serve your frontend
@app.route('/')
def serve_index():
    # 'send_from_directory' serves files from the current folder ('.')
    return send_from_directory('.', 'index.html')

# --- Your API Routes ---

@app.route('/api/names', methods=['GET'])
def get_names():
    print("GET request received. Sending names list.")
    return jsonify(names)

@app.route('/api/guests', methods=['GET'])
def get_guests():
    print("GET request received. Sending guest list.")
    return jsonify(guests)

@app.route('/api/guests', methods=['POST'])
def add_guest():
    # Get the JSON data from the request body
    data = request.get_json()

    if not data or 'name' not in data:
        # Simple validation
        return jsonify({ "error": "Name is required" }), 400

    new_name = data['name']

    # Find the highest existing ID and add 1
    new_id = max(guest['id'] for guest in guests) + 1 if guests else 1
    
    new_guest = {
        "id": len(guests) + 1,
        "name": new_name
    }

    guests.append(new_guest)
    print("POST request received. Added:", new_guest)

    # Send back the new guest list
    return jsonify(new_guest), 201

@app.route('/api/guests/delete', methods=['POST'])
def delete_guest():
    global guests
    data = request.get_json()

    if not data or 'id' not in data:
        return jsonify({ "error": "Guest ID is required" }), 400

    guest_id = data['id']
    guest = next((g for g in guests if g['id'] == guest_id), None)

    if guest is None:
        return jsonify({ "error": "Guest not found" }), 404

    guests = [g for g in guests if g['id'] != guest_id]
    print(f"POST request to delete guest_id {guest_id}. Guest removed.")
    
    return jsonify({ 
        "message": "Guest deleted successfully",
        "deleted_guest": {
            "id": guest['id'],
            "name": guest['name']
        }
    }), 200

@app.route('/api/guests/<int:guest_id>', methods=['PUT'])
def update_guest(guest_id):
    data = request.get_json()

    if not data or 'name' not in data:
        return jsonify({ "error": "Name is required" }), 400

    guest = next((g for g in guests if g['id'] == guest_id), None)

    if guest is None:
        return jsonify({ "error": "Guest not found" }), 404

    guest['name'] = data['name']
    print(f"PUT request for guest_id {guest_id}. Updated guest to:", guest)

    return jsonify(guest)

@app.route('/api/guests/<int:guest_id>', methods=['DELETE'])
def delete_guest_id(guest_id):
    global guests
    guest = next((g for g in guests if g['id'] == guest_id), None)

    if guest is None:
        return jsonify({ "error": "Guest not found" }), 404

    guests = [g for g in guests if g['id'] != guest_id]
    print(f"DELETE request for guest_id {guest_id}. Guest removed.")
    
    return jsonify({ "message": "Guest deleted successfully" }), 200

@app.route('/confess-your-feelings', methods=['POST'])
def confess_your_feelings():
    
    return jsonify({ "error": "Endpoint doesn't exist. She never saw you that way" }), 404

# --- Start the server ---
if __name__ == '__main__':
    app.run(port=3000, debug=True)

from flask import Flask,request, jsonify

app = Flask(__name__)

# In-memory "database"
# users will look like:
# {
#   1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
#   2: {"id": 2, "name": "Bob", "email": "bob@example.com"}
# }



users = {}
next_id = 1 # To keep track of the next user ID

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the User Management API is running!"}) , 200

# 1. Get all users  - HTTP GET /users
@app.route("/users", methods=["GET"])

def get_users():
    return jsonify(list(users.values())), 200

# 2. Get a user by ID - HTTP GET /users/<id>
@app.route("/users/<int:user_id>", methods=["GET"])

def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404
    
# 3. Create a new user - HTTP POST /users
@app.route("/users", methods=["POST"])
def create_user():
    global next_id 

 # Expecting JSON like: {"name": "Naveen", "email": "naveen@example.com"}
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400
    
    name = data.get("name")
    email = data.get("email")
    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400
    
# Create new user

    user = {"id": next_id, "name": name, "email": email}
    users[next_id] = user
    next_id += 1

    # Return the created user with 201 status code
    return jsonify(user), 201

# 4. Update a user by ID - HTTP PUT /users/<id>

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400
    
    # update user details
    user["name"] = name
    user["email"] = email
    return jsonify(user), 200

# 5. Delete a user by ID - HTTP DELETE /users/<id>
def delete_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    del users[user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True) # Run the Flask app in debug mode

    
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Get login data from the client
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Log the received data
    print(f"Received login info: Username: {username}, Password: {password}")
    
    # Respond to the client
    return jsonify({"message": "Login data received successfully"}), 200

if __name__ == '__main__':
    # Run the server on the specified IPv4 address
    app.run(host='192.168.88.253', port=5000)

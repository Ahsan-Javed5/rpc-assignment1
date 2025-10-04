from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    
    if 'x' not in data or 'y' not in data:
        return jsonify({"error": "Missing parameters 'x' or 'y'"}), 400
    
    try:
        x = int(data['x'])
        y = int(data['y'])
        result = x + y
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Parameters must be integers"}), 400

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    
    if 'x' not in data or 'y' not in data:
        return jsonify({"error": "Missing parameters 'x' or 'y'"}), 400
    
    try:
        x = int(data['x'])
        y = int(data['y'])
        result = x * y
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Parameters must be integers"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
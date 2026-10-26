"""
SDA2 Challenge 1: Hello FaaS
A simple Flask service demonstrating Function-as-a-Service principles
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """Health check endpoint"""
    return jsonify({
        "service": "SDA2 Challenge 1",
        "status": "running",
        "endpoints": ["/hello", "/goodbye"]
    })

@app.route('/hello', methods=['GET'])
def hello():
    """
    Greet a user by name
    Query parameter: name (optional, defaults to 'World')
    """
    name = request.args.get('name', 'World')
    return jsonify({"message": f"Hello, {name}!"})

# TODO: Add /goodbye endpoint here
# Your code goes below this line
@app.route('/goodbye', methods=['GET'])
def goodbye():
    """
    Say goodbye to a user by name
    Query parameter: name (optional, defaults to 'World')
    """
    name = request.args.get('name', 'World')
    return jsonify({"message": f"Goodbye, {name}!"})
  


if __name__ == '__main__':
    # Run on all interfaces (0.0.0.0) to allow external connections
    app.run(host='0.0.0.0', port=8080, debug=False)

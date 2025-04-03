from flask import Flask, request, jsonify
from .handlers import handle_request

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.json
    response = handle_request(data)
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
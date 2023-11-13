from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/format', methods=['POST'])
def format_result():
    data = request.json
    # Format the data into JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8082)

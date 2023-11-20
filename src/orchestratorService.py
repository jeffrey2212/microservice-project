from flask import Flask, jsonify
import requests


app = Flask(__name__)

@app.route('/', methods=['GET'])
def process_data():
    # Call the data reader service
    data_reader_url = 'http://reader:5010/'
    response = requests.get(data_reader_url)
    if response.status_code != 200:
        return jsonify({"error": "Failed to get data from Data Reader Service"}), response.status_code

    data = response.json()

    # Call the compute service
    compute_url = 'http://compute:5011/'
    compute_response = requests.post(compute_url, json=data)
    if compute_response.status_code != 200:
        return jsonify({"error": "Failed to process data in Compute Service"}), compute_response.status_code

    computed_data = compute_response.json()
    return jsonify(computed_data)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)

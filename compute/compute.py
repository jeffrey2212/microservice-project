from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/compute', methods=['POST'])
def compute():
    data = request.json
    # Calculate the total score and max difference
    for student in data:
        student['Total'] = sum([student[sub] for sub in student if sub != 'Name'])
        student['MaxDiff'] = max([student[sub] for sub in student if sub != 'Name']) - min([student[sub] for sub in student if sub != 'Name'])
    
    # Send data to Result Formatter Service
    formatter_service_url = 'http://result-formatter-service:8082/format' # Example URL
    response = requests.post(formatter_service_url, json=data)
    return jsonify({"status": "Processed", "formatter_response": response.status_code})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)

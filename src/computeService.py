from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def compute():
    data = request.json
    result = []

    for record in data:
        name = record.get('Name')
        subjects = [score for subject, score in record.items() if subject not in ['Name', 'Total', 'MaxDiff']]
        total_score = sum(subjects)
        max_diff = max(subjects) - min(subjects)

        # Transforming the data to the required format
        transformed_record = {
            "name": name,
            "range_data": max_diff,
            "sum_data": total_score
        }
        result.append(transformed_record)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5011)

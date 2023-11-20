from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def read_data():
    file_path = './data/GradeTable.xlsx'  # Adjust the path as necessary
    # Read the Excel file
    df = pd.read_excel(file_path)
    # Convert the DataFrame to a Python dictionary
    data_dict = df.to_dict(orient='records')
    # Use jsonify to return proper JSON
    return jsonify(data_dict)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5010)

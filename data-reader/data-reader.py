import pandas as pd
import requests

def read_data(file_path):
    # Read the Excel file
    data = pd.read_excel(file_path)
    return data.to_dict(orient='records')

def send_data(data, compute_service_url):
    # Send the data to the Compute Service
    response = requests.post(compute_service_url, json=data)
    return response.status_code

if __name__ == "__main__":
    file_path = './data/GradeTable.xlsx'  # Updated file path
    data = read_data(file_path)
    compute_service_url = 'http://compute-service:8081/compute' # Example URL
    status = send_data(data, compute_service_url)
    print(f"Data sent to Compute Service, Status Code: {status}")

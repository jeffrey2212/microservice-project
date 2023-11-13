
# EduScoreAnalytics

## Project Overview
EduScoreAnalytics is a microservices-based application designed to process student grade data. Developed as part of the CISC7403 CLOUD AND DISTRIBUTED SYSTEMS course at the University of Macau, this project showcases the implementation and interaction of microservices using Docker and Python. It reads student grade data from an Excel file, calculates total scores and the maximum score differences, and outputs the results in JSON format.

## Author
Jeffrey Chan

## Services
- **Data Reader Service**: Reads student data from an Excel file.
- **Compute Service**: Calculates total scores and maximum score differences.
- **Result Formatter Service**: Formats the calculated data into JSON.

## Technology Stack
- Python
- Flask
- Pandas
- Docker & Docker Compose

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Setup and Run
1. Clone the repository:
   ```bash
   git clone [repository-url]
   ```
2. Navigate to the project directory:
   ```bash
   cd EduScoreAnalytics
   ```
3. Build the Docker images:
   ```bash
   docker-compose build
   ```
4. Run the application:
   ```bash
   docker-compose up
   ```

### Directory Structure
- `/data-reader`: Contains the Data Reader Service and its Dockerfile.
- `/compute`: Contains the Compute Service and its Dockerfile.
- `/result-formatter`: Contains the Result Formatter Service and its Dockerfile.
- `/data`: Contains the Excel file with student grade data.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- University of Macau
- CISC7403 CLOUD AND DISTRIBUTED SYSTEMS Course

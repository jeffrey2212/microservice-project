# Microservice Project

## Overview
This project demonstrates a simple microservice architecture using Docker and Python Flask. It consists of three main services: a data reader service, a compute service, and an orchestrator service.

### Services
- **Data Reader Service**: Reads data from an Excel file and provides it in JSON format.
- **Compute Service**: Receives JSON data, calculates the total and range for each record, and returns the result.
- **Orchestrator Service**: Manages the flow of data between the data reader and compute services, and interfaces with the client.

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Setup
1. Clone the repository:
```
git clone https://github.com/jeffrey2212/microservice-project.git
```
2. Navigate to the project directory:
```
cd microservice-project
```

### Running the Application
1. Build the Docker images:
```
docker compose build
``` 
2. Run the services:
```
docker compose up -d
```


### Usage
Send a request to the orchestrator service to initiate the process:
```
curl -X GET http://localhost:8000/
```

## Architecture
This project uses a microservices architecture, with Docker containers for each service. Communication between services is managed through RESTful APIs.

## Contributions
Contributions are welcome. Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Project developed as part of a cloud and distributed systems course.
- Special thanks to University of Macau.






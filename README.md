# AITU Campus Shuttle Service Data Streamer

This project implements the Python foundation for processing real-time vehicle-location and passenger-count events for the Astana IT University campus shuttle service. 

## Prerequisites
Ensure Python 3.10+ is installed on your system. Install the required dependencies to run the analysis, API, and tests:
```bash
pip install fastapi uvicorn matplotlib pytest
```

## Running the Data Analysis 
To process the event stream, calculate the core analytics, and generate the visual evaluation graph, execute the main script:
```bash
python main.py
```
**Expected Output:**
* The console will output the average passenger count, maximum capacity, number of stopped events, and the busiest minute/bus.
* A graphical plot (`passenger_load_plot.png`) will be automatically generated and saved in the root directory. Open this file to visually evaluate the passenger load trends across the time series. Ensure this image is included alongside the code in your Moodle upload.

## Running the FastAPI Endpoint
To launch the REST API server for processing incoming JSON events:
```bash
uvicorn api:app --reload
```
Once the server is running, the endpoint listens at:
`http://127.0.0.1:8000/events`

You can test the endpoint using an API client (like Postman or cURL) by sending a POST request, or by navigating to `http://127.0.0.1:8000/docs` to use the interactive Swagger UI.

## Running the Tests
To execute the validation test suite and verify boundary conditions:
```bash
pytest test_events.py -v
```

## Project Structure
* `main.py`: Contains the synthetic dataset, event parsing, validation logic, lazy generator (`yield`), console analytics, and the plotting function.
* `api.py`: Contains the FastAPI application and the POST `/events` occupancy calculation logic.
* `test_events.py`: Contains unit tests validating proper acceptance and rejection of edge cases (e.g., negative speeds, invalid statuses).
```

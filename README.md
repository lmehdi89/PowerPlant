# Power Plant Production Plan API

This API calculates the production plan for power plants based on the given payload.

## Prerequisites

- [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- [Docker](https://docs.docker.com/get-docker/)

## Build and Launch

### Local Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/lmehdi89/PowerPlant.git
    ```

2. Navigate to the project directory:

    ```bash
    cd PowerPlant
    ```

3. install requirements:

    ```bash
    pip install -r ./requirements.txt
    ```

4. Run the application:

    ```bash
    uvicorn main:app --port 8888
    ```

The API will be accessible at http://localhost:8888.

### Docker Installation

1. Build Docker Image From Dockerfile:

    ```bash
    docker build -t powerplantexample .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 8888:8888 powerplantexample
    ```

The API will be accessible at http://localhost:8888.

## API Endpoint

### POST /productionplan

This endpoint accepts a JSON payload containing load and power plant information and returns the production plan.

Example payload:

```json
{
  "load": 50,
  "fuels": {
    "gas": 10,
    "kerosine": 20,
    "co2": 5,
    "wind": 30
  },
  "powerplants": [
    {
      "name": "gas_plant",
      "type": "gasfired",
      "efficiency": 0.5,
      "pmax": 100,
      "pmin": 10
    },
    {
      "name": "wind_turbine",
      "type": "windturbine",
      "efficiency": 1.0,
      "pmax": 200,
      "pmin": 0
    }
  ]
}
```

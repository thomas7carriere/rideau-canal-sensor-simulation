## Sensor Simluation Reposotiry

## Overview

The Rideau Canal Sensor Simulator generates random environmental data in a range for three locations (Dow's Lake, Fifth Avenue and NAC) along the Rideau canal and sends the data to Azure IoT Hub. The simulator mimics real-world sensor readings such as ice thickness, surface temperature, snow accumulation, and external temperature. This data is used downstream by Azure Stream Analytics, Cosmos DB, and the dashboard application to monitor ice safety conditions in real time.

Technologies Used:

- Python
- Azure IoT Device SDK for Python
- Python dotenv
- Azure IoT Hub

## Prequiresites

The following are required to run the the sensor simulation:

- Python
- Azure IoT Hub created
- Three IoT devices registered in IoT Hub
- Device connection strings for each device

## Installation

1. Clone this repository: `git clone https://github.com/your-repository/simulator`
2. Install dependencies in requirements.txt: `pip install -r requirements.txt`
3. Create a .env file with the device connection strings:
  ```
   DEVICE_CONN_STR_DOWS=your-device-connection-string
   DEVICE_CONN_STR_FIFTH=your-device-connection-string
   DEVICE_CONN_STR_NAC=your-device-connection-string
```

## Usage

Launch the application by running: ` python data_simulator.py`

## Code Structure

**Main Components**https://github.com/thomas7carriere/rideau-canal-sensor-simulation/tree/main

- Device Clients: Creates a connection between each simulated device and Azure IoT Hub
- Data Generator: Produces realistic sensor readings using random values within defined ranges
- Telemetry Sender: Formats sensor data into JSON and sends it to IoT Hub
- Loop: Sends data every 10 seconds continuously

**Key Functions**

- `generate_sensor_data(location)`: Creates the simulated sensor data for a location
- `send_data(client, location)`: Send the simulated sensor data to the Azure IoT Hub
- `main()`: Creates device connections and begins the loop

## Sensor Data Format
**JSON schema**
```
{
  "location": "string",
  "timestamp": "ISO 8601 datetime",
  "iceThickness": "number (cm)",
  "surfaceTemp": "number (°C)",
  "snowAccumulation": "number (cm)",
  "externalTemp": "number (°C)"
}
```
**Example output**
```
{
  "location": "Dow's Lake",
  "timestamp": "2026-03-15T14:30:00Z",
  "iceThickness": 24.6,
  "surfaceTemp": -6.2,
  "snowAccumulation": 1.4,
  "externalTemp": -8.1
}
```
## Troubleshooting

Problem: No data is being sent to the Azure IoT Hub

Possible Solutions: 
1. Confirm the connections strings for each device are valid
2. Confirm data_simulator.py is running
3. Confirm the proper configuration of the Azure IoT Hub Devices

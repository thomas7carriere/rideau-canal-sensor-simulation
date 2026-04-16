import json
import random
import time
import os
from datetime import datetime

from dotenv import load_dotenv
from azure.iot.device import IoTHubDeviceClient

# Load environment variables from .env
load_dotenv()

# Get connection strings from environment variables
DEVICE_CONNECTION_STRINGS = {
    "Dow's Lake": os.getenv("DEVICE_CONN_STR_DOWS"),
    "Fifth Avenue": os.getenv("DEVICE_CONN_STR_FIFTH"),
    "NAC": os.getenv("DEVICE_CONN_STR_NAC")
}

clients = {}

# Connect each device
for location, conn_str in DEVICE_CONNECTION_STRINGS.items():

    if not conn_str:
        raise ValueError(f"Missing environment variable for {location}")

    client = IoTHubDeviceClient.create_from_connection_string(conn_str)
    client.connect()

    clients[location] = client

    print(f"{location} device connected")

print("Sending telemetry every 10 seconds from all devices...")

while True:

    for location, client in clients.items():

        data = {
            "location": location,
            "timestamp": datetime.utcnow().isoformat(),

            "iceThickness": round(random.uniform(10, 40), 2),
            "surfaceTemp": round(random.uniform(-10, 2), 2),
            "snowAccumulation": round(random.uniform(0, 5), 2),
            "externalTemp": round(random.uniform(-15, 0), 2)
        }

        message = json.dumps(data)

        client.send_message(message)

        print(f"Sent from {location}: {message}")

    time.sleep(10)
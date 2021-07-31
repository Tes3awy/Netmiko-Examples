# Cisco DNA Center AO 1.3.1.4

import json

import requests
from requests.auth import HTTPBasicAuth as BasicAuth

# CONSTANTS
BASE_URL = "https://sandboxdnac2.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"
VERIFY = True  # Set to True in Case of Cisco Sandbox ONLY

# Inputs 1
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# Processing 1
# Using try/except block to handle any HTTP Error
try:
    token_response = requests.post(
        url=f"{BASE_URL}/dna/system/api/v1/auth/token",  # Using formatted string "f"
        headers=headers,
        auth=BasicAuth(USERNAME, PASSWORD),
        verify=VERIFY,
    )
    token_response.raise_for_status()
except Exception as ex:
    raise SystemExit(ex)

# Output 1
token = token_response.json()["Token"]

# ------------------------------------

# Inputs 2
headers_2 = {
    **headers,  # Using Spread Operator
    "X-Auth-Token": token,
}

# Processing 2
devices_config_response = requests.get(
    url=f"{BASE_URL}/dna/intent/api/v1/network-device/config",  # Using formatted string "f"
    headers=headers_2,
    verify=VERIFY,
)

# Output 2
devices_config = devices_config_response.json()["response"]  # Devices list of dicts

# Export devices_config to a JSON file (For ease of reading the output)
with open("devices-config.json", "w") as jsonfile:
    json.dump(devices_config, jsonfile, indent=4, sort_keys=True)

# Save each device configuration to a text file using the id from devices_config response
for config in devices_config:
    with open(f'{config["id"]}.txt', "w") as outfile:
        outfile.write(config["runningConfig"].lstrip())

print("Done")

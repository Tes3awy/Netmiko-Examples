# Cisco DNA Center AO 1.3.1.4

import json

import requests
from requests.auth import HTTPBasicAuth

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
try:
    token_response = requests.post(
        url=f"{BASE_URL}/dna/system/api/v1/auth/token",
        headers=headers,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
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
devices_response = requests.get(
    url=f"{BASE_URL}/dna/intent/api/v1/network-device",
    headers=headers_2,
    verify=VERIFY,
)

# Output 2
devices = devices_response.json()["response"]

# Save network-device response to a JSON file (For ease of reading the output)
with open("network-devices.json", "w") as outfile:
    json.dump(devices, outfile, indent=4, sort_keys=True)

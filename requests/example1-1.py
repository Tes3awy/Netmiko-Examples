# Cisco DNA Center AO 1.3.1.4
# POST: Generate Auth Token

import requests
from requests.auth import HTTPBasicAuth

# CONSTNATS
BASE_URL = "https://sandboxdnac2.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"
VERIFY = True  # Set to True in Case of Cisco Sandbox ONLY

# Input
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# Processing (Using try and except to handle any HTTP Error)
try:
    r = requests.post(
        url=f"{BASE_URL}/dna/system/api/v1/auth/token",
        headers=headers,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        verify=VERIFY,
    )
    r.raise_for_status()
except Exception as ex:
    raise SystemExit(ex)

# Output
print(r.json(), type(r.json()))

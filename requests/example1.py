# Cisco DNA Center AO 1.3.1.4

import requests
from requests.auth import HTTPBasicAuth as BasicAuth

# CONSTANTS
BASE_URL = "https://sandboxdnac2.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"
VERIFY = True  # Set to True in Case of Cisco Sandbox ONLY

# Inputs
headers = {"Content-Type": "application/json", "Accept": "application/json"}

# Processing
r = requests.post(
    url=f"{BASE_URL}/dna/system/api/v1/auth/token",
    headers=headers,
    auth=BasicAuth(USERNAME, PASSWORD),
    verify=VERIFY,
)

# Output token, its type, and its available attributes
print(r.json(), type(r.json()), dir(r))

# Cisco DNA Center AO 1.3.1.4

from pprint import pprint

import requests
from requests.auth import HTTPBasicAuth as BasicAuth
from requests.packages import urllib3

# To disable SSL warning when VERIFY is equal to False
# Remove line 7 and 11 if you are unsure of their use
urllib3.disable_warnings()

# CONSTNATS
BASE_URL = "https://sandboxdnac2.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"
VERIFY = False  # Set to True in Case of Cisco Sandbox ONLY

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
        auth=BasicAuth(USERNAME, PASSWORD),
        verify=VERIFY,
    )
    token_response.raise_for_status()
except Exception as ex:
    raise SystemExit(ex)

# Output 1
token = token_response.json()["Token"]

# --------------------------

# Inputs 2

headers_2 = {
    **headers,  # Using Spread Operator
    "X-Auth-Token": token,
}

# Processing 2 (Using params to select specifif site with its ID)
site_response = requests.get(
    url=f"{BASE_URL}/dna/intent/api/v1/site",
    params={"siteId": "e95d9cef-2a00-4eb9-82df-01c3291410be"},  # Any Site ID
    headers=headers_2,
    verify=VERIFY,
)

site = site_response.json()["response"]
# Output 2
pprint(site)

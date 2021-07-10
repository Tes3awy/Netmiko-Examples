# Cisco DNA Center AO 1.3.1.4

from datetime import datetime

import xlsxwriter

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

# -------------------------------------

# Inputs 2
headers_2 = {
    **headers,  # Using Spread Operator
    "X-Auth-Token": token,
}

# Processing 2
devices_response = requests.get(
    url=f"{BASE_URL}/dna/intent/api/v1/network-device",  # Using formatted string "f"
    headers=headers_2,
    verify=VERIFY,
)

# Output 2
devices = devices_response.json()["response"]  # Devices list of dicts
with xlsxwriter.Workbook("DNAC-Device-List.xlsx") as workbook:  # Create an Excel file
    # Create a sheet in the Excel file
    worksheet = workbook.add_worksheet("DNAC Device List")

    # Header row in Excel file
    header = {
        "A1": "Hostname",
        "B1": "MGMT IP Address",
        "C1": "Serial Number",
        "D1": "MAC Address",
        "E1": "Device Model",
        "F1": "SW Version",
        "G1": "Role",
        "H1": "Uptime",
        "I1": "Last Update",
        "J1": "Reachability Status",
    }

    for key, value in header.items():
        worksheet.write(key, value)

    # Staring values for row and col
    row, col = 1, 0

    # Grab data from each device into Excel file
    for device in devices:
        worksheet.write(row, col + 0, device["hostname"])
        worksheet.write(row, col + 1, device["managementIpAddress"])
        worksheet.write(row, col + 2, device["serialNumber"])
        worksheet.write(row, col + 3, device["macAddress"])
        worksheet.write(row, col + 4, device["platformId"])
        worksheet.write(row, col + 5, device["softwareVersion"])
        worksheet.write(row, col + 6, device["role"])
        worksheet.write(row, col + 7, device["upTime"])
        # lastUpdateTime comes in milliseconds (Removing the milliseconds)
        epoch_time = str(device["lastUpdateTime"])[:-3]
        # Converting timestamp to human readable format
        last_updated = datetime.fromtimestamp(int(epoch_time))
        worksheet.write(row, col + 8, last_updated.strftime("%Y-%m-%d %H:%M:%S"))
        worksheet.write(row, col + 9, device["reachabilityStatus"])

        # Jump to next row
        row += 1

print("Done")

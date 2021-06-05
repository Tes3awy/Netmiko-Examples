# Create an Excel sheet and save cdp neighbors detail data in

import xlsxwriter

from netmiko import ConnectHandler

# Create an Excel file
workbook = xlsxwriter.Workbook("Example5-1-CDP-Neighbors-Details.xlsx")
# Create an Excel sheet within the file
worksheet = workbook.add_worksheet("CDP Neighbors Details")
# Filters
worksheet.autofilter("A1:H1")

# Create Header line
header = {
    "A1": "Local Hostname",
    "B1": "Local Port",
    "C1": "Remote Hostname",
    "D1": "MGMT IP Address",
    "E1": "Capabilities",
    "F1": "Remote Host Platform",
    "G1": "Remote Host Port",
    "H1": "Remote Host SW Version",
}

# Loop over headers and create cells in first row (row 0)
for key, value in header.items():
    worksheet.write(key, value)

# Devices to SSH into
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "sandbox-iosxe-latest-1.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "port": 22,
    },
    {
        "device_type": "cisco_ios",
        "ip": "ios-xe-mgmt.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "port": 8181,
    },
]

# Starting values for row and column in the Excel workbook
row = 1
col = 0

# Loop over devices
for device in devices:
    # Create a connection instance
    with ConnectHandler(**device) as net_connect:
        hostname = net_connect.send_command("show version", use_textfsm=True)[0][
            "hostname"
        ]  # hostname of the current device
        cdp_neighbors_detail = net_connect.send_command(
            "show cdp neighbors detail", use_textfsm=True
        )
    # Check if cdp is enabled on that Cisco device
    if not "% CDP is not enabled" in cdp_neighbors_detail:
        # Loop over dicts in cdp neighbors detail list
        for neighbor in cdp_neighbors_detail:
            worksheet.write(row, col + 0, hostname)
            worksheet.write(row, col + 1, neighbor["local_port"])
            worksheet.write(row, col + 2, neighbor["destination_host"])
            worksheet.write(row, col + 3, neighbor["management_ip"])
            worksheet.write(row, col + 4, neighbor["capabilities"])
            worksheet.write(row, col + 5, neighbor["platform"])
            worksheet.write(row, col + 6, neighbor["remote_port"])
            worksheet.write(row, col + 7, neighbor["software_version"])
            # Jump to next row
            row += 1
    else:
        print(
            f"{cdp_neighbors_detail}. Please run `cdp run` command in Global Config mode on {hostname}"
        )

workbook.close()
print("Done")

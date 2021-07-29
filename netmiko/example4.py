# Create an Excel sheet and save data from show version in

import xlsxwriter

from netmiko import ConnectHandler

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
        "ip": "sandbox-iosxe-recomm-1.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "port": 22,
    },
]

# Create an Excel file
workbook = xlsxwriter.Workbook(filename="Example4-Device-Details.xlsx")
# Create an Excel sheet within the file
worksheet = workbook.add_worksheet(name="Device List")

worksheet.autofilter("A1:K1")
worksheet.freeze_panes(1, 1)

# Create Header cell for each entry
header = {
    "A1": "Hostname",
    "B1": "MGMT IP Address",
    "C1": "Serial Number",
    "D1": "MAC Address",
    "E1": "Device Model",
    "F1": "SW Version",
    "G1": "SW Type",
    "H1": "Operation Mode",
    "I1": "Last Reload Reason",
    "J1": "Restarted",
    "K1": "Device Up Time",
    "L1": "Config Register",
}

# Loop over headers and create cells in first row (row 0)
for cell, value in header.items():
    worksheet.write(cell, value)

# Starting values for row and column in the Excel workbook
row = 1
col = 0

# Loop over devices
for device in devices:
    # Create a connection instance
    with ConnectHandler(**device) as net_connect:
        facts = net_connect.send_command(
            command_string="show version", use_textfsm=True
        )

    # Loop over each value in facts variable and insert each value
    # in the corresponding cell according to the header above
    for value in facts:
        worksheet.write(row, col + 0, value["hostname"])
        worksheet.write(row, col + 1, device["ip"])  # use IP from device variable
        worksheet.write(row, col + 2, value["serial"][0])
        worksheet.write(row, col + 3, "N/A")
        worksheet.write(row, col + 4, value["hardware"][0])
        worksheet.write(row, col + 5, value["version"])
        worksheet.write(row, col + 6, value["rommon"])
        worksheet.write(row, col + 7, value["running_image"])
        worksheet.write(row, col + 8, value["reload_reason"])
        worksheet.write(row, col + 9, value["restarted"])
        worksheet.write(row, col + 10, value["uptime"])
        worksheet.write(row, col + 11, value["config_register"])
        # Jump to next row
        row += 1

# Close the Excel file
workbook.close()
print("Done")

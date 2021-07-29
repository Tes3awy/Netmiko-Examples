# Create an Excel sheet with Context Manager and save data from show version in

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
with xlsxwriter.Workbook(filename="Example4-2-Device-Details.xlsx") as workbook:
    # Create an Excel sheet within the file
    worksheet = workbook.add_worksheet(name="Device List")

    worksheet.autofilter("A1:K1")
    worksheet.freeze_panes(1, 1)

    # Create Header cell for each entry
    header = {
        "A1": "Device Hostname",
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
        "L1": "Configuration Register",
    }

    # Loop over headers and create cells in first row (row 0)
    for cell, value in header.items():
        worksheet.write(cell, value)

    # Starting values for row and column in the Excel workbook
    row, col = 1, 0

    # Loop over devices
    for device in devices:
        # Create a connection instance
        with ConnectHandler(**device) as net_connect:
            facts = net_connect.send_command(
                command_string="show version", use_textfsm=True
            )

        # Loop over each value in facts variable and insert each value
        # in the corresponding cell according to the header above
        for fact in facts:
            worksheet.write(row, col + 0, fact["hostname"])
            worksheet.write(row, col + 1, device["ip"])  # use IP from device variable
            worksheet.write(row, col + 2, fact["serial"][0])
            # Try/except block to handle IndexError
            try:
                worksheet.write(row, col + 3, fact["mac"][0])
            except IndexError:
                # if device is a CSR router, then it has no MAC Address
                worksheet.write(row, col + 3, "N/A")
            worksheet.write(row, col + 4, fact["hardware"][0])
            worksheet.write(row, col + 5, fact["version"])
            worksheet.write(row, col + 6, fact["rommon"])
            # Checking if `bin` is in fact["running_image"]
            if "bin" in fact["running_image"]:
                worksheet.write(row, col + 7, "Bundle")
            else:
                worksheet.write(row, col + 7, "Install")
            worksheet.write(row, col + 8, fact["reload_reason"])
            worksheet.write(row, col + 9, fact["restarted"])
            worksheet.write(row, col + 10, fact["uptime"])
            worksheet.write(row, col + 11, fact["config_register"])
            # Jump to next row
            row += 1

print("Done")

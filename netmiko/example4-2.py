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
        "fast_cli": False,
    },
    {
        "device_type": "cisco_ios",
        "ip": "sandbox-iosxe-recomm-1.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "port": 22,
        "fast_cli": False,
    },
]

# Create an Excel file
with xlsxwriter.Workbook(filename="Example4-2-Device-Details.xlsx") as workbook:
    # Create an Excel sheet within the file
    worksheet = workbook.add_worksheet(name="Device List")

    worksheet.autofilter("A1:L1")
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

    # Starting values for row only in the Excel workbook
    # Column will be indicated by its letter (A, B, C, etc) not index
    # Since we are using Column letters, we need to start at 2 because A1, B1, C1, etc is the header
    row = 2

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
            worksheet.write(f"A{row}", fact["hostname"])
            worksheet.write(f"B{row}", device["ip"])  # use IP from device variable
            worksheet.write(f"C{row}", fact["serial"][0])
            # Try/except block to handle IndexError
            try:
                worksheet.write(f"D{row}", fact["mac"][0])
            except IndexError:
                # if device is a CSR router, then it has no MAC Address
                worksheet.write(f"D{row}", "N/A")
            worksheet.write(f"E{row}", fact["hardware"][0])
            worksheet.write(f"F{row}", fact["version"])
            worksheet.write(f"G{row}", fact["rommon"])
            # Checking if `bin` is in fact["running_image"]
            if "bin" in fact["running_image"]:
                worksheet.write(f"H{row}", "Bundle")
            else:
                worksheet.write(f"H{row}", "Install")
            worksheet.write(f"I{row}", fact["reload_reason"])
            worksheet.write(f"J{row}", fact["restarted"])
            worksheet.write(f"K{row}", fact["uptime"])
            worksheet.write(f"L{row}", fact["config_register"])
            # Jump to next row
            row += 1

print("Done")

# Create an Excel sheet and save data with conditions from show inventory in

import xlsxwriter

from netmiko import ConnectHandler

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

# Create an Excel file
with xlsxwriter.Workbook(filename="Example5-Inventory.xlsx") as workbook:
    # Create an Excel sheet within the file
    worksheet = workbook.add_worksheet("Inventory")

    worksheet.autofilter("A1:B1")
    worksheet.freeze_panes(1, 1)

    # Create Header cell for each entry
    header = {"A1": "Hostname", "B1": "Serial Number"}

    # Loop over header and create cells in first row (row 0)
    for cell, value in header.items():
        worksheet.write(cell, value)

    # Starting values for row and column in the Excel workbook
    row = 1
    col = 0

    # Loop over devices
    for device in devices:
        # Create a connection instance
        with ConnectHandler(**device) as net_connect:
            # hostname of the current device
            hostname = net_connect.send_command(
                command_string="show version", use_textfsm=True
            )[0]["hostname"]
            inventory = net_connect.send_command(
                command_string="show inventory", use_textfsm=True
            )

        # Pick only Chassis serial number
        for item in inventory:
            if item["name"] == "Chassis":
                worksheet.write(row, col + 0, hostname)
                worksheet.write(row, col + 1, item["sn"])
                # Jump to next row
                row += 1

print("Done")

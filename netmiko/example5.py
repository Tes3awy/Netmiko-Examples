# Create an Excel sheet and save all data
# from `show inventory` command in

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
with xlsxwriter.Workbook(filename="Example5-Show-Inventory.xlsx") as workbook:
    # Loop over devices
    for device in devices:
        # Create a connection instance
        with ConnectHandler(**device) as net_connect:
            # hostname of the current device
            hostname = net_connect.send_command(
                command_string="show version", use_textfsm=True
            )[0]["hostname"]
            inventory = net_connect.send_command(
                command_string="show inventory", use_textfsm=True, delay_factor=3
            )

        # Create worksheet by hostname of each device
        worksheet = workbook.add_worksheet(f"{hostname} Inventory")

        worksheet.autofilter("A1:D1")
        worksheet.freeze_panes(1, 1)

        # Create Header cell for each entry
        header = {
            "A1": "Module Name",
            "B1": "Serial Number",
            "C1": "Product ID",
            "D1": "Description",
        }

        # Loop over header and create cells in first row (row 0)
        for cell, value in header.items():
            worksheet.write(cell, value)

        # Starting values for row and column in the Excel workbook
        row = 1
        col = 0

        for item in inventory:
            worksheet.write(row, col + 0, item["name"])
            worksheet.write(row, col + 1, item["sn"])
            worksheet.write(row, col + 2, item["pid"])
            worksheet.write(row, col + 3, item["descr"])
            # Jump to next row
            row += 1

print("Done")

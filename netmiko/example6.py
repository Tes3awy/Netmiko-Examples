# Create two Excel sheets and save data with conditions from show inventory
# and output from show ip interface brief
# Read the device list from a CSV file (Comma Seperated Value file)

import csv

import xlsxwriter

from netmiko import ConnectHandler

# Create an Excel file
workbook = xlsxwriter.Workbook(filename="Example6-Inventory-CSV.xlsx")
# Create two Excel sheets within the file
worksheet1 = workbook.add_worksheet(name="Inventory")
worksheet2 = workbook.add_worksheet(name="ip interface brief output")

worksheet1.autofilter("A1:B1")
worksheet2.autofilter("A1:E1")

worksheet1.freeze_panes(1, 1)
worksheet2.freeze_panes(1, 1)

# Create Header cell for each entry in sheet 1
header1 = {"A1": "Hostname", "B1": "Serial Number"}

# Create Header cell for each entry in sheet 2
header2 = {
    "A1": "Hostname",
    "B1": "Interface",
    "C1": "IP Address",
    "D1": "Status",
    "E1": "Protocol",
}

# Headers for sheet 1
for cell, value in header1.items():
    worksheet1.write(cell, value)

# Headers for sheet 2
for cell, value in header2.items():
    worksheet2.write(cell, value)

# Define devices variable
devices = []

# Read devices from device_list.csv CSV file
with open(
    file="device_list.csv", mode="rt", newline=""
) as csvfile:  # notice mode is rt: read text
    next(csvfile)  # Use next() function to skip the header line in the csv file
    # Each value is seperated based on the delimiter (comma (,))
    device_list = csv.reader(csvfile, dialect="excel", delimiter=",")
    for device in device_list:
        # Append devices from the CSV file to devices variable
        devices.append(
            {
                "device_type": device[0],
                "ip": device[1],
                "username": device[2],
                "password": device[3],
                "port": device[4],
                "fast_cli": False,
            }
        )

# Starting values for row and column in the Excel sheets
# sheet 1
row1, col1 = (1, 0)
# sheet 2
row2, col2 = (1, 0)

# Loop over devices
for device in devices:
    # Create a connection instance
    with ConnectHandler(**device) as net_connect:
        # hostname of current device
        hostname = net_connect.send_command(
            command_string="show version", use_textfsm=True
        )[0]["hostname"]
        inventory = net_connect.send_command(
            command_string="show inventory", use_textfsm=True
        )
        intf_brief = net_connect.send_command(
            command_string="show ip interface brief", use_textfsm=True
        )

    # Pick only "Chassis" serial number and save in sheet 1
    for module in inventory:
        if module["name"] == "Chassis":
            worksheet1.write(row1, col1 + 0, hostname)
            worksheet1.write(row1, col1 + 1, module["sn"])
            # Jump to next row
            row1 += 1

    # Pick show ip interface brief output and save in sheet 2
    for value in intf_brief:
        worksheet2.write(row2, col2 + 0, hostname)
        worksheet2.write(row2, col2 + 1, value["intf"])
        worksheet2.write(row2, col2 + 2, value["ipaddr"])
        worksheet2.write(row2, col2 + 3, value["status"])
        worksheet2.write(row2, col2 + 4, value["proto"])
        # Jump to next row
        row2 += 1


# Close the Excel file
workbook.close()
print("Done")

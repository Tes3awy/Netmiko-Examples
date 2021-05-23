# Create two Excel sheets and save data with conditions from show inventory
# and output from show ip interface brief

import csv

import xlsxwriter
from netmiko import ConnectHandler

# Create an Excel file
workbook = xlsxwriter.Workbook("Example6-Inventory-CSV.xlsx")
# Create an Excel sheets within the file
worksheet1 = workbook.add_worksheet("Inventory")
worksheet2 = workbook.add_worksheet("ip interface brief output")
# Filters
worksheet1.autofilter("A1:B1")
worksheet2.autofilter("A1:E1")

# Create Header cell for each entry in sheet 1
headers1 = {
    "A1": "Hostname",
    "B1": "Serial Number",
}

# Create Header cell for each entry in sheet 2
headers2 = {
    "A1": "Hostname",
    "B1": "Interface",
    "C1": "IP Address",
    "D1": "Status",
    "E1": "Protocol",
}

# Headers for sheet 1
for key, value in headers1.items():
    worksheet1.write(key, value)

# Headers for sheet 2
for key, value in headers2.items():
    worksheet2.write(key, value)

# Define devices variable
devices = []

# Read a csv file
with open("device_list.csv", mode="r") as csvfile:
    # Read devices from device_list.csv file
    device_list = csv.reader(csvfile, delimiter=",")
    for device in device_list:
        # Append devices from csv file to devices variable
        devices.append(
            {
                "device_type": device[0],
                "ip": device[1],
                "username": device[2],
                "password": device[3],
                "port": device[4],
            }
        )

# Starting values for row and column in the Excel sheets
row1 = 1
col1 = 0
# sheet 2
row2 = 1
col2 = 0

# Loop over devices
for device in devices:
    # Create a connection instance
    with ConnectHandler(**device) as net_connect:
        hostname = net_connect.send_command("show version", use_textfsm=True)[0][
            "hostname"
        ]  # hostname of current device
        inventory = net_connect.send_command("show inventory", use_textfsm=True)
        ip_int_brief = net_connect.send_command(
            "show ip interface brief", use_textfsm=True
        )

    # Pick only "Chassis" serial number and save in sheet 1
    for item in inventory:
        if item["name"] == "Chassis":
            worksheet1.write(row1, col1, hostname)
            worksheet1.write(row1, col1 + 1, item["sn"])
            # Jump to next row
            row1 += 1

    # Pick show ip interface brief output and save in sheet 2
    for value in ip_int_brief:
        worksheet2.write(row2, col2, hostname)
        worksheet2.write(row2, col2 + 1, value["intf"])
        worksheet2.write(row2, col2 + 2, value["ipaddr"])
        worksheet2.write(row2, col2 + 3, value["status"])
        worksheet2.write(row2, col2 + 4, value["proto"])
        # Jump to next row
        row2 += 1


# Close the Excel file
workbook.close()
print("Done")
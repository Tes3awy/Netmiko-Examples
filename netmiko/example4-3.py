# Create an Excel file and save data from
# show version command using pandas
# (Implicitly uses xlsxwriter to create the Excel file)

import pandas as pd

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
        "ip": "ios-xe-mgmt.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "port": 8181,
    },
]

# Create an empty list to hold all dicts
output = []

# Command to send
cmd = "show version"

# Loop over all devices
for device in devices:
    # Create a connection instance to each device
    with ConnectHandler(**device) as net_connect:
        result = net_connect.send_command(cmd, use_textfsm=True)
    # Append the show command output to the `output` empty list
    output.append(result[0])

# Create a data frame from the ouput list
df = pd.DataFrame(output)

# Name of exported excel file
excel_file = "Example4-3-Inventory-Details-pd.xlsx"

# Export data to an Excel file using to_excel from Pandas
df.to_excel(
    excel_writer=excel_file,  # name of Excel file
    index=False,  # remove automatically generated first index column
    sheet_name="Device List using Pandas",
    verbose=True,  # show verbose output for errors
    freeze_panes=(1, 1),  # freeze top row & most left column
    engine="xlsxwriter",  # the engine to create the Excel file
)

print("Done")

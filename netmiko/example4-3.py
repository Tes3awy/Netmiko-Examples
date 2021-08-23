# Create an Excel file and save data from
# show version command using pandas
# (Implicitly uses xlsxwriter to create the Excel file)

import pandas as pd
from pandas import ExcelWriter

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

# Create an empty list to hold all dicts
output = []

# Command to send
cmd = "show version"

# Name of exported excel file
excel_file = "Example4-3-Inventory-Details-pandas.xlsx"

with ExcelWriter(path=excel_file) as writer:
    # Loop over all devices
    for device in devices:
        # Create a connection instance to each device
        with ConnectHandler(**device) as net_connect:
            facts = net_connect.send_command(command_string=cmd, use_textfsm=True)
        # Append the show command output to the `output` empty list
        output.append(facts[0])

    # Create a data frame from the ouput list
    df = (
        pd.DataFrame(output)
        .reindex(  # to reorder the columns
            columns=[
                "hostname",
                "serial",
                "mac",
                "hardware",
                "rommon",
                "version",
                "running_image",
                "reload_reason",
                "uptime",
                "restarted",
                "config_register",
            ]
        )
        .rename(  # Rename the columns header
            columns={
                "hostname": "Device Hostname",
                "serial": "Serial Number",
                "mac": "MAC Address",
                "hardware": "Device Model",
                "rommon": "SW Type",
                "version": "SW Version",
                "running_image": "Running Image",
                "reload_reason": "Last Reload Reason",
                "uptime": "Uptime",
                "restarted": "Restarted at",
                "config_register": "Config Register",
            }
        )
    )

    # Export data to an Excel file using to_excel from Pandas
    df.to_excel(
        excel_writer=writer,  # name of Excel file
        index=False,  # remove automatically generated first index column
        sheet_name="Device List using Pandas",
        verbose=True,  # show verbose output for errors
        freeze_panes=(1, 1),  # freeze top row & most left column
        engine="xlsxwriter",  # the engine to create the Excel file
    )

print("Done")

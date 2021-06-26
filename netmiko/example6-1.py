# Create Excel file and save output from show ip interface brief
# of different devices into seperate sheets

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
        "ip": "ios-xe-mgmt.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "port": 8181,
    },
]

# Create an Excel file
with xlsxwriter.Workbook(filename="Example6-1-IP-Interface-Brief.xlsx") as workbook:
    id = 0  # ID to differentiate devices of same hostname
    # Iterate over devices
    for device in devices:
        # Create a connection instance to each device
        with ConnectHandler(**device) as net_connect:
            # command_string is an argument keyword inside the send_command function
            # command_string can be removed and the function runs without it
            hostname = net_connect.send_command(
                command_string="show version", use_textfsm=True
            )[0]["hostname"]
            output = net_connect.send_command(
                command_string="show ip interface brief",
                use_textfsm=True,
                delay_factor=2,
            )

        # Increment ID
        id += 1

        # Add worksheet with hostname of the device-ID
        worksheet = workbook.add_worksheet(f"{hostname}-{id}")

        worksheet.autofilter("A1:D1")
        worksheet.freeze_panes(1, 1)

        header_line = {
            "A1": "Interface Name",
            "B1": "IP Address",
            "C1": "Status",
            "D1": "Protocol",
        }

        # Write the header line
        for cell, value in header_line.items():
            worksheet.write(cell, value)

        # Initial values for row and col
        row = 1
        col = 0

        # Get intf values from output
        for intf in output:
            worksheet.write(row, col + 0, intf["intf"])
            worksheet.write(row, col + 1, intf["ipaddr"])
            worksheet.write(row, col + 2, intf["status"])
            worksheet.write(row, col + 3, intf["proto"])

            # Jump to next row
            row += 1

print("Done")

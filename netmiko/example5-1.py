# Create an Excel sheet and save cdp neighbors detail data in
# And check if `cdp` is enabled or not

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
with xlsxwriter.Workbook(filename="Example5-1-CDP-Neighbors-Details.xlsx") as workbook:
    # Starting values for row and col in the Excel workbook
    row, col = 1, 0

    # Loop over devices
    for device in devices:
        # Create a connection instance
        with ConnectHandler(**device) as net_connect:
            # hostname of the current device
            hostname = net_connect.send_command(
                command_string="show version", use_textfsm=True
            )[0]["hostname"]
            cdp_neighbors_detail = net_connect.send_command(
                command_string="show cdp neighbors detail",
                use_textfsm=True,
                delay_factor=2,
            )

        # Create a sheet for each device
        worksheet = workbook.add_worksheet(f"{hostname} Neighbors")

        # Worksheet customizations
        worksheet.autofilter("A1:H1")
        worksheet.freeze_panes(1, 1)

        # Create Header line
        header = {
            "A1": "Local Port",
            "B1": "Remote Hostname",
            "C1": "Remote Host Port",
            "D1": "Remote MGMT IP Address",
            "E1": "Capabilities",
            "F1": "Remote Host Platform",
            "G1": "Remote Host SW Version",
        }

        # Loop over headers and create cells in first row (row 0)
        for cell, value in header.items():
            worksheet.write(cell, value)

        # Check if cdp is enabled on that Cisco device
        if "% CDP is not enabled" not in cdp_neighbors_detail:
            print(f"Found cdp neighbors for {hostname}")
            # Loop over dicts in cdp neighbors detail list
            for neighbor in cdp_neighbors_detail:
                worksheet.write(row, col + 0, neighbor["local_port"])
                worksheet.write(row, col + 1, neighbor["destination_host"])
                worksheet.write(row, col + 2, neighbor["remote_port"])
                worksheet.write(row, col + 3, neighbor["management_ip"])
                worksheet.write(row, col + 4, neighbor["capabilities"])
                worksheet.write(row, col + 5, neighbor["platform"])
                worksheet.write(row, col + 6, neighbor["software_version"])
                # Jump to next row
                row += 1
        else:
            print(
                f"{cdp_neighbors_detail}. Please run `cdp run` command in Global Config mode on {hostname}"
            )

print("Done")

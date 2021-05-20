# Test cable diagnostics for up/up interfaces only
# and save output result to a text file

# Must run example4.py first

import time

import pandas as pd

from netmiko import ConnectHandler

# Read Excel file of .xlsx format
data = pd.read_excel("Example4-Inventory-Details.xlsx")

# Convert data to data frame
df = pd.DataFrame(data)

# Conevrt data frame from MGMT IP Address
device_ip_list = df["MGMT IP Address"].tolist()

# Define devices variable
devices = []

# Loop over values in device_ip_list
for ip in device_ip_list:
    # Append values to devices variable
    devices.append(
        {
            "device_type": "cisco_ios",  # must be the same for all devices
            "ip": ip,
            "username": "developer",  # must be the same for all devices
            "password": "C1sco12345",  # must be the same for all devices
            "port": 22,  # must be the same for all devices
            # If port for all devices is not 22 you will get an error
        }
    )

for device in devices:
    with ConnectHandler(**device) as net_connect:
        hostname = net_connect.find_prompt()[:-1]  # find hostname of current device
        output = net_connect.send_command(
            "show ip interface brief | include ^GigabitEthernet.*up.*up",
            use_textfsm=True,
        )

        for up_port in output:
            net_connect.send_command(
                f'test cable-diagnostics tdr interface {up_port["intf"]}'
            )

        # test cable-diagnostics command takes about 5 to 7 seconds to evaluate
        # Wait for a time factor to let the test of each interface take time
        time.sleep(8 * len(output))

        # Create a text file
        outfile = open(f"{hostname}-test-cable-diagnostics-result.txt", mode="w")
        for up_port in output:
            test_output = net_connect.send_command(
                f'show cable-diagnostics tdr interface {up_port["intf"]}'
            )
            # Write result of each interface in the text file
            outfile.write(f"{test_output}\n")
        # Close file
        outfile.close()

print("Done")

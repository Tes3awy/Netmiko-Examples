# Must run example4.py first
# Read an Excel sheet and save running config of devices using pandas

import pandas as pd

from netmiko import ConnectHandler

# Read Excel file of .xlsx format
data = pd.read_excel(io="Example4-Device-Details.xlsx", sheet_name=0)

# Convert data to data frame
df = pd.DataFrame(data=data)

# Conevrt data frame from MGMT IP Address to a list
device_ip_list = df.iloc[:, 1].tolist()

# Define devices variable
devices = []

for ip in device_ip_list:
    devices.append(
        {
            "device_type": "cisco_ios",  # must be the same for all devices
            "ip": ip,
            "username": "developer",  # must be the same for all devices
            "password": "C1sco12345",  # must be the same for all devices
            "port": 22,  # must be the same for all devices
            # If port for all devices is not 22 you will get an error
            "fast_cli": False,
        }
    )

for device in devices:
    # Create a connection instance
    with ConnectHandler(**device) as net_connect:
        # hostname of the current device
        hostname = net_connect.send_command(
            command_string="show version", use_textfsm=True
        )[0]["hostname"]
        run_cfg: str = net_connect.send_command(command_string="show running-config")

    # Create .txt for each running configuration of each device
    with open(file=f"{hostname}_ex7-run-cfg.txt", mode="w") as outfile:
        outfile.write(run_cfg.lstrip())

print("Done")

# Must run example4.py first
# Send new same configuration for each device and save the new running config

import pandas as pd

from netmiko import ConnectHandler

# Read Excel file of .xlsx format
data = pd.read_excel(io="Example4-Inventory-Details.xlsx", sheet_name=0)

# Convert data to data frame
df = pd.DataFrame(data)

# Conevrt data frame from MGMT IP Address
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
        }
    )

#  Sample config file
cfg_file = "config-sample-ex8.txt"

# Loop over each device in devices variable
for device in devices:
    # Create a connection instance
    with ConnectHandler(**device) as net_connect:
        # hostname of the current device
        hostname = net_connect.send_command(
            command_string="show version", use_textfsm=True
        )[0]["hostname"]
        # Reads and sends commands in cfg_file to each device
        output = net_connect.send_config_from_file(config_file=cfg_file)
        # Saves config with write memory command
        output += net_connect.save_config()

        run_cfg = net_connect.send_command(command_string="show running-config")

    # Create .txt for each running configuration of each device
    with open(file=f"{hostname}_ex8-run-cfg.txt", mode="w") as outfile:
        outfile.write(run_cfg.lstrip())

print("Done")

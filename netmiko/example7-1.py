# Must run example4.py first
# Read an Excel sheet and save running config of devices using pandas
# Alternate Solution for example 7

import pandas as pd

from netmiko import ConnectHandler

# Read Excel file of .xlsx format
# Read only column B (The MGMT IP Address column)
data = pd.read_excel(io="Example4-Inventory-Details.xlsx", sheet_name=0, usecols="B")

# Convert data to data frame
df = pd.DataFrame(data=data)

# Conevrt data frame from MGMT IP Address to a list
# Now column is 0 because it is the only column read in data variable
device_ip_list = df.iloc[:, 0].tolist()

# Define devices variable
devices = []

for ip in device_ip_list:
    devices.append(
        {
            "device_type": "cisco_ios",  # must be the same for all devices
            "ip": ip,  # IP of each device from the Excel file
            "username": "developer",  # must be the same for all devices
            "password": "C1sco12345",  # must be the same for all devices
            "port": 22,  # must be the same for all devices
            # If port for all devices is not 22 you will get an error
        }
    )

for device in devices:
    # Create a connection instance with try/except block to handle connection errors
    try:
        with ConnectHandler(**device) as net_connect:
            # hostname of the current device
            hostname = net_connect.send_command(
                command_sting="show version", use_textfsm=True
            )[0]["hostname"]
            run_cfg: str = net_connect.send_command(command_sting="show running-config")
        # Create .txt for each running configuration of each device
        with open(file=f"{hostname}_ex7-run-cfg.txt", mode="w") as outfile:
            outfile.write(run_cfg.lstrip())
    except Exception as e:  # Handle any exception
        raise SystemExit(e)

print("Done")

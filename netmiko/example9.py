# Create a Connection Instance Example

from netmiko import ConnectHandler

# Define a device
nxos_device = {
    "device_type": "cisco_nxos",
    "ip": "sbx-nxos-mgmt.cisco.com",
    "username": "admin",
    "password": "Admin_1234!",
    "secret": "",  # Optional (Enable secret)
    "port": 8181,  # Optional (Default to 22 for SSH)
    "verbose": True,  # Optional (Default False)
    "session_log": "ex9-session.txt",  # Optional (No default value)
    "global_delay_factor": 2,  # Optional (Default to 1)
}

# Create an SSH connection instance
with ConnectHandler(**nxos_device) as net_connect:
    output = net_connect.send_command("show version", use_textfsm=True)
    running_config = net_connect.send_command("show running-config")

with open(f"{output[0]['hostname']}-running_config.txt", "w") as outfile:
    outfile.write(running_config.strip())

print("Done")
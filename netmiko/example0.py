# Create a Connection Instance Example

from netmiko import ConnectHandler

# Define a device
device = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "secret": "",  # Optional (Default empty, Enable secret)
    "port": 22,  # Optional (Default to 22 for SSH and 23 for telnet)
    "verbose": True,  # Optional (Default False)
    "session_log": "ex0-session.txt",  # Optional (No default value)
    "fast_cli": False,  # (Multiplies delay factor by 0.1)
    "global_delay_factor": 2,  # Optional (Default to 1. 1 == 100 seconds)
    "conn_timeout": 12,  # Time duration to keep trying to connect to the device (seconds)
}

# Create an SSH connection instance (Traditional Method)
net_connect = ConnectHandler(**device)
run_cfg = net_connect.send_command(command_string="show running-config")
net_connect.disconnect()  # Explicit call of disconnect function
print(run_cfg)

print("Done")

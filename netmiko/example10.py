# Detect unknown device types

from pprint import pprint
from netmiko import ConnectHandler, SSHDetect

# Define a device
device = {
    "device_type": "autodetect",  # autodetect
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "port": 22,
}

# Create guessing variables
guesser = SSHDetect(**device)
best_match = guesser.autodetect()
print("\nDevice Type Best Match:", best_match, "\n")

# Override autodetect value with the best match
device["device_type"] = best_match

# Create an SSH connection instance
with ConnectHandler(**device) as net_connect:
    output = net_connect.send_command("show version", use_textfsm=True)
pprint(output)

print("Done")

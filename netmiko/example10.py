# Detect an unknown device types

from pprint import pprint

from netmiko import ConnectHandler, SSHDetect

# Define a device
device = {
    "device_type": "autodetect",  # Notice autodetect
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "port": 22,
    "fast_cli": False,
}

# Define guessing variables
best_match = SSHDetect(**device).autodetect()
print("\nDevice Type Best Match:", best_match, end="\n\n")

# Override autodetect value with the best match
device["device_type"] = best_match

# Create an SSH connection instance
with ConnectHandler(**device) as net_connect:
    facts = net_connect.send_command(command_sting="show version", use_textfsm=True)
pprint(facts)

print("Done")

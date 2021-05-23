# Detect unknown device types

from netmiko import ConnectHandler, SSHDetect

# Define a device
device = {
    "device_type": "autodetect",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "secret": "",
    "port": 22,
}

# Create an SSH connection instance
guesser = SSHDetect(**device)
best_match = guesser.autodetect()

# Override autodetect with the best match
device["device_type"] = best_match

with ConnectHandler(**device) as net_connect:
    output = net_connect.send_command("show version")
print(output)

print("Done")

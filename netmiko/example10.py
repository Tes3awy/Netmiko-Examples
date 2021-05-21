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

net_connect = ConnectHandler(**device)
output = net_connect.send_command("show version")
net_connect.disconnect()

print(output)
print("Done")

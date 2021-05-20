# Create a Connection Instance Example

from netmiko import ConnectHandler

# Define a device
device = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "port": 22,
}

# Create an SSH connection instance
with ConnectHandler(**device) as net_connect:
    output = net_connect.send_command("show version")

print(output)
print("Done")
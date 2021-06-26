# Create a Connection Instance Example

from netmiko import ConnectHandler

# Define a device
device = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "session_log": "ex1-session-log.txt",
    "port": 22,
}

# Create an SSH connection instance (Context Manager Method)
# Context manager handles connection and disconnection from the device
with ConnectHandler(**device) as net_connect:
    output = net_connect.send_command(command_string="show version")
# Notice no explicit call of disconnect function
# Check ex1-session-log.txt and you will find that the last line is exit which
# means connection instance is terminated (disconnected) successfully
print(output)

print("Done")

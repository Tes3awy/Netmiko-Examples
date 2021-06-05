# Create a Connection Instance Example

from netmiko import ConnectHandler

# Define a device
device = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "secret": "",  # Optional (Default empty, Enable secret)
    "port": 22,  # Optional (Default to 22 for SSH)
    "verbose": True,  # Optional (Default False)
    "session_log": "ex0-session.txt",  # Optional (No default value)
    "global_delay_factor": 2,  # Optional (Default to 1)
}

# Create an SSH connection instance (Traditional Method)
net_connect = ConnectHandler(**device)
output = net_connect.send_command("show running-config")
net_connect.disconnect()  # Explicit call of disconnect function
print(output)

print("Done")

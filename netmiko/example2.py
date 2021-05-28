# For Loop Example

from netmiko import ConnectHandler

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "sandbox-iosxe-latest-1.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "port": 22,
    },
    {
        "device_type": "cisco_ios",
        "ip": "ios-xe-mgmt.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "port": 8181,
    },
]

# The command to send
command = "show version"

# Loop over devices
for device in devices:
    # Create a connection instance
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_command(command, use_textfsm=True)
    print(output)

print("Done")

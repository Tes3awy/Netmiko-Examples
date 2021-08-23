# For Loop Example

from pprint import pprint

from netmiko import ConnectHandler

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "sandbox-iosxe-latest-1.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "port": 22,
        "fast_cli": False,
    },
    {
        "device_type": "cisco_ios",
        "ip": "sandbox-iosxe-recomm-1.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "port": 22,
        "fast_cli": False,
    },
]

# The command to send
command = "show version"

# Loop over devices
for device in devices:
    # Create a connection instance
    with ConnectHandler(**device) as net_connect:
        facts = net_connect.send_command(command_string=command, use_textfsm=True)
    pprint(facts)

print("Done")

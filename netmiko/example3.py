# Backup running configuration from multiple devices Example

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

# Loop over devices
for device in devices:
    # Create a connection instance
    with ConnectHandler(**device) as net_connect:
        hostname = net_connect.find_prompt()[:-1]  # find hostname of current device
        running_config = net_connect.send_command("show running-config")

    # Create files with device hostnames and save show running-config output to
    with open(f"{hostname}_ex3-running-config.txt", mode="w") as outfile:
        outfile.write(running_config.strip())

print("Done")
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
        "ip": "sandbox-iosxe-recomm-1.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "port": 22,
    },
]

# Loop over devices
for device in devices:
    # Create a connection instance
    with ConnectHandler(**device) as net_connect:
        # hostname of the current device
        hostname = net_connect.send_command(
            command_string="show version", use_textfsm=True
        )[0]["hostname"]
        run_cfg = net_connect.send_command(command_string="show running-config")

    # Create files with device hostnames and save show running-config output to
    with open(file=f"{hostname}_ex3-run-cfg.txt", mode="w") as outfile:
        outfile.write(run_cfg.lstrip())

print("Done")

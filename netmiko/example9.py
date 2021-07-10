# Create an SSH Connection Instance to a Nexus switch

from netmiko import ConnectHandler

# Define a device
nxos_device = {
    "device_type": "cisco_nxos",  # No telnet option for NXOS
    "ip": "sbx-nxos-mgmt.cisco.com",
    "username": "admin",
    "password": "Admin_1234!",
    "secret": "",  # Optional (Enable secret)
    "port": 8181,  # Optional (Default to 22 for SSH)
    "verbose": True,  # Optional (Default False)
    "session_log": "ex9-nxos-session.txt",  # Optional (No default value)
    "global_delay_factor": 2,  # Optional (Default to 1)
}

# Create an SSH connection instance
with ConnectHandler(**nxos_device) as net_connect:
    # hostname of the current device
    hostname = net_connect.send_command(
        command_string="show version", use_textfsm=True
    )[0]["hostname"]
    run_cfg = net_connect.send_command(command_string="show running-config")

with open(file=f"{hostname}-run-cfg.txt", mode="w") as outfile:
    outfile.write(run_cfg.lstrip())

print("Done")

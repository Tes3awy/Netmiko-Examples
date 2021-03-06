# Examples Explanation

> If you don't have the `netmiko`, `xlsxwriter`, and `pandas` libraries installed on your PC, type:

```powershell
path_to\netmiko> pip install -r requirements.txt --user
```

> in VSCode terminal.

## Example 0

> Shows how to initiate an SSH connection instance to a Cisco device and print its running configuration.

## Example 1

> Same as example 0, but with an improved method (Context Manager) of initiating the SSH connection.

## Example 2

> Shows how to loop over a list of multiple devices.

## Example 3

> Same as example 2, adding how to export the running config of all devices to text files.

## Example 4

> Shows how to create an Excel file and append needed data to.

## Example 4-1

> Same as example 4 with if condition for running mode.

## Example 4-2

> Same as example 4 using Context Manager for xlsxwriter (and another method to insert data into sheet cells)

## Example 4-3

> Same as example 4 using Pandas to create the Excel file.

## Example 5

> Same as example 4, but adds data from `show inventory` command.

## Example 5-1

> Same as example 4, but adds `show cdp neighbors detail` command output in an Excel file.

## Example 6

_Uses `device_list.csv` file_

> Same as example 5, but adds two sheets from different outputs.

## Example 6-1

> Shows how to grab `show ip interface brief` command output from multiple devices, and save data to separate sheets in an Excel file.

## Example 7

_Must run `example4.py` first_

> Shows how to read an Excel file, get values from a specific column, and export running config to text files.

## Example 7-1

_Must run `example4.py` first_

> Same as example 7, but uses alternate method of reading IP Address column ONLY from the Excel file.

## Example 8

_Must run `example4.py` first_

_Uses `config-sample-ex8.txt` file_

> Shows how to read an Excel file, get values from a specific column, send same configuration to all devices, and export the new running config to text files.

## Example 9

> Same as example 0 but for a Nexus device.

## Example 10

> Shows how Netmiko can help you determine the device type.

## Bonus Example

> **This is an advanced example**

_Must run `example4.py` first_

This bonus example that does the following:

1. Gets Up/Up interfaces for multiple Cisco switches. _(Routers won't work)_
2. Applies `test cable-diagnostics tdr interface <up_up_interface_name>` command for all Up/Up interfaces.
3. Waits till all tests on all interfaces are done.
4. Exports the result of `show cable-diagnostics tdr interface <up_up_interface_name>` of each switch to a text file.

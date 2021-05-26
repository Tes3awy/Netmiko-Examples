# Netmiko & Requests Examples for Cisco DevNet

- In `netmiko` folder, you will find 13 Python examples, `device_list.csv` file, `config-sample-ex8.txt` file, and a `requirements.txt` file.

- In `requests` folder, you will find seven Python examples and a `requirements.txt` file.

## How to use?

1. `Clone` this repo or `Download ZIP` by clicking on ![Code Button](assets/code-button.png)

2. Once downloaded, extract the ZIP file and `cd` into `netmiko` folder or `requests` folder.

3. Open `netmiko` or `requests` folder in VSCode.

4. Open `requirements.txt` file and if any of the libraries is not installed on your PC, run the following command in the PowerShell terminal within VSCode:

```powershell
path_to\folder> pip install -r requirements.txt --user
```

5. Explore each `example*.py` file. _**(where **\*** is the number of the example)**_

6. Run any Python example by typing the following command in PowerShell terminal in VSCode:

```powershell
path_to\folder> python example*.py ↵
```

---

## Used Libraries Documentation Links

Examples in `netmiko` and `requests` folder uses some Python libraries. These libraries are:

1. Netmiko (Multi-vendor library to simplify Paramiko SSH connections to network devices) [Documentation Link](https://github.com/ktbyers/netmiko/blob/develop/README.md).
2. XlsxWriter (XlsxWriter is a Python module for creating Excel XLSX files.) [Documentation Link](https://xlsxwriter.readthedocs.io/).
3. Pandas (Data Analysis Library) [Documentation Link](https://pandas.pydata.org/docs/).
4. Requests (HTTP Requests) [Documentation Link](https://docs.python-requests.org/en/master/).

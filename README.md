![Cisco DevNet](https://img.shields.io/badge/Cisco-DevNet-blue)
[![Tested on Python 3.6+](https://img.shields.io/badge/Python%203.6+-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads)
![Language](https://img.shields.io/github/languages/top/Tes3awy/Netmiko-Examples)
![Repo Size](https://img.shields.io/github/repo-size/Tes3awy/Netmiko-Examples)
[![Issues Open](https://img.shields.io/github/issues/Tes3awy/Netmiko-Examples)](https://github.com/Tes3awy/Netmiko-Examples/issues)
![Releases Download](https://img.shields.io/github/downloads/Tes3awy/Netmiko-Examples/total)
[![Commit Activity](https://img.shields.io/github/commit-activity/m/Tes3awy/Netmiko-Examples)](https://github.com/Tes3awy/Netmiko-Examples/commits/main)
![Last Commit](https://img.shields.io/github/last-commit/Tes3awy/Netmiko-Examples)
[![Release Date](https://img.shields.io/github/release-date/Tes3awy/Netmiko-Examples)](https://github.com/Tes3awy/Netmiko-Examples/releases)
[![License](https://img.shields.io/github/license/Tes3awy/Netmiko-Examples)](https://github.com/Tes3awy/Netmiko-Examples/blob/main/LICENSE)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# Netmiko & Requests Examples for Cisco DevNet

- In `netmiko` folder, you will find 18 Python examples, `device_list.csv` file, `config-sample-ex8.txt` file, a `requirements.txt` file, and an explanation of each example.

- In `requests` folder, you will find seven Python examples, a `requirements.txt` file, and an explanation of each example.

## How to use?

1. `Clone` this repo or `Download ZIP` by clicking on <img src="assets/code-button.png" alt="Code Button" title="Button" width="100"/> up above.
   _(Alternativley, you can click on Releases on the right hand side and download the latest release)_

2. Once downloaded, extract the ZIP file and `cd` into `netmiko` folder or `requests` folder.

3. Open `netmiko` or `requests` folder in VSCode.

4. Open `requirements.txt` file and if any of the libraries is not installed on your PC, run the following command in the PowerShell terminal within VSCode:

```powershell
path_to\folder> pip install -r requirements.txt --user ↵
```

5. Explore each `example*.py` file. _**(where **\*** is the number of the example)**_

6. Run any Python example by typing the following command in PowerShell terminal in VSCode:

```powershell
path_to\folder> python example*.py ↵
```

---

## Libraries Documentation Links

Examples in `netmiko` and `requests` folder uses some Python libraries. These libraries are:

1. Netmiko **v3.4.0** (Multi-vendor library to simplify Paramiko SSH connections to network devices) [Documentation Link](https://github.com/ktbyers/netmiko/blob/develop/README.md).
2. NTC Templates **v2.1.0** (TextFSM templates for parsing show commands of network devices) [Documentation Link](https://github.com/networktocode/ntc-templates).
3. XlsxWriter **v1.4.3** (XlsxWriter is a Python module for creating Excel XLSX files) [Documentation Link](https://xlsxwriter.readthedocs.io/).
4. Pandas **v1.2.5** (Data Analysis Library) [Documentation Link](https://pandas.pydata.org/docs/).
5. Openpyxl **v3.0.7** (A Python library to read/write Excel 2010 xlsx/xlsm files) [Documentation Link](https://openpyxl.readthedocs.io/en/stable/).
6. Requests **v2.25.1** (HTTP Requests) [Documentation Link](https://docs.python-requests.org/en/master/).

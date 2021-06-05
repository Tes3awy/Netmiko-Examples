![Black](https://img.shields.io/badge/code%20style-black-000000.svg)
![Repo Size](https://img.shields.io/github/repo-size/Tes3awy/Netmiko-Examples)
![Downloads](https://img.shields.io/github/downloads/Tes3awy/Netmiko-Examples/latest/total)
![License](https://img.shields.io/github/license/Tes3awy/Netmiko-Examples)
![Last Commit](https://img.shields.io/github/last-commit/Tes3awy/Netmiko-Examples)
![Release Date](https://img.shields.io/github/release-date/Tes3awy/Netmiko-Examples)

# Netmiko & Requests Examples for Cisco DevNet

- In `netmiko` folder, you will find 13 Python examples, `device_list.csv` file, `config-sample-ex8.txt` file, a `requirements.txt` file, and an explanation of each example.

- In `requests` folder, you will find seven Python examples, a `requirements.txt` file, and an explanation of each example.

## How to use?

1. `Clone` this repo or `Download ZIP` by clicking on <img src="assets/code-button.png" alt="Code Button" title="Button" width="100"/> up above.
   _(Alternativley, you can click on Releases on the right hand side and download the latest release)_

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

1. Netmiko (Multi-vendor library to simplify Paramiko SSH connections to network devices). [Documentation Link](https://github.com/ktbyers/netmiko/blob/develop/README.md).
2. XlsxWriter (XlsxWriter is a Python module for creating Excel XLSX files). [Documentation Link](https://xlsxwriter.readthedocs.io/)
3. Pandas (Data Analysis Library). [Documentation Link](https://pandas.pydata.org/docs/)
4. Requests (HTTP Requests). [Documentation Link](https://docs.python-requests.org/en/master/)

# Test requests library
import requests

# GET Request
r = requests.get("https://google.com/")

print(r, type(r))

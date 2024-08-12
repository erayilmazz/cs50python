import sys
import requests
import json

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

try:
    money = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

try:
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = request.json()
    bitcoin = data["bpi"]["USD"]["rate_float"]
    print(f"${bitcoin * money:,.4f}")

except requests.RequestException:
    print("Request Error")




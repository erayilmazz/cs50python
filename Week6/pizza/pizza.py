import sys
import csv
from tabulate import tabulate


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")


elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif sys.argv[1].split(".")[1] != "csv":
    sys.exit("Not a CSV file")


try:
    with open(sys.argv[1]) as file:
        print(tabulate(csv.DictReader(file), headers= "keys", tablefmt = "grid"))

except FileNotFoundError:
    sys.exit("File does not exist")




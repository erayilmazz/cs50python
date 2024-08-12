import sys
import csv


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")


elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

students = []


try:
    with open (sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["name"], "house": row["house"]})

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")


with open (sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames = ["first","last","house"])
    writer.writeheader()
    for student in students:
        last_name, first_name = student["name"].split(", ")
        writer.writerow({"first": first_name, "last": last_name, "house": student["house"]})



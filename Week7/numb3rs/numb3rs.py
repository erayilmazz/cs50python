import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$",ip):
        for i in range(1,5):
            if 0 > int(matches.group(i)) or int(matches.group(i)) > 255:
                return False
        return True
    return False





if __name__ == "__main__":
    main()

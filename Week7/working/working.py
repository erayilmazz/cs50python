import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d+):?(\d+)? (AM|PM) to (\d+):?(\d+)? (AM|PM)$",s):
        hour1, minute1, t1, hour2, minute2, t2 = matches.groups()

        if minute1 is None:
            minute1 = "00"

        if minute2 is None:
            minute2 = "00"

        try:
            hour1 = int(hour1)
            hour2 = int(hour2)
            minute1 = int(minute1)
            minute2 = int(minute2)
        except TypeError:
            raise ValueError

        if t1 == "PM" and hour1 != 12:
            hour1 += 12

        if t2 == "PM" and hour2 != 12:
            hour2 += 12

        if t1 == "AM" and hour1 == 12:
            hour1 = 0

        if t2 == "AM" and hour2 == 12:
            hour2 = 0

        if hour1 < 24 and hour2 < 24 and minute1 < 60 and minute2 < 60:
            return f"{hour1:02d}:{minute1:02d} to {hour2:02d}:{minute2:02d}"
        else:
            raise ValueError
    else:
        raise ValueError

if __name__ == "__main__":
    main()

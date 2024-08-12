
while True:
    try:
        value = input("Fraction: ")
        first , last = value.split("/")
        percent = round(int(first) / int(last) *100)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if percent > 100:
            pass
        elif percent <= 1:
            print("E")
            break
        elif percent >= 99:
            print("F")
            break
        else:
            print(f"{percent}%")
            break




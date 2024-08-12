
def main():
    when = input("What time is it? ")
    if convert(when) >= 7 and convert(when) <= 8:
        print("breakfast time")
    elif convert(when) >= 12 and convert(when) <= 13:
        print("lunch time")
    elif convert(when) >= 18 and convert(when) <= 19:
        print("dinner time")

def convert(time):
    hour , minute = time.split (":")
    return int(hour) + int(minute)/60


if __name__ == "__main__":
    main()
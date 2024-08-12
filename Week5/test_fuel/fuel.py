import sys

def main():
    func1 = input("Fraction: ")
    func2 = convert(func1)
    print(gauge(func2))



def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            f = x / y
            if f <= 1:
                return f*100
            else:
                fraction = input("Fraction: ")
                pass

        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"

    else:
        return f"{int(percentage)}%"


if __name__ == "__main__":
    main()







def main():
    greeting = input ("Greeting: ")
    amount = value(greeting)
    print(f"${amount}")


def value(greeting):
    if "hello" in greeting.lower().strip():
        return 0
    elif greeting[0] == "h" or greeting[0] == "H":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

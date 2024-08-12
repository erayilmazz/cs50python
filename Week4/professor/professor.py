import random


def main():
    level = get_level()
    question = 0
    score = 10
    while True:
        if question == 10:
            break
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        attempt = 0
        while True:
            if attempt == 3:
                print(f"{num1} + {num2} = {num1 + num2}")
                score -= 1
                question+=1
                break
            try:
                user_conc = int(input(f"{num1} + {num2} = "))
                if user_conc == num1 + num2:
                    question+=1
                    break
                attempt += 1
                print("EEE")

            except ValueError:
                attempt += 1
    print(f"Score: {score}")




def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n <= 3 and n >= 1:
                return n
        except ValueError:
            continue



def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()

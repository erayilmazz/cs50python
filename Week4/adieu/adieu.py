import inflect
p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
        if name == "":  
            break
        names.append(name)
    except EOFError:
        print()
        break

print(f"Adieu, adieu, to {p.join(names)}")



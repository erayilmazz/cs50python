x = input("Expression: ")
if "+" in x:
    first,last = x.split("+")
    print(float(first) + float(last))
elif "-" in x:
    first,last = x.split("-")
    print(float(first) - float(last))
elif "/" in x:
    first,last = x.split("/")
    print(float(first) / float(last))
elif "*" in x:
    first,last = x.split("*")
    print(float(first) * float(last))


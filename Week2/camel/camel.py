words = input("camelCase: ")
for i in words:
    if i.isupper() == True:
        print("_" + i.lower(),end="")
    else:
        print(i, end="")






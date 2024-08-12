x = input ("Greeting: ")
if "hello" in x.lower().strip():
    print("$0")
elif x[0] == "h" or x[0] == "H":
    print("$20")
else:
    print("$100")
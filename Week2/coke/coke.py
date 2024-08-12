due = 50
while True:
    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))
    if coin == 25:
        due -= 25
    elif coin ==10:
        due -= 10
    elif coin == 5:
        due -= 5
    if due <= 0:
        print (f"Change Owed: {due*-1}")
        break







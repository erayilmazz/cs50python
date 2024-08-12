def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    
    if s.isalnum() == False:
        return False

    one = []
    for i in s:
        one.append(i)

    if one[0].isdigit() == True or one[1].isdigit() == True:
        return False

    for i in range(2,6):
        if one[i].isdigit() == True:
            if one[i] == "0":
                return False
            for j in one[i:]:
                if j.isdigit() == False:
                    return False
            else:
                return True
    return True

main()

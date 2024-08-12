def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    letters = ["a","e","o","u","i"]
    for i in word:
        if i.lower() in letters:
            word = word.replace(i,"")
    return word




if __name__ == "__main__":
    main()










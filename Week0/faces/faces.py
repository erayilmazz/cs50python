def main():
    n = input("")
    print(convert(n))

def convert(x):
    return x.replace(":)","🙂").replace(":(","🙁")

main()


import re


def main():
    print(count(input("Text: ")))


def count(s):
    ums = re.findall(r"\b(um|Um)\b",s)
    return len(ums)



if __name__ == "__main__":
    main()

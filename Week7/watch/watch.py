import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"<iframe src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"></iframe>",s):
        return f"https://youtu.be/{matches.group(1)}"
    return None





if __name__ == "__main__":
    main()
#if matches := re.search(r'https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)', s):

from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()


if len(sys.argv) == 1:
    font = random.choice(fonts)
    figlet.setFont(font = font)

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "-font":
        if sys.argv[2] in fonts:
            figlet.setFont(font = sys.argv[2])
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

value = input("Input: ")
print(f"Output:\n{figlet.renderText(value)}")

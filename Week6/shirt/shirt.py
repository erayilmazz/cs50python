import sys
from PIL import Image, ImageOps



if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if not(sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".png")) or not (sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".png")):
    sys.exit("Invalid output")

elif sys.argv[1][-3:] != sys.argv[2][-3:]:
    sys.exit("Input and output have different extensions")




try:
    shirt = Image.open("shirt.png")
    muppet = Image.open(sys.argv[1])

except FileNotFoundError:
    sys.exit("Input does not exist")

try:
    size1,size2 = shirt.size
    muppet = ImageOps.fit(muppet,(size1,size2))
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("Output does not exist")

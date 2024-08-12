value = input("File name: ").lower().strip()
if value[-4] == ".":
    value = value[-3:]
elif value [-5] == ".":
    value = value[-4:]
else:
    print("application/octet-stream")
match value:
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")







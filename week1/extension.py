extension = input("")
extension = extension.replace("."," ")
extension = extension.split()
print(extension)
if extension[1] == "gif":
    print("image/gif")
elif extension[1] == "jpg":
    print("image/jpeg")
elif extension[1] == "jpeg":
    print("image/jpeg")
elif extension[1] == "png":
    print("image/png")
elif extension[1] == "pdf":
    print("application/pdf")
elif extension[1] == "txt":
    print("text/plain")
elif extension[1] == "zip":
    print("application/zip")
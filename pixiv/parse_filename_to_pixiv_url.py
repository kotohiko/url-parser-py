filename = input("filename: ")
if filename.__contains__("_"):
    filename = filename[:filename.index("_")]
filename = "https://www.pixiv.net/artworks/" + filename
print(filename)

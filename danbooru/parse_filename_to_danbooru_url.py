filename = input("filename: ")
filename = filename[:5] + "://" + filename[5:]
filename = filename[:26] + "/" + filename[26:]
filename = filename[:32] + "/" + filename[32:]
if filename.__contains__("?"):
    filename = filename[:filename.index("?")]
print(filename)

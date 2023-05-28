filename = input("filename: ")
filename = filename[:5] + "://" + filename[5:]
filename = filename[:24] + "/" + filename[24:]
filename = filename[:filename.index("opus") + 4] + "/" + filename[filename.index("opus") + 4:]
print(filename)

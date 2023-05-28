filename = input("filename: ")
filename = filename[:5] + "://" + filename[5:]
filename = filename[:16] + "/" + filename[16:]
filename = filename[:21] + "/" + filename[21:]
filename = filename[:26] + "/" + filename[26:]
print(filename)

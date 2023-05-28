filename = input("filename: ")
filename = filename[:5] + "://" + filename[5:]
filename = filename[:19] + "/" + filename[19:]
filename = filename[:filename.index("status")] + "/" + filename[filename.index("status"):]
filename = filename[:filename.index("status") + 6] + "/" + filename[filename.index("status") + 6:]
print(filename)

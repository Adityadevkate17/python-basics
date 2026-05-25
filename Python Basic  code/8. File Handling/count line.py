# Count number of lines in file.

file = open("myfile.txt", "r")
lines = file.readlines()
print("number of lines:", len(lines))
file.close()

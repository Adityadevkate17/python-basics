# Copy content from one file to another.

file1 = open("myfile.txt","r")
file2 = open("myfilecopy.txt","w")

content = file1.read()
file2.write(content)

file1.close()
file2.close()

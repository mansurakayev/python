import os
File = open("Test1.txt", "w")
File.write("test\n")
File.write("test1")
File.close()
txt = open("Test1.txt")
print(txt.read())
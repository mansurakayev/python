a = []
files_list = ["Test1.txt","Test2.txt"]
for elem in files_list:
   file = open(elem,'r')
   a.append(file.read())
print(a)
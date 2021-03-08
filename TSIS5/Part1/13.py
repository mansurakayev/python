cnt=0
source = open("Test1.txt")
destination = open("Test2.txt","w+")
for line in source:
    destination.write(line)
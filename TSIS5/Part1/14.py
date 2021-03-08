file1 = open("Test1.txt")
file2 = open("Test2.txt")
for i,j in zip(file1,file2):
    print(i+j)
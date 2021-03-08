import os
size = os.stat("Test1.txt")
print(size.st_size)
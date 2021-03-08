a = []
file = open("Test1.txt")
for line in file:
    a.append(line)
print(*a)
print(type(a))
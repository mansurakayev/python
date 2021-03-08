import collections
file = open("Test1.txt")
print(*collections.Counter(file))

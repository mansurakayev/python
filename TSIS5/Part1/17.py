import re
file = open("Test1.txt").readlines()
print([s.rstrip('\n')for s in file])
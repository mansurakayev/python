file = open("Test1.txt","r")
lines = file.readlines()
n=1
last_lines = lines[-n:]
print(last_lines)
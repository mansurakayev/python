file = open("Test3.txt","w+")
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cnt = 0
n = int(input())
lines = [s[i:i+n]+"\n" for i in range(0,26,n)]
for i in lines:
    file.write(i)
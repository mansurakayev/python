n = int(input())
mp={}
for i in range(n):
    a,b=input().split()
    mp[a]=b
    mp[b]=a
m = input()
print(mp[m])

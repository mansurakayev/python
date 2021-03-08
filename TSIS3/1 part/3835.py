a = list(map(int,input().strip().split()))
mn=11111
for i in a:
    if i > 0 and i < mn:
        mn=i
print(mn)
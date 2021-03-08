a = int(input())
b = list(map(int, input().split()))
mx = b[0]
for i in b:
    if i > mx:
        mx = i
print(mx)

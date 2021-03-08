a = int(input())
b = list(map(int, input().split()))
c = int(input())
ans = 1
for i in range(len(b)):
    if (b[i] >= c):
        ans += 1
print(ans)

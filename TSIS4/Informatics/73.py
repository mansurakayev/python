a = int(input())
b = list(map(int, input().split()))
ans = 1
for i in range(len(b) - 1):
    if b[i] != b[i + 1]:
        ans += 1
print(ans)

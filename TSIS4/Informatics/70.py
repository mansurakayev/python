a = int(input())
b = list(map(int, input().split()))
for i in range(0, len(b) - 1, 2):
    print(b[i + 1], b[i], end=" ")
if a % 2 == 1:
    print(b[a - 1])
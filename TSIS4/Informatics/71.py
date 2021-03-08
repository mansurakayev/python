a = int(input())
b = list(map(int, input().split()))
print(b[a - 1], *b[0:a - 1])

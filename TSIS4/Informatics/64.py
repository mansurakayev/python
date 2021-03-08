a = int(input())
b = list(map(int, input().split()))
print(*([i for i in b if i % 2 == 0]))

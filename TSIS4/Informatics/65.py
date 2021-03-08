a = int(input())
b = list(map(int, input().split()))
print(len([i for i in b if i > 0]))

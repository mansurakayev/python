a = set(input().split())
b = set(input().split())
print(*sorted(a&b,key=int))
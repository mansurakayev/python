n, m = [int(i) for i in input().split()]
a = set()
b = set()
for i in range(n):
    a.add(int(input()))
for i in range(m):
    b.add(int(input()))
print(len(a&b))
print(*sorted(a&b,key=int))
print(len(a-b))
print(*sorted(a-b,key=int))
print(len(b-a))
print(*sorted(b-a,key=int))
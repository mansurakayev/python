n = int(input())
for i in range(10**n, 0, -1):
    if len(str(i)) < n: break
    if i % 2 == 1: print(i, end=' ')
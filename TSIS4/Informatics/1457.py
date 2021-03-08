n, a, b, c, d = map(int, input().split())
m = [i for i in range(1, n + 1)]
a -= 1
c -= 1
m[a:b] = reversed(m[a:b])
m[c:d] = reversed(m[c:d])
print(*m)

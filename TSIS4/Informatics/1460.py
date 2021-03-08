m = int(input())
a = list(map(int, input().split()))
n = int(input()) % len(a)
if n < 0:
    n = abs(n)
    print(*a[n:], end=" ")
    print(*a[0:n])
else:
    print(*a[-n:], end=" ")
    print(*a[0:-n])

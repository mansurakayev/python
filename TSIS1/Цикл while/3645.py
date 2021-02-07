n, i, ch = int(input()), 1, False
while i <= n:
    if i == n:
        print("YES")
        ch = True
        break
    i *= 2
if ch == False: print("NO")